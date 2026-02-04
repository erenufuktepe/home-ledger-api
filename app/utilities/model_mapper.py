from typing import Annotated, Type, TypeVar, get_args, get_origin
import types
import typing

from pydantic import BaseModel

from app.models.base import Base

T = TypeVar("T", bound=Base)
S = TypeVar("S", bound=BaseModel)


class ModelMapperException(Exception):
    pass


class ModelMapper:
    @staticmethod
    def _unwrap_annotated(annotation):
        origin = get_origin(annotation)
        if origin is Annotated:
            args = get_args(annotation)
            if args:
                return args[0]
        return annotation

    @staticmethod
    def _unwrap_optional(annotation):
        origin = get_origin(annotation)
        if origin is None:
            return annotation
        args = get_args(annotation)
        if origin in (types.UnionType, typing.Union):
            non_none = [arg for arg in args if arg is not type(None)]
            if len(non_none) == 1:
                return non_none[0]
        return annotation

    @staticmethod
    def _unwrap_list(annotation):
        origin = get_origin(annotation)
        if origin is list:
            args = get_args(annotation)
            if args:
                return True, args[0]
        return False, annotation

    @classmethod
    def from_schema(cls, schema_obj: S, model_class: Type[T]) -> T:
        try:
            data = schema_obj.model_dump()
            fields = {col.name for col in model_class.__table__.columns}
            filtered = {k: v for k, v in data.items() if k in fields}
            return model_class(**filtered)
        except Exception as exc:
            raise ModelMapperException(f"Error converting schema to model: {exc}")

    @classmethod
    def from_model(cls, model_obj: T, schema_class: Type[S]) -> S:
        try:
            data = {
                attr: getattr(model_obj, attr)
                for attr in model_obj.__table__.columns.keys()
            }
            for field_name, field_info in schema_class.model_fields.items():
                if field_name in data:
                    continue
                if not hasattr(model_obj, field_name):
                    continue
                value = getattr(model_obj, field_name)
                annotation = cls._unwrap_annotated(field_info.annotation)
                annotation = cls._unwrap_optional(annotation)
                is_list, inner = cls._unwrap_list(annotation)
                if is_list:
                    if value is None:
                        data[field_name] = None
                    elif isinstance(inner, type) and issubclass(inner, BaseModel):
                        data[field_name] = [
                            cls.from_model(item, inner) for item in value
                        ]
                    else:
                        data[field_name] = value
                else:
                    if value is None:
                        data[field_name] = None
                    elif isinstance(annotation, type) and issubclass(annotation, BaseModel):
                        data[field_name] = cls.from_model(value, annotation)
                    else:
                        data[field_name] = value
            return schema_class(**data)
        except Exception as exc:
            raise ModelMapperException(f"Error converting model to schema: {exc}")

    @classmethod
    def from_model_list(cls, model_list: list[T], schema_class: Type[S]) -> list[S]:
        try:
            return [cls.from_model(model, schema_class) for model in model_list]
        except Exception as exc:
            raise ModelMapperException(
                f"Error converting model list to schema list: {exc}"
            )

    @classmethod
    def from_schema_list(cls, schema_list: list[S], model_class: Type[T]) -> list[T]:
        try:
            return [cls.from_schema(schema, model_class) for schema in schema_list]
        except Exception as exc:
            raise ModelMapperException(
                f"Error converting schema list to model list: {exc}"
            )

    @classmethod
    def from_schema_to_schema(cls, schema_obj: S, schema_class: Type[S]) -> S:
        try:
            data = schema_obj.model_dump()
            fields = schema_class.model_fields.keys()
            filtered = {k: v for k, v in data.items() if k in fields}
            return schema_class(**filtered)
        except Exception as exc:
            raise ModelMapperException(f"Error converting schema to schema: {exc}")
