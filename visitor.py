from abstractor_visitor import *

class Visitor(AbstractVisitor):
  def visitProgramConcreteFuncao(self, Program):
    Program.funcao.accept(self)
  
  def visitProgramConcreteFuncaoProgram(self, Program):
    Program.funcao.accept(self)
    Program.program.accept(self)
  
  def visitProgramConcreteAssign(self, Program):
    Program.assign.accept(self)
    Program.program.accept(self)
  
  def visitProgramConcreteAssign1(self, Program):
    Program.assign.accept(self)

  def visitFuncaoConcrete(self, Funcao):
    Funcao.ID.accept(self)
    Funcao.sigParams.accept(self)
    Funcao.body.accept(self)
  
  def visitiFuncaoConcrete1(self, Funcao):
    Funcao.ID.accept(self)
    Funcao.body.accept(self)

  def visitAssignConcrete(self, Assign):
    print(Assign.ID, end = ' ')
    Assign.exp.accept(self)
  
  def visitAssignConcrete1(self, Assign):
    print(Assign.assign, end = ' ')

  def visitSigparamsSingleConcrete(self, Sigparams):
    print(Sigparams.exp)
  
  def visitSigparamsSingleConcrete1(self, Sigparams):
    print(Sigparams.exp)
    print(Sigparams.sigParams)

  def visitBodyConcrete(self, Body):
    Body.stms.accept(self)
    print()
    print("end")

  def visitStmsSingleConcrete(self, Stms):
    Stms.stm.accept(self)

  def visitStmsMultiConcrete(self, Stms):
    Stms.stm.accept(self)
    Stms.stms.accept(self)

  def visitStmConcrete(self, Stm):
    Stm.exp.accept(self)

  def visitStmsWhileConcrete(self, While):
    While.exp.accept(self)
    print()
    print("while")
  
  def visitStmsWhileConcrete1(self, While):
    While.exp.accept(self)
    While.body.accept(self)
    print()
    print("while")

  def visitStmsForConcrete(self, For):
    print(For.ID, end = ' ')
    print(For.exp, end = ' ')
    For.body.accept(self)
    print()
    print("for")

  def visitStmsIfConcrete(self, If):
    If.exp.accept(self)
    If.body.accept(self)
    if If.opcional != None:
      If.opcional.accept(self)
  
  def visitStmsIfConcrete1(self, If):
    If.exp.accept(self)
    If.body.accept(self)
  
  def visitOpcionalConcrete(self, Opcional):
    Opcional.Elsif.accept(self)
    Opcional.exp.accept(self)
    Opcional.body.accept(self)
  
  def visitOpcionalConcrete1(self, Opcional):
    Opcional.Elsif.accept(self)
  
  def visitOpcionalConcrete2(self, Opcional):
    Opcional.Elsif.accept(self)
    Opcional.exp.accept(self)
    Opcional.body.accept(self)
    Opcional.opcional.accept(self)

  def visitStmsReturnConcrete(self, Return):
    Return.exp.accept(self)

  def visitExpAllConcrete(self, Exp):
    Exp.exp1.accept(self)
    Exp.exp2.accept(self)

  def visitCallConcrete(self, Call):
    print(Call.sigParams, end = ' ')
    print(Call.ID, end = ' ')

  def visitCallConcreteOnlyId(self, Call):
    print(Call.ID, end = ' ')