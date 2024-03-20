def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else :
        for i in range(len(string)):
            l = string[i]
            f = string[:i]
            b = string[i+1:]
            t = f+b
            permute(t,l+pocket)
print(permute('abc',''))
