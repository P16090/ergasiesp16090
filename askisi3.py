lista=[]
x=input("dwse lista: ")
lista=list(x)
pl=len(lista)
for i in range(0,pl):
 if lista[i]==0 or lista[i]=="0":
  del lista[i]
  lista.extend([0])
for i in range(-1,pl-1):
 if lista[i]==0 or lista[i]=="0":
  del lista[i]
  lista.extend([0])
print lista