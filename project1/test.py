#import math

#x = int(math.sqrt(9))

#print(x)

#x = 5
#y = -3

#print(pow(x,y))
#print(abs(y))


#recursion   
"""
1= 1 (*Jika steps == 1, fungsi langsung mengembalikan 1)
2= 2+1 (**Jika steps > 1, maka fungsi akan mengembalikan nilai 
3= 3+3  steps ditambah dengan hasil pemanggilan rekursif pada steps - 1)
4= 4+6
5= 5+10
6= 6+15
7= 7+21
**
else:
walk(7) mengembalikan 7 + walk(6)
walk(6) mengembalikan 6 + walk(5)
walk(5) mengembalikan 5 + walk(4)
walk(4) mengembalikan 4 + walk(3)
walk(3) mengembalikan 3 + walk(2)
walk(2) mengembalikan 2 + walk(1)
walk(1) mengembalikan 1 (base case)
***
walk(2) = 2 + 1 = 3
walk(3) = 3 + 3 = 6
walk(4) = 4 + 6 = 10
walk(5) = 5 + 10 = 15
walk(6) = 6 + 15 = 21
walk(7) = 7 + 21 = 28  ---> result
****
jika dari penghitungan matematika terlihat seperti ini:
1! = 1
2!= 2+1 
3!= 3+2+1
4!=4+3+2+1
5!=5+4+3+2+1
6!=6+5+4+3+2+1
7!=7+6+5+4+3+2+1
"""
def walk(steps):
    if steps == 1:
        return 1
    else:
        return steps + walk(steps-1)
    
result= walk(7)
print(result)


#iterative
#def walk(steps):
    #for step in range(steps):
        #print(step)

#walk(106)