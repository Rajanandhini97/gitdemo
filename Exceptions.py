
ItemsInCart = 0

# 2 items will be added to the cart

if ItemsInCart != 2:
   # raise Exception('Products cart count not matching')
    pass

assert(ItemsInCart == 0)

#try, catch

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except:
    print('exception block is executed as try block failed')
# printing type of error thrown in try block through exception
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print('cleaning up resources')