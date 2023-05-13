from abc import abstractmethod
from abc import ABCMeta
from visitor import *

class Program(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass
    
class ProgramConcreteFuncao(Program):
  def __init__(self, funcao):
    self.funcao = funcao
  def accept(self, visitor):
    return visitor.visitProgramConcreteFuncao(self)

class ProgramConcreteFuncaoProgram(Program):
  def __init__(self, funcao, program):
    self.funcao = funcao
    self.program = program
  def accept(self, visitor):
    return visitor.visitProgramConcreteFuncaoProgram(self)

class ProgramConcreteAssign(Program):
  def __init__(self, assign, program):
    self.assign = assign
    self.program = program
  def accept(self, visitor):
    return visitor.visitProgramConcreteAssign(self)

class ProgramConcreteAssign1(Program):
  def __init__(self, assign):
    self.assign = assign
  def accept(self, visitor):
    return visitor.visitProgramConcreteAssign1(self)
#Declaracao de funcao

class Funcao(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class FuncaoConcrete(Funcao):
  def __init__(self, ID, sigParams, body): 
    self.ID = ID
    self.sigParams = sigParams
    self.body = body
  def accept(self, visitor):
    return visitor.visitFuncaoConcrete(self)

class FuncaoConcrete1(Funcao):
  def __init__(self, ID, body):
    self.ID = ID
    self.body = body
  def accept(self, visitor):
    return visitor.visitFuncaoConcrete1(self)

#Declaração de Assinatura

class Assign(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class AssignConcrete(Assign):
    def __init__(self, ID, exp):
        self.ID = ID
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitAssignConcrete(self)

class AssignConcrete1(Assign):
    def __init__(self, assign):
        self.assign = assign 
    def accept(self, visitor):
        return visitor.visitAssignConcrete1(self)


#Parâmetros de assinatura de funcao

class Sigparams(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class SigparamsSingleConcrete(Sigparams):
  def __init__(self, exp):
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitSigparamsSingleConcrete(self)

class SigparamsSingleConcrete1(Sigparams):
  def __init__(self, exp, sigParams):
    self.exp = exp
    self.sigParams = sigParams
  def accept(self, visitor):
    return visitor.visitSigparamsSingleConcrete1(self)

#chamada de funcao
class Call(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class CallConcrete(Call):
  def __init__(self, sigParams, ID):
    self.sigParams = sigParams
    self.ID = ID
  def accept(self, visitor):
    return visitor.visitCallConcrete(self)

class CallConcreteOnlyId(Assign):
    def __init__(self, ID):
        self.ID = ID 
    def accept(self, visitor):
        return visitor.visitCallConcreteOnlyId(self)

#Corpo de uma função

class Body(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class BodyConcrete(Body):
  def __init__(self, stms):
    self.stms = stms
  def accept(self, visitor):
    return visitor.visitBodyConcrete(self)


#Comando Statement

class Stms(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class stmsSingleConcrete(Stms):
  def __init__(self,stm):
    self.stm = stm
    pass
  def accept(self,visitor):
    return visitor.visitStmsSingleConcrete(self)
    
class stmsMultiConcrete(Stms):
  def __init__(self,stm,stms):
    self.stm = stm
    self.stms = stms
    pass
  def accept(self,visitor):
    return visitor.visitStmsMultiConcrete(self)
    
class Stm(metaclass=ABCMeta):
  @abstractmethod
  def accept(self,visitor):
    pass

class stmConcrete(Stm):
  def __init__(self, exp):
    self.exp = exp
  def accept(self,visitor):
    return visitor.visitStmConcrete(self)
    
class While(metaclass=ABCMeta):
  @abstractmethod
  def accept(self,visitor):
    pass
    
class stmsWhileConcrete(While):
    def __init__(self, exp):  
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmsWhileConcrete(self)

class stmsWhileConcrete1(While):
    def __init__(self, exp, body):  
        self.exp = exp
        self.body= body
    def accept(self, visitor):
        return visitor.visitStmsWhileConcrete1(self)
      
class For(metaclass=ABCMeta):
  @abstractmethod
  def accept(self,visitor):
    pass
    
class stmsForConcrete(For):
    def __init__(self, ID ,exp, body):  
        self.ID = ID
        self.exp = exp
        self.body = body
    def accept(self, visitor):
        return visitor.visitStmsForConcrete(self)
      
class If(metaclass=ABCMeta):
  @abstractmethod
  def accept(self,visitor):
    pass
    
class stmsIfConcrete(If):
    def __init__(self, exp, body, opcional):  
        self.exp = exp
        self.body = body
        self.opcional = opcional 
    def accept(self, visitor):
        return visitor.visitStmsIfConcrete(self)

class stmsIfConcrete1(If):
    def __init__(self, exp, body):  
        self.exp = exp
        self.body = body 
    def accept(self, visitor):
        return visitor.visitStmsIfConcrete1(self)

      
# Opcional, a regra que deriva pra else ou elsif
class Opcional (metaclass=ABCMeta):
  @abstractmethod
  def accept (self, visitor):
    pass

class OpcionalConcrete (Opcional):
  def __init__(self, exp, body,Elsif):
    self.Elsif = Elsif
    self.exp = exp
    self.body = body
  def accept (self, visitor):
    return visitor.visitOpcionalConcrete(self)

class OpcionalConcrete1(Opcional):
  def __init__(self, Else):
    self.Else = Else
  def accept (self, visitor):
    return visitor.visitOpcionalConcrete1(self)

class OpcionalConcrete2 (Opcional):
  def __init__(self,Elsif, exp, body,opcional):
    self.Elsif = Elsif
    self.exp = exp
    self.body = body
    self.opcional = opcional
  def accept (self, visitor):
    return visitor.visitOpcionalConcrete2(self)
#-------------------------------------------------------------------------------
class Return(metaclass=ABCMeta):
  @abstractmethod
  def accept (self,visitor):
    pass
    
class ReturnConcrete(Stms):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmsReturnConcrete(self)

#Comandos de expressão

class Exp(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ExpPlusConcrete(Exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitExpPlusConcrete(self)

class ExpMinusConcrete(Exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitExpMinusConcrete(self)
                                                                
class ExpTimesConcrete(Exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitExpTimesConcrete(self)

class ExpDivideConcrete(Exp):
  def __init__(self, exp1, exp2):                                                     
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitExpDivideConcrete(self)

class ExpModConcrete(Exp):
  def __init__(self, exp1, exp2):                                                     
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitExpModConcrete(self)

class ExpExponenConcrete(Exp):
  def __init__(self, exp1, exp2):                                                     
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitExpDivideConcrete(self)

class ExpDoubleEqualConcrete(Exp):
  def __init__(self, exp1, exp2):                                                     
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitExpDoubleEqualConcrete(self)

class ExpTripleEqualConcrete(Exp):
  def __init__(self, exp1, exp2):                                                     
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitExpTripleEqualConcrete(self)

class ExpDiffConcrete(Exp):
  def __init__(self, exp1, exp2):                                                     
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitDiffConcrete(self)

class ExpMaiorQueConcrete(Exp):
  def __init__(self, exp1, exp2):                                                     
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitMaiorQueConcrete(self)

class ExpMaiorQueIgualConcrete(Exp):
  def __init__(self, exp1, exp2):                                                     
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitMaiorQueIgualConcrete(self)

class ExpMenorQueConcrete(Exp):
  def __init__(self, exp1, exp2):                                                     
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitMenorQueConcrete(self)

class ExpMenorQueIgualConcrete(Exp):
  def __init__(self, exp1, exp2):                                                     
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitMenorQueIgualConcrete(self)

class ExpOr(Exp):
  def __init__(self, exp1, exp2):                                                     
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitExpOr(self)

class ExpAnd(Exp):
  def __init__(self, exp1, exp2):                                                     
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitExpAnd(self)

class ExpNum(Exp):
  def __init__(self, exp1):
    self.exp1 = exp1
  def accept(self, visitor):
    return visitor.visitExpNum(self)

class Expcall(Exp):
  def __init__(self, call):
    self.call = call
  def accept(self,visitor):
    return visitor.visitExpcall(self)

class ExpAssign(Exp):
  def __init__(self, ID, sigparams):
    self.ID = ID
    self.sigparams = sigparams
  def accept(self, visitor):
    return visitor.visitExpAssign(self)