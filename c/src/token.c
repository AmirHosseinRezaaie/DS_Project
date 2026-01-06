#include "token.h"

/* Create number token */
Token* create_number_token(double value) {
    Token* token = (Token*)safe_malloc(sizeof(Token));
    token->type = TOKEN_NUMBER;
    token->value.number = value;
    return token;
}

/* Create variable token */
Token* create_variable_token(const char* name) {
    Token* token = (Token*)safe_malloc(sizeof(Token));
    token->type = TOKEN_VARIABLE;
    strncpy(token->value.variable, name, MAX_TOKEN_LENGTH - 1);
    token->value.variable[MAX_TOKEN_LENGTH - 1] = '\0';
    return token;
}

/* Create operator token */
Token* create_operator_token(const char* op) {
    Token* token = (Token*)safe_malloc(sizeof(Token));
    token->type = TOKEN_OPERATOR;
    strncpy(token->value.operator, op, 3);
    token->value.operator[3] = '\0';
    return token;
}

/* Create parenthesis token */
Token* create_paren_token(TokenType type) {
    Token* token = (Token*)safe_malloc(sizeof(Token));
    token->type = type;
    return token;
}

/* Free token memory */
void free_token(Token* token) {
    if (token != NULL) {
        free(token);
    }
}

/* Convert token to string for debugging */
char* token_to_string(const Token* token) {
    static char buffer[256];
    
    switch (token->type) {
        case TOKEN_NUMBER:
            snprintf(buffer, sizeof(buffer), "Token(NUMBER, %.2f)", token->value.number);
            break;
        case TOKEN_VARIABLE:
            snprintf(buffer, sizeof(buffer), "Token(VARIABLE, %s)", token->value.variable);
            break;
        case TOKEN_OPERATOR:
            snprintf(buffer, sizeof(buffer), "Token(OPERATOR, %s)", token->value.operator);
            break;
        case TOKEN_LPAREN:
            snprintf(buffer, sizeof(buffer), "Token(LPAREN, '(')");
            break;
        case TOKEN_RPAREN:
            snprintf(buffer, sizeof(buffer), "Token(RPAREN, ')')");
            break;
        default:
            snprintf(buffer, sizeof(buffer), "Token(UNKNOWN)");
    }
    
    return buffer;
}

/* Check if string is an operator */
bool is_operator(const char* str) {
    return (strcmp(str, "+") == 0 ||
            strcmp(str, "-") == 0 ||
            strcmp(str, "*") == 0 ||
            strcmp(str, "/") == 0 ||
            strcmp(str, "^") == 0 ||
            strcmp(str, "√") == 0);
}