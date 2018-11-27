sales = float(input("Enter sales: $"))
while sales >= 0:
 if sales < 1000:
  bouns = 0.1 * sales
  print(bouns)
 else:
  bouns = 0.15 * sales
  print(bouns)
 sales = float(input("Enter sales: $"))

