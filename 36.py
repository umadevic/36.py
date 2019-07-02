y=input()
f=0
for i in range(len(y)):
 if(y[i].isdigit() or y[i].isalpha() or y[i]==(" "))
  continue
 else:
  f+=1
 print(f)
