
# for loops
extras = "abc"
for i in extras:
    print(i)

for n in range(3):
    print(n)

names = ["Miguel", "Norman", "ley", "Nidhi", "Tom", "Mario"]

for name in names:
    if name.startswith("x"):
        print("found")
        break
else:  # this executes after fo loop breaks
    print("not found")

# while loops
guess = 0
answer = 7

while answer != guess:
    guess = int(input("Guess: "))
else:
    print(f"good {guess}")


def inc(number, by):
    return number + by


print(inc(5, 5))

# list of arguments -> topples


def multiply(*args):
    total = 1
    for number in args:
        total *= number
    return total


print(multiply(2, 5, 6, 2))

# key values -> dictionary


def save_user(**user):
    print(user)


print(save_user(id=1, name="miguel", role="admin"))


def fizz_buzz(input):
    if (input % 3 == 0) and input % 5 == 0:
        return "fizzbuzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"
    return input


print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(4))
print(fizz_buzz(6))
