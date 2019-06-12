#Consider the following series: 0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8

#This series is a mixture of 2 series all the odd terms in this series form even numbers in ascending order and every even term is derived from the previous term using the formula (x/2).

#Write a program to find the nth term in this series.


n=int(input("Enter number"));

if(n%2==1):
  if(n==1):
    print(0)
  else:
    n=n-1
    print(n)
else:
  if(n==2):
    print(0)
  else:
    n=n-2
    output=int(n/2)
    print(output)
