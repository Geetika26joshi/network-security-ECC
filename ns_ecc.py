a=int(input("enter a"))
b=int(input("enter b"))
p=int(input("enter p"))
pb = (197,167) #public key
m = (112,26) #original plaintext message
g = (2,2)
nb=101
def controller():
   y=int(input("enter y"))
   x=int(input("enter x"))
   print(x,y)
   print("is it valid point",isPoint(y,x))
   #print(res)
   print("All points: ", allPoints())
   pax, pay = mult(g,nb) 
   print("pubic key Pa:",(pax,pay))
   cipher = encrypt(m)
   print("Cipher: ",cipher)
   plaintext = decrypt(cipher)
   print("decrypted plaintext is : ",plaintext)


def isPoint(y,x):
   y=y*y
   #ym=y%p
   am=a*x
   x=x*x*x
   
   xm=(x+am+b)
   
   if( y== xm ):
    return True
   else:
      return False
      
def allPoints():
    lst = []
    for x in range(p):
        for y in range(p):
             if isPoint(x,y): lst.append((x,y))
    return lst
def mult(point, d):
     P = point
     if d == 0: return 0 # computation complete
     elif d == 1:return P[0],P[1]
     elif d % 2 == 1:
        x,y = mult(P, d - 1)
        return addPoints(P[0],P[1],x,y) # addition when d is odd
     else:
        return mult(addPoints(P[0],P[1],P[0],P[1]), d/2)

def addPoints(x1,y1,x2,y2):
    if x1 == x2 and y1 == y2:
        dell = ((3*pow(x1,2))*modInverse(2*y1)) % p
        xp  = x1
        x1 = (dell**2 - 2*x1) % p
        y1 = (dell*(xp-x1) - y1) % p

    else:
        dell  = ((y2-y1)*modInverse(x2-x1)) % p
        xp  = x1
        x1 = (dell**2 - x1 - x2) % p
        y1 = (dell*(xp-x1) - y1) % p
    
    return x1,y1

def modInverse(x) : 
    x = x % p; 
    for y in range(1, p) : 
        if ((x * y) % p == 1) : 
            return y 
    return 1
  



def encrypt(m):
    k = 41 
    c1x,c1y = mult(g,k)
    j,k = mult(pb,k)
    c2x,c2y = addPoints(m[0],m[1],j,k)
    cipher = [(c1x,c1y),(c2x,c2y)]
    return cipher

def decrypt(cipher):
    nb = 101 
    x,y = mult(cipher[0], nb)
    y = -y
    m = addPoints(cipher[1][0],cipher[1][1],x,y)
    return m


controller()