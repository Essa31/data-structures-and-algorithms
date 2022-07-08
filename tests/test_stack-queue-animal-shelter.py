import pytest
from stack_and_queue.stack_queue_animal_shelter import *



Animal=AnimalShelter()




def test_enqueue():


    actual= Animal.enqueue(Dog("log"))
    expected="dog"
    assert actual == expected



def test_enqueue2():

    actual=Animal.enqueue(Cat("log"))
    expected="cat"
    assert actual == expected

def test_not_animal_dequeue():
    assert Animal.dequeue("mouse") == None


def test_dequeue():
    Animal.enqueue(Cat("log"))
    Animal.enqueue(Dog("lona"))
    assert Animal.dequeue("dog") == "dog"




def test_dequeue2():
    Animal.enqueue(Cat("log"))
    Animal.enqueue(Dog("lona"))
    assert Animal.dequeue("cat") == "cat"