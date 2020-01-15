from lab4 import *
from threading import *

import random
import time

def show(object):
    object.show_info()

def waiting():
    wait = random.randint(2,10)
    time.sleep(wait)

def create_sedan():
    waiting()
    sedan = Sedan({'brand':'Toyota','model':'Corolla','e_volume':'1,6','transmission':'MT'})
    show(sedan)

def create_hatchback():
    waiting()
    hatchback = Hatchback({'brand':'Volvo','model':'V40','e_volume':'2,0','transmission':'MT'})
    show(hatchback)

def create_SUV():
    waiting()
    suv = SUV({'brand':'Mazda','model':'CX-5','e_volume':'2,0','transmission':'AT'})
    show(suv)

def create_coupe():
    waiting()
    coupe = Coupe({'brand':'Citroen','model':'C4','e_volume':'1,6','transmission':'AT'})
    show(coupe)




def threads():
    tsedan = Thread(target = create_sedan)
    thatchback = Thread(target = create_hatchback)
    tsuv = Thread(target = create_SUV)
    tcoupe = Thread(target = create_coupe)

    tsedan.start()
    thatchback.start()
    tsuv.start()
    tcoupe.start()

    tsedan.join()
    thatchback.join()
    tsuv.join()
    tcoupe.join()

def main():

    threads()

if __name__ == '__main__':
    main()
