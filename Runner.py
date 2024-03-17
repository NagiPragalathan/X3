from Parser.parser import parser

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    parser.parse(s)
