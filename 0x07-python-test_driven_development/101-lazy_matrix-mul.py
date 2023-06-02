#!/usr/bin/python3.5
"""
This module multiplies 2 matrixes
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrixes
    Args:
        m_a: matrix a
        m_b: matrix b
    Returns:
        result of the multiplication
    """

    return (np.matmul(m_a, m_b))
