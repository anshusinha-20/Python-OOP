## type checking
# """checking the type"""
# print(type("Hello world!"))
# print(type(123))

# """checking the id"""
# aString = "hello"
# print(id(aString))
# aString = 123
# print(id(aString))

# """a function definition"""
# def even(n):
#     return n % 2 == 0

# print(even(2))
# print(even(3))
# print(even("I like python!"))

# """type hints"""
# def odd(n: int) -> bool:
#     return n % 2 != 0

"""function to return a bool value, i.e, to check whether the 'n' is even or odd"""
def even(n: int) -> bool:
    return n % 2 == 0

def main():
    print(even("Hello world!"))

if __name__ == "__main__":
    main()
