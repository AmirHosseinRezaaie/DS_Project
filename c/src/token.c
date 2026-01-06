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