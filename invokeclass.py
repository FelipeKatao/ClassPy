
class Invoke():
    def __init__(self) -> None:
        self.Type = {"Get":"get","Invoke":"invoke","Set":"set"}
        pass

    def Invoke(self,ClassObj,Parans={"Dict":0},Type="get",ClassSet="get"):  
        if(Type == "class"):
            a = ClassObj()
            if(ClassSet == "get" or ClassSet == "set"):
                v_set =self.__VarsSet(a,Parans,ClassSet)
                if(ClassSet == "get"):
                    return v_set 
                return a
            if(ClassSet == "invoke"):
                if(Parans[1] == None):    
                    return self.__CallbackMethosd(a,Parans[0])
                return self.__CallbackMethosd(a,Parans[0],Parans[1])
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
        return Method_call(*args[0],**kwargs[0])
        