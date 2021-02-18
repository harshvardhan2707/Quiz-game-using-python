f=open('C:\\Users\\lenovo\\OneDrive\\Desktop\\CSE Project\\Question.txt','r')
A=eval(f.read())
f.close()
def add(Topic,ques,op1,op2,op3,op4,correctoption):
    global A
    correctoption=ord(correctoption.lower())-ord('a')
    A[Topic][ques]=[[op1,op2,op3,op4],correctoption]
    x=open('C:\\Users\\lenovo\\OneDrive\\Desktop\\CSE Project\\Question.txt','w')
    x.write(str(A))
    x.close()
def remove(Dict,ques):
    del A[Dict][ques]
    x=open('C:\\Users\\lenovo\\OneDrive\\Desktop\\CSE Project\\Question.txt','w')
    x.write(str(A))
    x.close()