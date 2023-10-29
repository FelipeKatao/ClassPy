from .functionsClassPy import FunctionsClass

class GenericType():
    GenericProp_val = ""
    def __init__(self) -> None:
        self.hee= ""
        pass

    @property
    def GenericValue(self):
        return self.TGENRETUVALU
    
    @GenericValue.setter
    def GenericValue(self,value):
        if(self.TGENVALUE == "Type"):
            self.TGENRETUVALU = value
            self.TGENVALUE = type(value)
        else:
            if(type(value) == self.TGENVALUE):
                self.TGENRETUVALU = value
            else:
                raise TypeError("Value type incompatible with the generic type created Type: "+str(self.TGENVALUE))

    
class PropsClass(FunctionsClass,GenericType):
    def __init__(self,propName = None) -> None:
        super().__init__()
        self.PropKeys = {}
        self.__a = "ola"
        pass

    def GetProp(self,Prop):
        return self.PropKeys[Prop]    
    
    def SetProp(self,PropName,SetProps=None):
        self.PropKeys[PropName] = SetProps
        return self.PropKeys[PropName]


    def Prop(self,PropName,*Props,**DefaultValues):
        
        if(DefaultValues!={}):
            varbase_ = DefaultValues['DefaultValues']
            varbase_ = DefaultValues['DefaultValues']
            self.PropKeys = {PropName:varbase_[0]}
        else:
            self.PropKeys = {PropName:0}

            
        if(len(Props)!=0):
           VarBases = 0
           index_base = 1
           try:    
              VarBases = DefaultValues['DefaultValues']
           except:
               VarBases = 0
            
           for i in Props:
               if(VarBases!=0):
                   if(index_base<len(VarBases)):
                        self.PropKeys.update({i:VarBases[index_base]})
               else:
                   self.PropKeys.update({i:0})
               index_base+=1
        print(self.PropKeys)


                   
