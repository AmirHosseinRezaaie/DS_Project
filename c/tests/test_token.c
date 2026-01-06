#include "../include/token.h"

void test_number_token() {
    printf("Testing number token...\n");
    
    Token* token = create_number_token(3.14);
    printf("  Created: %s\n", token_to_string(token));
    
    if (token->type == TOKEN_NUMBER && token->value.number == 3.14) {
        printf("  ✓ Number token test passed\n");
    } else {
        printf("  ✗ Number token test failed\n");
    }
    
    free_token(token);
}

void test_variable_token() {
    printf("Testing variable token...\n");
    
    Token* token = create_variable_token("x");
    printf("  Created: %s\n", token_to_string(token));
    
    if (token->type == TOKEN_VARIABLE && strcmp(token->value.variable, "x") == 0) {
        printf("  ✓ Variable token test passed\n");
    } else {
        printf("  ✗ Variable token test failed\n");
    }
    
    free_token(token);
}

void test_operator_token() {
    printf("Testing operator token...\n");
    
    Token* token = create_operator_token("+");
    printf("  Created: %s\n", token_to_string(token));
    
    if (token->type == TOKEN_OPERATOR && strcmp(token->value.operator, "+") == 0) {
        printf("  ✓ Operator token test passed\n");
    } else {
        printf("  ✗ Operator token test failed\n");
    }
    
    free_token(token);
}

void test_paren_tokens() {
    printf("Testing parenthesis tokens...\n");
    
    Token* lparen = create_paren_token(TOKEN_LPAREN);
    Token* rparen = create_paren_token(TOKEN_RPAREN);
    
    printf("  Created: %s\n", token_to_string(lparen));
    printf("  Created: %s\n", token_to_string(rparen));
    
    if (lparen->type == TOKEN_LPAREN && rparen->type == TOKEN_RPAREN) {
        printf("  ✓ Parenthesis token test passed\n");
    } else {
        printf("  ✗ Parenthesis token test failed\n");
    }
    
    free_token(lparen);
    free_token(rparen);
}

void test_is_operator() {
    printf("Testing is_operator...\n");
    
    if (is_operator("+") && is_operator("-") && 
        is_operator("*") && is_operator("/") &&
        is_operator("^") && is_operator("√") &&
        !is_operator("x") && !is_operator("5")) {
        printf("  ✓ is_operator test passed\n");
    } else {
        printf("  ✗ is_operator test failed\n");
    }
}

int main(void) {
    printf("========================================\n");
    printf("Token Structure Tests\n");
    printf("========================================\n\n");
    
    test_number_token();
    printf("\n");
    test_variable_token();
    printf("\n");
    test_operator_token();
    printf("\n");
    test_paren_tokens();
    printf("\n");
    test_is_operator();
    
    printf("\n========================================\n");
    printf("All token tests completed!\n");
    printf("========================================\n");
    
    return 0;
}