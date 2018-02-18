def strips_with_steps(midtime, stop, count = 5):
    """Print test strip timings - with steps between strips"""
    return [( (midtime*((2**stop)**curr_str)), (midtime*((2**stop)**curr_str)) )
            for curr_str in range(int(-((count + 1)/2)), int(((count + 1)/2)))]

i = 0
while i < 1000000:
    strips = strips_with_steps(30, 1/3, 10)
    i += 1

print (strips)
print (str(i) + " iterations")
