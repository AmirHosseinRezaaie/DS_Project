#include "utils.hpp"
#include <sstream>
#include <algorithm>

// Trim whitespace
std::string trim(const std::string& str) {
    size_t first = str.find_first_not_of(" \t\n\r");
    if (first == std::string::npos) {
        return "";
    }
    size_t last = str.find_last_not_of(" \t\n\r");
    return str.substr(first, last - first + 1);
}

// Split string by delimiter
std::vector<std::string> split(const std::string& str, char delimiter) {
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(str);
    
    while (std::getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    
    return tokens;
}

// Parse variables from input
std::pair<std::string, std::map<std::string, double>> parseVariables(const std::string& input) {
    std::map<std::string, double> variables;
    std::string expression = input;
    
    // Check if input contains ':'
    size_t colonPos = input.find(':');
    
    if (colonPos != std::string::npos) {
        // Split by ':'
        std::string varPart = input.substr(0, colonPos);
        expression = input.substr(colonPos + 1);
        
        // Parse variable assignments
        std::vector<std::string> pairs = split(varPart, ',');
        
        for (const auto& pair : pairs) {
            size_t equalPos = pair.find('=');
            if (equalPos != std::string::npos) {
                std::string varName = trim(pair.substr(0, equalPos));
                std::string varValue = trim(pair.substr(equalPos + 1));
                
                try {
                    double value = std::stod(varValue);
                    variables[varName] = value;
                } catch (const std::exception& e) {
                    throw std::runtime_error("Invalid variable value: " + varValue);
                }
            }
        }
    }
    
    return {trim(expression), variables};
}