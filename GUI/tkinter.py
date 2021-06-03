from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msgbox
from PIL import Image
import os
from datetime import datetime as dt
import time

# 두번째화면에서 워드클라우드
# 뒤로가기 버튼
# DB창


# 필요 실행 함수 #
def start_window4():
    window3.destroy()

    window4 = Tk()

    # window4  title지정
    window4.title('More Inforamtion2')

    # window4 크기 조절   / 편의상 고정하겠음
    window_width = '320'
    window_height = '130'
    window_size = window_width + 'x' + window_height
    window4.geometry(window_size)  # 크기도 일단 임의 선택, 후에 변경 가능
    window4.resizable(False, False)  # 일단 락걸어둠, 필요시 변경

    DB_QUESTION = Label(window4, text='DB를 선택해주세요.', font=('나눔고딕', 15))
    DB_QUESTION.place(x=20, y=30)

    # 확인버튼 입력하는 경우 윈도우 3번째 창 꺼짐, 4번째 창 켜짐
    def con1():
        print('db')

    def con2():
        print('local')

    def con3():
        print('both')

    def con4():
        msgbox.showinfo('알림', '종료합니다')
        window4.destroy()

    DB1 = Button(window4, text='로컬 저장', command=con1)
    DB1.place(x=20, y=70)

    DB2 = Button(window4, text='DB 저장', command=con2)
    DB2.place(x=100, y=70)

    DB3 = Button(window4, text='둘 다 저장', command=con3)
    DB3.place(x=180, y=70)

    DB4 = Button(window4, text='닫기', command=con4)
    DB4.place(x=260, y=70)

    window4.mainloop()

def start_window3():
    global window3

    # 2번째 창 삭제
    window2.destroy()

    # 3번쨰 창 띄우기
    window3 = Tk()

    # window3  title지정
    window3.title('More Inforamtion1')
    #
    # window3 크기 조절   / 편의상 고정하겠음
    window_width = '770'
    window_height = '180'
    window_size = window_width + 'x' + window_height
    window3.geometry(window_size)  # 크기도 일단 임의 선택, 후에 변경 가능
    window3.resizable(False, False)  # 일단 락걸어둠, 필요시 변경

    # ------------------------------------------------------------------------------------------------------#
    # 기간설정 질문
    DATE_QUESTION = Label(window3, text='기간을 입력해주세요.', font=('나눔고딕', 15))
    DATE_QUESTION.place(x=20, y=30)

    # 검색기간 선택
    frame_option = LabelFrame(window3, bg='white', borderwidth=0.1)
    frame_option.place(x=10, y=70, width=660, height=50)

    # 기간선택 여부
    select_period = Label(frame_option, text='기간선택', width=7, bg='white')
    select_period.pack(side='left', padx=5, pady=5)

    # 기간선택 박스
    select_option1 = ['안함', '선택']
    cmb_option1 = ttk.Combobox(frame_option, state='readonly', values=select_option1, width=6)
    cmb_option1.current(0)
    cmb_option1.pack(side='left', padx=5, pady=5)

    # year선택, month선택, day선택
    select_year = list(range(1990, dt.now().year + 1))
    select_month = list(range(1, 13))
    select_day = list(range(1, 32))
    # select_month2 = list(range(1, dt.now().month + 1))
    # select_day2 = list(range(1, dt.now().day + 1))

    seperator = Label(frame_option, font=('나눔고딕', 10), text=' 시작-끝 ', width=5, bg='white')
    seperator.pack(side='left', padx=5, pady=5)

    # # 시작 기간 선택
    start_period = Label(frame_option, text='기간 시작', width=8)
    start_period.place(x=500, y=500)
    com_p_year1 = ttk.Combobox(frame_option, state='readonly', values=select_year, width=5)
    com_p_year1.current(0)
    com_p_year1.pack(side='left', padx=5, pady=5)
    com_p_year1.set('년')
    com_p_month1 = ttk.Combobox(frame_option, state='readonly', values=select_month, width=5)
    com_p_month1.current(0)
    com_p_month1.pack(side='left', padx=5, pady=5)
    com_p_month1.set('월')
    com_p_day1 = ttk.Combobox(frame_option, state='readonly', values=select_day, width=5)
    com_p_day1.current(0)
    com_p_day1.pack(side='left', padx=5, pady=5)
    com_p_day1.set('일')

    # 시작과 끝 기간 구분자
    seperator2 = Label(frame_option, text='-', width=2, bg='white')
    seperator2.pack(side='left', padx=5, pady=5)

    # 끝 기간 선택
    com_p_year2 = ttk.Combobox(frame_option, state='readonly', values=select_year, width=5)
    com_p_year2.current(0)
    com_p_year2.pack(side='left', padx=5, pady=5)
    com_p_year2.set('년')
    com_p_month2 = ttk.Combobox(frame_option, state='readonly', values=select_month, width=5)
    com_p_month2.current(0)
    com_p_month2.pack(side='left', padx=5, pady=5)
    com_p_month2.set('월')
    com_p_day2 = ttk.Combobox(frame_option, state='readonly', values=select_day, width=5)
    com_p_day2.current(0)
    com_p_day2.pack(side='left', padx=5, pady=5)
    com_p_day2.set('일')

    confirm = Button(window3, text='확인', command=start_window4)
    confirm.place(x=680, y=120)

    close_window = Button(window3, text='닫기', command=window3.destroy)
    close_window.place(x=720, y=120)
    # # ------------------------------------------------------------------------------------------------------#
    window3.mainloop()

def start_window2() :
    window1.destroy()

    # 두 번째 윈도우 창
    global window2
    window2 = Tk()

    # window2 이름
    window2.title('Encore team1')

    # window2 크기 및 조절불가 설정
    window2.geometry('1000x640')
    window2.resizable(False, False)

    # window2 전체 배경화면 지정(흰 배경)
    photo2 = PhotoImage(file='whitebackground.png')
    label2 = Label(window2, image=photo2)
    label2.place(x=0, y=0)

    # window2 좌측 위에 로고
    photo3 = PhotoImage(file='pic1.png')
    label3 = Label(window2, image=photo3, borderwidth=0)
    label3.place(x=10, y=10)

    # 현재 검색어 표시
    sw1 = Label(window2, text='검색어', width=5, bg='white', font=('나눔고딕', 13))
    sw1.place(x=30, y=70)
    sw2 = Label(window2, text=search_word, width=30, bg='white', font=('나눔고딕', 13))
    sw2.place(x=100, y=70)

    # 추가정보 여부 확인하기
    pluses = Label(window2, text='추가 정보를 원하십니까?', font=('나눔고딕', 13), bg='white')
    pluses.place(x=30, y=400)


    def plno():
        msgbox.showinfo('알림', '종료합니다')
        window2.destroy()

    btn_yes = Button(window2, text='예', font=('나눔고딕', 13), bg='white', width=5, command=start_window3)
    btn_yes.place(x=220, y=395)
    btn_no = Button(window2, text='아니오', font=('나눔고딕', 13), bg='white', width=5, command=plno)
    btn_no.place(x=290, y=395)


    # ----- DB 창 설정 시작 ---------------------------------------------------------------------
    # 프레임 생성
    top_frame = Frame(window2)
    top_frame.place(x=35, y=110)  # 표 위치 임의로 설정

    # 컬럼 설정
    tree = ttk.Treeview(top_frame, columns=(0, 1, 2, 3), show='headings')
    tree.pack(side='left')

    # 컬럼명
    tree.heading(0, text='ID')
    tree.heading(1, text='Search')
    tree.heading(2, text='Date')
    tree.heading(3, text='ImageURL')

    # 컬럼 높이, 너비 설정
    tree.column(0, width=100)
    tree.column(1, width=200)
    tree.column(2, width=200)
    tree.column(3, width=300)

    # 스크롤바 설정 (https://myinbox.tistory.com/154)

    scroll = ttk.Scrollbar(top_frame, orient='vertical', command=tree.yview)
    scroll.pack(side='right', fill='y')
    tree.configure(yscrollcommand=scroll.set)

    ### 데이터 입력 - DB 연결
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
            [2, '아이패드', '2021-06-02-2021-06-02', ['www.naver.com', 'www.google.com']]]

    for i in data:
        tree.insert('', 'end', values=(i[0], i[1], i[2], i[3]))

    window2.mainloop()


    # def click_data(event):
    #     selected = tree.focus()
    #     getval = tree.item(selected).get('values')
    #     print('아이디는', getval[0])
    #
    #     tree.bind('<ButtonRelease-1>', click_data)




# --------------------------- 윈도우 창1 --------------------------- #
window1 = Tk()
# window1 이름
window1.title('Encore team1')

# window1 크기 및 조절불가 설정
window1.geometry('1000x640')
window1.resizable(False,False)

# window1 전체 배경화면 지정
photo1 = PhotoImage(file='teamwork2.png')
label1 = Label(window1, image=photo1)
label1.place(x=0, y=0)


# 검색어 입력받기
search_result = Entry(window1, width=100, font=('나눔고딕', 10), bg='white', borderwidth=1)
search_result.place(x=170, y=350, width=610, height=50)

def search_btn() :
    global search_word
    search_word = search_result.get()
    print(search_word)
    start_window2()

# 검색 버튼 띄우기
btn_search = Button(window1, font=('나눔고딕', 10), text='검색', command=search_btn)
btn_search.place(x=780, y=350, width=50, height=50)

window1.mainloop()