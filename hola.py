# My very first Python program!

def strips(midtime, stop):
    """Print test strip timings"""
    for strip in range(-3, 3):
        print(midtime*((2**stop)**strip))

print ("Hola Mundo!")
print (strips.__doc__)
mt = int(input("Gimme yo time! "))
st = float(input("Gimme yo stop-range! "))

strips(mt, st)
