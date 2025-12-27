def precedence(op: str) -> int:
    """
    Return operator precedence.
    Higher number = higher precedence
    ^ is right-associative, others left-associative
    """
    if op in ("+", "-"):
        return 1
    if op in ("*", "/"):
        return 2
    if op == "^":
        return 3
    if op == "√":
        return 4  # بالاترین اولویت - یک‌تایی
    return 0


def to_rpn(tokens: List[Token]) -> List[any]:
    """
    Convert infix tokens to Reverse Polish Notation using Shunting-Yard algorithm.
    Returns list of values (int or str) ready for tree building.
    """
    output = []
    stack = []

    
    for token in tokens:
        if token.type == "NUMBER":
            output.append(token.value)

        elif token.type == "OPERATOR":
            op = token.value
            while (stack and 
                   stack[-1] != "(" and 
                   precedence(stack[-1]) > precedence(op) or
                   (precedence(stack[-1]) == precedence(op) and op != "^")):  # left-associative
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