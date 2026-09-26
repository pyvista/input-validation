"""Type aliases for annotating the inputs and outputs of the validation functions."""

from __future__ import annotations

from ._guards import is_array_0d
from ._guards import is_array_1d
from ._guards import is_array_2d
from ._guards import is_array_3d
from ._guards import is_array_nd
from ._typing import ArrayLike
from ._typing import ArrayLikeBool
from ._typing import ArrayLikeFloat
from ._typing import ArrayLikeInt
from ._typing import MatrixLike
from ._typing import MatrixLikeBool
from ._typing import MatrixLikeFloat
from ._typing import MatrixLikeInt
from ._typing import RotationLike
from ._typing import TransformLike
from ._typing import VectorLike
from ._typing import VectorLikeBool
from ._typing import VectorLikeFloat
from ._typing import VectorLikeInt
from ._typing import _Array0D as Array0D
from ._typing import _Array1D as Array1D
from ._typing import _Array2D as Array2D
from ._typing import _Array3D as Array3D
from ._typing import _ArrayND as ArrayND
from ._typing import _Floating as Floating
from ._typing import _Integer as Integer
from ._typing import _Real as Real
from ._typing import _Scalar as Scalar

__all__ = [
    'Array0D',
    'Array1D',
    'Array2D',
    'Array3D',
    'ArrayLike',
    'ArrayLikeBool',
    'ArrayLikeFloat',
    'ArrayLikeInt',
    'ArrayND',
    'Floating',
    'Integer',
    'MatrixLike',
    'MatrixLikeBool',
    'MatrixLikeFloat',
    'MatrixLikeInt',
    'Real',
    'RotationLike',
    'Scalar',
    'TransformLike',
    'VectorLike',
    'VectorLikeBool',
    'VectorLikeFloat',
    'VectorLikeInt',
    'is_array_0d',
    'is_array_1d',
    'is_array_2d',
    'is_array_3d',
    'is_array_nd',
]
