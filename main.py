from parser import clean_input, normalize_signs, tokenize

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

        # مرحله ۱: پاک‌سازی
        cleaned = clean_input(expr)
        print(f"Cleaned:     {cleaned}")

        # مرحله ۲: عادی‌سازی علامت‌ها
        normalized = normalize_signs(cleaned)
        print(f"Normalized:  {normalized}")

        # مرحله ۳: توکنایزر
        try:
            tokens = tokenize(normalized)
            print(f"Tokens:      {tokens}")
        except ValueError as e:
            print(f"Tokenization Error: {e}")

        print("-" * 60)

if __name__ == "__main__":
    main()