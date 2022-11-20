import lexer
from lexer import Token, TokenType

tokens_from_lex = []
next_token = None
token_position = 0

begin_token = Token("begin", TokenType.KEYWORD)
end_token = Token("end", TokenType.KEYWORD)
loop_token = Token("loop", TokenType.KEYWORD)
either_token = Token("either", TokenType.KEYWORD)
or_token = Token("or", TokenType.KEYWORD)
ant_token = Token("ant", TokenType.KEYWORD)
semi_token = Token(";", TokenType.SPECIAL_SYMBOL)
lpar_token = Token("(", TokenType.SPECIAL_SYMBOL)
rpar_token = Token(")", TokenType.SPECIAL_SYMBOL)
less_token = Token("<", TokenType.OPERATOR)
less_eq_token = Token("<=", TokenType.OPERATOR)
great_token = Token(">", TokenType.OPERATOR)
great_eq_token = Token(">=", TokenType.OPERATOR)
eq_token = Token("==", TokenType.OPERATOR)
neq_token = Token("!=", TokenType.OPERATOR)
assign_token = Token("=", TokenType.OPERATOR)
div_token = Token("/", TokenType.OPERATOR)
mult_token = Token("*", TokenType.OPERATOR)
mod_token = Token("%", TokenType.OPERATOR)
plus_token = Token("+", TokenType.OPERATOR)
minus_token = Token("-", TokenType.OPERATOR)


def compare_tokens(token1, token2):
    if token1 is None or token2 is None:
        return False
    return token1.value == token2.value and token1.token_type == token2.token_type


def error(message):
    raise SyntaxError("{first} => {second}".format(
        first=next_token, second=message))


def switchNextToken():
    global tokens_from_lex, next_token, token_position
    if token_position < len(tokens_from_lex):
        print(next_token)
        next_token = tokens_from_lex[token_position]
        token_position += 1
    else:
        next_token = None
        error("Unexpected end of file!")


def check_var():
    print("Enter <var>")
    if not (next_token.token_type == TokenType.ID or next_token.token_type == TokenType.NUMBER):
        error("ID or Number token type is not matched!")
    switchNextToken()
    print("Exit <var>")


def check_factor():
    print("Enter <factor>")
    if compare_tokens(next_token, lpar_token):
        switchNextToken()
        check_expr()
        if not compare_tokens(next_token, rpar_token):
            error(") is missing")
        switchNextToken()
    else:
        check_var()
    print("Exit <factor>")


def check_term():
    print("Enter <term>")
    check_factor()
    while compare_tokens(next_token, div_token) or compare_tokens(next_token, mult_token)\
            or compare_tokens(next_token, mod_token):
        switchNextToken()
        check_factor()
    print("Exit <term>")


def check_expr():
    print("Enter <expr>")
    check_term()
    while compare_tokens(next_token, plus_token) or compare_tokens(next_token, minus_token):
        switchNextToken()
        check_term()
    print("Exit <expr>")


def compare_tokens_rel_op(next_token):
    return compare_tokens(next_token, eq_token) or compare_tokens(next_token, neq_token)\
        or compare_tokens(next_token, less_token) or compare_tokens(next_token, less_eq_token)\
        or compare_tokens(next_token, great_token) or compare_tokens(next_token, great_eq_token)


def check_cmp_expr():
    print("Enter <cmp_exp>")
    check_expr()
    while compare_tokens_rel_op(next_token):
        switchNextToken()
        check_expr()
    print("Exit <cmp_exp>")


def check_assignment():
    print("Enter <assignment>")
    if next_token.token_type != TokenType.ID:
        error("ID is missing!")
    switchNextToken()
    if not compare_tokens(next_token, assign_token):
        error("Operator = is not in place!")
    switchNextToken()
    check_cmp_expr()
    print("Exit <assignment>")


def check_declaration():
    print("Enter <declaration>")
    if not compare_tokens(next_token, ant_token):
        error("Keyword ant is not in place!")
    switchNextToken()
    if next_token.token_type != TokenType.ID:
        error("ID is missing!")
    else:
        switchNextToken()
    print("Exit <declaration>")


def check_loop():
    print("Enter <loop>")
    if not compare_tokens(next_token, loop_token):
        error("Keyword loop is not in place!")
    switchNextToken()
    if not compare_tokens(next_token, lpar_token):
        error("( is not in place!")
    switchNextToken()
    check_cmp_expr()
    if not compare_tokens(next_token, rpar_token):
        error(") is not in place!")
    switchNextToken()
    check_stmt()
    print("Exit <loop>")


def check_conditional_st():
    print("Enter <condition>")
    if not compare_tokens(next_token, either_token):
        error("Keyword either is not in place!")
    switchNextToken()
    if not compare_tokens(next_token, lpar_token):
        error("( is not in place!")
    switchNextToken()
    check_cmp_expr()
    if not compare_tokens(next_token, rpar_token):
        error(") is not in place!")
    switchNextToken()
    check_stmt()
    if compare_tokens(next_token, or_token):
        switchNextToken()
        check_stmt()
    print("Exit <condition>")


def check_stmt():
    print("Enter <stmt>")
    if compare_tokens(next_token, ant_token):
        check_declaration()
    elif compare_tokens(next_token, loop_token):
        check_loop()
    elif compare_tokens(next_token, either_token):
        check_conditional_st()
    elif next_token.token_type == TokenType.ID:
        check_assignment()
    else:
        error("Keyword or ID is missing!")
    if not compare_tokens(next_token, semi_token):
        error("Terminal symbol is missing!")
    switchNextToken()
    print("Exit <stmt>")


def check_program():
    # checks begin and end
    print("Enter <program>")
    switchNextToken()
    if not compare_tokens(next_token, begin_token):
        error("No begin token!")
    switchNextToken()
    while not compare_tokens(next_token, end_token) or next_token is None:
        check_stmt()
    if not compare_tokens(next_token, end_token):
        error("No end token!")
    print("Exit <program>")

tokens_from_lex = lexer.parse('test.txt')
#print(tokens_from_lex)
check_program()


