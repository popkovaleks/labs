from functools import reduce


class Car:

    def __init__(self, object):
        self.brand_name = object.get('brand')
        self.model_name = object.get('model')
        self.e_volume = object.get('e_volume')
        self.transmission = object.get('transmission')

    def test(self):
        print(self.__repr__())
        print(self.__str__())


class SUV(Car):
    body = 'SUV'
    def show_info(self):
        print('Brand name ' + self.brand_name + ', model ' + self.model_name + ', engine volume ' + self.e_volume + ', transmission ' + self.transmission + ', body ' + self.body)
        self.test()

class Coupe(Car):
    body = 'coupe'
    def show_info(self):
        print('Brand name ' + self.brand_name + ', model ' + self.model_name + ', engine volume ' + self.e_volume + ', transmission ' + self.transmission + ', body ' + self.body)
        self.test()


class Sedan(Car):
    body = 'sedan'
    def show_info(self):
        print('Brand name ' + self.brand_name + ', model ' + self.model_name + ', engine volume ' + self.e_volume + ', transmission ' + self.transmission + ', body ' + self.body)
        self.test()

class Hatchback(Car):
    body = 'hatchback'
    def show_info(self):
        print('Brand name ' + self.brand_name + ', model ' + self.model_name + ', engine volume ' + self.e_volume + ', transmission ' + self.transmission + ', body ' + self.body)
        self.test()



def main():


    sedan_objects = [
    {'brand':'Mazda','model':'3','e_volume':'2,0','transmission':'AT'},
    {'brand':'Volkswagen','model':'Polo','e_volume':'1,6','transmission':'MT'},
    {'brand':'Toyota','model':'Corolla','e_volume':'1,6','transmission':'MT'},
    ]

    hatchback_objects = [
    {'brand':'Volvo','model':'V40','e_volume':'2,0','transmission':'MT'},
    ]

    suv_objects = [
    {'brand':'Mazda','model':'CX-5','e_volume':'2,0','transmission':'AT'}
    ]

    coupe_objects = [
    {'brand':'Citroen','model':'C4','e_volume':'1,6','transmission':'AT'}
    ]


    sedan = [(Sedan(sedan_objects[i])) for i in range(len(sedan_objects))]
    hatchback = [(Hatchback(hatchback_objects[i])) for i in range(len(hatchback_objects))]
    suv = list(map(SUV, suv_objects))
    coupe = list(map(Coupe, coupe_objects))


    counts_objects = [len(sedan_objects), len(hatchback_objects), len(suv_objects), len(coupe_objects)]
    sum_objects = reduce(lambda a, b: a + b, counts_objects)
    print(sum_objects)


    
    suv[0].show_info()


if __name__ == '__main__':
    main()
