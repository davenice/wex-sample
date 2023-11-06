import evenorodd

def test_even():
    assert(evenorodd.even_or_odd(2) == "even")

def test_odd():
    assert(evenorodd.even_or_odd(71) == "odd")

def test_even_large_number():
    assert(evenorodd.even_or_odd(246) == "even")

def test_zero():
    assert(evenorodd.even_or_odd(0) == "even")
