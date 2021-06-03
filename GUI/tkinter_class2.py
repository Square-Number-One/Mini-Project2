from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from datetime import datetime as dt
from PIL import Image, ImageTk

class Window2():
    def __init__(self):
        self.search_word = ''
        self.window = Tk()
        self.window.title('EncoreTeam 1')
        self.window.geometry('700x700')
        self.window.resizable(False, False)

        self.data = []
        self.img = ''

    # 확인버튼 입력할 때 결과바디
    def search_btn(self):
        self.search_word = self.search_result.get()
        print(self.search_word)

    def show_result_window2(self, search):
        self.search_word = search
        print(search)

        # 데이터 입력받는다고 가정
        data = [['애플', '1', '2', '3']]
        img = 'cloud.png'
        self.data = data
        self.img = img

        photo1 = PhotoImage(file='bgw.png', master=self.window)
        label1 = Label(self.window, image=photo1)
        label1.place(x=0, y=0)

        photo2 = PhotoImage(file='pic1.png', master=self.window)
        label2 = Label(self.window, image=photo2, borderwidth=0)
        label2.place(x=0, y=1.5)

        # 검색어 입력받기
        self.search_result = Entry(self.window, width=100, font=('나눔고딕', 10), bg='white', borderwidth=1)
        self.search_result.place(x=190, y=20, width=370, height=33)

        # 검색 버튼 띄우기 (작동안함) -> DB로 테이블 ID 보내기 (뒤에)
        btn_search1 = Button(self.window, font=('나눔고딕', 9), text='검색', command=self.search_btn)
        btn_search1.place(x=570, y=20, width=50, height=34)

        # 되돌리기 버튼 띄우기
        btn_search2 = Button(self.window, font=('나눔고딕', 9), text='첫페이지', command=self.window.destroy)
        btn_search2.place(x=630, y=20, width=50, height=34)

        # 현재 검색어 표시
        sw1 = Label(self.window, text='검색어', width=5, bg='white', font=('나눔고딕', 13))
        sw1.place(x=20, y=70)
        sw2 = Label(self.window, text=self.search_word, width=10, fg='blue', bg='white' , font=('나눔고딕', 13))
        sw2.place(x=80, y=70)

        # ------------------------------DB 설정------------------------------------------------
        # 프레임 생성
        top_frame = Frame(self.window)
        top_frame.place(x=25, y=105)  # 표 위치 임의로 설정

        s = ttk.Style()
        s.configure('Treeview', rowheight=30)

        # 컬럼 설정
        tree = ttk.Treeview(top_frame, columns=(0, 1, 2, 3), show='headings')
        tree.pack(side='left')

        # 컬럼명
        tree.heading(0, text='ID')
        tree.heading(1, text='Search')
        tree.heading(2, text='Date')
        tree.heading(3, text='ImageURL')

        # 컬럼 높이, 너비 설정
        tree.column(0, width=50)
        tree.column(1, width=110)
        tree.column(2, width=220)
        tree.column(3, width=260)

        # 스크롤바 설정 (https://myinbox.tistory.com/154)
        scroll = ttk.Scrollbar(top_frame, orient='vertical', command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scroll.set)

        for i in self.data:
            tree.insert('', 'end', values=(i[0], i[1], i[2], i[3]))

        # ------------------------------이미지 설정------------------------------------------------
        # 워드클라우드 사진 올리기(resize 자유롭게 하기 위해 PIL-ImageTK사용)
        load = Image.open(self.img).resize((650, 300))
        image = ImageTk.PhotoImage(load, master=self.window)

        img = Label(self.window, image=image, borderwidth=5)
        img.image = image
        img.place(x=24, y=250)

        self.window.mainloop()
