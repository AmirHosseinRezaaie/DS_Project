import math
from typing import Optional, Dict
from graphviz import Digraph  # Import for visualization

class Node:
    def __init__(self, value: any, left: Optional['Node'] = None, right: Optional['Node'] = None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(rpn: List[any]) -> Optional[Node]:
    """
    Build binary expression tree from RPN.
    """
    stack = []
    
    for token in rpn:
        if isinstance(token, (int, float, str)):
            stack.append(Node(token))
        else:
            if token == "√" or (token == "-" and len(stack) == 1):
                left = stack.pop()
                right = None
            else:
                right = stack.pop()
                left = stack.pop()
            stack.append(Node(token, left, right))
    
    if len(stack) != 1:
        raise ValueError("Invalid RPN")
    
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
    Evaluate tree with variables.
    """
    if node is None:
        raise ValueError("None node")
    
    if isinstance(node.value, (int, float)):
        return float(node.value)
    
    if isinstance(node.value, str):
        return variables.get(node.value, raise ValueError(f"Undefined: {node.value}"))
    
    left_val = evaluate_tree(node.left, variables) if node.left else None
    right_val = evaluate_tree(node.right, variables) if node.right else None
    
    ops = {
        "+": lambda: left_val + right_val,
        "-": lambda: -left_val if right_val is None else left_val - right_val,
        "*": lambda: left_val * right_val,
        "/": lambda: left_val / right_val if right_val != 0 else raise ZeroDivisionError("Division by zero"),
        "^": lambda: math.pow(left_val, right_val),
        "√": lambda: math.sqrt(left_val) if left_val >= 0 else raise ValueError("Negative sqrt")
    }
    return ops.get(node.value, lambda: raise ValueError(f"Unknown op: {node.value}"))()

def visualize_tree(root: Optional[Node], filename: str = "expression_tree.png"):
    """
    Visualize tree using Graphviz and save as PNG.
    """
    if root is None:
        return
    dot = Digraph()
    def add_nodes(node, parent=None):
        if node:
            node_id = str(id(node))
            dot.node(node_id, str(node.value))
            if parent:
                dot.edge(parent, node_id)
            add_nodes(node.left, node_id)
            add_nodes(node.right, node_id)
    add_nodes(root)
    dot.render(filename, format='png', cleanup=True)
    print(f"Tree saved as {filename}")