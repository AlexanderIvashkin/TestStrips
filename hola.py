# My very first Python program!

def strips(midtime, stop):
    """Print test strip timings"""
    teststrips = []
    currentstrip = 0
    for strip in range(-3, 3):
        currentstrip = midtime*((2**stop)**strip))
        print(currentstrip)
        teststrips.append(currentstrip)
    return teststrips

print ("Hola Mundo!")
print (strips.__doc__)
mt = int(input("Gimme yo time! "))
st = float(input("Gimme yo stop-range! "))

strips(mt, st)
print("And now for something totally similar: " + strips(mt, st))
