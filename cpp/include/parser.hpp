#ifndef PARSER_HPP
#define PARSER_HPP

#include "token.hpp"
#include <string>
#include <vector>

// Clean input: remove whitespace
std::string cleanInput(const std::string& input);

// Normalize consecutive signs: +++5 → +5, ---7 → -7
std::string normalizeSigns(const std::string& input);

// Tokenize expression into tokens
std::vector<Token> tokenize(const std::string& normalized);

// Get operator precedence
int precedence(const std::string& op);

// Convert infix tokens to Reverse Polish Notation (RPN)
std::vector<TokenValue> toRPN(const std::vector<Token>& tokens);

#endif