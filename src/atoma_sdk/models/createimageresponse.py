"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .imagedata import ImageData, ImageDataTypedDict
from atoma_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class CreateImageResponseTypedDict(TypedDict):
    r"""Response format for image generation"""

    created: int
    data: List[ImageDataTypedDict]


class CreateImageResponse(BaseModel):
    r"""Response format for image generation"""

    created: int

    data: List[ImageData]
