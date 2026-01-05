#include "common.h"

/* Safe malloc with error checking */
void* safe_malloc(size_t size) {
    void* ptr = malloc(size);
    if (ptr == NULL) {
        fprintf(stderr, "Error: Memory allocation failed\n");
        exit(ERROR_MEMORY_ALLOCATION);
    }
    return ptr;
}

/* Safe realloc with error checking */
void* safe_realloc(void* ptr, size_t size) {
    void* new_ptr = realloc(ptr, size);
    if (new_ptr == NULL && size > 0) {
        fprintf(stderr, "Error: Memory reallocation failed\n");
        free(ptr);
        exit(ERROR_MEMORY_ALLOCATION);
    }
    return new_ptr;
}

/* Print error message based on error code */
void print_error(ErrorCode code, const char* message) {
    fprintf(stderr, "Error [%d]: ", code);
    
    switch (code) {
        case ERROR_MEMORY_ALLOCATION:
            fprintf(stderr, "Memory allocation failed");
            break;
        case ERROR_INVALID_INPUT:
            fprintf(stderr, "Invalid input");
            break;
        case ERROR_DIVISION_BY_ZERO:
            fprintf(stderr, "Division by zero");
            break;
        case ERROR_NEGATIVE_SQRT:
            fprintf(stderr, "Square root of negative number");
            break;
        case ERROR_UNDEFINED_VARIABLE:
            fprintf(stderr, "Undefined variable");
            break;
        case ERROR_MISMATCHED_PARENTHESES:
            fprintf(stderr, "Mismatched parentheses");
            break;
        case ERROR_INVALID_EXPRESSION:
            fprintf(stderr, "Invalid expression");
            break;
        default:
            fprintf(stderr, "Unknown error");
    }
    
    if (message != NULL) {
        fprintf(stderr, ": %s", message);
    }
    
    fprintf(stderr, "\n");
}