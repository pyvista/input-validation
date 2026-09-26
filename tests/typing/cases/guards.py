"""Typing cases for the rank type guards."""

from __future__ import annotations

from typing import Any

import numpy as np
import numpy.typing as npt
from type_assert import assert_types

from pyvista_validation.typing import Array0D
from pyvista_validation.typing import Array1D
from pyvista_validation.typing import Array2D
from pyvista_validation.typing import Array3D
from pyvista_validation.typing import ArrayND
from pyvista_validation.typing import is_array_0d
from pyvista_validation.typing import is_array_1d
from pyvista_validation.typing import is_array_2d
from pyvista_validation.typing import is_array_3d
from pyvista_validation.typing import is_array_nd

# Declared rather than inferred, so each case reads the array type it names.
SCALAR: npt.NDArray[np.float64] = np.array(1.0)
VECTOR: npt.NDArray[np.float64] = np.zeros(2)
MATRIX: npt.NDArray[np.int32] = np.zeros((2, 2), dtype=np.int32)
CUBE: npt.NDArray[np.bool_] = np.zeros((2, 2, 2), dtype=bool)
UNKNOWN: npt.NDArray[Any] = np.zeros(2)
F32_OR_TEXT: npt.NDArray[np.float32] | npt.NDArray[np.str_] = np.zeros(2, dtype=np.float32)
LIST_OR_ARRAY: list[float] | npt.NDArray[np.float64] = np.zeros(2)
ANYTHING: object = np.zeros(2)

# A guard narrows the rank and keeps a dtype the checker already knows.
assert_types(SCALAR if is_array_0d(SCALAR) else None, Array0D[np.float64] | None)
assert_types(VECTOR if is_array_1d(VECTOR) else None, Array1D[np.float64] | None)
assert_types(MATRIX if is_array_2d(MATRIX) else None, Array2D[np.int32] | None)
assert_types(CUBE if is_array_3d(CUBE) else None, Array3D[np.bool_] | None)
assert_types(VECTOR if is_array_nd(VECTOR) else None, ArrayND[np.float64] | None)

# An unknown dtype stays unknown, each member of a union is narrowed, and non-arrays drop out.
assert_types(UNKNOWN if is_array_1d(UNKNOWN) else None, Array1D[Any] | None)
assert_types(
    F32_OR_TEXT if is_array_1d(F32_OR_TEXT) else None,
    Array1D[np.float32] | Array1D[np.str_] | None,
)
assert_types(LIST_OR_ARRAY if is_array_1d(LIST_OR_ARRAY) else None, Array1D[np.float64] | None)
assert_types(ANYTHING if is_array_1d(ANYTHING) else None, Array1D[Any] | None)

# A dtype narrows the dtype too, to the members of a union that match it.
assert_types(UNKNOWN if is_array_1d(UNKNOWN, np.floating) else None, Array1D[np.floating] | None)
assert_types(
    F32_OR_TEXT if is_array_1d(F32_OR_TEXT, np.floating) else None, Array1D[np.float32] | None
)
assert_types(
    ANYTHING if is_array_2d(ANYTHING, np.dtype(np.int32)) else None, Array2D[np.int32] | None
)
assert_types(is_array_1d(VECTOR), bool)
