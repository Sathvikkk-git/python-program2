w=int(input("enter you weigth:"))
h=float(input("enter your height:"))
b=w/(h**2)
if b<18.5:
  print("underweight")
elif b<25:
  print("normal")
elif b<30:
  print("overweight")  
else:
  print("obesity")    
