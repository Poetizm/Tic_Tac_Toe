class Person:
    pass

n = 3

obj = Person()

for i in range(1,n+1):
    setattr(obj,f'attribute{i}', f'value{i}')

print(obj.__dict__)



