"""You are given an integer N you need to print all the Armstrong Numbers between 1 to N.

If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number.

For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )."""

N = int(input())
for i in range(1000, N + 1):
    a = i
    sum = 0
    while a != 0:
        sum += (a % 10) ** 3
        a = a // 10
    print(i, sum)
    if sum == i:
        print(i)
