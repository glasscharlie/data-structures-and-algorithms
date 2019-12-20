
class Animal:
    def __init__(self, value = None):
        self.value = None
        if value != 'cat' and value != 'dog':
            raise TypeError("must be a cat or dog")
        # self.next = None

class Dog(Animal):
  def __init__(self):
    super().__init__('dog')
    self.value = 'dog'
    self.next = None

class Cat(Animal):
  def __init__(self):
    super().__init__('cat')
    self.value = 'cat'
    self.next = None

class AnimalShelter:

  def __init__(self):  
    self.head = None
  
  def enqueue(self, Animal):
    new_animal = Animal
    # try:
    if self.head == None:
         self.head = new_animal
         return 

    #Values exist in queue
    current = self.head

        #Traverse the list
    while current:
        if current.next == None:
            current.next = new_animal
            return
        
            current = current.next
    # except ValueError as e:
    #     print('invalid animal')

  def dequeue(self, pref=None):
    current = self.head
    previous = self.head


    if pref is None:
        return 'enter cat or dog'

    while current:
        if current.value == pref:

            self.head = current.next
            current.next = None

            return current.value

        previous = current
        current = current.next    

    # return "pref_dequeue Error: Please enter 'cat' or 'dog'. "



shelter = AnimalShelter()
shelter.enqueue(Cat())
shelter.enqueue(Cat())
print(shelter.dequeue('cat'))

