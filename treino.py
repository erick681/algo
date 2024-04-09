import sys
import pdb

def ola(nome, c=1):
    print("Olá\n", nome)
    pdb.set_trace()
    if c == 3:
        sys.exit()
    c += 1
    ola(nome, c)
    tchau(nome)

def tchau(nome):
    print(f"Tchau {nome}")

ola("Maria")
