print("Variables and primitives")
students_count = 1000
rating = 4.99
is_published = False
course_name = "Javascript"
extras = """
multiples lines
miguel
angel
julio
"""
print(students_count, rating, is_published, course_name, extras)

print("Dynamic Typing - Python")

print(type(extras))

print("Python Primitive are inmutable")
print(id(extras))

extras = """
one - this is 1
two - this is 2
"""
print(id(extras))

print(len(extras), extras[0:3])

# strings and format
first = "miguel"
last = "julio"

print(f"{len(first)} {last}")
print(first.upper())

print(first.center(30, "-"))

x = input("enter your name: ")
print(f"Hello {x}")

# Falsy values:
# ""
# 0
# []
# None (null)

if not x.strip():
    print("we required your name")

age = input("enter your age: ")

# if age >= 18:
#     print('you are legal')
# elif age <= 18:
#     print("go home")
# else:
#     print("hello")

if 18 <= int(age) < 65:
    print(f"welcome {x}")

# ternary operator
message = input("enter message: ")
out = "we will pass along the message" if message != "" else "no message"

print(out)
