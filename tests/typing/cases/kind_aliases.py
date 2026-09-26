"""Typing cases for the array-like aliases of one kind."""

from __future__ import annotations

from typing import Any

import numpy as np
import numpy.typing as npt
from type_assert import assert_types

from pyvista_validation.typing import ArrayLikeBool
from pyvista_validation.typing import ArrayLikeFloat
from pyvista_validation.typing import ArrayLikeInt
from pyvista_validation.typing import MatrixLikeBool
from pyvista_validation.typing import MatrixLikeFloat
from pyvista_validation.typing import MatrixLikeInt
from pyvista_validation.typing import VectorLikeBool
from pyvista_validation.typing import VectorLikeFloat
from pyvista_validation.typing import VectorLikeInt

# Declared rather than inferred, so each case reads the array type it names.
FLOATS: npt.NDArray[np.float32] = np.zeros(3, dtype=np.float32)
INTS: npt.NDArray[np.int64] = np.zeros(3, dtype=np.int64)
BOOLS: npt.NDArray[np.bool_] = np.zeros(3, dtype=bool)
UNKNOWN: npt.NDArray[Any] = np.zeros(3)
UNKNOWN_MATRIX: npt.NDArray[Any] = np.zeros((2, 3))
COMPLEX: npt.NDArray[np.complex128] = np.zeros(3, dtype=complex)
MATRIX: np.ndarray[tuple[int, int], np.dtype[np.float64]] = np.zeros((2, 3))
VECTOR: np.ndarray[tuple[int], np.dtype[np.float64]] = np.zeros(3)


def vector_float(value: VectorLikeFloat) -> VectorLikeFloat:
    """Pass a float vector-like through."""
    return value


def vector_int(value: VectorLikeInt) -> VectorLikeInt:
    """Pass an int vector-like through."""
    return value


def vector_bool(value: VectorLikeBool) -> VectorLikeBool:
    """Pass a bool vector-like through."""
    return value


def matrix_float(value: MatrixLikeFloat) -> MatrixLikeFloat:
    """Pass a float matrix-like through."""
    return value


def matrix_int(value: MatrixLikeInt) -> MatrixLikeInt:
    """Pass an int matrix-like through."""
    return value


def matrix_bool(value: MatrixLikeBool) -> MatrixLikeBool:
    """Pass a bool matrix-like through."""
    return value


def array_float(value: ArrayLikeFloat) -> ArrayLikeFloat:
    """Pass a float array-like through."""
    return value


def array_int(value: ArrayLikeInt) -> ArrayLikeInt:
    """Pass an int array-like through."""
    return value


def array_bool(value: ArrayLikeBool) -> ArrayLikeBool:
    """Pass a bool array-like through."""
    return value


# The float kind takes Python ints and bools, and integer and boolean arrays, as floats.
assert_types(vector_float([1.0, 2.0]), VectorLikeFloat)
assert_types(vector_float((np.float32(1), np.int8(2))), VectorLikeFloat)
assert_types(vector_float(FLOATS), VectorLikeFloat)
assert_types(vector_float(INTS), VectorLikeFloat)
assert_types(vector_float(BOOLS), VectorLikeFloat)
assert_types(vector_float(UNKNOWN), VectorLikeFloat)
assert_types(vector_float(VECTOR), VectorLikeFloat)
assert_types(vector_int([1, 2]), VectorLikeInt)
assert_types(vector_int(INTS), VectorLikeInt)
assert_types(vector_int(BOOLS), VectorLikeInt)
assert_types(vector_bool([True, False]), VectorLikeBool)
assert_types(vector_bool(BOOLS), VectorLikeBool)

# A matrix is a 2-D array or a sequence of vectors, which may themselves be arrays.
assert_types(matrix_float([[1.0, 2.0], [3.0, 4.0]]), MatrixLikeFloat)
assert_types(matrix_float([FLOATS, INTS]), MatrixLikeFloat)
assert_types(matrix_float(MATRIX), MatrixLikeFloat)
assert_types(matrix_float(UNKNOWN_MATRIX), MatrixLikeFloat)
assert_types(matrix_int([[1, 2], [3, 4]]), MatrixLikeInt)
assert_types(matrix_bool([[True], [False]]), MatrixLikeBool)

# An array-like is an array of any rank, or sequences nested up to four deep.
assert_types(array_float(MATRIX), ArrayLikeFloat)
assert_types(array_float([[[1.0]]]), ArrayLikeFloat)
assert_types(array_float([[[[1.0]]]]), ArrayLikeFloat)
assert_types(array_float([FLOATS, FLOATS]), ArrayLikeFloat)
assert_types(array_int([[1], [2]]), ArrayLikeInt)
assert_types(array_bool([[True], [False]]), ArrayLikeBool)


# Never called: the runtime half rejects promotion, so it is checked statically only.
def promoted() -> None:
    """Pass Python ints and bools where floats and ints are expected."""
    vector_float([1.0, 2, True])
    vector_int([1, 2, True])
    matrix_float([[1.0, 2], [3, True]])


# Never called; each ignore is reported as unused if the checker stops rejecting the call.
def rejected() -> None:
    """Pass inputs of the wrong kind or rank."""
    vector_float(COMPLEX)  # type: ignore[arg-type]
    vector_float(['a'])  # type: ignore[list-item]
    vector_float(MATRIX)  # type: ignore[arg-type]
    vector_int([1.5])  # type: ignore[list-item]
    vector_int(FLOATS)  # type: ignore[arg-type]
    vector_bool([1])  # type: ignore[list-item]
    vector_bool(INTS)  # type: ignore[arg-type]
    matrix_float(VECTOR)  # type: ignore[arg-type]
    matrix_int([[1.5]])  # type: ignore[list-item]
    array_int(FLOATS)  # type: ignore[arg-type]
    array_bool([[1]])  # type: ignore[arg-type]
