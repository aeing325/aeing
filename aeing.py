import tkinter as tk
import random
from PIL import Image, ImageTk

아이디비번 = {'관리자':'ADMIN', '최이든':'비번', '부계':'부계', '':''}

window=tk.Tk()


frame1=tk.Frame(window)
frame1.pack(fill='both', expand=True)

# 회원가입 프레임
회원가입=tk.Frame(noot)
회원가입.place(x=0,y=0,relwidth=1,relheight=1)

#뽑기 프레임
뽑기=tk.Frame(noot)
뽑기.place(x=0,y=0,relwidth=1,relheight=1)

#뽑기 성공 프레임
뽑기성공=tk.Frame(noot)
뽑기성공.place(x=0,y=0,relwidth=1,relheight=1)

#거래하기 프레임
거래하기프레임=tk.Frame(noot)
거래하기프레임.place(x=0,y=0,relwidth=1,relheight=1)


# 처음에 보일 프레임
로그인=tk.Frame(noot)
로그인.place(x=0,y=0,relwidth=1,relheight=1)


# 로그인 프레임 코드
def login():
    아이디 = id.get()
    비번 = pw.get()
    if 아이디 in 아이디비번:
        if 아이디비번[아이디] == 비번:
            뽑기.tkraise()
        else:
            print('실패!')
    else:
        print('아이디 없음!')

def signupframe():
    회원가입.tkraise()

로label=tk.Label(로그인, text="로그인", width=20, height=0, fg="black", relief="flat")
로label.pack(pady=10)

id=tk.Entry(로그인)
id.pack()

pw=tk.Entry(로그인, show="*")
pw.pack()

loginbutton = tk.Button(로그인, overrelief="solid", width=15, text="로그인하기", command=login)
loginbutton.pack(pady=(10,0))

signupbutton = tk.Button(로그인, overrelief="solid", width=15, text="회원가입하기", command=signupframe)
signupbutton.pack(pady=(10,0))

# 회원가입 프레임 코드
def sign_up():
    아이디 = id2.get()
    비번 = pw2.get()
    if 아이디 in 아이디비번:
        print('이미 존재하는 아이디입니다')
    else:
        아이디비번[아이디] = 비번
    로그인.tkraise()

회label=tk.Label(회원가입, text="회원가입", width=20, height=0, fg="black", relief="flat")
회label.pack(pady=10)    

id2=tk.Entry(회원가입)
id2.pack()

pw2=tk.Entry(회원가입, show="*")
pw2.pack()

signupbutton2 = tk.Button(회원가입, overrelief="solid", width=15, text="회원가입완료", command=sign_up)
signupbutton2.pack()



#뽑기프레임

사과원래=Image.open("사과.png").resize((250, 230))
바나나원래=Image.open("바나나.png").resize((250,170))
오렌지원래=Image.open("오렌지.png").resize((200,190))

사과사진=ImageTk.PhotoImage(사과원래)
바나나사진=ImageTk.PhotoImage(바나나원래)
오렌지사진=ImageTk.PhotoImage(오렌지원래)                                           

초기아이템들={'삭와':사과사진 ,'반안아':바나나사진 ,'올엔지':오렌지사진}


사과거래=Image.open("사과.png").resize((125, 115))
바나나거래=Image.open("바나나.png").resize((125,85))
오렌지거래=Image.open("오렌지.png").resize((100,95))

사과사진2=ImageTk.PhotoImage(사과거래)
바나나사진2=ImageTk.PhotoImage(바나나거래)
오렌지사진2=ImageTk.PhotoImage(오렌지거래)  

전체아이템들={'사과':사과사진2 ,'바나나':바나나사진2 ,'오렌지':오렌지사진2}


def 뽑기함수():
    나온이름, 나온사진 = random.choice(list(초기아이템들.items()))
    
    뽑기성공글자label.config(text=f'{나온이름} 뽑기 성공')
    뽑기성공이미지label.config(image=나온사진)
    뽑기성공.tkraise()

뽑button=tk.Button(뽑기, text='뽑기', command=뽑기함수)
뽑button.pack()


#뽑기 성공 후 프레임 코드

#거래함수
def 거래함수():
    거래하기프레임.tkraise()




뽑기성공이미지label=tk.Label(뽑기성공, image=사과사진, width=250, height=0, fg="black", relief="flat")
뽑기성공이미지label.pack(pady=10)    

뽑기성공글자label=tk.Label(뽑기성공, text='뽑기 성공', width=20, height=0, fg="black", relief="flat")
뽑기성공글자label.pack(pady=10)

뽑기성공후거래버튼=tk.Button(뽑기성공,text='거래하기',command=거래함수)
뽑기성공후거래버튼.pack(pady=10)

#거래하기 프레임 코드

상대이미지=tk.Label(거래하기프레임, image=사과사진2, width=250, height=0, fg="black", relief="flat")
상대이미지.grid(row=0,column=0) 

자신이미지=tk.Label(거래하기프레임, image=오렌지사진2, width=250, height=0, fg="black", relief="flat")
자신이미지.grid(row=4,column=1) 

자신글자=tk.Label(거래하기프레임, text='나')
자신글자.grid(row=4,column=0) 

상대글자=tk.Label(거래하기프레임, text='상대')
상대글자.grid(row=0,column=1) 

거래하실=tk.Label(거래하기프레임, text='거래하실?')
거래하실.grid(row=1,column=0, columnspan=2) 

거래동의버튼=tk.Button(거래하기프레임,text='동의 ㄱ')
거래동의버튼.grid(row=2,column=0, columnspan=2) 

거래취소버튼=tk.Button(거래하기프레임,text='ㄴㄴ 취소')
거래취소버튼.grid(row=3,column=0, columnspan=2) 


window.mainloop()
