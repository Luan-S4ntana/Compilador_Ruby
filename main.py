from sintatico import *
parser = yacc.yacc()
parser.parse(debug = True)