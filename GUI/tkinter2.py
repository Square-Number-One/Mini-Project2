from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msgbox
from PIL import Image
import os
from datetime import datetime as dt
import time
from PIL import Image, ImageTk


def start_window1() :
    window = Tk()
    window.title('Encore Team 1')
    window.geometry('700x700')
    window.resizable(False, False)


    photo1 = PhotoImage(file='bgw.png')
    label1 = Label(window, image=photo1)
    label1.place(x=-2, y=0)

    photo2 = PhotoImage(file='teamwork2.png')
    label2 = Label(window, image=photo2, borderwidth=0)
    label2.place(x=-150, y=-50)

    # 검색어 입력받기
    search_result = Entry(window, width=100, font=('나눔고딕', 10), bg='white', borderwidth=1)
    search_result.place(x=90, y=330, width=480, height=40)

    def search_btn() :
        global search_word
        search_word = search_result.get()
        start_window2()
        # return search_word

    # 검색 버튼 띄우기
    btn_search = Button(window, font=('나눔고딕', 10), text='검색', command=search_btn)
    # command=lambda: [search_btn(), start_window2()])
    btn_search.place(x=570, y=329, width=50, height=41)


    # 추가정보 옵션 프레임
    photo3 = PhotoImage(file='boundary.png')
    label3 = Label(window, image=photo3, borderwidth=0)
    label3.place(x=89, y=400)

    frame_option = Label(window, text='[추가 정보 갱신을 원하시면 정보를 입력해주세요]', width=33, bg='white', font=('나눔고딕', 10))
    frame_option.place(x=101,y=409)


    # 기간 선택 여부
    period_yesno = Label(window, text='기간 선택 여부', width=10, bg='white', font=('나눔고딕', 8))
    period_yesno.place(x=98,y=440)

    # yes or no 선택
    sp = ['No', 'Yes']
    selc_period= ttk.Combobox(window, state='readonly', values=sp, width=7)
    selc_period.current(0)
    selc_period.place(x=103, y=460)

    # year선택, month선택, day선택
    select_year = list(range(1990, dt.now().year+1))
    select_month = list(range(1,13))
    select_day = list(range(1,32))
    select_month2= list(range(1,dt.now().month+1))
    select_day2 = list(range(1,dt.now().day+1))

    #시작 기간 선택
    start_period = Label(window, text='기간 시작', width=7, bg='white', font=('나눔고딕', 8))
    start_period.place(x=185,y=440)
    com_p_year1 = ttk.Combobox(window, state='readonly', values=select_year, width=5)
    com_p_year1.current(0)
    com_p_year1.place(x=190,y=460)
    com_p_year1.set('년')
    com_p_month1 = ttk.Combobox(window, state='readonly', values=select_month, width=5)
    com_p_month1.current(0)
    com_p_month1.place(x=255,y=460)
    com_p_month1.set('월')
    com_p_day1 = ttk.Combobox(window, state='readonly', values=select_day, width=5)
    com_p_day1.current(0)
    com_p_day1.place(x=320,y=460)
    com_p_day1.set('일')

    # 시작과 끝 기간 구분자
    seperator2 = Label(window, text='-', width=1, bg='white')
    seperator2.place(x=389,y=460)

    #끝 기간 선택
    start_period = Label(window, text='기간 끝', width=5, bg='white', font=('나눔고딕', 8))
    start_period.place(x=406,y=440)
    com_p_year2 = ttk.Combobox(window, state='readonly', values=select_year, width=5)
    com_p_year2.current(0)
    com_p_year2.place(x=409,y=460)
    com_p_year2.set('년')
    com_p_month2 = ttk.Combobox(window, state='readonly', values=select_month2, width=5)
    com_p_month2.current(0)
    com_p_month2.place(x=474,y=460)
    com_p_month2.set('월')
    com_p_day2 = ttk.Combobox(window, state='readonly', values=select_day2, width=5)
    com_p_day2.current(0)
    com_p_day2.place(x=539,y=460)
    com_p_day2.set('일')


    def con1():
        print('db')
        # 0 번 리턴

    def con2():
        print('local')
        # 1번 리턴

    def con3():
        print('both')
        # 2번 리턴

    def con4():
        msgbox.showinfo('알림', '종료합니다')
        window.destroy()


    DB1 = Button(window, text='로컬 저장', bg='white', width=16,  borderwidth=0.5,command=con1)
    DB1.place(x=103, y=505)

    DB2 = Button(window, text='DB 저장', bg='white', width=16, borderwidth=0.5,command=con2)
    DB2.place(x=228, y=505)

    DB3 = Button(window, text='둘 다 저장', bg='white', width=16, borderwidth=0.5, command=con3)
    DB3.place(x=353, y=505)

    DB4 = Button(window, text='닫기', bg='white', width=16, borderwidth=0.5,command=con4)
    DB4.place(x=478, y=505)


    window.mainloop()



def start_window2():

    window2 = Tk()
    window2.title('Encore Team 1')
    window2.geometry('700x800')
    window2.resizable(False, False)

    photo1 = PhotoImage(file='bgw.png')
    label1 = Label(window2, image=photo1)
    label1.place(x=0, y=0)

    photo2 = PhotoImage(file='pic1.png')
    label2 = Label(window2, image=photo2, borderwidth=0)
    label2.place(x=0, y=1.5)

    # 검색어 입력받기
    search_result = Entry(window2, width=100, font=('나눔고딕', 10), bg='white', borderwidth=1)
    search_result.place(x=190, y=20, width=370, height=33)

    def search_btn():
        global search_word
        search_word = search_result.get()
        print(search_word)
        return search_word

    # 검색 버튼 띄우기
    btn_search1 = Button(window2, font=('나눔고딕', 9), text='검색', command=search_btn)
    btn_search1.place(x=570, y=20, width=50, height=34)

    ##### 되돌리기 버튼 띄우기 (window1으로 연결)
    btn_search2 = Button(window2, font=('나눔고딕', 9), text='첫페이지', command=window2.destroy)
    btn_search2.place(x=630, y=20, width=50, height=34)

    ##### search_word 연결
    search_word = '사과'

    # 현재 검색어 표시
    sw1 = Label(window2, text='검색어', width=5, bg='white', font=('나눔고딕', 13))
    sw1.place(x=20, y=70)
    sw2 = Label(window2, text=search_word, width=3, fg='blue', bg='white' , font=('나눔고딕', 13))
    sw2.place(x=80, y=70)

    # ----- DB 창 설정 시작 ---------------------------------------------------------------------
    def data_input(search):
        data = [[1, '사과', '2019-03-01-2020-03-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']],
                [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']]]

        for i in data:
            tree.insert('', 'end', values=(i[0], i[1], i[2], i[3]))

    # 프레임 생성
    top_frame = Frame(window2)
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

    ### 데이터 입력 - DB 연결
    data_input(search_word)


    # ---------------------------------------------------------------------------------------

    # 워드클라우드 사진 올리기(resize 자유롭게 하기 위해 PIL-ImageTK사용)
    load = Image.open('cloud.png').resize((650, 300))
    image = ImageTk.PhotoImage(load)

    img = Label(window2, image=image, borderwidth=5)
    img.image = image
    img.place(x=24, y=450)


    window2.mainloop()


#
#
# def window_start_func() :
#     start_window1()
#     start_window2()


if __name__ == '__main__':
    # start_window1()
    start_window2()

