import sys

s = sys.argv[2]
s1 = sys.argv[3]
k=s.split('=')
k1=s1.split('=')
print(k)
print(k[1])
print('-----------')
print(k1)
print(k1[1])

def uret(str):
    a="127.0.0.1"
    b=0
    s = sys.argv[2]
    s1 = sys.argv[3]
    a = s.split('=')[1]
    b = s1.split('=')[1]
    return a, b

x,y=uret(sys.argv)



