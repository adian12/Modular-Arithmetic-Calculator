

def mod(g,exponent, p):
    return pow(g,exponent,p)

def main():
    g = int(input("Enter the base g? g^e (mod P) "))
    e = int(input("Enter exponent e? g^e (mod p) "))
    p = int(input("Enter the modulus p: g^e (mod p) "))

    print(mod(g,e,p))
    



if __name__ == "__main__":
    main()

