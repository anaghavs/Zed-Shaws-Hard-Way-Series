def add(a, b):
        print(f"ADDING {a} + {b}")
        return  a+b
def sub(a,b):
        print(f"SUBTRACTING {a} -{b}")
        return a-b

def mul(a,b):
        print(f"MULTIPLYING {a} *{b}")
        return a*b

def div(a,b):
        print(f"DIVIDING {a} /{b}")
        return a/b

print("Lets do some math with just functions!")
    
age=add(30,5)
height = sub(78,4)
weight = mul(90,2)
iq = div(100, 2)

print(f"Age: {age}, Height:{height},Weight: {weight},IQ: {iq}")
#a puzzle for extra credit
print("Here is a puxxle")

what =add(age, sub(height, mul(weight, div(iq, 2))))

print("that becomes:",what, "can you do it by hand?")
print(24+34/100-1023)