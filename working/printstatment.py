import ply.lex as lex
import ply.yacc as yacc

# Token list
tokens = (
    'PRINT',
    'STRING',
    'NUMBER',
)

# Token regular expressions
t_PRINT = r'print'
t_STRING = r'"[^"]*"'
t_NUMBER = r'\d+'

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Grammar rules
def p_statement_print(p):
    'statement : PRINT expression'
    print(p[2])

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1][1:-1]  # Remove quotation marks from the string

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = int(p[1])

def p_error(p):
    if p:
        print("Syntax error at line %d: Unexpected token '%s'" % (p.lineno, p.value))
    else:
        print("Syntax error: Unexpected end of input")

# Build the parser
parser = yacc.yacc()

# Test input
input_string = 'print "Hello, world!"'

# Parsing the input
parser.parse(input_string)
