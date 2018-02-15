# My very first Python program!

print ("Hola Mundo!")

# Print a test strip timings

midtime = int(input("Gimme yo time! "))
stop = float(input("Gimme yo stop-range! "))

for strip in range(-3, 3):
    print(midtime*((2**stop)**strip))
