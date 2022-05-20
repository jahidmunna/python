n = 17
binary = bin(n)[2:]
length = len(binary)
    
for i in range(1, n+1):
    # Decimal
    dec = i
    # Octal
    octa = oct(dec)[2:]
    #Hexadecimal (capitalized)
    hexa = hex(dec)[2:].upper()
    # Binary
    binary = bin(dec)[2:]
    
    print(f"{dec:>{length}} {octa:>{length}} {hexa:>{length}} {binary:>{length}}")



