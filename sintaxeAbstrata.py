from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

#Declaracao de funcao

class Funcao(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class FuncaoConcrete(Funcao):
  def __init__(self, signature, body): 
    self.signature = signature
    self.body = body
  def accept(self, visitor):
    return visitor.visitFuncaoConcrete(self)

#Declaração de Assinatura

class Assign(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class AssignConcrete(Assign):
    def __init__(self, name, sigParams):
        self.name = name
        self.sigParams = sigParams
    def accept(self, visitor):
        return visitor.visitAssignConcrete(self)


#Parâmetros de assinatura de funcao

class Sigparams(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class SigparamsSingleConcrete(Sigparams):
  def __init__(self, var):
    self.var = var
  def accept(self, visitor):
    return visitor.visitSigparamsSingleConcrete(self)


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
    return visitor.visitstmsSingleConcrete(self)
    
class stmsMultiCocnrete(Stms):
  def __init__(self,stm,stms):
    self.stm = stm
    self.stms = stms
    pass
  def accept(self,visitor):
    return visitor.visitstmsMultiConcrete(self)
    
class Stm(metaclass=ABCMeta):
  @abstractmethod
  def accept(self,visitor):
    pass

class stmConcrete(Stm):
  def __init__(self, exp):
    self.exp = exp
  def accept(self,visitor):
    return visitor.visitstmConcrete(self)
    
class While(metaclass=ABCMeta):
  @abstractmethod
  def accept(self,visitor):
    pass
    
class stmswhileConcrete(While):
    def __init__(self, exp, body):  
        self.exp = exp
        self.body = body
    def accept(self, visitor):
        return visitor.visitstmswhileConcrete(self)
      
class For(metaclass=ABCMeta):
  @abstractmethod
  def accept(self,visitor):
    pass
    
class stmsForConcrete(For):
    def __init__(self, nameobj,namelist, body):  
        self.nameobj = nameobj
        self.namelist = namelist
        self.body = body
    def accept(self, visitor):
        return visitor.visitstmsForConcrete(self)
      
class If(metaclass=ABCMeta):
  @abstractmethod
  def accept(self,visitor):
    pass
    
class stmsIfConcrete(If):
    def __init__(self, exp, s1, s2):  
        self.exp = exp
        self.s1 = s1
        self.s2 = s2 
    def accept(self, visitor):
        return visitor.visitstmsIfConcrete(self)
    
class StmsReturn(Stms):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmsReturn(self)

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

#comandos de chamada

class Call(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass
    
# comando assign
class Assign(metaclass = ABCMeta):
  @abstractmethod
  def accept(self,visitor):
    pass
class AssignConcrete(Assign):
  def __init__(self, ID, exp):
    self.ID = ID
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitAssignConcrete(self)