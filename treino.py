import sys
def ola(nome):
    print("ola\n ",nome)
    c = 1
    c += 1 
    if c >= 3 :
        sys.exit()
    ola(nome)
    tchau()
def tchau():
    return f"tchau {nome}"
ola("maria")
