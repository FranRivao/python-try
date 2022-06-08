# class Menu:
#     def __init__(self):
#         self.list = {
#             'coca': 10,
#             'agua': 12,
#             'salchicha': 15
#         }

#     def removeItem(self, item):
#         self.list += item

#     def addItem(self, item, price):
#         self.list.append(item, price)


class Factura: 
    def __init__(self):
        self.total = 0
        self.objects = []
        self.menu = Menu()

    def add(self, object):
        self.objects.append(object)
        self.total += self.menu.list[object]

    def remove(self, object):
        self.objects.pop()
        self.total -= self.menu.list[object]

    def print(self, tax, service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total
        total = self.total + tax + service

        print("Factura:")
        for object in self.objects:
            print(f'{object.capitalize()}: ${self.menu.list[object]}')

        print(f'{"Total:"} ${total}')