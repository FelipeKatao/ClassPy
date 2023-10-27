
class Classpy:
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
        self.OBJECTKEY = [className.__class__,dir(className)]
        self.OBJECTNAME = "0"
        self.CLASSNAME = className
        self.Parcials_class = []
  
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