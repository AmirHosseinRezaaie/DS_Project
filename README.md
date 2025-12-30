# Advanced Mathematical Expression Evaluator with Expression Tree

A high-performance, full-featured mathematical expression parser and evaluator built from scratch using core Data Structures & Algorithms concepts.

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
- ✅ **Graphical visualization** of Expression Tree using Graphviz
- ✅ Clean, modular, and well-structured implementation

## 📁 Project Structure
```
DS_Project/
├── python/           # Python implementation (Complete ✅)
├── cpp/             # C++ implementation (Coming soon 🚧)
└── README.md        # This file
```

## 🐍 Python Implementation

### Requirements
```bash
pip install graphviz
```

### Usage
```bash
cd python/src
python main.py
```

### Example
```
> x=7 : √(4^2 + 3^2) * (x + 5) - 10 / 2
Cleaned:     √(4^2+3^2)*(x+5)-10/2
Normalized:  √(4^2+3^2)*(x+5)-10/2
Tokens:      [Token(NUMBER, 4.0), Token(OPERATOR, ^), ...]
RPN:         [4.0, 2.0, '^', 3.0, 2.0, '^', '+', '√', ...]

Expression Tree:
└── -
    ├── *
    │   ├── √
    │   │   └── +
    │   │       ├── ^
    │   │       │   ├── 4.0
    │   │       │   └── 2.0
    │   │       └── ^
    │   │           ├── 3.0
    │   │           └── 2.0
    │   └── +
    │       ├── x
    │       └── 5.0
    └── /
        ├── 10.0
        └── 2.0

Result:      55.0
```

## 🎓 Educational Value

This project demonstrates:
- **Stack-based algorithms** (Shunting-yard for RPN conversion)
- **Tree data structures** (Binary expression trees)
- **Recursive algorithms** (Tree traversal and evaluation)
- **String parsing** (Tokenization and normalization)
- **Error handling** (Division by zero, invalid input)

## 📊 Implementation Status

| Feature | Python | C++ |
|---------|--------|-----|
| Tokenizer | ✅ | 🚧 |
| RPN Conversion | ✅ | 🚧 |
| Expression Tree | ✅ | 🚧 |
| Evaluation | ✅ | 🚧 |
| Variables | ✅ | 🚧 |
| Visualization | ✅ (Graphviz) | 🚧 (Text-based) |
| Error Handling | ✅ | 🚧 |

## 🚀 Upcoming

- [ ] C++ implementation with standard library only
- [ ] Performance benchmarks
- [ ] Extended operator support
- [ ] Multi-variable expressions

## 📝 License

MIT License - Feel free to use for educational purposes

## 👨‍💻 Author

[AmirHosseinRezaaie](https://github.com/AmirHosseinRezaaie)
