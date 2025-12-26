"""
Module for input processing: cleaning, normalization, and tokenization.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class Token:
    type: str      # NUMBER, OPERATOR, LPAREN, RPAREN
    value: any

    def __repr__(self) -> str:
        return f"Token({self.type}, {repr(self.value)})"


def clean_input(raw_input: str) -> str:
    """Remove all whitespace characters."""
    return raw_input.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "")


def normalize_signs(expression: str) -> str:
    """Handle consecutive + and - signs intelligently."""
    normalized = ""
    i = 0
    while i < len(expression):
        current = expression[i]

        if current in "0123456789()*/^√":
            normalized += current
            i += 1
            continue

        if current in "+-":
            sign_count = 0
            while i < len(expression) and expression[i] in "+-":
                if expression[i] == "-":
                    sign_count += 1
                i += 1

            is_unary = (
                not normalized or
                normalized[-1] in "(√" or
                (i < len(expression) and expression[i] == "√")
            )

            final_sign = "-" if sign_count % 2 == 1 else "+"

            if is_unary:
                if final_sign == "-":
                    normalized += "-"
            else:
                normalized += final_sign

            continue

        normalized += current
        i += 1

    return normalized


def tokenize(expression: str) -> List[Token]:
    """
    Convert normalized expression to list of tokens.
    Supports: numbers, +, -, *, /, ^, √, (, )
    """
    tokens = []
    i = 0
    while i < len(expression):
        ch = expression[i]

        # Numbers
        if ch.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            tokens.append(Token("NUMBER", num))
            continue

        # Operators
        if ch in "+-*/^":
            tokens.append(Token("OPERATOR", ch))
            i += 1
            continue

        # Square root (unary operator)
        if ch == "√":
            tokens.append(Token("OPERATOR", "√"))
            i += 1
            continue

        # Parentheses
        if ch == "(":
            tokens.append(Token("LPAREN", "("))
            i += 1
            continue

        if ch == ")":
            tokens.append(Token("RPAREN", ")"))
            i += 1
            continue

        raise ValueError(f"Unknown character: {ch}")

    return tokens