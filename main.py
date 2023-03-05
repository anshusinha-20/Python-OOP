## Type checking
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

# """function to return a bool value, i.e, to check whether the 'n' is even or odd"""
# def even(n: int) -> bool:
#     return n % 2 == 0

# def main():
#     print(even("Hello world!"))

# if __name__ == "__main__":
#     main()

#####

## Creating python classes
# """creating a class name 'MyFristClass' """
# class MyFirstClass:
#     pass


# a = MyFirstClass()
# b = MyFirstClass()
# print(a)
# print(b)
# print(a is b)

#####

## Adding attributes
# """creating a class named 'Point' """
# class Point:
#     pass

# """creating two objects"""
# p1 = Point()
# p2 = Point()

# """adding attributes to the objects"""
# p1.x = 5
# p1.y = 4

# p2.x = 3
# p2.y = 6

# print(p1.x, p1.y)
# print(p2.x, p2.y)

#####

## Making it do something
# """creating a class"""
# class Point:

#     """function definition to reset the x and y position"""
#     def reset(self):
#         self.x = 0
#         self.y = 0


# """creating an object"""
# p = Point()
# p.reset()
# print(p.x, p.y)