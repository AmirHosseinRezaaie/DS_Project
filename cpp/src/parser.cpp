#include "parser.hpp"
#include <stack>
#include <cctype>
#include <stdexcept>
#include <sstream>
#include <algorithm>

// Token toString implementation
std::string Token::toString() const {
    std::string typeStr;
    switch (type) {
        case TokenType::NUMBER: typeStr = "NUMBER"; break;
        case TokenType::VARIABLE: typeStr = "VARIABLE"; break;
        case TokenType::OPERATOR: typeStr = "OPERATOR"; break;
        case TokenType::LPAREN: typeStr = "LPAREN"; break;
        case TokenType::RPAREN: typeStr = "RPAREN"; break;
    }
    
    std::string valueStr;
    if (std::holds_alternative<double>(value)) {
        valueStr = std::to_string(std::get<double>(value));
    } else {
        valueStr = std::get<std::string>(value);
    }
    
    return "Token(" + typeStr + ", " + valueStr + ")";
}

// Clean input: remove all whitespace
std::string cleanInput(const std::string& input) {
    std::string result;
    for (char c : input) {
        if (!std::isspace(c)) {
            result += c;
        }
    }
    return result;
}

// Normalize consecutive signs
std::string normalizeSigns(const std::string& input) {
    std::string result;
    size_t i = 0;
    
    while (i < input.length()) {
        if (input[i] == '+' || input[i] == '-') {
            // Collect consecutive signs
            int negCount = 0;
            while (i < input.length() && (input[i] == '+' || input[i] == '-')) {
                if (input[i] == '-') {
                    negCount++;
                }
                i++;
            }
            // Odd number of negatives → negative, even → positive
            result += (negCount % 2 == 1) ? '-' : '+';
        } else {
            result += input[i];
            i++;
        }
    }
    
    return result;
}

// Tokenize expression
std::vector<Token> tokenize(const std::string& normalized) {
    std::vector<Token> tokens;
    size_t i = 0;
    size_t n = normalized.length();
    
    while (i < n) {
        char c = normalized[i];
        
        // Number (including decimal)
        if (std::isdigit(c) || (c == '.' && i + 1 < n && std::isdigit(normalized[i + 1]))) {
            std::string numStr;
            while (i < n && (std::isdigit(normalized[i]) || normalized[i] == '.')) {
                numStr += normalized[i];
                i++;
            }
            tokens.push_back(Token(TokenType::NUMBER, std::stod(numStr)));
            continue;
        }
        
        // Variable (alphabetic characters)
        if (std::isalpha(c)) {
            std::string varStr;
            while (i < n && std::isalpha(normalized[i])) {
                varStr += normalized[i];
                i++;
            }
            tokens.push_back(Token(TokenType::VARIABLE, varStr));
            continue;
        }
        
        // Operators
        if (c == '+' || c == '-' || c == '*' || c == '/' || c == '^') {
            tokens.push_back(Token(TokenType::OPERATOR, c));
            i++;
            continue;
        }
        
        // Square root (√)
        if (c == '√' || (c == 's' && i + 3 < n && 
            normalized.substr(i, 4) == "sqrt")) {
            tokens.push_back(Token(TokenType::OPERATOR, "√"));
            i += (c == '√') ? 1 : 4;  // Skip "sqrt" if used
            continue;
        }
        
        // Left parenthesis
        if (c == '(') {
            tokens.push_back(Token(TokenType::LPAREN, c));
            i++;
            continue;
        }
        
        // Right parenthesis
        if (c == ')') {
            tokens.push_back(Token(TokenType::RPAREN, c));
            i++;
            continue;
        }
        
        // Unknown character
        throw std::runtime_error(std::string("Unknown character: ") + c);
    }
    
    return tokens;
}

// Operator precedence
int precedence(const std::string& op) {
    if (op == "+" || op == "-") return 1;
    if (op == "*" || op == "/") return 2;
    if (op == "^") return 3;
    if (op == "√") return 4;
    return 0;
}

// Convert infix to RPN using Shunting-yard algorithm
std::vector<TokenValue> toRPN(const std::vector<Token>& tokens) {
    std::vector<TokenValue> output;
    std::stack<std::string> stack;
    
    for (const auto& token : tokens) {
        // Numbers and variables go directly to output
        if (token.type == TokenType::NUMBER || token.type == TokenType::VARIABLE) {
            output.push_back(token.value);
        }
        // Operators
        else if (token.type == TokenType::OPERATOR) {
            std::string op = std::get<std::string>(token.value);
            
            // Pop operators with higher or equal precedence
            // (except for ^ which is right-associative)
            while (!stack.empty() && 
                   stack.top() != "(" &&
                   (precedence(stack.top()) > precedence(op) ||
                    (precedence(stack.top()) == precedence(op) && op != "^"))) {
                output.push_back(stack.top());
                stack.pop();
            }
            stack.push(op);
        }
        // Left parenthesis
        else if (token.type == TokenType::LPAREN) {
            stack.push("(");
        }
        // Right parenthesis
        else if (token.type == TokenType::RPAREN) {
            // Pop until matching left parenthesis
            while (!stack.empty() && stack.top() != "(") {
                output.push_back(stack.top());
                stack.pop();
            }
            
            if (stack.empty()) {
                throw std::runtime_error("Mismatched parentheses");
            }
            
            stack.pop();  // Remove '('
        }
    }
    
    // Pop remaining operators
    while (!stack.empty()) {
        if (stack.top() == "(") {
            throw std::runtime_error("Mismatched parentheses");
        }
        output.push_back(stack.top());
        stack.pop();
    }
    
    return output;
}