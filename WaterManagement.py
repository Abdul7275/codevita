'''

Problem : Water Management There are N tubs of water, numbered from 1 to N. Initially there is a few litres of water in each tub. Each water tub has 2 taps attached to it. Incoming Tap with speed x litres / second and Outgoing Tap with speed y litres / second. Let water(i) denote the final volume of water in ith tub. Amit wants to attain such a situation that water(i) < water(i+1) for 1<=i <=N. i.e. water in each tub must be less than water in the tub next to it. He wants to do this as quickly as possible. You task is to find out and tell Amit, what is the minimum number of seconds required to attain in this situation.

  Input Format: First line will contains the number of tubs, denoted by N Next N lines contain a tuple with 3 integers delimited by white space. The tuple contents are 
Wi - volume of water present initially in ith tub (in litres)
x - speed of incoming tap of ith tub ( in litres/second)
y - speed of outgoing tap of ith tub ( in litres/second)

Output Format:
Minimum time in seconds, needed to arrange water in N tubs, in ascending order of volume.
Constraints:
2 <= N <= 100000 0 <= W <= 1000000000 (1 billion) for each tub 1 <= x <= 10000 for each tub1 <= y <= 10000 for each tub A tap can be used only for integral number of seconds i.e. you cannot use a tap for 0.3 or 0.5 seconds. It can be used either for 1,2,3.... Seconds Capacity of each tub is infinite.Volume of water in any tub cannot be less than zero at any point of time. Any number of taps can be turned on or off simultaneously.   Sample Input and Output 

Sample Input:           Sample output:
3                       1
2 3 3
3 5 5
3 5 5


Sample Input:           Sample output:
3                       2
6 2 1
4 1 3
4 1 4

'''




w,x,y=[],[],[]
n=input()
time=0
for i in range(n):
    abdul=map(int,raw_input().split())
    w.append(abdul[0])
    x.append(abdul[1])
    y.append(abdul[2])

for i in range(n-1):
    if w[i]<w[i+1]:
        continue
    else:
        time+=1
        cmp(time,i)
print time
        
def cmp(time,i):
        if (w[i]-y[i]>0 and i==0):
            w[i] = w[i]-y[i]

        elif (w[i]-y[i]>0 and w[i]>w[i-1]):
            w[i]= w[i]-y[i]

        if(w[i+1]<=w[i]):
            w[i+1]=w[i+1]+x[i+1]

            if(w[i+1]<=w[i]):
                time+=1
                
