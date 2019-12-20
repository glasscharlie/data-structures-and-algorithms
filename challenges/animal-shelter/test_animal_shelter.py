from animal_shelter import Animal, Cat, Dog, AnimalShelter

def test_create_cat():
    cat = Cat()
    assert type(cat) == Cat

def test_create_dog():
    dog = Dog()
    assert type(dog) == Dog

def test_create_shelter():
    shelter = AnimalShelter()
    assert type(shelter) == AnimalShelter

def test_add_one():
        shelter = AnimalShelter()
        shelter.enqueue(Cat())
        assert shelter.head.value == 'cat'

def test_add_two():
        shelter = AnimalShelter()
        shelter.enqueue(Cat())
        shelter.enqueue(Dog())
        assert shelter.head.next.value == 'dog'

def test_not_cat_or_dog():
    shelter = AnimalShelter()
    actual = shelter.enqueue(Cat())
    assert actual == None

def test_dequeue_first():
    shelter = AnimalShelter()
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    actual = shelter.dequeue('cat')
    assert actual == 'cat'

def test_dequeue_second():
    shelter = AnimalShelter()
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    actual = shelter.dequeue('dog')
    assert actual == 'dog'

def test_dequeue_no_pref():
    shelter = AnimalShelter()
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    actual = shelter.dequeue()
    assert actual == 'enter cat or dog'
