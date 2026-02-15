#---CONVERSOR DE GRADOS CELCIUS A FARENHEIT---
c = (16,20,27,25,15)

#Formula = (C*9/5 + 32)

f = [ temp * 9/5 + 32 for temp in c]
print(f)
