is_even=int(input('Input numbers: '))
def test():
    if is_even % 2 == 0:
        return True
    else:
        return False
print(test())
def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(8) == True
    assert is_even(100) == True
    assert is_even(101) == False
print("YOUR CODE IS CORRECT!")
