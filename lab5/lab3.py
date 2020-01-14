class Car:

    def __init__(self, object):
        self.brand_name = object.get('brand')
        self.model_name = object.get('model')
        self.e_volume = object.get('e_volume')
        self.transmission = object.get('transmission')
        self.body = object.get('body')

    def test(self):
        print(self.__repr__())
        print(self.__str__())

class SUV(Car):
    type = 'SUV'





def main():
    objects = [
    {'brand':'Mazda','model':'3','e_volume':'2,0','transmission':'AT', 'body':'sedan'},
    {'brand':'Volvo','model':'V40','e_volume':'2,0','transmission':'MT', 'body':'hatchback'},
    {'brand':'Volkswagen','model':'Polo','e_volume':'1,6','transmission':'MT', 'body':'sedan'},
    {'brand':'Toyota','model':'Corolla','e_volume':'1,6','transmission':'MT', 'body':'sedan'},
    {'brand':'Citroen','model':'C4','e_volume':'1,6','transmission':'AT', 'body':'coupe'}
    ]

    suv_objects = [
    {'brand':'Mazda','model':'3','e_volume':'2,0','transmission':'AT', 'body':'sedan'}
    ]

    car = []
    for i in range(len(objects)):
        car.append(Car(objects[i]))

    suv = []
    for i in range(len(suv_objects)):
        suv.append(SUV(suv_objects[i]))

    car[1].test()
    suv[0].test()
if __name__ == '__main__':
    main()
