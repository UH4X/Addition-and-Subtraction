nums = []

while True:
    try:
        print()
        user = int(input("Addition Number: "))
        nums.append(user)
        if user >=0:
            show = sum(nums)
            res = sum(nums)
            print(f"{user} + {show - user}")
            print(f"nums={res}")
        if user <=0:
            show = sum(nums)
            res = sum(nums)
            print(f"{abs(user)} - {show - user}")
            print(f"Your result: = {res}")
    except KeyboardInterrupt:
        exit()
        

