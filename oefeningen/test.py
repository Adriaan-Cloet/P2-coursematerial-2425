class A:
    def show(self):
        print("A.show()")


class B(A):
    def show(self):
        print("B.show()")
        super().show()


class C(B):
    def show(self):
        super().show()
        print("C.show()")


obj = C()
obj.show()
