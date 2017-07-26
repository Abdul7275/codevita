'''
Problem : Catch-22 A robot is programmed to move forward F meters and
backwards again, say B meters, in a straight line. The Robot covers 1 meter
in T units of time. On Robot's path there is a ditch at a distance FD from
initial position in forward direction as well as a ditch at a distance BD from
initial position in backward direction. This forward and backward movement is
performed repeatedly by the Robot. Your task is to calculate amount of time
taken, before the Robot falls in either ditch, if at all it falls in a ditch.

Input Format:
First line contains total number of test cases, denoted by N Next N lines,
contain a tuple containing 5 values delimited by space F B T FD BD, where 
F denotes forward displacement in meters
B denotes backward displacement in meters
T denotes time taken to cover 1 meter
FD denotes distance from Robot's starting position and the ditch in forward direction
BD denotes distance from Robot's starting position and the ditch in backward direction

Output Format:
For each test case print time taken by the Robot to fall in the ditch and
also state which ditch he falls into. Print F for forward and B for backward.
Both the outputs must be delimited by whitespace OR Print No Ditch if the
Robot does not fall in either ditch

Constraints:
First move will always be in forward direction 1 <= N <= 100 forward
displacement > 0 backward displacement > 0 time > 0 distance of ditch in
forward direction (FD) > 0 distance of ditch in backward direction (BD) > 0
All input values must be positive integers only

Sample Input            Output
3
9 4 3 13 10             63 F
9 7 1 11 13             25 F
4 4 3 8 12              No Ditch

5
8 4 7 11 22             133 F
4 5 4 25 6              216 B
4 9 3 6 29              231 B
7 10 6 24 12            408 B
10 10 1 9 7             9 F
'''



for i in range(input()):
    f,b,t,fd,bd=map(int,raw_input().split())
    temp,c=0,0
    if f==b and f<fd and b<bd:
        print 'No Ditch'
    elif f>=b:
        while(True):
            temp=temp+f
            c=c+f
            if c>=fd:
                break
            c=c-b
            temp=temp+b
        temp=temp -(c-fd)
        print temp*t,'F'
    else:
        while(True):
            temp=temp+f
            c=c-f
            a=c+b
            #print c,
            if a>=bd:
                break
            c=c+b
            temp=temp+b
            #print temp
        temp=temp-(c-bd)
        print temp*t,'B'
            
