from parser import clean_input, normalize_signs, tokenize, to_rpn

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
            # مرحله ۱: پاک‌سازی
            cleaned = clean_input(expr)
            print(f"Cleaned:     {cleaned}")

            # مرحله ۲: عادی‌سازی علامت‌ها
            normalized = normalize_signs(cleaned)
            print(f"Normalized:  {normalized}")

            # مرحله ۳: توکنایزر
            tokens = tokenize(normalized)
            print(f"Tokens:      {tokens}")

            # مرحله ۴: تبدیل به RPN
            rpn = to_rpn(tokens)
            print(f"RPN:         {rpn}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

        print("-" * 70)

if __name__ == "__main__":
    main()