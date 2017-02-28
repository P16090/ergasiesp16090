lista=[]
x=(raw_input("dwse: "))
lista=list(x)
def synarthsh(lista):
    anoikse = 0
    kleise = 0
    change_shifts = False
    while len(lista) > 0:
     poped_item = lista.pop()
     if poped_item  == ')' and not change_shifts:
       kleise += 1
     elif poped_item  == ')' and change_shifts:
       return False
     elif poped_item  == '(':
       change_shifts = True
       anoikse += 1
 
    return anoikse == kleise
print(synarthsh(lista))
   