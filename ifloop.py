greeting = "Good Morning"
a = 45
if a < 50:
    print("Condition matches")
    print("Second line")
else:
    print("Condition does not match")
print("if condition code is completed")

#for loop

obj = [3, 4, 5 ,6 ,7]
for i in obj:
    print(i*2)

#sum of first five natural numbers

summation = 0
for j in range(1,6):
    summation = summation + j
print("{} {}". format('The summation of first five natural numbers is',summation))
print('*********SKIPPING INDEX************************')

for k in range(1,10,2):
    print(k)
print("*********NO STARTING INDEX JUST MAX RANGE************************")

for m in range(10):
    print(m)