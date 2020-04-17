n=int(input("Enter number of test cases"))
for each in range(n):
    s1=list(input("s1"))
    s2=list(input("s2"))
    d=0
    m=len(s1)+len(s2)
    print("The length is {}".format(m))
    l1=set(s1).intersection(set(s2))
    l2=len(l1)
    print(l1)
    for i in l1:
        d=d+min(s1.count(i),s2.count(i))
        print(d)
    print("The final answer is {}".format(m-2*d))