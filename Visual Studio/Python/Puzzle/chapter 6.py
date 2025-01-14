#It will print hello then break
for x in range(0, 20):

             print('hello %s' % x)

             if x < 9:

                 break


x = 0
while x < 16:
        x = x + 2
        print(x)


ingredients = ['Mushroom', 'Tomato', 'Lettuce','Turkey', 'Cheese']
for i in ingredients:
        print(i)

        
earth_weight = 16.5
moon_weight = 0.165
for weight in range(0,16):
    total = weight * earth_weight * moon_weight
    print('%s = %s' % (weight, total))
