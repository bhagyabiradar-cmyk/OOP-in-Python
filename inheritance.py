class A:
    def f1(self):
        print("f1 works")

        def f2(self):
            print("f2 works")
class B(A):
    def f3(self):
        print("f3 works")

        def f4(self):
            print("f4 works")
class C(B):
    def f5(self):
            print("f5 works")
    

obj1 = A()
obj1.f1()    