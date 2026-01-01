cmake_minimum_required(VERSION 3.10)
project(ExpressionEvaluator)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include directories
include_directories(include)

# Libraries
add_library(parser src/parser.cpp)
add_library(tree src/tree.cpp)
add_library(utils src/utils.cpp)

# Test executables
add_executable(test_parser src/test_parser.cpp)
target_link_libraries(test_parser parser)

add_executable(test_tree src/test_tree.cpp)
target_link_libraries(test_tree parser tree utils)

# Main executable (Phase 4)
# add_executable(expression_evaluator src/main.cpp)
# target_link_libraries(expression_evaluator parser tree utils)