#include "parser.hpp"
#include "tree.hpp"
#include "utils.hpp"
#include <iostream>

void testTree() {
    std::cout << "=== Testing Tree Operations ===\n\n";
    
    // Test 1: Simple expression
    std::string expr1 = "3 + 4 * 2";
    std::cout << "Expression: " << expr1 << "\n";
    
    auto cleaned = cleanInput(expr1);
    auto normalized = normalizeSigns(cleaned);
    auto tokens = tokenize(normalized);
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
    
    auto tree = buildTree(rpn);
    std::cout << "Tree:\n";
    printTree(tree.get());
    
    double result = evaluateTree(tree.get());
    std::cout << "\nResult: " << result << "\n";
    std::cout << "Expected: 11\n\n";
    
    // Test 2: With variables
    std::string expr2 = "x=3, y=4 : √(x^2 + y^2)";
    std::cout << "Expression: " << expr2 << "\n";
    
    auto [expression, variables] = parseVariables(expr2);
    std::cout << "Parsed expression: " << expression << "\n";
    std::cout << "Variables:\n";
    for (const auto& [name, value] : variables) {
        std::cout << "  " << name << " = " << value << "\n";
    }
    
    cleaned = cleanInput(expression);
    normalized = normalizeSigns(cleaned);
    tokens = tokenize(normalized);
    rpn = toRPN(tokens);
    tree = buildTree(rpn);
    
    std::cout << "\nTree:\n";
    printTree(tree.get());
    
    result = evaluateTree(tree.get(), variables);
    std::cout << "\nResult: " << result << "\n";
    std::cout << "Expected: 5\n\n";
    
    // Test 3: Error handling
    std::cout << "Testing error handling...\n";
    try {
        std::string expr3 = "10 / 0";
        cleaned = cleanInput(expr3);
        normalized = normalizeSigns(cleaned);
        tokens = tokenize(normalized);
        rpn = toRPN(tokens);
        tree = buildTree(rpn);
        result = evaluateTree(tree.get());
    } catch (const std::exception& e) {
        std::cout << "✓ Caught error: " << e.what() << "\n";
    }
    
    try {
        std::string expr4 = "√(-4)";
        cleaned = cleanInput(expr4);
        normalized = normalizeSigns(cleaned);
        tokens = tokenize(normalized);
        rpn = toRPN(tokens);
        tree = buildTree(rpn);
        result = evaluateTree(tree.get());
    } catch (const std::exception& e) {
        std::cout << "✓ Caught error: " << e.what() << "\n";
    }
}

int main() {
    try {
        testTree();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << "\n";
        return 1;
    }
    return 0;
}