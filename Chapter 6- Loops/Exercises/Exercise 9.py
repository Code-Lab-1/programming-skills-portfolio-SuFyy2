#Find the total price of the ticket for 5 people of any age
prompt="Under 3yr ticket is free\nEnter your age "
total=0
i=0
while i<5:
  age= int(input(prompt))
  i = i+1
  if age<3:
    continue
  total +=100
print(total)