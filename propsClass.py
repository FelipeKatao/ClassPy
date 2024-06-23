from .functionsClassPy import FunctionsClass
import warnings
import types

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
        self.ClassUsed = None
        pass

    def GetProp(self,Prop,varatt = None):

        if(varatt != None and repr(Prop)+varatt in self.PropKeys ):
            return self.PropKeys[repr(Prop)+varatt]  
        warnings.warn("Non-existent object variable", UserWarning)
    
    def SetProp(self,PropName,SetProps=None,varAtt=None,dynamic=False):
       
        if("class" in str(type(PropName))):
                    if str(PropName)+varAtt in self.PropKeys:
                        if(type(self.Invoke(PropName,[varAtt,SetProps],"get")) == type(SetProps)):
                            self.Invoke(PropName,[varAtt,SetProps],"set")
                            self.PropKeys[str(PropName)+varAtt] = SetProps
                            return str(PropName)+varAtt
                        else:
                           type_validd =type(self.Invoke(PropName,[varAtt,SetProps],"get"))
                           raise  RuntimeError(f"The type defined for this variable is not supported, the expected type is: '{type_validd}' ") 

        # Created new prop
        if("class" in str(type(PropName))):
            #self.ClassUsed = PropName
            #setattr(PropName, '__setattr__', self.__instanceProp)
            if("Nothing value or variable reach in the class Map." == self.Invoke(PropName,[varAtt,SetProps],"get")):
                setattr(PropName,varAtt,SetProps)
                setattr(self,varAtt,SetProps)
            self.PropKeys[str(PropName)+varAtt] = SetProps
            return str(PropName)+varAtt
        self.PropKeys[PropName] = SetProps
        return self.PropKeys[PropName]

    def CreateTypeValues(self,obj):
        self.ClassUsed = obj
        setattr(obj,'__setattr__', self.__instanceProp)
            

    def ModelView(self,ClassModel,NewModel):
        Atributes = vars(ClassModel)
        Atributes = {key: value for key, value in Atributes.items() if '__' not in key}
        Atributes = {key: value for key, value in Atributes.items() if ' object at' not in key}
        Class_name = str(self.__class__).replace("<class","").replace(">","").replace("'","").replace(" ","")
        att_adds={}
        for a in Atributes.items():
            ab,ac ="<"+Class_name,str(a[1])
            if (ab in ac) == False:
                att_adds[a[0]] = a[1]
        for i in att_adds.items():
            self.SetProp(NewModel,i[1],i[0])
            self.SetProp(self,i[1],i[0])



    def __instanceProp(self,name,value):
        expected_type = self.Invoke(self, [name,None], "get")
        if not isinstance(value, type(expected_type)):
            raise ValueError(f"Value being assigned is of the incorrect type, the expected type is: {type(expected_type)}")
        self.__ModifyValue(self.ClassUsed,name,value)
        self.__setattr__(name, value)
        setattr(self.ClassUsed,name,value)


    def __ModifyValue(self,object,name,value):
        setattr(object,name,value)

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


                   