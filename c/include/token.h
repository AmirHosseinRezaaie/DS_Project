#ifndef TOKEN_H
#define TOKEN_H

#include "common.h"

/* Token types */
typedef enum {
    TOKEN_NUMBER,      /* 3.14, 5, 0.5 */
    TOKEN_VARIABLE,    /* x, y, count */
    TOKEN_OPERATOR,    /* +, -, *, /, ^, √ */
    TOKEN_LPAREN,      /* ( */
    TOKEN_RPAREN       /* ) */
} TokenType;

/* Token structure */
typedef struct {
    TokenType type;
    union {
        double number;           /* For TOKEN_NUMBER */
        char variable[MAX_TOKEN_LENGTH];  /* For TOKEN_VARIABLE */
        char operator[4];        /* For TOKEN_OPERATOR */
    } value;
} Token;

/* Token creation functions */
Token* create_number_token(double value);
Token* create_variable_token(const char* name);
Token* create_operator_token(const char* op);
Token* create_paren_token(TokenType type);

/* Token utility functions */
void free_token(Token* token);
char* token_to_string(const Token* token);
bool is_operator(const char* str);

#endif /* TOKEN_H */