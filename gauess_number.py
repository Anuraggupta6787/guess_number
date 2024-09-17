import random
wining_number=random.randint(1,100)
count=1
num=int(input("Enter the Number between 1 to 100 = "))
game_over=False
while not game_over:
 if wining_number==num:
   print(f"you win , and you find this number in {count} times !!")
   game_over=True
 else:
  if num>wining_number:
      print("too high!")
     
  if num<wining_number:
      print("too low!")    
  count+=1
  num=int(input("Enter again = "))
