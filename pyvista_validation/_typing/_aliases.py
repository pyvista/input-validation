"""Core type aliases."""

from __future__ import annotations

from collections.abc import Sequence
import sys
from typing import TYPE_CHECKING
from typing import Union

import numpy as np
import numpy.typing as npt

from ._array_like import _AnyDType
from ._array_like import _Array1D
from ._array_like import _Array2D

if sys.version_info >= (3, 13):
    from typing import TypeVar
else:
    from typing_extensions import TypeVar

if TYPE_CHECKING:
    from pyvista_validation import _lazy_import

# Array-likes of one kind, matching optype's ToFloat1D and friends; a float admits int and bool.
_PyT = TypeVar('_PyT', default=float)
_DTypeT = TypeVar('_DTypeT', bound=_AnyDType, default=_AnyDType)
_Item = Union[_PyT, _DTypeT, npt.NDArray[_DTypeT]]
# _PyT comes first in each alias, since a generic alias takes its parameters in that order.
_VectorLikeOf = Union[Sequence[Union[_PyT, _DTypeT]], _Array1D[_DTypeT]]
_MatrixLikeOf = Union[Sequence[_VectorLikeOf[_PyT, _DTypeT]], _Array2D[_DTypeT]]
# Sequences nested up to four deep, each level holding items or shallower sequences.
_Nested1 = Sequence[_Item[_PyT, _DTypeT]]
_Nested2 = Sequence[Union[_Item[_PyT, _DTypeT], _Nested1[_PyT, _DTypeT]]]
_Nested3 = Sequence[Union[_Item[_PyT, _DTypeT], _Nested1[_PyT, _DTypeT], _Nested2[_PyT, _DTypeT]]]
_Nested4 = Sequence[
    Union[
        _Item[_PyT, _DTypeT],
        _Nested1[_PyT, _DTypeT],
        _Nested2[_PyT, _DTypeT],
        _Nested3[_PyT, _DTypeT],
    ]
]
_ArrayLikeOf = Union[_Nested4[_PyT, _DTypeT], npt.NDArray[_DTypeT]]

_FloatDType = Union[np.floating, np.integer, np.bool_]
_IntDType = Union[np.integer, np.bool_]

VectorLikeFloat = _VectorLikeOf[float, _FloatDType]
VectorLikeInt = _VectorLikeOf[int, _IntDType]
VectorLikeBool = _VectorLikeOf[bool, np.bool_]
MatrixLikeFloat = _MatrixLikeOf[float, _FloatDType]
MatrixLikeInt = _MatrixLikeOf[int, _IntDType]
MatrixLikeBool = _MatrixLikeOf[bool, np.bool_]
ArrayLikeFloat = _ArrayLikeOf[float, _FloatDType]
ArrayLikeInt = _ArrayLikeOf[int, _IntDType]
ArrayLikeBool = _ArrayLikeOf[bool, np.bool_]

RotationLike = Union[
    MatrixLikeFloat, '_lazy_import.vtkMatrix3x3', '_lazy_import.Rotation[tuple[()]]'
]
TransformLike = Union[RotationLike, '_lazy_import.vtkMatrix4x4', '_lazy_import.vtkTransform']

# A scalar or any array-like.
_ArrayLikeOrScalar = Union[float, _FloatDType, ArrayLikeFloat]
