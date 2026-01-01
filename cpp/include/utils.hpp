#ifndef UTILS_HPP
#define UTILS_HPP

#include "token.hpp"
#include <string>
#include <map>
#include <vector>

// Parse variables from input string
std::pair<std::string, std::map<std::string, double>> parseVariables(const std::string& input);

// Helper: trim whitespace from string
std::string trim(const std::string& str);

// Helper: split string by delimiter
std::vector<std::string> split(const std::string& str, char delimiter);

// Helper: convert TokenValue to string for printing
std::string tokenValueToString(const TokenValue& val);

#endif // UTILS_HPP