from tkinter import *
import random

#  예제 1) tkinter 파이썬 GUI 레이블(label)
# tkinter를 사용하여 텍스트를 나타내보자
menulist = ['짜장면', '짬뽕', '라면', '국밥', '떡볶이', '김밥', '육회비빔밥', '닭볶음탕', '햄버거', '피자', '치킨']

# 1. 루트화면 (root window) 생성
tk = Tk() 
# 2. 텍스트 표시
label = Label(tk,text='AI가 추천해주는 메뉴는?') 
# 3. 레이블 배치 실행
label.pack()

tk.title("menu")
tk.geometry('300x100')

# 예제2) 버튼만들기
tk = Tk()

tk.title("menu")
tk.geometry('300x100')
# 함수 정의 (버튼을 누르면 텍스트 내용이 바뀜)
def event():
    menu = random.choice(menulist)
    button['text'] = f'{menu} 추천'

button = Button(tk,text='추천 메뉴',command=event)
quit = Button(tk, text='종료하기', command=tk.quit)
quit.pack()

button.pack(side=LEFT,padx=10,pady=10) #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 
quit.pack(side=RIGHT, padx=10, pady= 10)

# 4. 메인루프 실행
tk.mainloop()
