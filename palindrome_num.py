import math

num = int(input())


def palindrome(a):

    list_num = str(a)

    for i in range(0, len(list_num)//2):

        if list_num[i] == list_num[len(list_num) - 1 - i]:

            continue
        else:

            return False

    return True


if palindrome(num) == True:

    print("yes, palindrome")

else:

    print("not, palindrome")
