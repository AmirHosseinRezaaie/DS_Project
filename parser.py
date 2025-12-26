# Module for input processing: cleaning, normalization, and tokenization.


def clean_input(raw_input: str) -> str:

    # Remove all whitespace characters: spaces, tabs, newlines.

    cleaned = raw_input.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "")
    return cleaned


def normalize_signs(expression: str) -> str:
    
    # Handle consecutive + and - signs.
    # Examples:
    #     +++5    → +5
    #     --5     → +5
    #     -++-5   → -5
    #     ---√16  → -√16
    #     ++(--5) → +( -5 )
    
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
           
            if (normalized == "" or normalized[-1] in "(√" or 
                (i < len(expression) and expression[i] == "√")):
                if sign_count % 2 == 1:
                    normalized += "-"
                else:
                    normalized += "+"
            else:
                if sign_count % 2 == 1:
                    normalized += "-"
                else:
                    normalized += "+"

            continue

        normalized += current
        i += 1

    return normalized