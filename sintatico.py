import ply.yacc as yacc
from lexico import *

def p_program(p):
  '''program : funcao program'''
  pass
def p_program_ID(p):
  '''program : ID'''
  pass
  
def p_program_assign(p):
  '''program : assign '''
  pass
  
def p_program_func(p):
  '''program : funcao'''
  pass
def p_funcao(p):
  '''funcao : DEF ID LPAREN sigParams RPAREN stms END'''
  pass
  
def p_stms(p):
  '''stms : stm | 
            stm stms'''
  pass
  
def p_opcional(p):
  '''opcional : ELSIF exp THEN stms END | 
                ELSE stms END |
                '''
  pass
def p_stms_while1(p):
  '''stm : exp |
           WHILE LAPREN exp RPAREN stms END
  '''
  pass
  
def p_stms_while2(p):
  '''stm : exp | 
           WHILE exp stms END '''
  pass
  
def p_stms_for1(p):
  '''stm : exp | 
           FOR ID IN exp DO stms END '''
  pass

def p_stms_for2(p):
  '''stm : exp | 
           FOR ID IN exp stms END'''
  pass

def p_stms_if1(p):
  '''stm : exp | 
           IF exp THEN stms END opcional'''
  pass

def p_smts_if2(p):
  '''stm : exp | 
           IF exp stms END opcional'''
  pass

def p_stms_if3(p):
  '''stm : exp | 
           IF LPAREN exp RPAREN THEN stms END opcional'''
  pass

def p_stms_if4(p):
  '''stm : exp |
           IF LPAREN exp RPAREN stms END opcional'''
  pass

def p_stms_return(p):
  '''stm : exp |
           return exp'''
  pass

def p_exp_soma(p):
  '''exp : exp PLUS exp'''
  pass

def p_exp_subtracao(p):
  '''exp : exp MINUS exp'''
  pass

def p_exp_multiplicacao(p):
  '''exp : exp TIMES exp'''
  pass

def p_exp_divisao(p):
  '''exp : exp DIVIDE exp'''
  pass

def p_exp_mod(p):
  '''exp : exp REST exp'''
  pass

def p_exp_doubleequal(p):
  '''exp : exp EQUAL exp'''
  pass

def p_exp_tripleequal(p):
  '''exp : exp TRIPLEEQUAL exp'''
  pass

def p_exp_diff(p):
  '''exp : exp DIFF exp'''
  pass

def p_exp_maiorque(p):
  '''exp : exp BIGGEST exp'''
  pass

def p_exp_maiorQueIgual(p):
  '''exp : exp BIGGESTEQUAL exp'''
  pass

def p_exp_menorque(p):
  '''exp : exp SMALL exp'''
  pass

def p_exp_menorqueIgual(p):
  '''exp : exp SMALLEQUAL exp'''
  pass

def p_exp_or(p):
  '''exp : exp OR exp'''
  pass

def p_exp_and(p):
  '''exp : exp AND exp'''
  pass

def p_exp_negative(p):
  '''exp : exp EXCLAMATION  exp'''
  pass

def p_exp_call(p):
  '''exp : call'''
  pass
  
def p_exp_assign(p):
  '''exp : assign'''
  pass

def p_exp_ID(p):
  '''exp : ID'''
  pass

def p_call_complete(p):
  '''call : ID LPAREN sigParams RPAREN'''
  pass

def p_call_without_param(p):
  '''call : ID LPAREN RPAREN'''
  pass

def p_call_only_id(p):
  '''call : ID'''
  pass

def p_call_only_id_param(p):
  '''call : ID sigParams'''
  pass

def p_sigparams(p):
  '''sigParams :  exp'''
  pass

def p_sigparams1(p):
  '''sigParams :  exp VIRGULA sigParams'''
  pass

def p_assign(p):
  '''assign : ID EQUAL exp'''
  pass