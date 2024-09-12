for i in range(2,10):
    for j in range(1,10):
            print(i*j, end=" ")
    print('')


result = [num * 3 for num in a]

result = []
for num in a:
      if num%2 == 0:
            result.append(num*3)
            