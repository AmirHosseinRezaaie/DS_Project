def parse_variables(input_str: str) -> tuple[str, dict[str, float]]:
    """
    Parse variables from input like 'x=7, y=5 : expression'.
    Returns (expression, variables_dict).
    """
    variables = {}
    expr = input_str
    
    if ':' in input_str:
        parts = input_str.split(':', 1)
        var_part = parts[0].strip()
        expr = parts[1].strip()
        
        var_pairs = var_part.split(',')
        for pair in var_pairs:
            if '=' in pair:
                key, val = pair.split('=', 1)
                variables[key.strip()] = float(val.strip())
    
    return expr, variables