

class PropsClass():
    def __init__(self,propName = None) -> None:
        self.PropKeys = {}
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
                   
