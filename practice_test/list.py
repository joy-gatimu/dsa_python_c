import random



values=random.sample(range(10),5)
print(values)
print(values[2:])
print(f"stop at index 3{list[:3]}")# it will stop at index 3
values.append(5)
values.append(9)
values.append(2)
values.append(6)

print(values)
values_a=values[-1]#get last index
print(values_a)