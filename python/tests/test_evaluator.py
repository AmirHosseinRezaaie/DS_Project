import sys
sys.path.insert(0, '../src')

from parser import clean_input, normalize_signs, tokenize, to_rpn
from tree import build_tree, evaluate_tree
from variables import parse_variables


def test_basic_operations():
    """Test basic arithmetic"""
    cases = [
        ("3 + 4", {}, 7.0),
        ("10 - 5", {}, 5.0),
        ("3 * 4", {}, 12.0),
        ("10 / 2", {}, 5.0),
        ("2 ^ 3", {}, 8.0),
    ]
    
    for expr, vars, expected in cases:
        result = evaluate_expression(expr, vars)
        assert abs(result - expected) < 0.001, f"Failed: {expr}"


def test_precedence():
    """Test operator precedence"""
    cases = [
        ("3 + 4 * 2", {}, 11.0),
        ("(3 + 4) * 2", {}, 14.0),
        ("2 ^ 3 ^ 2", {}, 512.0),  # Right associative
    ]
    
    for expr, vars, expected in cases:
        result = evaluate_expression(expr, vars)
        assert abs(result - expected) < 0.001, f"Failed: {expr}"


def test_unary_operations():
    """Test unary operators"""
    cases = [
        ("√16", {}, 4.0),
        ("√(9 + 16)", {}, 5.0),
        ("-5", {}, -5.0),
    ]
    
    for expr, vars, expected in cases:
        result = evaluate_expression(expr, vars)
        assert abs(result - expected) < 0.001, f"Failed: {expr}"


def test_variables():
    """Test variable substitution"""
    cases = [
        ("x", {"x": 10.0}, 10.0),
        ("x + 5", {"x": 10.0}, 15.0),
        ("x^2 + 2*x + 1", {"x": 3.0}, 16.0),
    ]
    
    for expr, vars, expected in cases:
        result = evaluate_expression(expr, vars)
        assert abs(result - expected) < 0.001, f"Failed: {expr}"


def test_complex_expressions():
    """Test complex expressions"""
    expr = "√(4^2 + 3^2) * (x + 5) - 10 / 2"
    vars = {"x": 7.0}
    expected = 55.0
    
    result = evaluate_expression(expr, vars)
    assert abs(result - expected) < 0.001


def test_errors():
    """Test error handling"""
    import pytest
    
    # Division by zero
    with pytest.raises(ZeroDivisionError):
        evaluate_expression("10 / 0", {})
    
    # Negative sqrt
    with pytest.raises(ValueError):
        evaluate_expression("√(-4)", {})
    
    # Undefined variable
    with pytest.raises(ValueError):
        evaluate_expression("x + 5", {})


def evaluate_expression(expr, variables):
    """Helper function"""
    cleaned = clean_input(expr)
    normalized = normalize_signs(cleaned)
    tokens = tokenize(normalized)
    rpn = to_rpn(tokens)
    root = build_tree(rpn)
    return evaluate_tree(root, variables)


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])