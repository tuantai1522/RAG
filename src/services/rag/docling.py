from typing import Any
from docling.document_converter import DocumentConverter, PdfFormatOption, ImageFormatOption
from docling.chunking import HybridChunker
from docling.datamodel.base_models import InputFormat

from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    PictureDescriptionApiOptions,
    TableFormerMode,
)
from transformers import AutoTokenizer
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    TableStructureOptions,
)
from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend

from src.core import settings

class DoclingService:
    def __init__(self):
        self.converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_options=self._create_pdf_pipeline_options(),
                    backend=PyPdfiumDocumentBackend
                )
            }
        )

        self.chunker = HybridChunker(
            tokenizer = HuggingFaceTokenizer(
                tokenizer = AutoTokenizer.from_pretrained(settings.docling.TOKEN_MODEL_ID)
            ),
            merge_peers=True,
        )

    def get_chunks_by_link_url(self, link_url: str):
        # 1. Get content in source
        doc = self.converter.convert(link_url).document

        # 2. Chunk content
        chunks = list(self.chunker.chunk(dl_doc=doc))

        # 3. Return list results
        return [
            {
                "text": chunk.text,
                "metadata": {
                    "file_name": chunk.meta.origin.filename,
                    "page_numbers": [
                        page_no
                        for page_no in sorted(
                            set(
                                prov.page_no
                                for item in chunk.meta.doc_items
                                for prov in item.prov
                            )
                        )
                    ]
                    or None,
                    "title": chunk.meta.headings[0] if chunk.meta.headings else None,
                },
            }
            for chunk in chunks
        ]

    def _create_picture_description_options(self) -> PictureDescriptionApiOptions:
        return PictureDescriptionApiOptions(
            url=f"{settings.ollama.BASE_URL}/v1/chat/completions",
            params=dict[str, Any](
                model=settings.ollama.VISION_MODEL_ID,
                think=False,
                seed=42,
                max_completion_tokens=256,
            ),
            prompt="Describe the image in three sentences. Be consise and accurate.",
            timeout=250
        )
    
    def _create_pdf_pipeline_options(self) -> PdfPipelineOptions:
        return PdfPipelineOptions(
            enable_remote_services=True,

            do_ocr=False,

            do_table_structure=True,

            table_structure_options=TableStructureOptions(
                mode=TableFormerMode.ACCURATE,
                do_cell_matching=True
            ),

            generate_picture_images=True,
            do_picture_description=True,
            picture_description_options=self._create_picture_description_options()
        )
