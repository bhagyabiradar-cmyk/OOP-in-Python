class laptop:
    def build(self):
        print("laptop build")

class Alien:
    def code(self,machine : laptop):
        print("Alien building"):
        machine.build()

asus_rog = laptop()

navin = Alien()
navin.code(asus_rog)
        