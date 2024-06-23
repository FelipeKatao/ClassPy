from .functionsClassPy import FunctionsClass
import warnings

class GenericType():
    GenericProp_val = ""
    def __init__(self) -> None:
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
            
    def AddElementGenericList(self,element):
        if(type(self.GenericValue[0]) == type(element)):
            self.GenericValue.append(element)
        else:
          raise TypeError("Value type incompatible with the generic type created Type: "+str(type(self.GenericValue[0])))  

    
class PropsClass(FunctionsClass,GenericType):
    def __init__(self,propName = None) -> None:
        super().__init__()
        self.PropKeys = {}
        self.__a = "ola"
        pass

    def GetProp(self,Prop,varatt = None):

        if(varatt != None and repr(Prop)+varatt in self.PropKeys ):
            return self.PropKeys[repr(Prop)+varatt]  
        warnings.warn("Non-existent object variable", UserWarning)
    
    def SetProp(self,PropName,SetProps=None,varAtt=None,dynamic=False):
       
        if("class" in str(type(PropName))):
                    if str(PropName)+varAtt in self.PropKeys:
                        if(self.Invoke(PropName,[varAtt,SetProps],"get") == None):
                           print("aqui é nulo")
                        if(type(self.Invoke(PropName,[varAtt,SetProps],"get")) == type(SetProps)):
                            self.Invoke(PropName,[varAtt,SetProps],"set")
                            self.PropKeys[str(PropName)+varAtt] = SetProps
                            return str(PropName)+varAtt
                        else:
                           type_validd =type(self.Invoke(PropName,[varAtt,SetProps],"get"))
                           raise  RuntimeError(f"The type defined for this variable is not supported, the expected type is: '{type_validd}' ") 

        # Created new prop
        if("class" in str(type(PropName))):
            if("Nothing value or variable reach in the class Map." == self.Invoke(PropName,[varAtt,SetProps],"get")):
                setattr(PropName,varAtt,SetProps)
            self.PropKeys[str(PropName)+varAtt] = SetProps
            return str(PropName)+varAtt
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


                   
