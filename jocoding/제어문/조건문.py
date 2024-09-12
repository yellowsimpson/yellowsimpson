"""
pocket = ['paper', 'cellphone']
card = False
a = True

while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffe = coffe -1
    print("남은 커피의 양은 %d 개입니다." %coffe)
    if coffe == 0:
        print("커피가 다 떨어졌습니다. ")
        break


test_list = ['1','2','3']
for i  in test_list:
    print(i)
"""

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d pass" % number)
    else:
        print("%d fail" % number)

