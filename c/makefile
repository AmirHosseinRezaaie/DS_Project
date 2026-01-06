# Test executables
test_token: $(SRC_DIR)/common.o $(SRC_DIR)/token.o $(TEST_DIR)/test_token.o
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

# Test target
test: test_token
	@echo "Running token tests..."
	./test_token

# ... (بقیه)

.PHONY: all clean debug release run test help

# Compiler settings
CC = gcc
CFLAGS = -std=c99 -Wall -Wextra -Wpedantic -Iinclude
LDFLAGS = -lm

# Directories
SRC_DIR = src
INC_DIR = include
TEST_DIR = tests

# Target executable
TARGET = expression_evaluator

# Source files
SRCS = $(SRC_DIR)/common.c \
       $(SRC_DIR)/token.c \
       $(SRC_DIR)/main.c

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

# Test executables
test_token: $(SRC_DIR)/common.o $(SRC_DIR)/token.o $(TEST_DIR)/test_token.o
	@echo "Building test_token..."
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

# Test target
test: test_token
	@echo "Running tests..."
	@echo ""
	./test_token

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

# Help
help:
	@echo "Available targets:"
	@echo "  make          - Build the project"
	@echo "  make test     - Build and run tests"
	@echo "  make debug    - Build with debug symbols"
	@echo "  make release  - Build optimized release"
	@echo "  make clean    - Remove build files"
	@echo "  make run      - Build and run"
	@echo "  make help     - Show this help"

.PHONY: all clean debug release run test help