import ply.yacc as yacc
from lexico import *

precedence = (
    ('left', 'OR', 'AND'),
    ('left', 'DIFF','DOUBLEEQUAL','TRIPLEEQUAL'),
    ('left', 'BIGGESTEQUAL','BIGGEST','SMALL','SMALLEQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE','REST'),
    ('left', 'EXPONEN'),
    ('left', 'ID')
)

def p_program(p):
  '''program : funcao program'''
  p[0]= p[1] + p[2]
  
def p_program_assignProgram(p):
  '''program : assign program'''
  p[0]= p[1] + p[2]
  
def p_program_assign(p):
  '''program : assign '''
  p[0]= p[1]
  
def p_program_func(p):
  '''program : funcao'''
  p[0] = p[1]
  
def p_funcao(p):
  '''funcao : DEF ID LPAREN sigParams RPAREN BREAKLINE body'''
  p[0]= p[1] + p[2]+ p[3] + p[4] + p[5] + p[6]

def p_funcao2(p):
  '''funcao : DEF ID BREAKLINE body'''
  p[0]= p[1] + p[2]+ p[3] + p[4]
  
def p_stms(p):
  '''stms : stm  
          |  stm stms'''
  if (len(p) == 2):
    p[0] = p[1] + p[2]
  else:
    p[0] = p[1]
  
def p_opcional(p):
  '''opcional : ELSIF exp THEN body  
              | ELSE stms END 
              | 
              | ELSIF exp THEN body opcional'''
  if (len(p) == 4):
    p[0] = p[1] + p[2] + p[3] + p[4]
  elif (len(p) == 3):
    p[0] = p[1] + p[2] + p[3]
  elif (len(p) == 5):
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
  else:
    p[0]

def p_body(p):
  '''body : stms END'''
  p[0] = p[1] + p[2]
  
    ###                                     LEMBRETEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE 
    ### tirar o pass e adicionar o vetor que fara a analise sintatica de cada regra p[0] = p[1] + p[2]
def p_stms_while1(p):
  '''stm : exp BREAKLINE 
        |   WHILE LPAREN exp RPAREN BREAKLINE body
  '''
  if (len(p) == 6):
    p[0] = p[1] + p[2] + p[3] + p[3] + p[4] + p[5] + p[6]
    
  else:
    p[0] = p[1] + p[2]
  
def p_stms_while2(p):
  '''stm : WHILE exp BREAKLINE body'''
  p[0] = p[1] + p[2] + p[3] + p[4]
  
def p_stms_for1(p):
  '''stm : FOR ID IN exp DO BREAKLINE body'''
  p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]

def p_stms_for2(p):
  '''stm : FOR ID IN exp BREAKLINE body'''
  p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

def p_stms_if1(p):
  '''stm : IF exp THEN BREAKLINE body opcional'''
  p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

def p_smts_if2(p):
  '''stm : IF exp BREAKLINE body opcional'''
  p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

def p_stms_if3(p):
  '''stm : IF LPAREN exp RPAREN THEN BREAKLINE body opcional'''
  p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8]

def p_stms_if4(p):
  '''stm : IF LPAREN exp RPAREN BREAKLINE body opcional'''
  p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]

def p_stms_return(p):
  '''stm : RETURN exp BREAKLINE'''
  p[0] = p[1] + p[2] + p[3]

def p_stms_return2(p):
  '''stm : RETURN BREAKLINE'''
  p[0] = p[1] + p[2]
  
#expressoes
def p_exp_soma(p):
  '''exp : exp PLUS exp'''
  p[0] = p[1] + p[2] + p[3]
  
def p_exp_exponen(p):
  '''exp : exp EXPONEN exp'''
  p[0] = p[1] + p[2] + p[3]
  
def p_exp_subtracao(p):
  '''exp : exp MINUS exp'''
  p[0] = p[1] + p[2] + p[3]

def p_exp_multiplicacao(p):
  '''exp : exp TIMES exp'''
  p[0] = p[1] + p[2] + p[3]

def p_exp_divisao(p):
  '''exp : exp DIVIDE exp'''
  p[0] = p[1] + p[2] + p[3]

def p_exp_mod(p):
  '''exp : exp REST exp'''
  p[0] = p[1] + p[2] + p[3]

def p_exp_doubleequal(p):
  '''exp : exp DOUBLEEQUAL exp'''
  p[0] = p[1] + p[2] + p[3]

def p_exp_tripleequal(p):
  '''exp : exp TRIPLEEQUAL exp'''
  p[0] = p[1] + p[2] + p[3]

def p_exp_diff(p):
  '''exp : exp DIFF exp'''
  p[0] = p[1] + p[2] + p[3]

def p_exp_maiorQue(p):
  '''exp : exp BIGGEST exp'''
  p[0] = p[1] + p[2] + p[3]

def p_exp_maiorQueIgual(p):
  '''exp : exp BIGGESTEQUAL exp'''
  p[0] = p[1] + p[2] + p[3]

def p_exp_menorQue(p):
  '''exp : exp SMALL exp'''
  p[0] = p[1] + p[2] + p[3]

def p_exp_menorQueIgual(p):
  '''exp : exp SMALLEQUAL exp'''
  p[0] = p[1] + p[2] + p[3]

def p_exp_or(p):
  '''exp : exp OR exp'''
  p[0] = p[1] + p[2] + p[3]

def p_exp_and(p):
  '''exp : exp AND exp'''
  p[0] = p[1] + p[2] + p[3]

def p_exp_call(p):
  '''exp : call'''
  p[0] = p[1]
  
def p_exp_assign(p):
  '''exp : assign'''
  p[0] = p[1]
  
def p_expNum(p):
  '''exp : NUMBER'''
  p[0] = p[1]
  
def p_call_complete(p):
  '''call : ID LPAREN sigParams RPAREN'''
  p[0] = p[1] + p[2] + p[3] + p[4]

def p_call_without_param(p):
  '''call : ID LPAREN RPAREN'''
  p[0] = p[1] + p[2] + p[3]

def p_call_only_id(p):
  '''call : ID'''
  p[0] = p[1]

def p_call_only_id_param(p):
  '''call : ID sigParams'''
  p[0] = p[1] + p[2]

def p_sigparams(p):
  '''sigParams :  exp'''
  p[0] = p[1]

def p_sigparams1(p):
  '''sigParams :  exp VIRGULA sigParams'''
  p[0] = p[1] + p[2] + p[3]

def p_assign(p):
  '''assign : ID EQUAL exp'''
  p[0] = p[1] + p[2] + p[3]

def p_assign_break(p):
  '''stm : assign BREAKLINE'''
  p[0] = p[1] + p[2]

def p_error(p):
    print("Syntax error in input!")