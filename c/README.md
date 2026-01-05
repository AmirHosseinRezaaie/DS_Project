# C Implementation

## 🎯 Overview
Pure C (C99) implementation of the Mathematical Expression Evaluator using only standard library.

## 🛠️ Build Requirements
- C compiler (GCC 7+ or Clang 5+)
- Make
- Standard C library

## 📦 Build Instructions

### Linux/macOS
```bash
cd c
make
./expression_evaluator
```

### Windows (MinGW)
```bash
cd c
mingw32-make
expression_evaluator.exe
```

## 🚀 Quick Start
```bash
# Build
make

# Run
make run

# Debug build
make debug

# Clean
make clean
```

## 📁 Project Structure
```
c/
├── include/        # Header files
├── src/            # Source files
├── tests/          # Test programs
├── examples/       # Sample expressions
├── Makefile        # Build configuration
└── README.md       # This file
```

## 🎓 Implementation Status
- [ ] Data Structures
- [ ] Parser
- [ ] Expression Tree
- [ ] Variable Management
- [ ] Main Program
- [ ] Documentation

## 📝 Memory Management
This implementation uses manual memory management:
- All `malloc()` calls have corresponding `free()` calls
- Proper cleanup on error paths
- Verified with valgrind

## 🔗 Related Implementations
- [Python Implementation](../python/)
- [C++ Implementation](../cpp/)

---

**Status**: 🚧 In Development