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

#     """method to reset the x and y position"""
#     def reset(self):
#         self.x = 0
#         self.y = 0


# """creating an object"""
# p = Point()
# p.reset()
# print(p.x, p.y)

#####

## Talking to yourself
# """creating a class"""
# class Point:

#     """method to reset the x and y position"""
#     def reset(self):
#         self.x = 0
#         self.y = 0


# """creating an object"""
# p = Point()
# """attaching the reset method to the 'p' object using the 'Point' class"""
# Point.reset(p)
# print(p.x, p.y)

# """what happens if we forget to inlcude the self argument?"""

# class Point:

#     """method to reset the x and y position"""
#     def reset():
#         x = 0
#         y = 0


# """creating an object"""
# p = Point()
# """attaching the reset method to the 'p' object using the 'Point' class"""
# p.reset()
# print(p.x, p.y)

#####

## More arguments

# """importing math module"""
# import math

# """creating class"""
# class Point:

#     """move method"""
#     def move(self, x: float, y: float) -> None:
#         self.x = x
#         self.y = y

#     """reset method"""
#     def reset(self) -> None:
#         self.move(0, 0)

#     """calculateDistance method"""
#     def calculateDistance(self, other: "Point") -> float:
#         return math.hypot(self.x - other.x, self.y - other.y)
    

# """creating objects"""
# p1 = Point()
# p2 = Point()

# """attaching methods to the objects"""
# p1.reset()
# p2.move(5, 0)
# print(p2.calculateDistance(p1))

#####

## Initializing the object
# """importing math module"""
# import math

# """creating a class"""
# class Point:

#     """creating initialzing method"""
#     def __init__(self, x: float, y: float) -> None:
#         self.move(x, y)

#     """creating move method"""
#     def move(self, x: float, y:float) -> None:
#         self.x = x
#         self.y = y

#     """creating reset method"""
#     def reset(self) -> None:
#         self.move(0, 0)

#     """creating calculateDistance method"""
#     def calculateDistance(self, other: "Point") -> float:
#         return math.hypot(self.x - other.x, self.y - other.y)
    

# """constructing a point instance"""
# p = Point(3, 5)
# print(p.x, p.y)