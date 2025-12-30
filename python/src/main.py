import sys
import os

# Fix Unicode encoding for Windows console
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())

from parser import clean_input, normalize_signs, tokenize, to_rpn
from tree import build_tree, print_tree, evaluate_tree, visualize_tree
from variables import parse_variables


def main():
    print("=" * 80)
    print("Advanced Mathematical Expression Evaluator (Python)")
    print("=" * 80)
    print("\nSupported operators: + - * / ^ √ ( )")
    print("Variables: x=10, y=5 : expression")
    print("Commands: 'quit' to exit, 'help' for examples\n")

    while True:
        try:
            input_str = input("> ").strip()
        except UnicodeDecodeError:
            print("Invalid input encoding. Please use ASCII characters.")
            continue
        
        if input_str.lower() == "quit":
            print("\nGoodbye!")
            break
        
        if input_str.lower() == "help":
            print("\nExample expressions:")
            print("  3 + 4 * 2")
            print("  √(4^2 + 3^2)  or  sqrt(4^2 + 3^2)")
            print("  x=7 : x^2 + 2*x + 1")
            print("  a=3, b=4 : √(a^2 + b^2)")
            print()
            continue
        
        if not input_str:
            print("Please enter a valid expression.\n")
            continue

        try:
            # Parse variables if present
            expr, variables = parse_variables(input_str)
            
            # Processing steps
            cleaned = clean_input(expr)
            print(f"Cleaned:     {cleaned}")

            normalized = normalize_signs(cleaned)
            print(f"Normalized:  {normalized}")

            tokens = tokenize(normalized)
            print(f"Tokens:      {[str(t) for t in tokens]}")

            rpn = to_rpn(tokens)
            print(f"RPN:         {rpn}")

            # Build and display tree
            root = build_tree(rpn)
            print("\nExpression Tree:")
            print_tree(root)

            # Visualize and save
            visualize_tree(root)

            # Evaluate
            result = evaluate_tree(root, variables)
            print(f"\n{'Result:':<13}{result}")
            
            if variables:
                print(f"Variables:   {variables}")

        except ZeroDivisionError as e:
            print(f"\n❌ Math Error: {e}")
        except ValueError as e:
            print(f"\n❌ Error: {e}")
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")

        print("-" * 80 + "\n")


if __name__ == "__main__":
    main()