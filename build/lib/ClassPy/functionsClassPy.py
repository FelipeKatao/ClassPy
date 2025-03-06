from inspect import signature
from ClassPy.invokeclass import Invoke

class FunctionsClass(Invoke):
    def __init__(self) -> None:
        super().__init__()
        
    def CreateOverloadMethod(self,function):
        FuncName =  function.__name__
        try:
            #append to list
            self.METHOD_LIST[FuncName].append(function)
        except:
            #Create new Key to FuncName Function
            self.METHOD_LIST.update({FuncName:[function]})

    def CallOverloadFunction(self,function,Params,ClassSelf):
        Function_Overload =  self.METHOD_LIST[function.__name__]
        CountElems = len(Params)
        for i in Function_Overload:
            sing = str(signature(i))
            sing =sing.replace("(","").replace(")","")
            sing = sing.split(",")
            sing.pop(0)
            if(CountElems == len(sing)):
                self.Function_call = i
                break
        Sig_function = str(signature(self.Function_call))
        Sig_function = Sig_function.replace("(","").replace(")","")
        Sig_function = Sig_function.split(",")
        Sig_function.remove("self")
        Index = 0
        P ={}
        while(Index< len(Sig_function)):
            Param = Sig_function[Index]
            Param_value = Params[Index]
            P.update({Param:Param_value})
            Index+=1
        #Assembl = str(P).replace("{",'').replace("}",'').replace(":","=")
        #print(Assembl)
        if(CountElems == 0):
            self.Function_call(ClassSelf)
        if(CountElems == 1):
            self.Function_call(ClassSelf,Params[0])
        if(CountElems == 2):
            self.Function_call(ClassSelf,Params[0],Params[1])
        if(CountElems == 3):
            self.Function_call(ClassSelf,Params[0],Params[1],Params[2])
        if(CountElems == 4):
            self.Function_call(ClassSelf,Params[0],Params[1],Params[2],Params[3])
        if(CountElems == 5):
            self.Function_call(ClassSelf,Params[0],Params[1],Params[2],Params[3],Params[4])
        if(CountElems == 6):
            self.Function_call(ClassSelf,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5])
        if(CountElems == 7):
            self.Function_call(ClassSelf,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6])
        if(CountElems == 8):
            self.Function_call(ClassSelf,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7])
        if(CountElems == 9):
            self.Function_call(ClassSelf,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8])
        if(CountElems == 10):
            self.Function_call(ClassSelf,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],Params[9])
        
    def TransportOverload(self,ClassPy):
        ClassPy.METHOD_LIST = self.METHOD_LIST

