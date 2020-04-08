from math import sqrt 

value = 10
print(f'The value is {value}')

d = dict(tom='22',sam='50')

for k,v in d.items():
    print("Key={} Value={}",k,v)

#Collection comprehension
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x))+1):
        if x%i == 0:
            return False
    return True

l = [x for x in range(101) if is_prime(x)] 
print(l)