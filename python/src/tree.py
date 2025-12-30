import math
from typing import Optional, Dict, List
from graphviz import Digraph
import os


class Node:
    def __init__(self, value, left: Optional['Node'] = None, right: Optional['Node'] = None):
        self.value = value
        self.left = left
        self.right = right


def build_tree(rpn: List) -> Optional[Node]:
    """Build binary expression tree from RPN"""
    stack = []
    operators = {'+', '-', '*', '/', '^', '√'}
    
    for token in rpn:
        # Check if token is an operator
        if token in operators:
            # Unary operators (√)
            if token == '√':
                if not stack:
                    raise ValueError("Invalid expression: sqrt without operand")
                operand = stack.pop()
                stack.append(Node(token, operand, None))
            # Binary operators
            else:
                if len(stack) < 2:
                    raise ValueError(f"Invalid expression: {token} needs two operands")
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(token, left, right))
        # Operand (number or variable)
        else:
            stack.append(Node(token))
    
    if len(stack) != 1:
        raise ValueError("Invalid RPN: too many operands")
    
    return stack[0]


def print_tree(node: Optional[Node], prefix: str = "", is_tail: bool = True):
    """Print tree structure with proper formatting"""
    if node is None:
        return
    
    print(prefix + ("└── " if is_tail else "├── ") + str(node.value))
    
    children = []
    if node.left:
        children.append(node.left)
    if node.right:
        children.append(node.right)
    
    for i, child in enumerate(children):
        is_last = (i == len(children) - 1)
        extension = "    " if is_tail else "│   "
        print_tree(child, prefix + extension, is_last)


def evaluate_tree(node: Optional[Node], variables: Dict[str, float] = None) -> float:
    """Evaluate expression tree with variable substitution"""
    if variables is None:
        variables = {}
    
    if node is None:
        raise ValueError("None node encountered")
    
    # Number
    if isinstance(node.value, (int, float)):
        return float(node.value)
    
    # Variable (string that's not an operator)
    if isinstance(node.value, str):
        operators = {'+', '-', '*', '/', '^', '√'}
        if node.value not in operators:
            if node.value not in variables:
                raise ValueError(f"Undefined variable: {node.value}")
            return variables[node.value]
    
    # Evaluate children
    left_val = evaluate_tree(node.left, variables) if node.left else None
    right_val = evaluate_tree(node.right, variables) if node.right else None
    
    # Apply operator
    op = node.value
    if op == '+':
        return left_val + right_val
    elif op == '-':
        return left_val - right_val
    elif op == '*':
        return left_val * right_val
    elif op == '/':
        if right_val == 0:
            raise ZeroDivisionError("Division by zero")
        return left_val / right_val
    elif op == '^':
        return math.pow(left_val, right_val)
    elif op == '√':
        if left_val < 0:
            raise ValueError("Square root of negative number")
        return math.sqrt(left_val)
    else:
        raise ValueError(f"Unknown operator: {op}")


def visualize_tree(root: Optional[Node], filename: str = "expression_tree", output_dir: str = "../output"):
    """
    Generate tree visualization using Graphviz and save to output directory.
    
    Args:
        root: Root node of expression tree
        filename: Name of output file (without extension)
        output_dir: Directory to save output (relative to src/)
    """
    if root is None:
        print("Empty tree, no visualization generated")
        return
    
    # Create output directory if it doesn't exist
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_output_dir = os.path.join(script_dir, output_dir)
    os.makedirs(full_output_dir, exist_ok=True)
    
    # Create Graphviz object
    dot = Digraph(comment='Expression Tree')
    dot.attr(rankdir='TB')
    dot.attr('node', shape='circle', style='filled', fillcolor='lightblue')
    
    operators = {'+', '-', '*', '/', '^', '√'}
    
    def add_nodes(node, parent_id=None):
        if node is None:
            return
        
        node_id = str(id(node))
        label = str(node.value)
        
        # Color coding for different node types
        if isinstance(node.value, (int, float)):
            dot.node(node_id, label, fillcolor='lightgreen')
        elif isinstance(node.value, str) and node.value not in operators:
            dot.node(node_id, label, fillcolor='lightyellow')  # Variables
        else:
            dot.node(node_id, label, fillcolor='lightblue')  # Operators
        
        if parent_id:
            dot.edge(parent_id, node_id)
        
        add_nodes(node.left, node_id)
        add_nodes(node.right, node_id)
    
    add_nodes(root)
    
    # Save to output directory
    output_path = os.path.join(full_output_dir, filename)
    dot.render(output_path, format='png', cleanup=True)
    
    print(f"✓ Tree visualization saved: {output_path}.png")