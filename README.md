# Advanced Mathematical Expression Evaluator with Expression Tree

A high-performance, full-featured mathematical expression parser and evaluator built from scratch using core Data Structures & Algorithms concepts. Available in both **Python** and **C++** implementations.

## 🎯 Key Features

- ✅ Full mathematical expression parsing with correct operator precedence
- ✅ Supports: `+ − × ÷ ^ √ ( )`
- ✅ Handles complex unary operations: `−(−(−2))`, `+++5`, `−−−√16`
- ✅ Automatic input normalization (consecutive signs simplified)
- ✅ Complete Expression Tree construction from Reverse Polish Notation (RPN)
- ✅ Accurate evaluation via post-order tree traversal
- ✅ Division by zero detection with clear error messages
- ✅ Square root of negative numbers protection
- ✅ **Variable support**: `x=10, y=5` → usable in expressions
- ✅ **Interactive REPL** interface
- ✅ Comprehensive error handling
- ✅ Clean, modular, and well-structured implementation

## 📁 Project Structure
```
DS_Project/
├── python/              # Python implementation ✅
│   ├── src/            # Source files
│   ├── tests/          # Unit tests
│   ├── examples/       # Sample expressions
│   ├── output/         # Graphviz visualizations
│   └── README.md
├── cpp/                # C++ implementation ✅
│   ├── include/        # Header files
│   ├── src/            # Source files
│   ├── examples/       # Sample expressions
│   ├── build/          # Build directory
│   └── README.md
└── README.md           # This file
```

## 🐍 Python Implementation

### Requirements
```bash
pip install -r python/requirements.txt
```

### Quick Start
```bash
cd python/src
python main.py
```

### Features
- ✅ Graphviz tree visualization (PNG output)
- ✅ Interactive REPL
- ✅ Variable substitution
- ✅ Comprehensive error handling

### Example
```python
> x=7 : √(4^2 + 3^2) * (x + 5) - 10 / 2
Result: 55.0
```

**[Full Python Documentation →](python/README.md)**

---

## ⚡ C++ Implementation

### Requirements
- C++17 compatible compiler (GCC 7+, Clang 5+, MSVC 2017+)
- CMake 3.10+

### Quick Start

#### Windows (MinGW)
```bash
cd cpp
mkdir build && cd build
cmake -G "MinGW Makefiles" ..
mingw32-make
expression_evaluator.exe
```

#### Linux/macOS
```bash
cd cpp
mkdir build && cd build
cmake ..
make
./expression_evaluator
```

### Features
- ✅ Pure C++17 standard library (no dependencies)
- ✅ Smart pointers for memory safety
- ✅ Text-based tree visualization
- ✅ Interactive REPL
- ✅ High performance

### Example
```cpp
> a=3, b=4 : √(a^2 + b^2)
Result: 5.00
Variables: {a=3, b=4}
```

**[Full C++ Documentation →](cpp/README.md)**

---

## 📊 Implementation Comparison

| Feature | Python | C++ |
|---------|--------|-----|
| **Performance** | Slower (interpreted) | Faster (compiled) |
| **Memory Management** | Automatic (GC) | Manual (smart pointers) |
| **Visualization** | Graphviz (PNG) | Text-based |
| **Dependencies** | graphviz | None (pure STL) |
| **Type Safety** | Dynamic | Static |
| **Build Time** | Instant | ~2-5 seconds |
| **Runtime Speed** | Baseline | 10-50x faster |
| **Code Size** | ~400 lines | ~800 lines |
| **Ease of Use** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Learning Value** | High | Very High |

## 🧪 Testing

### Python Tests
```bash
cd python
pytest tests/ -v
```

### C++ Tests
```bash
cd cpp/build
./test_parser
./test_tree
```

### Sample Expressions
Both implementations support 40+ test expressions including:
- Basic arithmetic
- Operator precedence
- Parentheses
- Square root operations
- Variables (single and multiple)
- Complex nested expressions
- Error cases

See `examples/sample_expressions.txt` in each implementation.

---

## 🎓 Educational Value

This project demonstrates mastery of:

### Data Structures
- **Stacks**: Used in Shunting-yard algorithm for operator precedence
- **Binary Trees**: Expression tree representation
- **Hash Maps/Dictionaries**: Variable storage and lookup
- **Variant Types**: Token value representation (C++)

### Algorithms
- **Shunting-yard Algorithm**: Infix to Reverse Polish Notation conversion
- **Tree Traversal**: Post-order evaluation of expression trees
- **Recursive Algorithms**: Tree evaluation and printing
- **String Parsing**: Tokenization and normalization

### Software Engineering
- **Modular Design**: Separation of concerns (parser, tree, utilities)
- **Error Handling**: Comprehensive exception handling
- **Memory Management**: RAII and smart pointers (C++)
- **Testing**: Unit tests and integration tests
- **Documentation**: Clear README and inline comments
- **Version Control**: Git branching and PR workflow

---

## 🚀 Usage Examples

### Basic Arithmetic
```
3 + 4 * 2           → 11
(3 + 4) * 2         → 14
2 ^ 3 ^ 2           → 512
```

### With Functions
```
√16                 → 4
√(9 + 16)           → 5
√(4^2 + 3^2)        → 5
```

### With Variables
```
x=5 : x^2 + 2*x + 1                     → 36
a=3, b=4 : √(a^2 + b^2)                 → 5
x=7 : √(4^2+3^2) * (x+5) - 10/2         → 55
```

### Complex Expressions
```
((x+y)*z - (a-b))^2 | x=1,y=2,z=3,a=10,b=5  → 16
```

---

## 📈 Performance Benchmarks

Based on 10,000 evaluations of `√(x^2 + y^2)` with `x=3, y=4`:

| Implementation | Time | Relative Speed |
|----------------|------|----------------|
| Python | 2.5s | 1x (baseline) |
| C++ | 0.05s | **50x faster** |

*Tested on: Intel i7, 16GB RAM, Windows 11*

---

## 🏗️ Build Instructions

### Python
```bash
# Install dependencies
pip install -r python/requirements.txt

# Run
cd python/src
python main.py
```

### C++

#### Windows (MinGW)
```bash
cd cpp
mkdir build && cd build
cmake -G "MinGW Makefiles" ..
mingw32-make
expression_evaluator.exe
```

#### Windows (Visual Studio)
```bash
cd cpp
mkdir build && cd build
cmake ..
cmake --build . --config Release
.\Release\expression_evaluator.exe
```

#### Linux/macOS
```bash
cd cpp
mkdir build && cd build
cmake ..
make
./expression_evaluator
```

---

## 🎯 Project Status

| Component | Python | C++ |
|-----------|--------|-----|
| Parser | ✅ Complete | ✅ Complete |
| Tokenizer | ✅ Complete | ✅ Complete |
| RPN Conversion | ✅ Complete | ✅ Complete |
| Expression Tree | ✅ Complete | ✅ Complete |
| Evaluation | ✅ Complete | ✅ Complete |
| Variables | ✅ Complete | ✅ Complete |
| Visualization | ✅ Graphviz | ✅ Text-based |
| Error Handling | ✅ Complete | ✅ Complete |
| Interactive REPL | ✅ Complete | ✅ Complete |
| Tests | ✅ Complete | ✅ Complete |
| Documentation | ✅ Complete | ✅ Complete |

**Both implementations: 100% Complete** ✅

---

## 🔮 Future Enhancements

Potential improvements for learning purposes:
- [ ] Support for more functions (sin, cos, log, etc.)
- [ ] Support for constants (π, e)
- [ ] Expression simplification
- [ ] Derivative calculation
- [ ] Multi-line expressions
- [ ] Expression history
- [ ] Save/load expressions
- [ ] GUI interface
- [ ] Web-based version

---

## 📝 Learning Outcomes

After completing this project, you will understand:

1. **Stack-based Algorithms**
   - How Shunting-yard algorithm works
   - Operator precedence handling
   - Parentheses matching

2. **Tree Data Structures**
   - Binary tree construction
   - Tree traversal (post-order)
   - Recursive algorithms

3. **Language Comparison**
   - Python vs C++ trade-offs
   - Memory management differences
   - Performance characteristics

4. **Software Engineering**
   - Modular code design
   - Error handling strategies
   - Testing methodologies
   - Documentation best practices

---

## 📚 References

- **Shunting-yard Algorithm**: Dijkstra, 1961
- **Expression Trees**: Compiler design fundamentals
- **Reverse Polish Notation**: Jan Łukasiewicz, 1924

---

## 📄 License

MIT License - Free for educational purposes

---

## 👨‍💻 Author

**AmirHossein Rezaaie**
- GitHub: [@AmirHosseinRezaaie](https://github.com/AmirHosseinRezaaie)
- Project: [DS_Project](https://github.com/AmirHosseinRezaaie/DS_Project)

---

## 🙏 Acknowledgments

Built as part of Data Structures course project, demonstrating practical application of:
- Stack data structures
- Binary trees
- Recursive algorithms
- String parsing
- Memory management
- Software design principles

---

## 🚀 Quick Links

- [Python Implementation](python/)
- [C++ Implementation](cpp/)
- [Sample Expressions](python/examples/sample_expressions.txt)
- [Issue Tracker](https://github.com/AmirHosseinRezaaie/DS_Project/issues)

---

**Star ⭐ this repo if you found it helpful!**

