#!/usr/bin/python3
""" a function that multiplies 2 matrices by using the module NumPy"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Returns multiple of 2 matrix`"""
    return numpy.matmul(m_a, m_b)
