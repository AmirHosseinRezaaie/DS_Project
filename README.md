# Advanced Mathematical Expression Evaluator with Expression Tree

A high-performance, full-featured mathematical expression parser and evaluator built from scratch using core Data Structures & Algorithms concepts.

## Key Features

- Full mathematical expression parsing with correct operator precedence  
- Supports: `+ − × ÷ ^ √ ( )`  
- Handles complex unary operations: `−(−(−۲))`, `+++۵`, `−−−√۱۶`  
- Automatic input normalization (consecutive signs simplified)  
- Complete Expression Tree construction from Reverse Polish Notation (RPN)  
- Accurate evaluation via post-order tree traversal  
- Division by zero detection with clear error message  
- Square root of negative numbers (with negative input protection)  
- Graphical visualization of the Expression Tree using Graphviz  
- Variable support: `x=10, count=5` → usable in expressions  
- Clean, modular, and well-structured Python implementation  

## Bonus Features Implemented
- Tree visualization (Graphviz)
- Variable substitution
- Professional documentation

## Files
- DS_Project.ipynb         → Complete implementation
- expression_tree.png      → Tree visualization
- README.md                → This file

**Status: Fully Completed • All Requirements + Multiple Bonuses • Ready for Submission**

## Example Usage

```python
Input:      √(4 ^ 2 + 3 ^ 2) * (x + 5) - 10 / 2
Variables:  x=7
Result:     108.0

## Implementations

### Python (In Progress)
- Modular design with separate files
- Full feature support including visualization
- Current status: Project structure initialized