import ply.lex as lex


tokens = ['COMMENT', 'MINUS', 'PLUS', 'TIMES', 'DIVIDE', 'REST', 'EXPONEN', 'LSHIFT', 'RSHIFT', 'BIGGEST', 'SMALL','EQUAL', 'SMALLEQUAL', 'BIGGESTEQUAL', 'BIGSMALLERESQUAL','DOUBLEEQUAL','TRIPLEEQUAL', 'DIFF', 'SIMPLEE', 'SIMPLEBAR', 'EXCLAMATION', 'DOUBLEE', 'DOUBLEBAR',  'LPAREN', 'RPAREN', 'AND', 'OR', 'FALSE','TRUE','NOT','IF', 'ELSE', 'ELSIF', 'BEGIN', 'BREAK', 'CLASS', 'DEF', 'DO', 'END', 'FOR', 'IN', 'MODULE', 'NIL', 'RETURN', 'SELF', 'SUPER', 'THEN', 'WHILE', 'NUMBER', 'ID','OPENKEY','CLOSEKEY','PONTO','PONTOEVIRGULA','VIRGULA', 'LINHA', 'IDENT', 'DEDENT','BREAKLINE']

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
  return t
    
def t_BREAKLINE(t):
  r'\n+'                                 
  return t

def t_BRANCO(t):
  r'\s+'
  pass

def t_error(t):
    print("ERROR in INITIAL state[", t.value, "]")
   ## print(t.value)
    t.lexer.skip(1)

lex.lex()
programa = """def perm
    if len
       return 2
    for i in r do 
             s = lili + lost
             p = perm
             for x in pix
                append = x + pix
              =begin
              asdiaosdja
              =end
    return
    end
"""
lex.input(programa)


#for token in lex.lexer:
#    print('[', token.type, ',', token.value, ']->')
