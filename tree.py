import math

def evaluate_tree(node: Optional[Node]) -> float:
    """
    Recursively evaluate the expression tree.
    Returns float result.
    """
    if node is None:
        raise ValueError("Cannot evaluate None node")

    # برگ: عدد
    if isinstance(node.value, int):
        return float(node.value)

    # عملگرها
    if node.value == "+":
        return evaluate_tree(node.left) + evaluate_tree(node.right)

    if node.value == "-":
        if node.right is None:  # عملگر یک‌تایی منفی (مثل -5)
            return -evaluate_tree(node.left)
        return evaluate_tree(node.left) - evaluate_tree(node.right)

    if node.value == "*":
        return evaluate_tree(node.left) * evaluate_tree(node.right)

    if node.value == "/":
        left_val = evaluate_tree(node.left)
        right_val = evaluate_tree(node.right)
        if right_val == 0:
            raise ZeroDivisionError("Division by zero occurred!")
        return left_val / right_val

    if node.value == "^":
        left_val = evaluate_tree(node.left)
        right_val = evaluate_tree(node.right)
        return math.pow(left_val, right_val)

    if node.value == "√":
        if node.left is None:
            raise ValueError("√ operator missing operand")
        val = evaluate_tree(node.left)
        if val < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(val)

    raise ValueError(f"Unknown operator: {node.value}")