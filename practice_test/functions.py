import random

def max_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
            print(f"Current min {minimum}")
    return minimum# when you try to print smth and forget return it will  display none
#return is inside the for loop thus statement is not executed once.program exits when it hits a return statement
def get_values():
    list = random.sample(range(50, 100), 10)

    print("Generated list:", list)
    

    result = max_min(list)
    print("Final minimum:", result)

get_values()