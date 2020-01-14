class Car:

    def __init__(self, object):
        self.brand_name = object.get('brand')
        self.model_name = object.get('model')
        self.e_volume = object.get('e_volume')
        self.transmission = object.get('transmission')
        self.body = object.get('body')

    def show_info(self):
        print(self.brand_name + ' ' + self.model_name + ' Engine volume: ' + self.e_volume + ' Transmission: ' + self.transmission + ' Body type: ' + self.body)

    def show_by_brand(self, brand):
        if self.brand_name == brand:
            print(self.brand_name + ' ' + self.model_name + ' Engine volume: ' + self.e_volume + ' Transmission: ' + self.transmission + ' Body type: ' + self.body)

    def show_by_tr(self, tr):
        if self.transmission == tr:
            print(self.brand_name + ' ' + self.model_name + ' Engine volume: ' + self.e_volume + ' Transmission: ' + self.transmission + ' Body type: ' + self.body)



objects = [
{'brand':'Mazda','model':'3','e_volume':'2,0','transmission':'AT', 'body':'sedan'},
{'brand':'Volvo','model':'V40','e_volume':'2,0','transmission':'MT', 'body':'hatchback'},
{'brand':'Volkswagen','model':'Polo','e_volume':'1,6','transmission':'MT', 'body':'sedan'},
{'brand':'Toyota','model':'Corolla','e_volume':'1,6','transmission':'MT', 'body':'sedan'},
{'brand':'Citroen','model':'C4','e_volume':'1,6','transmission':'AT', 'body':'coupe'}
]

car = []
for i in range(len(objects)):
    car.append(Car(objects[i]))
    car[i].show_info()

print("Please, enter the brand you want to see on your screen:")
brand = input()

for i in range(len(objects)):
    car[i].show_by_brand(brand)

print("Please, enter the type of transmission, you want to see on yor screen(AT or MT only):")
tr = input()

for i in range(len(objects)):
    car[i].show_by_tr(tr)
