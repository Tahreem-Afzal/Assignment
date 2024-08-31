print('----Lets Explore the Numbers----')
name=input('Enter your name: ')
num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))
num3=int(input('Enter third number: '))
l = [num1, num2, num3]
print(f"Hello, {name}! Let's explore your favorite numbers:")
for i in l:
    if i%2==0:
        print(f'The number {i} is an even number')
    else:
        print(f'The number {i} is an odd number')
for i in l:
    print(f'The number {i} and its square: {i},{i*i}')
s=0
for i in l:
    s+=i
print(f'Amazing! The sum of your favorite numbers is: {s}')
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(s):
    print(f"The sum {s} is a prime number.")
else:
    print(f"The sum {s} is not a prime number.")