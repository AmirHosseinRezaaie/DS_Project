import math
from typing import Optional, Dict, List
from graphviz import Digraph


class Node:
    def __init__(self, value, left: Optional['Node'] = None, right: Optional['Node'] = None):
        self.value = value
        self.left = left
        self.right = right


def build_tree(rpn: List) -> Optional[Node]:
    """Build binary expression tree from RPN"""
    stack = []
    
    for token in rpn:
        # Operand (number or variable)
        if isinstance(token, (int, float, str)) and token not in "+-*/^√":
            stack.append(Node(token))
        # Operator
        else:
            # Unary operators (√ or unary -)
            if token == "√":
                if not stack:
                    raise ValueError("Invalid expression")
                operand = stack.pop()
                stack.append(Node(token, operand, None))
            # Binary operators
            else:
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(token, left, right))
    
    if len(stack) != 1:
        raise ValueError("Invalid RPN")
    
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
    
    # Variable
    if isinstance(node.value, str) and node.value not in "+-*/^√":
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


def visualize_tree(root: Optional[Node], filename: str = "expression_tree"):
    """Generate tree visualization using Graphviz"""
    if root is None:
        print("Empty tree, no visualization generated")
        return
    
    dot = Digraph(comment='Expression Tree')
    dot.attr(rankdir='TB')
    
    def add_nodes(node, parent_id=None):
        if node is None:
            return
        
        node_id = str(id(node))
        label = str(node.value)
        dot.node(node_id, label)
        
        if parent_id:
            dot.edge(parent_id, node_id)
        
        add_nodes(node.left, node_id)
        add_nodes(node.right, node_id)
    
    add_nodes(root)
    dot.render(filename, format='png', cleanup=True)
    print(f"Tree visualization saved as {filename}.png")