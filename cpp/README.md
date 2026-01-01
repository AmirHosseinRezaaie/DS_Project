# C++ Implementation

## 🎯 Features

- ✅ Pure C++17 standard library (no external dependencies)
- ✅ Smart pointers for memory safety
- ✅ Complete expression parsing with operator precedence
- ✅ Binary expression tree construction
- ✅ Variable substitution support
- ✅ Comprehensive error handling
- ✅ Text-based tree visualization
- ✅ Interactive REPL interface

## 🛠️ Build Instructions

### Requirements
- C++17 compatible compiler (GCC 7+, Clang 5+, MSVC 2017+)
- CMake 3.10+

### Build Steps

#### Linux/macOS
```bash
cd cpp
mkdir build && cd build
cmake ..
make
```

#### Windows (Visual Studio)
```bash
cd cpp
mkdir build && cd build
cmake ..
cmake --build . --config Release
```

#### Windows (MinGW)
```bash
cd cpp
mkdir build && cd build
cmake -G "MinGW Makefiles" ..
mingw32-make
```

## 🚀 Usage

### Interactive Mode
```bash
./expression_evaluator
```

### Example Session
```
> 3 + 4 * 2
Cleaned:     3+4*2
Normalized:  3+4*2
Tokens:      [Token(NUMBER, 3.000000), Token(OPERATOR, +), ...]
RPN:         [3, 4, 2, *, +]

Expression Tree:
└── +
    ├── 3.000000
    └── *
        ├── 4.000000
        └── 2.000000

Result:      11.00
```

### With Variables
```
> x=7 : √(4^2 + 3^2) * (x + 5) - 10 / 2

Result:      55.00
Variables:   {x=7}
```

## 📁 Project Structure
```
cpp/
├── include/
│   ├── token.hpp       # Token struct and enums
│   ├── parser.hpp      # Parser functions
│   ├── tree.hpp        # Tree operations
│   └── utils.hpp       # Utility functions
├── src/
│   ├── parser.cpp      # Parser implementation
│   ├── tree.cpp        # Tree implementation
│   ├── utils.cpp       # Utilities
│   ├── main.cpp        # REPL interface
│   ├── test_parser.cpp # Parser tests
│   └── test_tree.cpp   # Tree tests
├── examples/
│   ├── sample_expressions.txt
│   └── test_cases.txt
├── build/              # Build directory (generated)
├── CMakeLists.txt      # Build configuration
└── README.md           # This file
```

## 🧪 Testing

### Run Tests
```bash
cd build
./test_parser
./test_tree
```

### Manual Testing
Use expressions from `examples/sample_expressions.txt`:
```bash
./expression_evaluator < ../examples/test_cases.txt
```

## 📊 Supported Operations

| Operation | Symbol | Example | Result |
|-----------|--------|---------|--------|
| Addition | + | 3 + 4 | 7 |
| Subtraction | - | 10 - 5 | 5 |
| Multiplication | * | 3 * 4 | 12 |
| Division | / | 10 / 2 | 5 |
| Power | ^ | 2 ^ 3 | 8 |
| Square Root | √ | √16 | 4 |
| Parentheses | ( ) | (3+4)*2 | 14 |
| Variables | x=val | x=5:x^2 | 25 |

## 🎓 Implementation Details

### Data Structures
- **Token**: Variant type (double or string)
- **Node**: Binary tree with smart pointers
- **Stack**: For Shunting-yard algorithm
- **Map**: For variable storage

### Algorithms
- **Shunting-yard**: Infix to RPN conversion
- **Tree Construction**: Stack-based from RPN
- **Post-order Traversal**: Recursive evaluation

### Memory Management
- **Smart Pointers**: `std::unique_ptr` for tree nodes
- **No Manual Memory**: RAII principles
- **Exception Safety**: Strong guarantee

## ⚠️ Error Handling

The program handles:
- Division by zero
- Square root of negative numbers
- Undefined variables
- Mismatched parentheses
- Invalid expressions
- Unknown operators

## 🔄 Comparison with Python

| Feature | Python | C++ |
|---------|--------|-----|
| Performance | Slower | Faster (compiled) |
| Memory | GC overhead | Manual (smart ptrs) |
| Visualization | Graphviz | Text-based |
| Dependencies | graphviz | None |
| Type Safety | Dynamic | Static |

## 📝 License

MIT License - For educational purposes

## 👨‍💻 Author

[AmirHosseinRezaaie](https://github.com/AmirHosseinRezaaie)