
class ClassFlag():
    def __init__(self,className) -> None:
        self.OBJECTKEY = [className.__class__,dir(className)]
        self.OBJECTNAME = "0"
        self.CLASSNAME = className
        self.Parcials_class = []
        self.object_value_key = ""
        self.Flag = ""
        self.Implement_error =  None