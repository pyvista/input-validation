"""Core type aliases."""

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Union

from ._array_like import ArrayLikeFloat
from ._array_like import MatrixLikeFloat
from ._array_like import _FloatDType

if TYPE_CHECKING:
    from pyvista_validation import _lazy_import

RotationLike = Union[
    MatrixLikeFloat, '_lazy_import.vtkMatrix3x3', '_lazy_import.Rotation[tuple[()]]'
]
TransformLike = Union[RotationLike, '_lazy_import.vtkMatrix4x4', '_lazy_import.vtkTransform']

# A scalar or any array-like.
_ArrayLikeOrScalar = Union[float, _FloatDType, ArrayLikeFloat]
