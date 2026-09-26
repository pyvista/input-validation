"""Type guards for NumPy arrays by rank, matching optype's ``is_array_*`` functions."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING
from typing import Any
from typing import cast
from typing import overload

import numpy as np

from pyvista_validation.check import _issubdtype

if sys.version_info >= (3, 13):
    from typing import TypeVar
else:
    from typing_extensions import TypeVar

if TYPE_CHECKING:
    from typing import TypeAlias

    from typing_extensions import TypeIs

    from pyvista_validation._typing import _Array0D
    from pyvista_validation._typing import _Array1D
    from pyvista_validation._typing import _Array2D
    from pyvista_validation._typing import _Array3D
    from pyvista_validation._typing import _ArrayND

    # A scalar type or a dtype, as optype's ToDType; np.generic cannot be subscripted at runtime.
    _AnyDTypeLike: TypeAlias = type[np.generic[object]] | np.dtype[np.generic[object]]

_ScalarT = TypeVar('_ScalarT', bound='np.generic[object]', default='np.generic[object]')
_ToDType: TypeAlias = 'type[_ScalarT] | np.dtype[_ScalarT]'


def _ndim(a: object, dtype: _AnyDTypeLike | None, /) -> int:
    """Return the rank of ``a`` if it is an array with a subtype of ``dtype``, else -1."""
    if not isinstance(a, np.ndarray):
        return -1
    array = cast('np.ndarray[tuple[int, ...], np.dtype[np.generic[object]]]', a)
    return array.ndim if dtype is None or _issubdtype(array.dtype, dtype) else -1


# fmt: off
@overload
def is_array_nd(a: object, /, dtype: None = None) -> TypeIs[_ArrayND[Any]]: ...
@overload
def is_array_nd(a: object, /, dtype: _ToDType[_ScalarT]) -> TypeIs[_ArrayND[_ScalarT]]: ...
# fmt: on
def is_array_nd(a: object, /, dtype: _AnyDTypeLike | None = None) -> bool:
    """Return whether ``a`` is an array, with a subtype of ``dtype`` if given."""
    return _ndim(a, dtype) >= 0


# fmt: off
@overload
def is_array_0d(a: object, /, dtype: None = None) -> TypeIs[_Array0D[Any]]: ...
@overload
def is_array_0d(a: object, /, dtype: _ToDType[_ScalarT]) -> TypeIs[_Array0D[_ScalarT]]: ...
# fmt: on
def is_array_0d(a: object, /, dtype: _AnyDTypeLike | None = None) -> bool:
    """Return whether ``a`` is a 0-D array, with a subtype of ``dtype`` if given."""
    return _ndim(a, dtype) == 0


# fmt: off
@overload
def is_array_1d(a: object, /, dtype: None = None) -> TypeIs[_Array1D[Any]]: ...
@overload
def is_array_1d(a: object, /, dtype: _ToDType[_ScalarT]) -> TypeIs[_Array1D[_ScalarT]]: ...
# fmt: on
def is_array_1d(a: object, /, dtype: _AnyDTypeLike | None = None) -> bool:
    """Return whether ``a`` is a 1-D array, with a subtype of ``dtype`` if given."""
    return _ndim(a, dtype) == 1


# fmt: off
@overload
def is_array_2d(a: object, /, dtype: None = None) -> TypeIs[_Array2D[Any]]: ...
@overload
def is_array_2d(a: object, /, dtype: _ToDType[_ScalarT]) -> TypeIs[_Array2D[_ScalarT]]: ...
# fmt: on
def is_array_2d(a: object, /, dtype: _AnyDTypeLike | None = None) -> bool:
    """Return whether ``a`` is a 2-D array, with a subtype of ``dtype`` if given."""
    return _ndim(a, dtype) == 2


# fmt: off
@overload
def is_array_3d(a: object, /, dtype: None = None) -> TypeIs[_Array3D[Any]]: ...
@overload
def is_array_3d(a: object, /, dtype: _ToDType[_ScalarT]) -> TypeIs[_Array3D[_ScalarT]]: ...
# fmt: on
def is_array_3d(a: object, /, dtype: _AnyDTypeLike | None = None) -> bool:
    """Return whether ``a`` is a 3-D array, with a subtype of ``dtype`` if given."""
    return _ndim(a, dtype) == 3
