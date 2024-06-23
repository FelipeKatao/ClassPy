
class Invoke():
    def __init__(self) -> None:
        self.Type = {"Get":"get","Invoke":"invoke","Set":"set"}
        pass

    def GetclassType(self,ClassObject,CompareObj=None):
        Type_class = str(type(ClassObject))
        Type_class = Type_class.replace("class ","").replace("<","").replace(">","").replace("__main__.","")
        if(CompareObj!=None):
            Type_compare = str(type(CompareObj))
            Type_compare = Type_compare.replace("class ","").replace("<","").replace(">","").replace("__main__.","")
            return Type_compare == Type_class
        return Type_class
    
    def Invoke(self,ClassObj,Parans={"Dict":0},Type="get",ClassSet="get"):  
        if(Type == "class"):
            a = ClassObj()
            if(ClassSet == "get" or ClassSet == "set"):
                v_set =self.__VarsSet(a,Parans,ClassSet)
                del a
                if(ClassSet == "get"):
                    return v_set 
                return a
            if(ClassSet == "invoke"):
                if(Parans[1] == None):    
                    InovkeReturn = self.__CallbackMethosd(a,Parans[0])
                    del a
                    return InovkeReturn
                InvokeReturn_a =  self.__CallbackMethosd(a,Parans[0],Parans[1])
                del a
                return InvokeReturn_a
        else:
            return self.__VarsSet(ClassObj,Parans,Type)

        
    
    def __VarsSet(self,ClassObj,Parans,Type):
        # Workflow for set vars      
        Variables =vars(ClassObj)
        Value = Variables.setdefault(Parans[0],None)
        if(Value !=None and Type == "get"):
            return Value
        elif(Value !=None and Type == "set"):
            return setattr(ClassObj,Parans[0],Parans[1])
        return "Nothing value or variable reach in the class Map."
    
    def __CallbackMethosd(self,Obj,Method,*args,**kwargs):
        Method_call = getattr(Obj,Method)
        if(len(args) == 0):
            return Method_call()
        if(len(args) == 1):
            return Method_call(args[0],**kwargs)    
        return Method_call(*args[0],**kwargs)
        