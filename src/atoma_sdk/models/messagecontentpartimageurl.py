"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from atoma_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class MessageContentPartImageURLTypedDict(TypedDict):
    r"""Represents the image URL of a message content part.

    This is used to represent the image URL of a message content part in the chat completion request.
    It can be either a URL or a base64 encoded image data.
    """

    url: str
    r"""Either a URL of the image or the base64 encoded image data."""
    detail: NotRequired[Nullable[str]]
    r"""Specifies the detail level of the image."""


class MessageContentPartImageURL(BaseModel):
    r"""Represents the image URL of a message content part.

    This is used to represent the image URL of a message content part in the chat completion request.
    It can be either a URL or a base64 encoded image data.
    """

    url: str
    r"""Either a URL of the image or the base64 encoded image data."""

    detail: OptionalNullable[str] = UNSET
    r"""Specifies the detail level of the image."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["detail"]
        nullable_fields = ["detail"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
