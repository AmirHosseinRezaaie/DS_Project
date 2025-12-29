"""
Module for expression tree: Node class, building, printing, and evaluation.
"""

from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class Node:
    value: Any          # int یا str (عملگر)
    left: Optional['Node'] = None
    right: Optional['Node'] = None

    def __repr__(self) -> str:
        return f"Node({repr(self.value)})"


def build_tree(rpn: list) -> Node:
    """
    Build expression tree from Reverse Polish Notation.
    Uses a stack-based approach.
    """
    if not rpn:
        raise ValueError("Empty RPN expression")

    stack: list[Node] = []

    for item in rpn:
        if isinstance(item, int):  # عدد
            stack.append(Node(item))

        else:  # عملگر
            if item == "√":
                # عملگر یک‌تایی: فقط فرزند چپ
                if not stack:
                    raise ValueError("Invalid RPN: missing operand for √")
                left = stack.pop()
                node = Node("√", left=left, right=None)
                stack.append(node)

            else:
                # عملگر دودویی
                if len(stack) < 2:
                    raise ValueError(f"Invalid RPN: not enough operands for {item}")
                right = stack.pop()
                left = stack.pop()
                node = Node(item, left=left, right=right)
                stack.append(node)

    if len(stack) != 1:
        raise ValueError("Invalid RPN: multiple roots remain")

    return stack[0]


def print_tree(node: Optional[Node], level: int = 0, prefix: str = "Root: ") -> None:
    """
    Simple indented tree printing for debugging.
    """
    if node is not None:
        print("  " * level + prefix + str(node.value))
        if node.left:
            print_tree(node.left, level + 1, "L── ")
        if node.right:
            print_tree(node.right, level + 1, "R── ")