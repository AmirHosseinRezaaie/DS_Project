#include "parser.hpp"
#include "tree.hpp"
#include "utils.hpp"
#include <iostream>
#include <string>
#include <iomanip>
#include <variant> 

// Print welcome message
void printWelcome() {
    std::cout << std::string(80, '=') << "\n";
    std::cout << "Advanced Mathematical Expression Evaluator (C++)\n";
    std::cout << std::string(80, '=') << "\n\n";
    std::cout << "Supported operators: + - * / ^ √ ( )\n";
    std::cout << "Variables: x=10, y=5 : expression\n";
    std::cout << "Commands: 'quit' to exit, 'help' for examples\n\n";
}

// Print help message
void printHelp() {
    std::cout << "\nExample expressions:\n";
    std::cout << "  3 + 4 * 2\n";
    std::cout << "  √(4^2 + 3^2)\n";
    std::cout << "  (3 + 4) * (5 - 2)\n";
    std::cout << "  x=7 : x^2 + 2*x + 1\n";
    std::cout << "  a=3, b=4 : √(a^2 + b^2)\n";
    std::cout << "  x=7 : √(4^2 + 3^2) * (x + 5) - 10 / 2\n\n";
}

// Process and evaluate expression
void processExpression(const std::string& input) {
    try {
        // Parse variables
        auto [expression, variables] = parseVariables(input);
        
        // Clean input
        std::string cleaned = cleanInput(expression);
        std::cout << "Cleaned:     " << cleaned << "\n";
        
        // Normalize signs
        std::string normalized = normalizeSigns(cleaned);
        std::cout << "Normalized:  " << normalized << "\n";
        
        // Tokenize
        auto tokens = tokenize(normalized);
        std::cout << "Tokens:      [";
        for (size_t i = 0; i < tokens.size(); ++i) {
            if (i > 0) std::cout << ", ";
            std::cout << tokens[i].toString();
        }
        std::cout << "]\n";
        
        // Convert to RPN
        auto rpn = toRPN(tokens);
        std::cout << "RPN:         [";
        for (size_t i = 0; i < rpn.size(); ++i) {
            if (i > 0) std::cout << ", ";
            std::cout << tokenValueToString(rpn[i]); 
        }
        std::cout << "]\n";
        
        // Build tree
        auto tree = buildTree(rpn);
        std::cout << "\nExpression Tree:\n";
        printTree(tree.get());
        
        // Evaluate
        double result = evaluateTree(tree.get(), variables);
        std::cout << "\nResult:      " << std::fixed << std::setprecision(2) << result << "\n";
        
        // Show variables if any
        if (!variables.empty()) {
            std::cout << "Variables:   {";
            bool first = true;
            for (const auto& [name, value] : variables) {
                if (!first) std::cout << ", ";
                std::cout << name << "=" << value;
                first = false;
            }
            std::cout << "}\n";
        }
        
    } catch (const std::runtime_error& e) {
        std::cout << "\n❌ Error: " << e.what() << "\n";
    } catch (const std::exception& e) {
        std::cout << "\n❌ Unexpected error: " << e.what() << "\n";
    }
}

int main() {
    printWelcome();
    
    std::string input;
    
    while (true) {
        std::cout << "> ";
        
        // Read input
        if (!std::getline(std::cin, input)) {
            break;  // EOF or error
        }
        
        // Trim input
        input = trim(input);
        
        // Check for empty input
        if (input.empty()) {
            std::cout << "Please enter a valid expression.\n\n";
            continue;
        }
        
        // Check for quit command
        if (input == "quit" || input == "exit" || input == "q") {
            std::cout << "\nGoodbye!\n";
            break;
        }
        
        // Check for help command
        if (input == "help" || input == "h" || input == "?") {
            printHelp();
            continue;
        }
        
        // Process expression
        processExpression(input);
        
        std::cout << std::string(80, '-') << "\n\n";
    }
    
    return 0;
}