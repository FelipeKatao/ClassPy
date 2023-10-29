from .propsClass import PropsClass,GenericType
class ClassFlag(PropsClass):
    def __init__(self,className) -> None:
        super().__init__(className)
        self.OBJECTKEY = [className.__class__,dir(className)]
        self.OBJECTNAME = "0"
        self.CLASSNAME = className
        self.Parcials_class = []
        self.object_value_key = ""
        self.Flag = ""
        self.Implement_error =  None
        self.METHOD_LIST = {}
        self.Function_call = None
        self.TGENVALUE = "Type"
        self.TGENRETUVALU = None
        self.Object_base_generic = 0