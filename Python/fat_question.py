def cgpa(gradelist,studentcredits,dgdict,temp):
    anslst=[]
    for i in gradelist[temp]:
        z=dgdict[i]
        anslst.append(z)
    sum1=0
    for i in range(len(studentcredits[temp])):
        sum1+=(studentcredits[temp][i]*anslst[i])
    ans=format(sum1/sum(studentcredits[temp]),'0.2f')
    return ans

dgdict={}
studentregno=[]
studentmarks=[]
studentcredits=[]

ns=int(input())
nm=int(input())
ndg=int(input())
for i in range(ndg):
    y=input()
    x=int(input())
    dgdict[y]=x

for i in range(ns):
    studentregno.append(input())
for i in range(ns):
    marks=[]
    for i in range(nm):
        marks.append(int(input()))
    studentmarks.append(marks)
for i in range(ns):
    credits=[]
    for i in range(nm):
        credits.append(int(input()))
    studentcredits.append(credits)
gradelist=[]
for i in studentmarks:
    grade=[]
    for j in i:
        if(j>=90):
            grade.append('S')
        if(j>=80 and j<90):
            grade.append('A')
        if(j>=70 and j<80):
            grade.append('B')
        if(j>=60 and j<70):
            grade.append('C')
        if(j>=55 and j<60):
            grade.append('D')
        if(j>=50 and j<55):
            grade.append('E')
        if(j<50):
            grade.append('F')
    gradelist.append(grade)
temp=0
for i in studentregno:
    print(i)
    print("CGPA is ",end="")
    print(cgpa(gradelist,studentcredits,dgdict,temp))
    temp+=1