from typing import List

class Token:
    def __init__(self, type: str, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"


def clean_input(expr: str) -> str:
    """Remove whitespace, tabs, newlines"""
    return ''.join(expr.split())


def normalize_signs(expr: str) -> str:
    """Simplify consecutive signs: +++5 → +5, ---7 → -7"""
    result = []
    i = 0
    while i < len(expr):
        if expr[i] in '+-':
            # Collect consecutive signs
            signs = []
            while i < len(expr) and expr[i] in '+-':
                signs.append(expr[i])
                i += 1
            # Count negatives
            neg_count = signs.count('-')
            result.append('-' if neg_count % 2 == 1 else '+')
        else:
            result.append(expr[i])
            i += 1
    return ''.join(result)


def tokenize(normalized: str) -> List[Token]:
    """Tokenize: numbers, variables, operators, parentheses, √"""
    tokens = []
    i = 0
    n = len(normalized)
    
    while i < n:
        c = normalized[i]
        
        if c.isspace():
            i += 1
            continue
        
        # Number (including decimal)
        if c.isdigit() or (c == '.' and i+1 < n and normalized[i+1].isdigit()):
            num = ''
            while i < n and (normalized[i].isdigit() or normalized[i] == '.'):
                num += normalized[i]
                i += 1
            tokens.append(Token("NUMBER", float(num)))
            continue
        
        # Variable
        if c.isalpha():
            var = ''
            while i < n and normalized[i].isalpha():
                var += normalized[i]
                i += 1
            tokens.append(Token("VARIABLE", var))
            continue
        
        # Operators and parentheses
        if c in "+-*/^√":
            tokens.append(Token("OPERATOR", c))
        elif c == '(':
            tokens.append(Token("LPAREN", c))
        elif c == ')':
            tokens.append(Token("RPAREN", c))
        else:
            raise ValueError(f"Unknown character: {c}")
        
        i += 1
    
    return tokens


def precedence(op: str) -> int:
    """Operator precedence"""
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '√': 4}
    return prec.get(op, 0)


def to_rpn(tokens: List[Token]) -> List:
    """Convert infix to RPN using Shunting-yard algorithm"""
    output = []
    stack = []
    
    for token in tokens:
        if token.type in ("NUMBER", "VARIABLE"):
            output.append(token.value)
        
        elif token.type == "OPERATOR":
            op = token.value
            # Pop operators with higher or equal precedence (except ^)
            while (stack and 
                   stack[-1] != "(" and 
                   (precedence(stack[-1]) > precedence(op) or
                    (precedence(stack[-1]) == precedence(op) and op != "^"))):
                output.append(stack.pop())
            stack.append(op)
        
        elif token.type == "LPAREN":
            stack.append("(")
        
        elif token.type == "RPAREN":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if not stack:
                raise ValueError("Mismatched parentheses")
            stack.pop()  # Remove '('
    
    while stack:
        if stack[-1] == "(":
            raise ValueError("Mismatched parentheses")
        output.append(stack.pop())
    
    return output