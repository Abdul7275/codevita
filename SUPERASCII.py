'''
Problem : Super ASCII String Checker

In the Byteland country a string "S" is said to super ascii string if and only if count of each character in the string is equal to its ascii value.

In the Byteland country ascii code of 'a' is 1, 'b' is 2 ...'z' is 26.

Your task is to find out whether the given string is a super ascii string or not.

Input Format:
First line contains number of test cases T, followed by T lines, each containing a string "S".

Output Format:
For each test case print "Yes" if the String "S" is super ascii, else print "No"

Constraints:
1<=T<=100
1<=|S|<=400, S will contains only lower case alphabets ('a'-'z').

Sample Input         Output
2
bba                  Yes
scca                 No

'''




for _ in range(input()):
    abdul = raw_input()
    kalam={}
    for i in abdul:
        if i in kalam:
            continue
        else:
            kalam.update({i:abdul.count(i)})
    flag=0
    #print kalam
    for key,value in kalam.iteritems():
        #print key,value,ord(key)-96
        if value!=ord(key)-96:
            flag=1
            break
    print 'Yes' if flag==0 else'no'
