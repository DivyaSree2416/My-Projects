#24-5-25
'''
place=input()
if place=='campus':
    place=input()
    if place=='block':
        place=input()
        if place=='floor':
            place=input()
            if place=='class':
                print("Talented person")
            else:
                print("corridar")
        else:
            print("Library")
    else:
        print("canteen")
else:
    print("cinema ki vellaru")
'''
'''
def secretcode(s):
    uc=lc=ss=sp=di=0
    for i in s:
        if i.isupper():
            uc+=1
        elif i.islower():
            lc+=1
        elif i.isdigit():
            di+=1
        elif i.isspace():
            sp+=1
        else:
            ss+=1
    if(len(s)>=8 and s[0].isupper() and uc>=2 and lc>=2 and sp==0 and di>0 and ss>0):
        print("Valid Secret Code")
    else:
        print("Not a valid secret code")
    print(f"Capitals-{uc}")
    print(f"Small-{lc}")
    print(f"Numbers-{di}")
    print("Special - %d"%ss)
    print("Space -{}".format(sp))
string=input()
secretcode(string)
'''
'''
li=[]
for i in range(5):
    li.append(i)
print(li)
'''
'''
li=[1,2,3,4,5,6]
for i in li:
    li.remove(i)
print(li)
'''
'''
d={}
for i in range(5):
    a=input()
    b=int(input())
    d[a]=b
print(d)
'''
''''
names=['divi','priya','joo']
d={}
for i in names:
    d[i]=len(i)
print(d)
print(max(d.values()))
print({name : len(name) for name in names})
print({name:éven_length'' if len(name)%2==0 else ödd_lengt
'''
''''
print({k:k*k for k in range(10,16)})
'''
name=input()
d={i:name.count(i) for i in name}
print(d)

            
        
