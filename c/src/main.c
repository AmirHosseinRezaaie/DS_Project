#include "common.h"

int main(void) {
    printf("========================================\n");
    printf("Expression Evaluator (C Implementation)\n");
    printf("Version %d.%d.%d\n", VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH);
    printf("========================================\n");
    printf("\nProject structure initialized!\n");
    printf("Status: Setup complete\n");
    
    /* Test safe memory allocation */
    char* test = (char*)safe_malloc(100 * sizeof(char));
    strcpy(test, "Memory allocation working!");
    printf("\nTest: %s\n", test);
    free(test);
    
    printf("\nNext: Implementing data structures...\n");
    
    return SUCCESS;
}