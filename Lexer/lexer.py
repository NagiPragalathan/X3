import ply.lex as lex
from Tokens.defaultToken import *

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t'

# Define the regular expressions for these tokens
t_FLOOR_DIVIDE = r'//'
t_POWER = r'\*\*'


def t_NUMBER(t):
    r'\d+(\.\d+)?'  # Regular expression for float numbers
    try:
        t.value = float(t.value)  # Convert the token value to float
    except ValueError:
        print("Invalid number:", t.value)
        t.value = 0.0
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
