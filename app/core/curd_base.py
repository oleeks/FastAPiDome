from typing import Generic, Type, TypeVar, Any, Optional, List

from pydantic import BaseModel

from app.models.base import BaseModel as Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, model_id: Any) -> Optional[ModelType]:
        return self.model.qurey.where(self.model.id == model_id).gino.first()

    def get_multi(
            self,  *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        offset = (skip - 1) * limit

        return self.model.query.offset(offset).limit(limit).gino.all()
        # return self.model.query.gino.all()

    @property
    def count(self):
        return self.model.count()
