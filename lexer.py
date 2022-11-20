import re
from enum import Enum

class TokenType(Enum):
    NONE = 0
    ID = 1
    NUMBER = 2
    OPERATOR = 3
    SPECIAL_SYMBOL = 4
    KEYWORD = 5

class Token:
    def __init__(self, value, token_type) -> None:
        self.value = value
        self.token_type = token_type
    def __str__(self) -> str:
        return 'Token(value="{}",TokenType="{}")'.format(self.value, self.token_type)
    def __repr__(self) -> str:
        return self.__str__()
        

keywords = { 'loop': 'LOOP', 'either': 'EITHER', 'or':'OR',
            'begin':'BEGIN', 'end':'END', 'ant':'ANT'} 



# token_types = {'<':'cmp_op', '>':'cmp_op', '<=':'cmp_op', '>=':'cmp_op', '==':'cmp',
#                 '!=':'cmp', '=':'asgn_op', '/':'hi_op', '*':'hi_op', '%':'hi_op',
#                 '+':'low_op', '-':'low_op', ';':'sta_sep', '(':'br_left', ')':'br_right'}

operator_chars = "<>=!/*%+-"
special_symbols = ";()"

def checkIDlen(line):
    #print(line)
    if len(line) < 6 or len(line) > 8:
        raise ValueError("ID length is not correct => token: {}".format(line))

def checkNumber(num):
    num_re = r'[0-9]+\$[1248]'
    if re.match(num_re, num) is None:
        raise ValueError("Integer literal is not correct => token: {}".format(num))

def checkOperator(oper):
    operators = set(['<','>', '<=', '>=', '==', '!=', '/', '*', '%', '+', '-', '='])
    if oper not in operators:
        raise ValueError("Operator is not correct => token: {}".format(oper))







def parse(file_name):
    file = open(file_name, 'r')
    data = file.read()
    exit = False
    position = 0
    tokens = []
    value = ""
    state = TokenType.NONE
    try:
        while not exit:  
            if state == TokenType.NONE:
                if data[position].isalpha() or data[position] == "_":
                    state = TokenType.ID
                    value = data[position]
                elif data[position].isdigit():
                    state = TokenType.NUMBER
                    value = data[position]
                elif data[position] in operator_chars:
                    state = TokenType.OPERATOR
                    value = data[position]
                elif data[position] in special_symbols:
                    tokens.append(Token(data[position], TokenType.SPECIAL_SYMBOL))
                elif data[position].isspace():
                    pass
                else:
                    raise ValueError("Symbol is not defined.")
            elif state == TokenType.ID:
                if data[position].isalpha() or data[position] == "_":
                    value += data[position]
                elif data[position].isdigit():
                    state = TokenType.NUMBER
                    if value in keywords:
                        tokens.append(Token(value, TokenType.KEYWORD))
                    else:
                        checkIDlen(value)
                        tokens.append(Token(value, TokenType.ID))
                    value = data[position]
                    # or NONE
                elif data[position] in operator_chars:
                    state = TokenType.OPERATOR
                    if value in keywords:
                        tokens.append(Token(value, TokenType.KEYWORD))
                    else:
                        checkIDlen(value)
                        tokens.append(Token(value, TokenType.ID))
                    value = data[position]
                elif data[position] in special_symbols:
                    state = TokenType.NONE
                    if value in keywords:
                        tokens.append(Token(value, TokenType.KEYWORD))
                    else:
                        checkIDlen(value)
                        tokens.append(Token(value, TokenType.ID))
                    value = ""
                    tokens.append(Token(data[position], TokenType.SPECIAL_SYMBOL))
                elif data[position].isspace():
                    state = TokenType.NONE
                    if value in keywords:
                        tokens.append(Token(value, TokenType.KEYWORD))
                    else:
                        checkIDlen(value)
                        tokens.append(Token(value, TokenType.ID))
                    value = ""
                else:
                    raise ValueError("Symbol is not defined.")
            elif state == TokenType.NUMBER:
                if data[position].isalpha() or data[position] == "_":
                    state = TokenType.ID
                    checkNumber(value)
                    tokens.append(Token(value, TokenType.NUMBER))
                    value = data[position]
                elif data[position].isdigit() or data[position] == "$":
                    value += data[position]
                    # or NONE
                elif data[position] in operator_chars:
                    state = TokenType.OPERATOR
                    checkNumber(value)
                    tokens.append(Token(value, TokenType.NUMBER))
                    value = data[position]
                elif data[position] in special_symbols:
                    state = TokenType.NONE
                    checkNumber(value)
                    tokens.append(Token(value, TokenType.NUMBER))
                    tokens.append(Token(data[position], TokenType.SPECIAL_SYMBOL))
                    value = ""
                elif data[position].isspace():
                    state = TokenType.NONE
                    checkNumber(value)
                    tokens.append(Token(value, TokenType.NUMBER))
                    value = ""
                else:
                    raise ValueError("Symbol is not defined.")
            elif state == TokenType.OPERATOR:
                if data[position].isalpha() or data[position] == "_":
                    state = TokenType.ID
                    checkOperator(value)
                    tokens.append(Token(value, TokenType.OPERATOR))
                    value = data[position]
                elif data[position].isdigit() or data[position] == "$":
                    state = TokenType.NUMBER
                    checkOperator(value)
                    tokens.append(Token(value, TokenType.OPERATOR))
                    value = data[position]
                    # or NONE
                elif data[position] in operator_chars:
                    value += data[position]
                elif data[position] in special_symbols:
                    state = TokenType.NONE
                    checkOperator(value)
                    tokens.append(Token(value, TokenType.OPERATOR))
                    tokens.append(Token(data[position], TokenType.SPECIAL_SYMBOL))
                    value = ""
                elif data[position].isspace():
                    state = TokenType.NONE
                    checkOperator(value)
                    tokens.append(Token(value, TokenType.OPERATOR))
                    value = ""
                else:
                    raise ValueError("Symbol is not defined.")
            position += 1
            if position >= len(data):
                if state == TokenType.ID:
                    state = TokenType.NONE
                    if value in keywords:
                        tokens.append(Token(value, TokenType.KEYWORD))
                    else:
                        checkIDlen(value)
                        tokens.append(Token(value, TokenType.ID))
                    value = ""
                elif state == TokenType.NUMBER:
                    state = TokenType.NONE
                    checkNumber(value)
                    tokens.append(Token(value, TokenType.NUMBER))
                    value = ""
                elif state == TokenType.OPERATOR:
                    state = TokenType.NONE
                    checkOperator(value)
                    tokens.append(Token(value, TokenType.OPERATOR))
                    value = ""
                break

    except:
        print(tokens)
        raise

    file.close()
    return tokens

if __name__ == "__main__":
    tokens = parse('test.txt')

    for token in tokens:
        print(token)

