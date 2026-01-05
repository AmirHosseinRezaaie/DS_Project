# Compiler settings
CC = gcc
CFLAGS = -std=c99 -Wall -Wextra -Wpedantic -Iinclude
LDFLAGS = -lm

# Directories
SRC_DIR = src
INC_DIR = include
TEST_DIR = tests
BUILD_DIR = build

# Target executable
TARGET = expression_evaluator

# Source files (will be added progressively)
SRCS = 

# Object files
OBJS = $(SRCS:.c=.o)

# Default target
all: $(TARGET)

# Build executable
$(TARGET): $(OBJS)
	@echo "Building $(TARGET)..."
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)
	@echo "Build complete!"

# Compile source files
%.o: %.c
	@echo "Compiling $<..."
	$(CC) $(CFLAGS) -c $< -o $@

# Clean build files
clean:
	@echo "Cleaning..."
	rm -f $(SRC_DIR)/*.o $(TEST_DIR)/*.o
	rm -f $(TARGET) test_*
	@echo "Clean complete!"

# Debug build
debug: CFLAGS += -g -DDEBUG
debug: clean $(TARGET)

# Release build
release: CFLAGS += -O2 -DNDEBUG
release: clean $(TARGET)

# Run program
run: $(TARGET)
	./$(TARGET)

# Memory check with valgrind (Linux/macOS)
valgrind: $(TARGET)
	valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./$(TARGET)

# Help
help:
	@echo "Available targets:"
	@echo "  make          - Build the project"
	@echo "  make debug    - Build with debug symbols"
	@echo "  make release  - Build optimized release"
	@echo "  make clean    - Remove build files"
	@echo "  make run      - Build and run"
	@echo "  make valgrind - Run with memory checker"
	@echo "  make help     - Show this help"

.PHONY: all clean debug release run valgrind help