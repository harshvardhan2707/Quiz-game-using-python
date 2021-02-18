import Questions
import random
import tkinter as tk
import pygame
import sys
import os
run=0
Spaceinvlifeline=[0,0]
Attemptedques=[]
score=0
NoOfAttemptedQuestions=0
ListofQues=["Question1.mp3","Question2.mp3","Question3.mp3","Question4.mp3","Question4(1).mp3","Question5.mp3","Question6.mp3","Question7.mp3","Question8.mp3","Question9.mp3","Question10.mp3"]
a=list(Questions.A.keys())
pygame.init()

def credentials():
    for x in root.winfo_children():
        x.destroy()
    username_var.set("")
    password_var.set("")
    username = tk.Label(root, text = 'USERNAME', font = ('calibre',15,'bold'),pady=28)
    username.pack()
    username_entry= tk.Entry(root,textvariable = username_var, font=('calibre',30,'normal'),)
    username_entry.pack()
    password = tk.Label(root, text = 'PASSWORD', font = ('calibre',15,'bold'),pady=28)
    password.pack()
    password_entry= tk.Entry(root,textvariable = password_var, font=('calibre',30,'normal'),show="*")
    password_entry.pack()
    def aftersubmission():
        sub_btn['state']=tk.DISABLED
        verify()
    sub_btn=tk.Button(root,text="SUBMIT",fg="blue",bg="white",font=("Helevetica",15),command=aftersubmission)
    sub_btn.pack()
    MenuEnd()
    
    tk.mainloop()

def verify():
    global c
    username=username_var.get()
    password=password_var.get()
    if(username=="doons" and password=="12345"):
        change()
    else:
        error=tk.Label(root,text="INCORRECT! You have "+str(c)+" chances left",fg="red",bg="pink",font=("Verdana",12))
        error.pack()
        
        if(c>0):
            c-=1
            chance=tk.Button(root,text="Try again",fg="blue",bg="white",font=("Verdana",15),command=credentials)
            chance.pack(side=tk.BOTTOM)
        else:
            for x in root.winfo_children():
                x.destroy()
            error=tk.Label(root,text="YOU HAVE EXHAUSTED ALL YOUR CHANCES",fg="red",pady=100,font=("Verdana",20,"bold"))
            error.pack(side=tk.TOP)
            MenuEnd()

def change():
    for x in root.winfo_children():
        x.destroy()
    message=tk.Label(root,text="Select your choice",fg="green",bg="white",pady=29,font=("Verdana",30))
    message.pack(side=tk.TOP)
    add=tk.Radiobutton(root,text="ADD QUESTIONS",fg="blue",pady=25,font=("Helevetica",25,"bold"),command=enter)
    add.pack()
    rem=tk.Radiobutton(root,text="REMOVE QUESTIONS",fg="blue",pady=30,font=("Helevetica",25,"bold"),command=remove)
    rem.pack()
    MenuEnd()
    tk.mainloop()

def enter():
    for x in root.winfo_children():
        x.destroy()
    Category_var.set("")
    question_var.set("")
    op1_var.set("")
    op2_var.set("")
    op3_var.set("")
    op4_var.set("")
    correct_op_var.set("")
    Category_label = tk.Label(root, text = 'Category', font = ('calibre',10,'bold'))
    Category_label.pack()
    Category= tk.Entry(root,textvariable = Category_var, font=('calibre',10,'normal'))
    Category.pack()
    question_label = tk.Label(root, text = 'Question', font = ('calibre',10,'bold'))
    question_label.pack()
    question= tk.Entry(root,textvariable = question_var, font=('calibre',10,'normal'))
    question.pack()
    op1_label = tk.Label(root, text = 'Option 1', font = ('calibre',10,'bold'))
    op1_label.pack()
    op1= tk.Entry(root,textvariable = op1_var, font=('calibre',10,'normal'))
    op1.pack()
    op2_label = tk.Label(root, text = 'Option 2', font = ('calibre',10,'bold'))
    op2_label.pack()
    op2= tk.Entry(root,textvariable = op2_var, font=('calibre',10,'normal'))
    op2.pack()
    op3_label = tk.Label(root, text = 'Option 3', font = ('calibre',10,'bold'))
    op3_label.pack()
    op3= tk.Entry(root,textvariable = op3_var, font=('calibre',10,'normal'))
    op3.pack()
    op4_label = tk.Label(root, text = 'Option 4', font = ('calibre',10,'bold'))
    op4_label.pack()
    op4= tk.Entry(root,textvariable = op4_var, font=('calibre',10,'normal'))
    op4.pack()
    correct_op_label = tk.Label(root, text = 'Correct Option', font = ('calibre',10,'bold'))
    correct_op_label.pack()
    correct_op= tk.Entry(root,textvariable = correct_op_var, font=('calibre',10,'normal'))
    correct_op.pack()
    def submission():
        sub_btn['state']=tk.DISABLED
        submit()
    sub_btn=tk.Button(root,text="SUBMIT",fg="blue",bg="white",font=("Helevetica",12),command=submission)
    sub_btn.pack()
    tk.Button(root,text="Back",fg="blue",bg="white",font=("Helevetica",12),command=change).pack()
    MenuEnd()
    tk.mainloop()


def remove():
    for x in root.winfo_children():
        x.destroy()
    user_category.set("")
    user_question.set("")
    cat = tk.Label(root, text = 'Category', font = ('calibre',15,'bold'),pady=28)
    cat.pack()
    user_cat= tk.Entry(root,textvariable = user_category, font=('calibre',30,'normal'),)
    user_cat.pack()
    ques = tk.Label(root, text = 'Question', font = ('calibre',15,'bold'),pady=28)
    ques.pack()
    user_ques= tk.Entry(root,textvariable = user_question, font=('calibre',30,'normal'))
    user_ques.pack()
    def aftersub():
        sub_btn['state']=tk.DISABLED
        removal()
    sub_btn=tk.Button(root,text="SUBMIT",fg="blue",bg="white",font=("Helevetica",15),command=aftersub)
    sub_btn.pack()
    menu=tk.Button(root,text="Menu",fg="black",font=("Helevetica",19),bg="white", command=main,pady=12)
    menu.pack(side=tk.LEFT)
    exit=tk.Button(root,text="Exit",fg="red",bg="white",font=("Helevetica",19),command=root.destroy,pady=12)
    exit.pack(side=tk.RIGHT)
    tk.mainloop()

def removal():
    r_category=user_category.get()
    r_question=user_question.get()
    if(r_category =="" or r_question==""):
        a = tk.Label(root, text="One or more text fields are empty",fg="red",bg  ="pink",font=("Verdana",15))
        a.pack()
        sub_btn=tk.Button(root,text="Try again",fg="blue",bg="white",font=("Helevetica",15),command=remove)
        sub_btn.pack()
    else:
        if(r_category in Questions.A.keys()):
            if(r_question in Questions.A[r_category].keys()):
                Questions.remove(r_category,r_question)
                d = tk.Label(root, text="Successfully removed",fg="green",bg="white",font=("Verdana",15))
                d.pack()
                sub_btn=tk.Button(root,text="Continue",fg="black",bg="white",font=("Helevetica",15),command=remove)
                sub_btn.pack()
            else:
                tk.Label(root, text="Please enter valid question",fg="red",bg="white",font=("Verdana",15)).pack()
        else:
            tk.Label(root, text="Please enter valid question",fg="red",bg="white",font=("Verdana",15)).pack()
    tk.Button(root,text="Back",fg="black",bg="white",font=("Helevetica",15),command=change).pack()
    tk.mainloop()


def submit():
    category=Category_var.get()
    question=question_var.get()
    op1=op1_var.get()
    op2=op2_var.get()
    op3=op3_var.get()
    op4=op4_var.get()
    correct_op=correct_op_var.get()
    if(category =="" or question =="" or op1 =="" or op2 =="" or op3 =="" or op4 =="" or correct_op ==""):
        a = tk.Label(root, text="One or more text fields are empty",fg="red",bg  ="pink",font=("Verdana",10))
        a.pack()
        sub_btn=tk.Button(root,text="Try again",fg="blue",bg="white",font=("Helevetica",10),command=enter)
        sub_btn.pack()
    else:
        d = tk.Label(root, text="Successfully added",fg="green",bg="white",font=("Verdana",10))
        d.pack()
        sub_btn=tk.Button(root,text="Continue",fg="black",bg="white",font=("Helevetica",10),command=enter)
        sub_btn.pack()
    tk.mainloop()

def MenuEnd():
    menu=tk.Button(root,text="Menu",fg="black",font=("Helevetica",15),pady=5,bg="white", command=restart)
    menu.pack(anchor='sw',side=tk.LEFT)
    exit=tk.Button(root,text="Exit",fg="red",bg="white",font=("Helevetica",15),pady=5,command=root.destroy)
    exit.pack(anchor='se',side=tk.RIGHT)

def For():
    for x in root.winfo_children():
        x.destroy()

def restart():
    root.destroy()
    pygame.quit()
    os.system('python "TheQuiz Mania.py"')


def main():
    For()   
    root.title('The Quiz Mania')
    greet=tk.Label(root,text="THE QUIZ MANIA",fg="white",bg="black",pady=33,padx=10,font=("Verdana",32,"bold"))
    greet.pack(side=tk.TOP)
    start=tk.Button(root,text="START",fg="blue",bg="white",pady=10,font=("Helevetica",17),command=MainQuiz)
    start.pack()
    instr=tk.Button(root,text="INSTRUCTIONS",fg="green",bg="white",pady=10,font=("Helevetica",17),command=inst)
    instr.pack()
    admin=tk.Button(root,text="ADMIN",fg="brown",bg="white",pady=10,font=("Helevetica",17),command=credentials)
    admin.pack()
    exit=tk.Button(root,text="EXIT",fg="red",bg="white",pady=10,font=("Helevetica",17),command=root.destroy)
    exit.pack()
    root.geometry("1100x415")
    tk.mainloop()


def inst():
    For()
    a = tk.Label(root, text="1. Choose the subject of your expertise.",fg="green",pady=12,bg="white",font=("Helevetica",18))
    a.pack()
    b = tk.Label(root, text="2. Select the correct options to move forward.",pady=12,fg="blue",bg="white",font=("Helevetica",18))
    b.pack()
    c = tk.Label(root, text="3. If your answer is inocrrect, Select the mini game which you want to play.",pady=12,fg="orange",bg="white",font=("Helevetica",18))
    c.pack()
    d = tk.Label(root, text="4. Get back to the quiz once you beat the game.",pady=12,fg="brown",bg="white",font=("Helevetica",18))
    d.pack()
    f = tk.Label(root, text="5. Get back to the quiz once you beat the game.",pady=12,fg="red",bg="white",font=("Helevetica",18))
    f.pack()
    e = tk.Label(root, text="All THE BEST!!",pady=12,fg="purple",bg="white",font=("Helevetica",18))
    e.pack()
    MenuEnd()
    tk.mainloop()



def SnakeGame(Topic):
    For()
    tk.Label(root,text='''You've chosen Snake game as your lifeline. Try to score 10 points to continue the quiz. 
    After you score the required points, the game window will shut and you will have the option to either quit the game 
    or go back to continuing the quiz.''',fg="red",pady=5,font=("Helevetica",17)).pack()
    z=tk.StringVar()
    tk.Radiobutton(root,text="Start game",variable=z,fg="blue",font=("Helevetica",17),pady=16,value="Start game",command=lambda:StartSnake(Topic)).pack()
    MenuEnd()
def StartSnake(Topic):
    global Spaceinvlifeline
    Spaceinvlifeline[1]+=1
    import game
    game.game_over=False
    game.gameLoop()
    if(game.game_over==True and game.Length_of_snake<11):
        For()
        Attemptedques=[]
        Spaceinvlifeline[1]=0
        tk.Label(root,text="Sorry you failed, better luck next time :)",fg="red",pady=5,font=("Helevetica",17)).pack()
        tk.Label(root,text="Your Final Quiz Score is: "+str(score),fg="green",font=("Helevetica",30)).pack()
        game.pygame.quit()
        MenuEnd()
    elif(game.game_over==True and game.Length_of_snake>=11):
        For()
        z=tk.StringVar()
        tk.Label(root,text='''Congratulations, you've won the Snake game.
        Your lifeline is now valid. Now you can get back to the quiz.''',fg="red",pady=5,font=("Helevetica",17)).pack()
        tk.Radiobutton(root,text="You won, return to quiz",variable=z,fg="blue",font=("Helevetica",17),pady=30,value="Return to quiz",command=lambda:callMain(Topic)).pack()
        MenuEnd()
        game.pygame.quit()
        game.pygame.init()

def MainQuiz():
    For()
    m=0
    tk.Label(root, text="Choose the subject of your expertise:",fg="green",bg="white",pady=8,font=("Verdana",19)).pack()
    r=tk.StringVar()
    for x in a:
        tk.Radiobutton(root,text=x,variable=r,value=x,fg="blue",font=("Helevetica",17),pady=10,command=lambda:callMain(r.get())).pack()
        m+=1
    MenuEnd()
    m=random.choice(["Starting.mp3","LetsPlay.mp3","Beginning.mp3"])
    pygame.mixer.music.load(m)
    pygame.mixer.music.play()
    tk.mainloop() 



def SpaceInvds(Topic):
    For()
    tk.Label(root,text='''You've chosen Space Invaders as your lifeline. Try to score 10 points to continue the quiz. 
    After you score the required points, the game window will shut and you will have the option to either 
    quit the game or go back to continuing the quiz.''',fg="red",pady=5,font=("Helevetica",17)).pack()
    z=tk.StringVar()
    tk.Radiobutton(root,text="Start game",variable=z,fg="blue",font=("Helevetica",17),pady=16,value="Start game",command=lambda:StartSpaceInvds(Topic)).pack()
    MenuEnd()

def StartSpaceInvds(Topic):
    global Spaceinvlifeline
    global run
    Spaceinvlifeline[0]+=1
    import Main
    print(Main.pygame.get_init())
    Main.pygame.init()
    Main.running=True
    Main.playerX=370
    Main.playerX_change=0
    Main.score_value=0
    Main.bulletX=0
    Main.bulletY=480
    Main.bullet_state="ready"
    Main.StartGame()
    if(Main.running==False and Main.score_value<10):
        For()
        Attemptedques=[]
        Spaceinvlifeline[0]=0
        tk.Label(root,text="Sorry you failed, better luck next time :)",fg="red",pady=5,font=("Helevetica",17)).pack()
        tk.Label(root,text="Your Final Quiz Score Is: "+str(score),fg="green",font=("Helevetica",30)).pack()
        MenuEnd()
        Main.pygame.quit()
        Main.pygame.init()
    elif(Main.running==False and Main.score_value>=10):
        For()
        z=tk.StringVar()
        tk.Label(root,text='''Congratulations, you've completed the Space Invaders game. 
        Your lifeline is now valid. Now you can get back to the quiz.''',fg="red",pady=5,font=("Helevetica",17)).pack()
        tk.Radiobutton(root,text="You won, return to quiz",variable=z,fg="blue",font=("Helevetica",17),pady=30,value="Return to quiz",command=lambda:callMain(Topic)).pack()
        MenuEnd()
        Main.pygame.quit()
        Main.pygame.init()


def CorrectAns(A,value,Topic,n):
    global NoOfAttemptedQuestions
    if(A[1]==value):
        global score
        global NoOfAttemptedQuestions
        score=score+1
        For()
        x="Right_Answer.mp3"
        if(NoOfAttemptedQuestions<n and NoOfAttemptedQuestions<10):
            if(NoOfAttemptedQuestions<3):
                y=random.choice([x,ListofQues[NoOfAttemptedQuestions]])
                NoOfAttemptedQuestions+=1
                pygame.mixer.music.load(y)
                pygame.mixer.music.play()
            elif(NoOfAttemptedQuestions==3):
                y=random.choice(ListofQues[3:5])
                NoOfAttemptedQuestions+=1
                pygame.mixer.music.load(y)
                pygame.mixer.music.play()
            elif(NoOfAttemptedQuestions>3):
                y=random.choice([x,ListofQues[NoOfAttemptedQuestions+1]])
                NoOfAttemptedQuestions+=1
                pygame.mixer.music.load(y)
                pygame.mixer.music.play()
        MenuEnd()
        callMain(Topic)

    else:
        NoOfAttemptedQuestions+=1
        For()
        global Spaceinvlifeline
        if(Spaceinvlifeline!=[1,1]):
            tk.Label(root,text='''Your Answer was INCORRECT!''',fg="red",font=("Helevetica",15),bg="pink").pack()
            tk.Label(root,text='''Choose one of the following to continue...''',fg="red",font=("Helevetica",15)).pack()
            z=tk.StringVar()
            if(Spaceinvlifeline[0]==0):
                tk.Radiobutton(root,text="Space Invaders",variable=z,fg="blue",font=("Helevetica",17),pady=30,value="Space Invaders",command=lambda:SpaceInvds(Topic)).pack()
            if(Spaceinvlifeline[1]==0):
                tk.Radiobutton(root,text="Snake",variable=z,fg="blue",font=("Helevetica",17),pady=16,value="Snake",command=lambda:SnakeGame(Topic)).pack()
            pygame.mixer.music.load("WrongAnswer.mp3")
            pygame.mixer.music.play()
        else:
            tk.Label(root,text="Sorry you failed, better luck next time :)",fg="red",pady=5,font=("Helevetica",17)).pack()
            tk.Label(root,text="Score: "+str(score),fg="green",font=("Helevetica",30)).pack()
        MenuEnd()


def callMain(value):
    global score
    For()
    m=0
    root.title(value)
    Queslist=list(Questions.A[value])
    if(set(Attemptedques)==set(Queslist)):
        for x in root.winfo_children():
            x.destroy()
        tk.Label(root,text="You Won. Your Final Quiz Score is: "+str(score),fg="green",font=("Helevetica",30)).pack()
        MenuEnd()
    else:
        Randomq=random.choice(list(set(Queslist)-set(Attemptedques)))
        Attemptedques.append(Randomq)
        tk.Label(root,text=Randomq,fg="purple",font=("Verdana",18),pady=8,bg="white").pack()
        r=tk.IntVar()
        for x in Questions.A[value][Randomq][0]:
            tk.Radiobutton(root,text=x,variable=r,value=m,fg="blue",font=("Helevetica",17),pady=17,command=lambda:CorrectAns(Questions.A[value][Randomq],r.get(),value,len(Queslist))).pack()
            m+=1  
        MenuEnd()
        global NoOfAttemptedQuestions
        if(NoOfAttemptedQuestions==0):
            NoOfAttemptedQuestions+=1
            pygame.mixer.music.load("Question1.mp3")
            pygame.mixer.music.play()


root=tk.Tk()
c=2
Category_var=tk.StringVar()
question_var=tk.StringVar()
op1_var=tk.StringVar()
op2_var=tk.StringVar()
op3_var=tk.StringVar()
op4_var=tk.StringVar()
correct_op_var=tk.StringVar()
username_var=tk.StringVar()
password_var=tk.StringVar()
user_category=tk.StringVar()
user_question=tk.StringVar()
main()
