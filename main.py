from parser import clean_input, normalize_signs, tokenize, to_rpn
from tree import build_tree, print_tree, evaluate_tree, visualize_tree
from variables import parse_variables

def main():
    print("Advanced Mathematical Expression Evaluator (Python)")
    print("Enter expression (or 'quit' to exit). Variables like x=10, y=5 optional:\n")

    while True:
        input_str = input("> ").strip()
        
        if input_str.lower() == "quit":
            print("Goodbye!")
            break
        
        if not input_str:
            print("Please enter a valid expression.\n")
            continue

        try:
            expr, variables = parse_variables(input_str)
            
            cleaned = clean_input(expr)
            print(f"Cleaned:     {cleaned}")

            normalized = normalize_signs(cleaned)
            print(f"Normalized:  {normalized}")

            tokens = tokenize(normalized)
            print(f"Tokens:      {tokens}")

            rpn = to_rpn(tokens)
            print(f"RPN:         {rpn}")

            root = build_tree(rpn)
            print("\nExpression Tree:")
            print_tree(root)

            # Visualize tree
            visualize_tree(root)

            result = evaluate_tree(root, variables)
            print(f"\nResult:      {result}")

        except ZeroDivisionError as e:
            print(f"\nMath Error: {e}")
        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nUnexpected error: {e}")

        print("-" * 80)

if __name__ == "__main__":
    main()