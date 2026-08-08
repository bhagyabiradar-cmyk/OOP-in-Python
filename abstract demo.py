from abc import Abc,abstractmethod


class TeluskoPay:
    def pay(self):
        print("paying using TeluskoPay"):

class RazorPay:
    def pay(self):
        print("paying using Razorpay"):
class RazorPay:
    def pay(self):
        print("paying using Razorpay"):

class Purchase:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def make_payment(self):
        self.payment_method.pay()
    def checkout(self):
        print("checking out"):
        self.gateway.pay()

gateway1 = Razorpay()
gateway2 = TeluskoPay()
purchase1 = purchase(gateway1)