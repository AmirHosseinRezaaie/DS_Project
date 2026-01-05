#ifndef COMMON_H
#define COMMON_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include <math.h>

/* Version information */
#define VERSION_MAJOR 1
#define VERSION_MINOR 0
#define VERSION_PATCH 0

/* Configuration */
#define MAX_INPUT_LENGTH 1024
#define MAX_TOKEN_LENGTH 256
#define INITIAL_ARRAY_CAPACITY 16
#define INITIAL_STACK_CAPACITY 32
#define HASHMAP_SIZE 64

/* Error codes */
typedef enum {
    SUCCESS = 0,
    ERROR_MEMORY_ALLOCATION = 1,
    ERROR_INVALID_INPUT = 2,
    ERROR_DIVISION_BY_ZERO = 3,
    ERROR_NEGATIVE_SQRT = 4,
    ERROR_UNDEFINED_VARIABLE = 5,
    ERROR_MISMATCHED_PARENTHESES = 6,
    ERROR_INVALID_EXPRESSION = 7
} ErrorCode;

/* Safe memory allocation wrapper */
void* safe_malloc(size_t size);
void* safe_realloc(void* ptr, size_t size);

/* Error handling */
void print_error(ErrorCode code, const char* message);

#endif /* COMMON_H */