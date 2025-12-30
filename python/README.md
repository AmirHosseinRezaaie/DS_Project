# Python Implementation

## Installation
```bash
pip install -r requirements.txt
```

## Running
```bash
python src/main.py
```

## Testing
```bash
python -m pytest tests/
```

## Example Expressions
```
3 + 4 * 2
√(16) + 5
x=10 : x^2 + 2*x + 1
a=3, b=4 : √(a^2 + b^2)
```

## Architecture

- `parser.py`: Input cleaning, tokenization, RPN conversion
- `tree.py`: Expression tree building and evaluation
- `variables.py`: Variable parsing and substitution
- `main.py`: Interactive REPL interface