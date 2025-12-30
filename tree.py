import math
from typing import Optional, Dict

class Node:
    def __init__(self, value: any, left: Optional['Node'] = None, right: Optional['Node'] = None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(rpn: List[any]) -> Optional[Node]:
    """
    Build binary expression tree from RPN.
    Handles unary - and √.
    Treat variables as leaves.
    """
    stack = []
    
    for token in rpn:
        if isinstance(token, (int, float, str)):  # Number or variable (str)
            stack.append(Node(token))
        else:  # Operator
            if token == "√" or token == "-":  # Unary possible for -
                if len(stack) < 1:
                    raise ValueError("Invalid RPN for unary operator")
                right = None
                left = stack.pop()
            else:
                if len(stack) < 2:
                    raise ValueError("Invalid RPN")
                right = stack.pop()
                left = stack.pop()
            
            stack.append(Node(token, left, right))
    
    if len(stack) != 1:
        raise ValueError("Invalid RPN expression")
    
    return stack[0]

def print_tree(node: Optional[Node], indent: str = ""):
    """
    Print tree structure.
    """
    if node is None:
        return
    print(f"{indent}{node.value}")
    if node.left:
        print_tree(node.left, indent + "├── ")
    if node.right:
        print_tree(node.right, indent + "└── ")

def evaluate_tree(node: Optional[Node], variables: Dict[str, float] = {}) -> float:
    """
    Evaluate tree recursively with variables.
    """
    if node is None:
        raise ValueError("Cannot evaluate None node")

    if isinstance(node.value, (int, float)):
        return float(node.value)
    
    if isinstance(node.value, str):  # Variable
        if node.value in variables:
            return variables[node.value]
        raise ValueError(f"Undefined variable: {node.value}")

    left_val = evaluate_tree(node.left, variables) if node.left else None
    right_val = evaluate_tree(node.right, variables) if node.right else None

    if node.value == "+":
        return left_val + right_val
    
    if node.value == "-":
        if right_val is None:  # Unary -
            return -left_val
        return left_val - right_val
    
    if node.value == "*":
        return left_val * right_val
    
    if node.value == "/":
        if right_val == 0:
            raise ZeroDivisionError("Division by zero!")
        return left_val / right_val
    
    if node.value == "^":
        return math.pow(left_val, right_val)
    
    if node.value == "√":
        if left_val < 0:
            raise ValueError("Square root of negative!")
        return math.sqrt(left_val)
    
    raise ValueError(f"Unknown operator: {node.value}")