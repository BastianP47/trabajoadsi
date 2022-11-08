from os import strerror

cunts = {chr(ch):0 for ch in range(ord('a'), ord('z')+1)}
archivos = input(str("Digite el nombre del archivo: "))

try:
    f = open(archivos, "r")
    for file in f:
        for dat in file:
            if dat.isalpha():
                cunts[dat.lower()]+=1
    f.close()
    for ch in cunts.keys():
        cant = cunts[ch]
        if cant > 99:
            print (dat, '-->', cant)
            
except IOError as e:
    print("Error no existe el archivo", strerror(e.errno))
