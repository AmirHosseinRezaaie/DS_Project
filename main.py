from parser import clean_input, normalize_signs, tokenize, to_rpn
from tree import build_tree, print_tree, evaluate_tree

def main():
    print("Advanced Mathematical Expression Evaluator (Python)")
    print("Enter expression (or 'quit' to exit):\n")

    while True:
        expr = input("> ").strip()
        
        if expr.lower() == "quit":
            print("Goodbye!")
            break
        
        if not expr:
            print("Please enter a valid expression.\n")
            continue

        try:
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

            # مرحله جدید: محاسبه نتیجه
            result = evaluate_tree(root)
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