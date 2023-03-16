import ply.lex as lex 

TOP = -1
stack = [0]

tokens = ("LINHA", "WHITESPACE", "INDENT", "DEDENT", "EOF")

states = (
  ('dedentstate', 'exclusive'),
  ('indentstate', 'exclusive'),
)

tokens =['COMMENT', 'MINUS', 'PLUS', 'TIMES', 'DIVIDE', 'REST', 'EXPONEN', 'LSHIFT', 'RSHIFT', 'BIGGEST', 'SMALL','EQUAL', 'SMALLEQUAL', 'BIGGESTEQUAL', 'BIGSMALLERESQUAL','DOUBLEEQUAL','TRIPLEEQUAL', 'DIFF', 'SIMPLEE', 'SIMPLEBAR', 'EXCLAMATION', 'DOUBLEE', 'DOUBLEBAR', 'ATR', 'LPAREN', 'RPAREN', 'AND', 'OR', 'FALSE','TRUE','NOT','IF', 'ELSE', 'ELSIF', 'BEGIN', 'BREAK', 'CLASS', 'DEF', 'DO', 'END', 'FOR', 'IN', 'MODULE', 'NIL', 'RETURN', 'SELF', 'SUPER', 'THEN', 'WHILE', 'NUMBER', 'ID','OPENKEY','CLOSEKEY','PONTO','PONTOEVIRGULA','VIRGULA']

# operadores e delimitadores
t_MINUS = r'-'
t_PLUS = r'\+'
t_TIMES = r'\*'
t_DIVIDE = r'\\'
t_EXPONEN = r'\*\*'
t_REST = r'\%'
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_EQUAL = r'\='
t_BIGGEST = r'>'
t_SMALL = r'<'
t_SMALLEQUAL = r'<\='
t_BIGGESTEQUAL = r'>\='
t_BIGGSMALLEQUAL = r'<\=>'
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
t_ATR = r'='

# literais reservadas

t_OR = r'\or'
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

def t_COMMENT(t):
  r'\#.*'

def t_LINHA(t):
  r'[A-Za-z][A-Za-z \t]+'
  t.lexer.begin('indentstate')    
  return t
    

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)


#INDENT STATE
def t_indentstate_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


def t_indentstate_error(t):
  print("Erro de identacao '%s'" % t.value[0])
  t.lexer.skip(1)


def t_indentstate_WHITESPACE(t):
  r'[ \t]+'
  spaces_in_token = 0

  for space in t.value:
    if space == ' ':
      spaces_in_token += 1

  if spaces_in_token > stack[TOP]:
    stack.append(spaces_in_token)
    t.type = 'INDENT'
    t.lexer.begin('INITIAL')
    return t

  elif spaces_in_token < stack[TOP]:
    t.lexer.skip(-len(t.value))
    t.lexer.begin('dedentstate')

  elif spaces_in_token == stack[TOP]:
    t.lexer.begin('INITIAL')


#DEDENT STATE
def t_dedentstate_WHITESPACE(t):
  r'[ \t]+'
  spaces_in_token = 0

  for space in t.value:
    if space == ' ':
      spaces_in_token += 1

  if spaces_in_token < stack[TOP]:
    stack.pop()
    t.type = 'DEDENT'
    t.lexer.skip(-len(t.value))

    return t

  elif spaces_in_token > stack[TOP]:
    stack.append(spaces_in_token)
    t.lexer.begin('INITIAL')
    

  else:
    t.lexer.begin('INITIAL')


def t_dedentstate_error(t):
  print("Erro de dendentação '%s'" % t.value[0])
  t.lexer.skip(1)
