import unittest

class Car(object):
    #Constructor
    def __init__(self, name = 'General', model = 'GM', body_type = 'saloon'):
        #Clean all imput
        inpt = [name, model, body_type]
        for i in inpt:
          if not type(i) is str:
            raise ValueError("Invalid input on Car Creation")
      
        self.name = name
        self.model = model
        self.body_type = body_type
        self.speed = 0

        self.num_of_doors = 4
        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2

        self.num_of_wheels = 4
        self.top_speed = 1000.0
        self.max_throttle = 3.0
        if self.body_type == 'trailer':
            self.num_of_wheels = 8
            self.top_speed = 77.0
            self.max_throttle = 7.0
        self.throttle_response = self.top_speed / self.max_throttle

    def is_saloon(self):
        if self.body_type == 'saloon':
            return True
        else:
            return False

    def drive(self, throttle):
        if type(throttle) is int:
            if throttle <= self.max_throttle and throttle > 0:
                self.speed = int(round(throttle * self.throttle_response))
            return self
        else:
            raise ValueError("Invalid input on drive")

class CarClassTest(unittest.TestCase):
    """docstring for CarClassTest"""

    def test_car_instance(self):
        honda = Car('Honda')
        self.assertIsInstance(honda, Car, msg='The object should be an instance of the `Car` class')

    def test_object_type(self):
        honda = Car('Honda')
        self.assertTrue((type(honda) is Car), msg='The object should be a type of `Car`')

    def test_default_car_name(self):
        gm = Car()
        self.assertEqual('General', gm.name,
                         msg='The car should be called `General` if no name was passed as an argument')

    def test_default_car_model(self):
        gm = Car()
        self.assertEqual('GM', gm.model, msg="The car's model should be called `GM` if no model was passed as an argument")

    def test_car_properties(self):
        toyota = Car('Toyota', 'Corolla')
        self.assertListEqual(['Toyota', 'Corolla'],
                             [toyota.name, toyota.model],
                             msg='The car name and model should be a property of the car')

    def test_car_doors(self):
        opel = Car('Opel', 'Omega 3')
        porshe = Car('Porshe', '911 Turbo')
        self.assertListEqual([opel.num_of_doors,
                             porshe.num_of_doors,
                             Car('Koenigsegg', 'Agera R').num_of_doors],
                             [4, 2, 2],
                             msg='The car shoud have four (4) doors except its a Porshe or Koenigsegg')

    def test_car_wheels(self):
        man = Car('MAN', 'Truck', 'trailer')
        koenigsegg = Car('Koenigsegg', 'Agera R')
        self.assertEqual([8, 4], [man.num_of_wheels, koenigsegg.num_of_wheels],
                         msg='The car shoud have four (4) wheels except its a type of trailer')

    def test_car_type(self):
        koenigsegg = Car('Koenigsegg', 'Agera R')
        self.assertTrue(koenigsegg.is_saloon(),
                        msg='The car type should be saloon if it is not a trailer')

    def test_car_speed(self):
        man = Car('MAN', 'Truck', 'trailer')
        parked_speed = man.speed
        moving_speed = man.drive(7).speed

        self.assertListEqual([parked_speed, moving_speed],
                             [0, 77],
                             msg='The Trailer should have speed 0 km/h until you put `the pedal to the metal`')

    def test_car_speed2(self):
        man = Car('Mercedes', 'SLR500')
        parked_speed = man.speed
        moving_speed = man.drive(3).speed

        self.assertListEqual([parked_speed, moving_speed],
                             [0, 1000],
                             msg='The Mercedes should have speed 0 km/h until you put `the pedal to the metal`')

    def test_drive_car(self):
        man = Car('MAN', 'Truck', 'trailer')
        moving_man = man.drive(7)
        moving_man_instance = isinstance(moving_man, Car)
        moving_man_type = type(moving_man) is Car
        self.assertListEqual([True, True, man.speed],
                             [moving_man_instance, moving_man_type, moving_man.speed],
                             msg='The car drive function should return the instance of the Car class')

if __name__ == "__main__":
  unittest.main()