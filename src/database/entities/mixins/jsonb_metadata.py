from __future__ import annotations

from typing import Any, ClassVar, Generic, TypeVar

from pydantic import BaseModel

TMeta = TypeVar("TMeta", bound=BaseModel)


class JsonbMetadataMixin(Generic[TMeta]):
    """
    Reusable helpers for entities that store structured metadata in a JSON/JSONB column.

    Usage:
      - set __metadata_field__ to the JSON/JSONB attribute name on the entity (default: "attributes")
      - set __metadata_model__ to the Pydantic model class used for that JSON blob
    """

    __metadata_field__: ClassVar[str] = "attributes"
    __metadata_model__: ClassVar[type[TMeta]]

    def set_meta(self, meta: TMeta) -> None:
        setattr(self, self.__metadata_field__, meta.model_dump())

    def get_meta(self) -> TMeta:
        raw: Any = getattr(self, self.__metadata_field__)
        return self.__metadata_model__.model_validate(raw)

