def getPrime(x, y):  # Function to find the prime between two numbers (found on the internet but done initially by myself, just was much longer lol)
    while y: x, y = y, x % y
    return abs(x)

def getCoeff(a, b):  # Function for the Advanced Euclidean Algorithm
    aOrig = a
    bOrig = b
    
    if b > a:
        b = aOrig
        a = bOrig
    
    c = 0
    d = 69
    aList = []
    bList = []
    cList = []
    dList = []
    
    while d > 1:
        aList.append(a)
        bList.append(b)
        
        d = a % b
        c = int(a / b)
        
        cList.append(c)
        dList.append(d)
        
        print(f"{a} = {b}({c}) + {d}")
        
        a = b
        b = d
        
    print(f"A List: {aList}\nB List: {bList}\nC List: {cList}\nD List: {dList}")
    
p = 26513  # The two numbers that will be used (taken from Cryptohack, Modular Arithmetic, in which I am using to learn cryptography)
q = 32321

gcd = getPrime(p, q)
print(f"Prime number: {gcd}") # 1

getCoeff(p, q) # Currently the Standard Euclidean Algorithm
