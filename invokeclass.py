
class Invoke():
    def __init__(self) -> None:
        self.Type = {"Get":"get","Invoke":"invoke","Set":"set"}
        pass

    def Invoke(self,ClassObj,Parans={"Dict":0},Type="get"):
        Variables =vars(ClassObj)
        return Variables[Parans]
        