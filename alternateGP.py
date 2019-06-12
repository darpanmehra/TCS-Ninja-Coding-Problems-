#Consider the following series: 1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187…

#This series is a mixture of 2 series – all the odd terms in this series form a geometric series and all the even terms form yet another geometric series. Write a program to find the Nth term in the series.

import math
n=int(input("Enter Number:"))

if(n%2==0):
  if(n==2):
    print(1)
  else:
    n=n//2
    n=n-1
    output=math.pow(3,n)
    output=int(output)
    print(output)

else:
  if (n==1):
    print(1)
  n=(n//2)+1
  n=n-1
  output=math.pow(2,n)
  output=int(output)
  print(output)
