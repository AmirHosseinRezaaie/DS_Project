#ifndef TREE_HPP
#define TREE_HPP

#include "token.hpp"
#include <memory>
#include <map>
#include <string>
#include <vector>

// Node class for binary expression tree
class Node {
public:
    TokenValue value;
    std::unique_ptr<Node> left;
    std::unique_ptr<Node> right;
    
    // Constructors
    Node(double val);
    Node(const std::string& val);
    Node(const std::string& op, std::unique_ptr<Node> l, std::unique_ptr<Node> r);
    
    // Check if node is an operator
    bool isOperator() const;
    
    // Check if node is a number
    bool isNumber() const;
    
    // Check if node is a variable
    bool isVariable() const;
    
    // Get string representation
    std::string toString() const;
};

// Build expression tree from RPN
std::unique_ptr<Node> buildTree(const std::vector<TokenValue>& rpn);

// Print tree structure (text-based visualization)
void printTree(const Node* node, const std::string& prefix = "", bool isTail = true);

// Evaluate expression tree with variables
double evaluateTree(const Node* node, const std::map<std::string, double>& variables = {});

#endif