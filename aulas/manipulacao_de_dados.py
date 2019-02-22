num_int = 5
num_dec = 7.3
cal_str = "o valor é: "


print("Concatenando inteiro: ", num_int)
print("Concatenando inteiro: %i" % num_int)
print("Concatenando inteiro: " + str(num_int))

print("Concatenando decimal: ", num_dec)
print("Concatenando decimal: %.2f" % num_dec)
print("Concatenando decimal: " + str(num_dec))

print("Concatenando strings", cal_str)

print("Concatenando strings %s" % cal_str, num_int)
print("Concatenando strings " + cal_str)

