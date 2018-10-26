import pdb
import math

def isPrime(check):
    if check == 2:
        return True
    for i in range(2, int(math.sqrt(check))):
        if check % i == 0:
            return False
    return True


#divide first by 2, then by 3, then by 4, etc.

divisor = 2
num = 600851475143

while divisor < num:
    if num%divisor == 0:
        print(num, "/", divisor, "= ", num/divisor)
        if isPrime(int(num/divisor)):
            print(num/divisor)
            break
    divisor += 1

input("press enter to quit")
