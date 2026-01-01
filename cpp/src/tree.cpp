#include "tree.hpp"
#include <stack>
#include <stdexcept>
#include <cmath>
#include <iostream>
#include <set>

// Operator set for checking
const std::set<std::string> OPERATORS = {"+", "-", "*", "/", "^", "√"};

// Node constructors
Node::Node(double val) : value(val), left(nullptr), right(nullptr) {}

Node::Node(const std::string& val) : value(val), left(nullptr), right(nullptr) {}

Node::Node(const std::string& op, std::unique_ptr<Node> l, std::unique_ptr<Node> r)
    : value(op), left(std::move(l)), right(std::move(r)) {}

// Check if node is operator
bool Node::isOperator() const {
    if (std::holds_alternative<std::string>(value)) {
        return OPERATORS.count(std::get<std::string>(value)) > 0;
    }
    return false;
}

// Check if node is number
bool Node::isNumber() const {
    return std::holds_alternative<double>(value);
}

// Check if node is variable
bool Node::isVariable() const {
    if (std::holds_alternative<std::string>(value)) {
        std::string str = std::get<std::string>(value);
        return OPERATORS.count(str) == 0;
    }
    return false;
}

// Get string representation
std::string Node::toString() const {
    if (std::holds_alternative<double>(value)) {
        return std::to_string(std::get<double>(value));
    } else {
        return std::get<std::string>(value);
    }
}

// Build tree from RPN
std::unique_ptr<Node> buildTree(const std::vector<TokenValue>& rpn) {
    std::stack<std::unique_ptr<Node>> stack;
    
    for (const auto& token : rpn) {
        // Check if it's an operator
        bool isOp = false;
        std::string opStr;
        
        if (std::holds_alternative<std::string>(token)) {
            opStr = std::get<std::string>(token);
            isOp = OPERATORS.count(opStr) > 0;
        }
        
        if (isOp) {
            // Unary operator (√)
            if (opStr == "√") {
                if (stack.empty()) {
                    throw std::runtime_error("Invalid expression: sqrt without operand");
                }
                auto operand = std::move(stack.top());
                stack.pop();
                stack.push(std::make_unique<Node>(opStr, std::move(operand), nullptr));
            }
            // Binary operators
            else {
                if (stack.size() < 2) {
                    throw std::runtime_error("Invalid expression: operator needs two operands");
                }
                auto right = std::move(stack.top());
                stack.pop();
                auto left = std::move(stack.top());
                stack.pop();
                stack.push(std::make_unique<Node>(opStr, std::move(left), std::move(right)));
            }
        }
        // Operand (number or variable)
        else {
            if (std::holds_alternative<double>(token)) {
                stack.push(std::make_unique<Node>(std::get<double>(token)));
            } else {
                stack.push(std::make_unique<Node>(std::get<std::string>(token)));
            }
        }
    }
    
    if (stack.size() != 1) {
        throw std::runtime_error("Invalid RPN: too many operands");
    }
    
    return std::move(stack.top());
}

// Print tree with proper formatting
void printTree(const Node* node, const std::string& prefix, bool isTail) {
    if (node == nullptr) {
        return;
    }
    
    std::cout << prefix << (isTail ? "└── " : "├── ") << node->toString() << "\n";
    
    // Collect children
    std::vector<const Node*> children;
    if (node->left) children.push_back(node->left.get());
    if (node->right) children.push_back(node->right.get());
    
    // Print children
    for (size_t i = 0; i < children.size(); ++i) {
        bool isLast = (i == children.size() - 1);
        std::string extension = isTail ? "    " : "│   ";
        printTree(children[i], prefix + extension, isLast);
    }
}

// Evaluate tree recursively
double evaluateTree(const Node* node, const std::map<std::string, double>& variables) {
    if (node == nullptr) {
        throw std::runtime_error("Null node encountered");
    }
    
    // Number
    if (node->isNumber()) {
        return std::get<double>(node->value);
    }
    
    // Variable
    if (node->isVariable()) {
        std::string varName = std::get<std::string>(node->value);
        auto it = variables.find(varName);
        if (it == variables.end()) {
            throw std::runtime_error("Undefined variable: " + varName);
        }
        return it->second;
    }
    
    // Operator - evaluate children
    std::string op = std::get<std::string>(node->value);
    
    double leftVal = 0.0;
    double rightVal = 0.0;
    
    if (node->left) {
        leftVal = evaluateTree(node->left.get(), variables);
    }
    
    if (node->right) {
        rightVal = evaluateTree(node->right.get(), variables);
    }
    
    // Apply operator
    if (op == "+") {
        return leftVal + rightVal;
    } else if (op == "-") {
        return leftVal - rightVal;
    } else if (op == "*") {
        return leftVal * rightVal;
    } else if (op == "/") {
        if (rightVal == 0.0) {
            throw std::runtime_error("Division by zero");
        }
        return leftVal / rightVal;
    } else if (op == "^") {
        return std::pow(leftVal, rightVal);
    } else if (op == "√") {
        if (leftVal < 0.0) {
            throw std::runtime_error("Square root of negative number");
        }
        return std::sqrt(leftVal);
    } else {
        throw std::runtime_error("Unknown operator: " + op);
    }
}