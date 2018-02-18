# My very first Python program!

def strips(midtime, stop):
    """Print test strip timings"""
    teststrips = []
    currentstrip = 0
    for strip in range(-3, 3):
        currentstrip = midtime*((2**stop)**strip)
        # print(currentstrip)
        teststrips.append(currentstrip)
    return teststrips

print ("Hola Mundo!")
print (strips.__doc__)
mt = float(input("Gimme yo time! "))
st = float(input("Gimme yo stop-range! "))

# strips(mt, st)
# print("And now for something totally similar: ")
for s in strips(mt, st):
    # print("Current strip: " + str(s))
    print("Current strip: {}".format(s))

def strips_listcomp(midtime, stop):
    """Print test strip timings - listcomp version"""
    return [midtime*((2**stop)**str) for str in range(-3,3)]

print (strips_listcomp(mt, st))

def strips_with_steps(midtime, stop):
    """Print test strip timings - with steps between strips"""
    return [midtime*((2**stop)**str) for str in range(-3,3)]

