#include "parser.hpp"
#include <iostream>

void testParser() {
    std::cout << "=== Testing Parser ===\n\n";
    
    // Test 1: Clean input
    std::string input = "3 + 4  *   2";
    std::string cleaned = cleanInput(input);
    std::cout << "Input:   " << input << "\n";
    std::cout << "Cleaned: " << cleaned << "\n\n";
    
    // Test 2: Normalize signs
    std::string expr = "3++-+4";
    std::string normalized = normalizeSigns(expr);
    std::cout << "Expression:  " << expr << "\n";
    std::cout << "Normalized:  " << normalized << "\n\n";
    
    // Test 3: Tokenize
    std::string testExpr = "3+4*2";
    auto tokens = tokenize(testExpr);
    std::cout << "Expression: " << testExpr << "\n";
    std::cout << "Tokens:\n";
    for (const auto& token : tokens) {
        std::cout << "  " << token.toString() << "\n";
    }
    std::cout << "\n";
    
    // Test 4: RPN conversion
    auto rpn = toRPN(tokens);
    std::cout << "RPN: ";
    for (const auto& val : rpn) {
        if (std::holds_alternative<double>(val)) {
            std::cout << std::get<double>(val) << " ";
        } else {
            std::cout << std::get<std::string>(val) << " ";
        }
    }
    std::cout << "\n\n";
    
    // Test 5: Complex expression with variables
    std::string complexExpr = "√(x^2+y^2)";
    cleaned = cleanInput(complexExpr);
    normalized = normalizeSigns(cleaned);
    tokens = tokenize(normalized);
    rpn = toRPN(tokens);
    
    std::cout << "Complex Expression: " << complexExpr << "\n";
    std::cout << "RPN: ";
    for (const auto& val : rpn) {
        if (std::holds_alternative<double>(val)) {
            std::cout << std::get<double>(val) << " ";
        } else {
            std::cout << std::get<std::string>(val) << " ";
        }
    }
    std::cout << "\n";
}

int main() {
    try {
        testParser();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << "\n";
        return 1;
    }
    return 0;
}