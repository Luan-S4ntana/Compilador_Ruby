import ply.lex as lex 

stack = [0]

def space_counter(token):
    spaces = 0
    for c in token.value:
        if c == ' ':
            spaces += 1
        elif c == '\t':
            spaces += 8 - (spaces % 8)
    return spaces

states = (('idstate', 'exclusive'),
          ('dedstate', 'exclusive'),)

tokens = ['COMMENT', 'MINUS', 'PLUS', 'TIMES', 'DIVIDE', 'REST', 'EXPONEN', 'LSHIFT', 'RSHIFT', 'BIGGEST', 'SMALL','EQUAL', 'SMALLEQUAL', 'BIGGESTEQUAL', 'BIGSMALLERESQUAL','DOUBLEEQUAL','TRIPLEEQUAL', 'DIFF', 'SIMPLEE', 'SIMPLEBAR', 'EXCLAMATION', 'DOUBLEE', 'DOUBLEBAR',  'LPAREN', 'RPAREN', 'AND', 'OR', 'FALSE','TRUE','NOT','IF', 'ELSE', 'ELSIF', 'BEGIN', 'BREAK', 'CLASS', 'DEF', 'DO', 'END', 'FOR', 'IN', 'MODULE', 'NIL', 'RETURN', 'SELF', 'SUPER', 'THEN', 'WHILE', 'NUMBER', 'ID','OPENKEY','CLOSEKEY','PONTO','PONTOEVIRGULA','VIRGULA', 'LINHA', 'IDENT', 'DEDENT']
#Comentário de multiplas linhas
def t_MULTILINECOMMENT(t):
  r'=begin(.|\n)*=end'
  pass
# operadores e delimitadores
t_MINUS = r'-'
t_PLUS = r'\+'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXPONEN = r'\*\*'
t_REST = r'\%'
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_EQUAL = r'\='
t_BIGGEST = r'>'
t_SMALL = r'<'
t_SMALLEQUAL = r'<\='
t_BIGGESTEQUAL = r'>\='
t_BIGSMALLERESQUAL = r'<\=>'
t_DOUBLEEQUAL = r'\=\='
t_TRIPLEEQUAL = r'\=\=\='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PONTO = r'\.'
t_PONTOEVIRGULA = r';'
t_OPENKEY = r'{'
t_CLOSEKEY = r'}'
t_VIRGULA = r','

t_DIFF = r'!='
t_SIMPLEE = r'&'
t_SIMPLEBAR = r'\|'
t_EXCLAMATION = r'\!'
t_DOUBLEE = r'\&\&'
t_DOUBLEBAR = r'\|\|'

# literais reservadas

t_OR = r'or'
t_AND = r'\and'
t_FALSE = r'\false'
t_TRUE = r'\true'
t_NOT = r'\not'

# palavras reservadas
t_IF = r'if '
t_ELSE = r'else '
t_ELSIF = r'elsif'
t_BEGIN = r'begin '
t_BREAK = r'break'
t_CLASS = r'class'
t_DEF = r'def '
t_DO = r'do'
t_END = r'end '
t_FOR = r'for'
t_IN = r'in'
t_MODULE = r'module'
t_NIL = r'nil'
t_RETURN = r'return '
t_SELF = r'self'
t_SUPER = r'super'
t_THEN = r'then'
t_WHILE = r'while'

def t_NUMBER(t):
  r'\d+'
  t.value = int(t.value)
  return t

def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  for key in tokens:
    if key == (t.value).upper():
      t.type = key
      return t
  return t

def t_NUMFLOAT(t):
  r'\d+.\d*'
  t.value = float(t.value)
  return t 

def t_COMMENT(t):
  r'\#.*'

def t_LINHA(t):
  r'[A-Za-z][A-Za-z \t]+'
  t.lexer.begin('indentstate')    
  return t
    

def t_breakline(t):
    r'\n+'                                 
    t.lexer.lineno += len(t.value) 
    t.lexer.begin('idstate')

def t_idstate_blankline(t):
    r'([ \t]+)\n'                          
    pass

def t_idstate_linewithcode(t):
    '([ \t]+) | ([a-zA-Z])'                 
    n_spaces = space_counter(t)
    t.lexer.begin('INITIAL')
    if n_spaces < stack[-1]:
        t.lexer.skip(-len(t.value))
        stack.pop()
        t.type='DEDENT'
        t.lexer.begin('dedstate')
        return t
    elif n_spaces > stack[-1]:
        stack.append(n_spaces)
        t.type='IDENT'
        return t
    elif n_spaces == 0:
        t.lexer.skip(-1)

def t_dedstate_linewithdedent(t):
    '([ \t]+) | ([a-zA-Z])'                 
    n_spaces = space_counter(t)
    if n_spaces < stack[-1]:
        t.lexer.skip(-len(t.value))
        stack.pop()
        t.type='DEDENT'
        return t
    elif n_spaces >= stack[-1]:  
        t.lexer.begin('INITIAL')
        if n_spaces > stack[-1]:
            print('Erro de dedentação --->', n_spaces)
        elif n_spaces == 0:                  
            t.lexer.skip(-1)

def t_error(t):
    print("ERROR in INITIAL state")
    print(t.value)
    t.lexer.skip(1)

def t_idstate_error(t):
    print("ERROR in idstate state")
    t.lexer.skip(1)

def t_dedstate_error(t):
    print("ERROR in dedstate state")
    t.lexer.skip(1)

lex.lex()
programa = """cleardef perm
    if len lsurf   
                
       return lalala land
r sapore torf
    for i in range len l  
             s  lili lost
             p perm
             for x in pix
                append tipo tor
              =begin
              asdiaosdja
              =end
    return r
"""
lex.input(programa)


##for token in lex.lexer:
 ##   print('[', token.type, ',', token.value, ']->', stack)
