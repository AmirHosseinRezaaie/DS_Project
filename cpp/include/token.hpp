#ifndef TOKEN_HPP
#define TOKEN_HPP

#include <string>
#include <variant>

// Token types
enum class TokenType {
    NUMBER,      // 3.14, 5, 0.5
    VARIABLE,    // x, y, count
    OPERATOR,    // +, -, *, /, ^, √
    LPAREN,      // (
    RPAREN       // )
};

// Token value can be either double or string
using TokenValue = std::variant<double, std::string>;

// Token structure
struct Token {
    TokenType type;
    TokenValue value;
    
    // Constructors
    Token(TokenType t, double v) : type(t), value(v) {}
    Token(TokenType t, const std::string& v) : type(t), value(v) {}
    Token(TokenType t, char v) : type(t), value(std::string(1, v)) {}
    
    // Helper to check if token is an operator
    bool isOperator() const {
        return type == TokenType::OPERATOR;
    }
    
    // Get string representation for debugging
    std::string toString() const;
};

#endif