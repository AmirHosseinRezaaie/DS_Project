"""
Advanced Mathematical Expression Evaluator
A comprehensive expression parser and evaluator with tree visualization.
"""

from .parser import clean_input, normalize_signs, tokenize, to_rpn
from .tree import Node, build_tree, evaluate_tree, print_tree, visualize_tree
from .variables import parse_variables

__version__ = "1.0.0"
__author__ = "AmirHosseinRezaaie"

__all__ = [
    'clean_input',
    'normalize_signs', 
    'tokenize',
    'to_rpn',
    'Node',
    'build_tree',
    'evaluate_tree',
    'print_tree',
    'visualize_tree',
    'parse_variables'
]