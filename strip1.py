def strips_with_steps(midtime, stop, count = 5):
    """Print test strip timings - with steps between strips"""
    strips = [(midtime*((2**stop)**curr_str))
            for curr_str in range(int(-((count + 1)/2)), int(((count + 1)/2)))]

    return [(strips[0], strips[0])] + \
            [(strips[i], strips[i] - strips[i-1]) for i in range(1, len(strips))]

i = 0
str_mt = float(30)
str_st = 1/3
str_cnt = 10
print ("Midtime: {:.1f}, stop interval: {:.1f}, count: {}".format(str_mt, str_st, str_cnt))
while i < 1000000:
    strips = strips_with_steps(str_mt, str_st, str_cnt)
    i += 1

print (strips)
print (str(i) + " iterations")
