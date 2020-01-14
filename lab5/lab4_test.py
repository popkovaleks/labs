import unittest
from lab4 import *

class Test(unittest.TestCase):

    def test_suv_show_info(self):
        suv = SUV({'brand':'Mazda','model':'CX-5','e_volume':'2,0','transmission':'AT'})
        self.assertEqual(suv.info(), "Brand name Mazda, model CX-5, engine volume 2,0, transmission AT, body SUV" )

    def test_objects(self):
        coupe = Coupe({'brand':'Citroen','model':'C4','e_volume':'1,6','transmission':'AT'})
        hatchback = Hatchback({'brand':'Volvo','model':'V40','e_volume':'2,0','transmission':'MT'})
        self.assertIsNot(coupe, hatchback)


if __name__ == '__main__':
    unittest.main()
