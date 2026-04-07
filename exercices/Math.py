result = 2 + 3 * 4 ** 2 - 8 // 3 - 6
print("result 1: " + str(result)) #42

x = 5
result = not x > 3 and x != 4 or x == 5
print("result 2: " + str(result)) # True, because x > 3 is True, so not x > 3 is False, and x != 4 is True, so False and True is False, but x == 5 is True, so False or True is True