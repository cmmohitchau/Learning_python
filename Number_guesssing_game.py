import random

num = random.random()

print(f"Random float [0.0, 1.0): {num}")

intNum = random.randint(1 , 10)

print(f"Random float [1, 10): {intNum}")

rand_uniform = random.uniform(5 , 15)

print(f"Random float [5 , 15): {rand_uniform}" , end=" ")

items = ['apple', 'banana', 'cherry']

rand_choice = random.choice(items)

print(rand_choice)

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")

random.seed(42)
print(f"Random number with seed 42: {random.randint(1, 100)}")