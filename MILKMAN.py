'''
Problem : Milk Man and His Bottles A Milkman serves milk in packaged bottles of
varied sizes. The possible size of the bottles are {1, 5, 7 and 10} litres.
He wants to supply desired quantity using as less bottles as possible
irrespective of the size. Your objective is to help him find the minimum
number of bottles required to supply the given demand of milk.

Input Format:
First line contains number of test cases N Next N lines, each contain a positive
integer Liwhich corresponds to the demand of milk. 

Output Format:
For each input Li, print the minimum number of bottles required to fulfill the
demand 

Constraints:
1 <= N <= 1000 Li > 0 1 <= i <= N

Sample Input and Output
Sample Input        Sample Output
2 
17                  2
65                  7
'''



for _ in range(input()):
    totalMilk = input()
    bottles = [10,7,5,1]
    count,j=0,0
    while(totalMilk>0):
       ltrs=totalMilk/bottles[j]
       totalMilk-=ltrs*bottles[j]
       j+=1
       count+=ltrs
       
    print count
