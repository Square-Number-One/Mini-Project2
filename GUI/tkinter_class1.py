from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from datetime import datetime as dt
from PIL import Image, ImageTk

from tkinter_class2 import Window2 # 경로변경하세요!


class Window1():

    def __init__(self):
        self.search_word = ''
        self.type = '' # DB 타입
        self.window = Tk()
        self.window.title('EncoreTeam 1')
        self.window.geometry('700x700')
        self.window.resizable(False, False)

    # DB 타입 설정
    def con1(self):
        self.type = 'db'
        print(self.type)
        print(self.get_date)
    def con2(self):
        self.type = 'local'
        print(self.type)
        print(self.get_date)
    def con3(self):
        self.type = 'both'
        print(self.type)
        print(self.get_date)

    # 닫기 버튼 (DB 옆)
    def con4(self):
        msgbox.showinfo('알림', '종료합니다')
        self.window.destroy()

    def search_btn(self):
        self.search_word = self.search_result.get()

        window2 = Window2()
        window2.show_result_window2(self.search_word)

    def date_get(self):
        pp = self.selc_period.get()
        if pp == 'NO':
            self.get_date = '{}-{}-{}~{}-{}-{}'.format(dt.now().year, dt.now().month, dt.now().day, dt.now().year,
                                                    dt.now().month, dt.now().day)
            msgbox.showinfo('알림', '기본설정 기간으로 갱신합니다')
        else:
            y1 = self.com_p_year1.get()
            m1 = self.com_p_month1.get()
            d1 = self.com_p_day1.get()
            y2 = self.com_p_year2.get()
            m2 = self.com_p_month2.get()
            d2 = self.com_p_day2.get()
            self.get_date = '{}-{}-{}~{}-{}-{}'.format(y1, m1, d1, y2, m2, d2)

        print(self.get_date)

        return self.get_date

    def get_search_window1(self):

        # 배경화면 설정
        photo1 = PhotoImage(file='bgw.png', master=self.window)
        label1 = Label(self.window, image=photo1)
        label1.place(x=-2, y=0)

        photo2 = PhotoImage(file='teamwork2.png', master=self.window)
        label2 = Label(self.window, image=photo2, borderwidth=0)
        label2.place(x=-150, y=-50)

        # 검색어 입력받기
        self.search_result = Entry(self.window, width=100, font=('나눔고딕', 10), bg='white', borderwidth=1)
        self.search_result.place(x=90, y=330, width=480, height=40)


        # 검색 버튼 띄우기
        btn_search = Button(self.window, font=('나눔고딕', 10), text='검색', command=self.search_btn)
        # command=lambda: [search_btn(), start_window2()])
        btn_search.place(x=570, y=329, width=50, height=41)

        # ----------------- 기간 설정 --------------------------------------------

        photo3 = PhotoImage(file='boundary.png', master=self.window)
        label3 = Label(self.window, image=photo3, borderwidth=0)
        label3.place(x=89, y=400)

        frame_option = Label(self.window, text='[추가 정보 갱신을 원하시면 정보를 입력해주세요]', width=33, bg='white', font=('나눔고딕', 10))
        frame_option.place(x=101, y=409)

        # 기간 선택 여부
        period_yesno = Label(self.window, text='기간 선택 여부', width=10, bg='white', font=('나눔고딕', 8))
        period_yesno.place(x=98, y=440)

        # yes or no 선택
        self.sp = ['No', 'Yes']
        self.selc_period = ttk.Combobox(self.window, state='readonly', values=self.sp, width=7)
        self.selc_period.current(0)
        self.selc_period.place(x=103, y=460)

        # year선택, month선택, day선택
        select_year = list(range(1990, dt.now().year + 1))
        select_month = list(range(1, 13))
        select_day = list(range(1, 32))
        select_month2 = list(range(1, dt.now().month + 1))
        select_day2 = list(range(1, dt.now().day + 1))

        # 시작 기간 선택
        start_period = Label(self.window, text='기간 시작', width=7, bg='white', font=('나눔고딕', 8))
        start_period.place(x=185, y=440)
        self.com_p_year1 = ttk.Combobox(self.window, state='readonly', values=select_year, width=5)
        self.com_p_year1.current(0)
        self.com_p_year1.place(x=190, y=460)
        self.com_p_year1.set('년')
        self.com_p_month1 = ttk.Combobox(self.window, state='readonly', values=select_month, width=5)
        self.com_p_month1.current(0)
        self.com_p_month1.place(x=255, y=460)
        self.com_p_month1.set('월')
        self.com_p_day1 = ttk.Combobox(self.window, state='readonly', values=select_day, width=5)
        self.com_p_day1.current(0)
        self.com_p_day1.place(x=320, y=460)
        self.com_p_day1.set('일')

        # 시작과 끝 기간 구분자
        seperator2 = Label(self.window, text='-', width=1, bg='white')
        seperator2.place(x=389, y=460)

        # 끝 기간 선택
        start_period = Label(self.window, text='기간 끝', width=5, bg='white', font=('나눔고딕', 8))
        start_period.place(x=406, y=440)
        self.com_p_year2 = ttk.Combobox(self.window, state='readonly', values=select_year, width=5)
        self.com_p_year2.current(0)
        self.com_p_year2.place(x=409, y=460)
        self.com_p_year2.set('년')
        self.com_p_month2 = ttk.Combobox(self.window, state='readonly', values=select_month2, width=5)
        self.com_p_month2.current(0)
        self.com_p_month2.place(x=474, y=460)
        self.com_p_month2.set('월')
        self.com_p_day2 = ttk.Combobox(self.window, state='readonly', values=select_day2, width=5)
        self.com_p_day2.current(0)
        self.com_p_day2.place(x=539, y=460)
        self.com_p_day2.set('일')

        self.date_get()

        # ----------------- DB 저장 타입 설정 --------------------------------------------
        DB1 = Button(self.window, text='로컬 저장', bg='white', width=16, borderwidth=0.5, command=self.con1)
        DB1.place(x=103, y=505)

        DB2 = Button(self.window, text='DB 저장', bg='white', width=16, borderwidth=0.5, command=self.con2)
        DB2.place(x=228, y=505)

        DB3 = Button(self.window, text='둘 다 저장', bg='white', width=16, borderwidth=0.5, command=self.con3)
        DB3.place(x=353, y=505)

        DB4 = Button(self.window, text='닫기', bg='white', width=16, borderwidth=0.5, command=self.con4)
        DB4.place(x=478, y=505)


        self.window.mainloop()

        return self.search_word, self.date_get, self.type



if __name__ == '__main__':

    # 윈도우1 창생성
    window1 = Window1()
    window1.get_search_window1()



