##ANimal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

##Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ##dog has-a name
        self.name = name
    ##cat is-a Animal
    class Cat(Animal):

        def __init__(self, name):
            ##dog has-a name
            self.name = name

##person is-a object
class Person(object):

    def __init__(self, name):
        ##person has-a name
        self.name = name

        ##Person has-a pet
        self.pet = None

#employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
      #employee has-a salary
        self.salary = salary


#fish is-a object
class Fish(object):
    pass

#salmon is-a fish
class Salmon(Fish):
    pass

#halibut is-a Fish
class Halibut(Fish):
    pass

#rover is-a Dog
rover = Dog("Rover")

#santa is-a Cat
santa = Cat("Santa")

#mary is-a person
mary = person("Mary")

#mary has-a pet
mary.pet = santa

#frank is-a Employee
frank = Employee("Frank", 120000)

#frank has-a pet
frank.pet = rover

#flipper is-a Fish
flipper = Fish()

#crouse is-a Salmon
crouse = Salmon()

#harry is-a Halibut
harry=Halibut()
