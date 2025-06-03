class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    @property
    def amount(self):
        return self.__amount

    @property
    def currency(self):
        return self.__currency

    def __add__(self, other):
        if self.__currency != other.currency:
            raise RuntimeError("Mismatched currencies!")
        return Money(self.__amount + other.amount, self.__currency)
    
    def __sub__(self, other):
        if self.__currency != other.currency:
            raise RuntimeError("Mismatched currencies!")
        return Money(self.__amount - other.amount, self.__currency)
    
    def __mul__(self, number):
        return Money(self.__amount * number, self.__currency)