from typing import List, Optional
# Assuming Token class
class Token:
    def __init__(self, type: str, value: any):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

def tokenize(normalized: str) -> List[Token]:
    """
    Tokenize the normalized expression.
    Supports numbers, operators, variables (letters), parentheses, √.
    """
    tokens = []
    i = 0
    n = len(normalized)
    
    while i < n:
        c = normalized[i]
        
        if c.isspace():
            i += 1
            continue
        
        if c.isdigit() or (c == '.' and i+1 < n and normalized[i+1].isdigit()):
            # Number
            num = ''
            while i < n and (normalized[i].isdigit() or normalized[i] == '.'):
                num += normalized[i]
                i += 1
            tokens.append(Token("NUMBER", float(num)))
            continue
        
        if c.isalpha():
            # Variable (simple: single letter or word)
            var = ''
            while i < n and normalized[i].isalpha():
                var += normalized[i]
                i += 1
            tokens.append(Token("VARIABLE", var))
            continue
        
        if c in "+-*/^()√":
            tokens.append(Token("OPERATOR" if c in "+-*/^√" else "LPAREN" if c == "(" else "RPAREN", c))
            i += 1
            continue
        
        raise ValueError(f"Unknown character: {c}")
    
    return tokens

# Rest of parser.py remains the same (precedence, to_rpn)
# Update to_rpn to handle VARIABLE like NUMBER
def to_rpn(tokens: List[Token]) -> List[any]:
    """
    Convert infix tokens to RPN.
    Treat variables like numbers.
    """
    output = []
    stack = []
    
    for token in tokens:
        if token.type in ("NUMBER", "VARIABLE"):
            output.append(token.value)
        
        elif token.type == "OPERATOR":
            op = token.value
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
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                raise ValueError("Mismatched parentheses")
    
    while stack:
        if stack[-1] == "(":
            raise ValueError("Mismatched parentheses")
        output.append(stack.pop())
    
    return output