number = input("Enter a number: ")

# 1st method: converting a string(num) to list and then converting each str(list item) into int
# and finding sum of list items, converting the sum to string to find length of number,
# if length is '1' and num is 1 then magic number, else recurse into function
def sum_num(num):
    num = list(num)
    print(num)
    for i in range(0, len(num)):
        num[i] = int(num[i])
    num = str(sum(num))

    if len(num) == 1:
        if num == '1':
            print("Magic number")
        else:
            print("Not a magic number")
    else:
        sum_num(num)

sum_num(number)

# 2nd method: divisibility by 9, any number when divided by 9 if leaves remainder 1
# then it is magic number. (x = 1, 10, 19, 28, 37.... their previous numbers y = 0, 9, 18, 27, 36....
# are multiples of 9)

if int(number) % 9 == 1:
    print("Magic number")
else:
    print("Not a magic number")

