from .flagsClass import ClassFlag
from .functionsClassPy import FunctionsClass
from .propsFunction import PropsFunctions

class Classpy(ClassFlag):
    def __init__(self,className) -> None:
        """Creating class protection, in className pass the name of the 
        class that is being used in the current context.
        ----------
        `className : class`
         Class that should be used in-context
        -------
        Create your class with a ClassPy property contained within it::

         class TestClass():
         def __init__(self):
         class_py = ClassPy(TestClass)
        """

        super().__init__(className)
  
  
    def Private(self):
        """
        Method to make your function private, use it at the beginning of your function

        -------
        To apply this method, call it in the initial body of your method::

         Clss_Py.Private():
         
        """ 
        if(self.OBJECTKEY != self.OBJECTNAME ):
            raise RuntimeError("The private function can't be called ")
        else:
            self.OBJECTKEY = 0 
            return self.OBJECTKEY

    def PassMethod(self,ObjectClass):
        """Checks if your method can be called, if it's inside 
        the class that created it, it grants access.
        ----------
        `ObjectClass : class`
         Class that should be used in-context
        -------
        To use it, put this method at the beginning of the function you want to check the method pass, if it is 
        the same class it allows access to the private function::

         class A():
         def method_private():
         ...
         def acess_private():
         class_py.PassMethod(A)
         ...
        """
        self.OBJECTNAME = []
        self.OBJECTNAME = [self.CLASSNAME.__class__,dir(ObjectClass)]
        return self.OBJECTNAME

    def MergeParcialClass(self,*ParcialClass):
        """Merge your partial classes with the same 
        name or not, being able to pass as many classes as you want.
        ----------
        `*ParcialClass : class`
         pass any number of classes within this parameter
        -------
        To use, create the object of your class and then join them together::

         from a import A as A
         from aclone import A as A2
         obj_a = A2()
         obj_b = A()
         MergeParcialClass(self,Obj_a,Obj_b)
         ...
        """
        Vector_parcials_class = []
        for i in ParcialClass:
            Vector_parcials_class.append(i)
        self.Parcials_class = Vector_parcials_class
        return Vector_parcials_class
    
    def MergeParcialWithCall(self,Indice,*ParcialClass):
        """Creates the vector of partial classes 
        and allows them to be called in this same method
        ----------
        `Index : Number`
         Position of the index you want to access

         `*ParcialClass : class`
         pass any number of classes within this parameter
        -------
        To use, create the object of your class and then join them together::

         from a import A as A
         from aclone import A as A2
         obj_a = A2()
         obj_b = A()
         MergeParcialWithCall(1,Obj_a,Obj_b).func()
         ...
         Replace func with the function of the class you're 
         trying to access
        """
        Vector_parcials_class = []
        Dirs_Merge = []
        for i in ParcialClass:
            Vector_parcials_class.append(i)
        self.Parcials_class = Vector_parcials_class
        for q in Vector_parcials_class:
            Dirs_Merge.append(dir(q))
        return self.Parcials_class[Indice]
    
    def CallParcialClass(self,Index,ParcialClasses=None):
        """Call the function you want with a vector 
        of partials created with the MergePartialClass function.
        ----------
        `Index : Number`
         Position of the index you want to access

         `ParcialClasses : None or Vector Class`
         Accesses the class vector created, if it is None 
         it returns the Index created by Classpy itself
        -------
        Call only when you get the vector of classes already built::

         CallParcialClass(1,MergeParcial
         Class(self,a2,a)).func()
         ...
         Replace func with the function of the class you're 
         trying to access
        """
        if(ParcialClasses == None):
            return self.Parcials_class[Index]
        return ParcialClasses[Index]
    

    def Interface(self,*Interfaces):
        """Creates an association between the chosen 
        class and between one or more interfaces.
        ----------
        `*Interfaces : Class and Interface`
         The first element returns your class (or self) and the second element
         your interface implementation, you can use one or more 
         interfaces after the first parameter that is your class.

        -------
        You can create an interface binding within your class::

            class Iainterface():
            class A():
            def __init__(self):
            self.classPy.Interface(self,
            Iainterface)
            ...
        """
        value = self.__Interface_implement(*Interfaces)
        if(value != 0):
            raise ReferenceError(f"  :the function {self.Implement_error} has not been implemented from the Source Interface, implement the method in the class")


    def __Interface_implement(self,*Interfaces):
        """Private method for Interface Methods.
        ----------
        `*interfaces`
         Return Interfaces and classes association
        """
        Interfaces_Vector = []
        CallFunctions = []
        for i in Interfaces:
            Interfaces_Vector.append(i)
        def ValidateInterfaceClass(Interfaces):
            index = 0
            Based_funcs = []
            while(index<len(Interfaces)):
                for i in dir(Interfaces[index]):
                    value = str(i)
                    if(value.__contains__("__") == False):
                        Based_funcs.append(value)
                CallFunctions.append(Based_funcs)
                index+=1
                Based_funcs =[]
 
            Implement_error = ""
            Count_error = 0
            try:
                index_value = 1
                Validation_element = False
                while(len(CallFunctions)>index_value):
                    for d in CallFunctions[index_value]:
                        for d_in in CallFunctions[0]:
                            Implement_error = d
                            self.Implement_error = d
                            if(d_in == d):
                                Validation_element = True 
                        if(Validation_element == False):
                            Count_error+=1
                            raise RuntimeError(f"  :the function {Implement_error} has not been implemented from the Source Interface, implement the method in the class")
                        Validation_element = False
                    index_value+=1
            except Exception as w:
                 return "execpt"+str(w)
            return Count_error
        return ValidateInterfaceClass(Interfaces_Vector)