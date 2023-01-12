import random

rand_num = random.randint(1, 100)

print(rand_num)

cnt = 1

while True:
    try:
        num = int(input("enter 1~100 num : "))
        if num < rand_num:
            print("up")
        elif num > rand_num:
            print("down")
        else:
            print(f"success in {cnt}")
            break
        cnt += 1
    except:
        print("try again")
