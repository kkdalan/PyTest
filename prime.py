import sympy

a,b = 10,100
numbers = range(a,b)
prime_numbers = filter(sympy.isprime,numbers)

print "Prime numbers({}:{}): ".format(a,b)

for prime_number in prime_numbers:
    print prime_number, 
