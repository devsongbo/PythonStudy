

from sys import stdout

def myfunc():

    print("我是一个函数")

    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != k) and (i != j) and (j != k):
                    print (i, j, k)








myfunc()


def myfunc2(name = "宋博"):

    print("我是 %s" %  (name))




myfunc2(name="老李")




def isPerfectNumber (num):
    # for j in range(2, num+1):
    #     print(type(j))
        j = num
        k = []
        for i in range(1, j):
            if j % i == 0:
                k.append(i)


        if sum(k) == j and j == num:
            return  True
            print(j)
        else:
            return  False




print(isPerfectNumber(6))





