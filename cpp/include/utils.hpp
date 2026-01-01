#ifndef UTILS_HPP
#define UTILS_HPP

#include <string>
#include <map>

// Parse variables from input string
// Format: "x=10, y=5 : expression" or "expression"
// Returns: pair<expression, variables>
std::pair<std::string, std::map<std::string, double>> parseVariables(const std::string& input);

// Helper: trim whitespace from string
std::string trim(const std::string& str);

// Helper: split string by delimiter
std::vector<std::string> split(const std::string& str, char delimiter);

#endif