from icecream import ic

from src.sample import my_sum
def test_sum1():
    assert(78==ic(my_sum(3,5, 20)))

def test_sum2():
    assert(63==ic(my_sum(3,0, 20)))

def test_sum3():
    assert(30==ic(my_sum(0,5, 20)))

def test_sum4():
    assert(78==ic(my_sum(target=20)))

def test_sum5():
    assert(0==ic(my_sum(0,0, 1)))