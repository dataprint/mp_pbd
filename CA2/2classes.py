#define a class for a car
#private instance variables of a class begin with two unerscores characters
#(__colour) cannot be directly accessed
class Car(object):
    
    #private instance variables are initialized in a special method naems __init__
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        #publick atribute
        self.wheels = 4
        
    #we return an atribute
    def get_colour(self):
       return self.__colour
   
    def get_make(self):
        return self.__make
    
    def get_mileage (self):
        return self.__mileage
    
    #we set an atribute
    def set_colour(self, colour):
        self.__colour = colour
        
    def set_make(self, make):
        self.__make = make
    
    def set_mileage(self, mileage):
        self.__mileage = mileage
    
    #creare publick function to change colour    
    def spray(self, new_colour):
        print ('Car sprayed from' + self.__colour + 'to ' + new_colour)
        self.__colour = new_colour
        
    def move(self,distance):
        print ('Moved ' + str(distance) + 'kms.')
        self.__mileage = self.__mileage + distance
        
    def paint (self, colour):
        print ('Getting a paint job ~ new colour is: ' + colour)
        self.__colour = colour


            
#create instance

johns_car = Car()
print johns_car.wheels
#update atribute
johns_car.wheels = 2
print johns_car.wheels

pauls_car = Car()
print pauls_car.wheels

#call a funtion not an attribute, bring nothing because no collor
print johns_car.get_colour() 
#assigne color trought the function
johns_car.spray('red')
#if atribute not publick we need to create function
print johns_car.get_colour()


johns_car.set_make('BMW')
johns_car.set_mileage(3000)

print(johns_car.get_make())
print(johns_car.get_mileage())

#we move a car 15km
johns_car.move(15)
#everytime we move it increases mileage
print (johns_car.get_mileage())
