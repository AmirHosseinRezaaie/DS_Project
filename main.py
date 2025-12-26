from parser import clean_input, normalize_signs

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

        # مرحله ۱: پاک‌سازی اولیه (حذف فاصله‌ها و کاراکترهای سفید)
        cleaned = clean_input(expr)
        print(f"Cleaned:     {cleaned}")

        # مرحله ۲: عادی‌سازی علامت‌های متوالی
        normalized = normalize_signs(cleaned)
        print(f"Normalized:  {normalized}")

        # بعداً اینجا ادامه پردازش (توکنایزر، درخت و ...) اضافه می‌شه
        print("-" * 50)

if __name__ == "__main__":
    main()
    