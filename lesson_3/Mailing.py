class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track





#тип данных `Address` в контексте указания поля класса `Mailing` представляет из себя ссылку на экземпляр класса `Address`. 
#В твоём коде это будет означать, что поля `to_address` и `from_address` класса `Mailing` должны быть объектами, 
#созданными из класса `Address`. Так ты сможешь использовать атрибуты и методы класса `Address` в качестве атрибутов класса `Mailing`.