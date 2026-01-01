cmake_minimum_required(VERSION 3.10)
project(ExpressionEvaluator)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include directories
include_directories(include)

# Parser library
add_library(parser src/parser.cpp)

# Test parser (optional)
add_executable(test_parser src/test_parser.cpp)
target_link_libraries(test_parser parser)

# Main executable (will be added in Phase 3)
# add_executable(expression_evaluator src/main.cpp)
# target_link_libraries(expression_evaluator parser tree utils)