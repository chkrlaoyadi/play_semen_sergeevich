from tkinter import *
from random import randint


root = Tk()
lab_xp_dragon = None
lab_xp_hero = None
num = None
zer = False
name_oryj = ''
dragon = ''
name = ''
rounds = 0
money = 0
bonys = ''
b = 0
b1 = 0
b2 = 0
b3 = 0
vibor = 0
vibor1 = 0
vibor2 = 0
vibor3 = 0
vibor4 = 0
var = 1
xp = 0
yr = 0
bron = 0
dragon_xp = 0
dragon_yr = 0
dragon_bron = 0
l = -1
perks = []
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0
g6 = 0
chet = 0
chet1 = 0
schet = 1
schet1 = 0
schet3 = 0
hod = True
n = 0

def j():
    global dragon_xp
    global dragon_bron
    global yr
    global num
    dragon_xp = dragon_xp - yr - dragon_bron
    g1.destroy()
    g2.destroy()
    g3.destroy()
    g4.destroy()
    g5.destroy()
    num.destroy()


def h():
    global xp
    global yr
    global dragon_yr
    global dragon_xp
    global dragon_bron
    global schet
    global schet1
    global schet3
    global num
    if vibor == 'перекат':
        xp += 50
        g1.destroy()
        g2.destroy()
        g3.destroy()
        g4.destroy()
        g5.destroy()
        num.destroy()
    elif vibor == 'умножение':
        if schet == 1:
            dragon_xp = dragon_xp - 3 * yr
            schet += 1
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor == 'блок':
        if schet1 < 3:
            dragon_yr = 0
            schet1 += 1
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor == 'ярость':
        if schet3 < 5:
            dragon_xp = dragon_xp - yr * 2 - dragon_bron
            schet3 += 1
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor == 'мантия неведимка':
        if schet1 < 3:
            dragon_yr = 0
            schet1 += 1
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor == 'живая вода':
        if schet3 < 5:
            xp += xp // 100 * 20
            schet3 += 1
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()


schet2 = 0
schet4 = 0
schet5 = 0


def h1():
    global xp
    global yr
    global dragon_yr
    global dragon_xp
    global schet2
    global schet4
    global schet5
    global dragon_bron
    global num
    if vibor1 == 'ветер':
        if schet2 < 4:
            dragon_xp = dragon_xp - yr
            schet2 += 1
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor1 == 'лёд':
        if schet4 < 4:
            schet4 += 1
            dragon_xp = dragon_xp - 60 - dragon_bron
            dragon_yr = dragon_yr // 2
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor1 == 'отражение':
        if schet5 < 2:
            schet5 += 1
            xp += dragon_yr
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor1 == 'рассечение':
        if schet2 < 3:
            schet2 += 1
            dragon_xp -= (yr + yr) - dragon_bron
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor1 == 'огненный шар':
        if schet2 < 3:
            dragon_xp -= 100
            schet2 += 1
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor1 == 'ледяные пики':
        if schet4 < 5:
            schet4 += 1
            dragon_xp -= 60
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()


schet6 = 0
schet7 = 0


def h2():
    global b
    global xp
    global yr
    global dragon_yr
    global dragon_xp
    global schet6
    global schet7
    global dragon_bron
    global num
    if vibor2 == 'шипы':
        if schet6 < 3:
            schet6 += 1
            yr += dragon_yr // 100 * 20
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor2 == 'уйти в тень':
        if schet7 < 5:
            schet7 += 1
            xp += 100
            dragon_xp += 20
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor2 == 'меч короля Артура':
        if schet6 < 1:
            schet6 += 1
            dragon_xp = dragon_xp - yr * 5 - dragon_bron
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor2 == 'святой меч':

        if schet7 < 1:
            schet7 += 1
            dragon_yr -= dragon_yr // 100 * 20
            dragon_bron -= dragon_bron // 100 * 40
            b = dragon_yr - dragon_yr // 100 * 20
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor2 == 'увядание':
        if schet6 < 4:
            schet6 += 1
            dragon_yr -= dragon_yr // 100 * 20
            dragon_bron -= dragon_bron // 100 * 20
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor2 == 'ослепление':
        if schet7 < 3:
            schet7 += 1
            dragon_bron = 0
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()


schet11 = 0
schet12 = 0


def h3():
    global b3
    global bron
    global xp
    global yr
    global dragon_yr
    global dragon_xp
    global schet11
    global schet12
    global dragon_bron
    global num
    if vibor3 == 'град стрел':
        if schet11 < 3:
            schet11 += 1
            dragon_xp = dragon_xp - yr * 5
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor3 == 'кислотный дождь':
        if schet12 < 10:
            schet12 += 1
            dragon_xp = dragon_xp - yr
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor3 == 'броня бога':
        bron = 30
        g1.destroy()
        g2.destroy()
        g3.destroy()
        g4.destroy()
        g5.destroy()
        num.destroy()
    elif vibor3 == 'аура света':
        if schet11 < 4:
            schet11 += 1
            xp += 70
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor3 == 'щит':
        if schet11 < 2:
            xp += 200
            schet11 += 1
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor3 == 'божья кара':
        if schet12 < 5:
            b3 = randint(20, 100)
            schet12 += 1
            dragon_xp = dragon_xp - b3
            g1.destroy()
            g2.destroy()
            g3.destroy()
            g4.destroy()
            g5.destroy()
            num.destroy()
    elif vibor3 == 'зеркало':
        global zer
        zer = True
        xp -= 100
        g1.destroy()
        g2.destroy()
        g3.destroy()
        g4.destroy()
        g5.destroy()
        num.destroy()

def d1():
    global xp
    global chet
    global bron
    global zer
    global hod
    global num
    if zer == False:

        xp -= 50 - bron
    else:
        global dragon_xp
        global dragon_bron
        dragon_xp -= 50 - dragon_bron

        zer = False
    chet += 1
    if chet % 3 == 0:
        hod = True
    dr1.destroy()
    dr2.destroy()
    dr3.destroy()
    dr4.destroy()
    dr5.destroy()
    num.destroy()


def d2():
    global dragon_yr
    global chet
    global hod
    global num
    chet += 1
    if chet % 3 == 0:
        hod = True
    dragon_yr += 5
    dr1.destroy()
    dr2.destroy()
    dr3.destroy()
    dr4.destroy()
    dr5.destroy()
    num.destroy()


def d3():
    global dragon_bron
    global chet
    global hod
    global num
    chet += 1
    if chet % 3 == 0:
        hod = True
    dragon_bron += 5
    dr1.destroy()
    dr2.destroy()
    dr3.destroy()
    dr4.destroy()
    dr5.destroy()
    num.destroy()


def d4():
    global dragon_xp
    global chet
    global chet1
    global hod
    global num
    if chet1 <= 3:
        chet1 += 1
        dragon_xp += 100
    chet += 1
    if chet % 3 == 0:
        hod = True
    dr1.destroy()
    dr2.destroy()
    dr3.destroy()
    dr4.destroy()
    dr5.destroy()
    num.destroy()


def d5():
    global xp
    global bron
    global chet
    global hod
    global num
    chet += 1
    if chet % 3 == 0:
        hod = True
    if hod:
        if zer == False:
            xp -= 40 - bron
        else:
            global dragon_bron
            global dragon_xp
            dragon_xp -= 40 - dragon_bron
        dr1.destroy()
        dr2.destroy()
        dr3.destroy()
        dr4.destroy()
        dr5.destroy()
        num.destroy()
        hod = False


def g():
    global xp
    global yr
    global name
    global l
    global dragon
    global dragon_xp
    global dragon_yr
    global dragon_bron
    global name_oryj
    global money
    global bonys
    global vibor
    global vibor1
    global vibor2
    global vibor3
    global vibor4
    global perks
    global b
    with open("file_for_zapis.txt", "r", encoding="UTF-8") as file:
        stroke = 1
        for line in file:
            if line == "+20 монет\n":
                money = 20
            if stroke == 1:
                name = line
            elif stroke == 2:
                dragon = line
            elif stroke == 3:
                name_oryj = line
            elif stroke == 5:
                bonys = line
            stroke += 1
        vibor = randint(1, 2)
        vibor1 = randint(3, 4)
        vibor2 = randint(5, 6)
        vibor3 = randint(7, 8)
        vibor4 = randint(9, 10)

        if name_oryj == 'лук':
            if vibor == 1:
                vibor = 'перекат'
            elif vibor == 2:
                vibor = 'ускорение'
            if vibor1 == 3:
                vibor1 = 'ветер'
            elif vibor1 == 4:
                vibor1 = 'лед'
            if vibor2 == 5:
                vibor2 = 'шипы'
            elif vibor2 == 6:
                vibor2 = 'уйти в тень'
            if vibor3 == 7:
                vibor3 = 'кислотный дождь'
            elif vibor3 == 8:
                vibor3 = 'град стрел'
            if vibor4 == 9:
                yr += yr // 100 * 20
            elif vibor4 == 10:
                xp += 100
        else:
            if name_oryj == 'меч':
                if vibor == 1:
                    vibor = 'блок'
                elif vibor == 2:
                    vibor = 'ярость'
                if vibor1 == 3:
                    vibor1 = 'отражение'
                elif vibor1 == 4:
                    vibor1 = 'рассечение'
                if vibor2 == 5:
                    vibor2 = 'меч короля Артура'
                elif vibor2 == 6:
                    vibor2 = 'святой меч'
                if vibor3 == 7:
                    vibor3 = 'броня бога'
                elif vibor3 == 8:
                    vibor3 = 'аура света'
                if vibor4 == 9:
                    xp += xp // 100 * 50
                elif vibor4 == 10:
                    xp += xp // 100 * 5
                    yr += yr // 100 * 20
            else:
                if vibor == 1:
                    vibor = 'мантия неведимка'
                elif vibor == 2:
                    vibor = 'живая вода'
                if vibor1 == 3:
                    vibor1 = 'огненный шар'
                elif vibor1 == 4:
                    vibor1 = 'ледяные пики'
                if vibor2 == 5:
                    vibor2 = 'увядание'
                elif vibor2 == 6:
                    vibor2 = 'ослепление'
                if vibor3 == 7:
                    vibor3 = 'щит'
                elif vibor3 == 8:
                    vibor3 = 'зеркало'
                if vibor4 == 9:
                    xp += 40
                elif vibor4 == 10:
                    yr += 20




    if dragon == 'лазурный\n':
        dragon_xp = 1000
        dragon_yr = 30
        dragon_bron = 20
        b = dragon_yr
        b2 = dragon_bron
    elif dragon == 'ледяной\n':
        dragon_xp = 800
        dragon_yr = 50
        dragon_bron = 10
        b = dragon_yr
        b2 = dragon_bron
    else:
        dragon_xp = 900
        dragon_yr = 40
        dragon_bron = 15
        b2 = dragon_bron
        b = dragon_yr
    h = ''


def t():
    global var
    var += 1
    text['text'] = 'вы спите несколько часов и после идёте дальше'
    r.destroy()
    r1.destroy()
    r2.destroy()


def osnov():
    global b
    global b1
    global name_oryj
    global var
    global money
    global r
    global r1
    global r2
    global bonys
    global xp
    global yr
    global bron
    global dragon_xp
    global lab_xp_dragon
    global lab_xp_hero
    global rounds
    if var == 1:
        text['text'] = 'после молитвы вы понимаете что вам негде переночевать, куда вы отправитесь ,'
        r = Checkbutton(text='в монастырь', command=t)
        r1 = Checkbutton(text='на улицу', command=t)
        r.pack()
        r1.pack()
        r2 = Checkbutton(text='')
        if money == 20:
            r2 = Checkbutton(text='напроситесь переночевать(-20мон)', command=t)
            r2.pack()
    elif var == 2:
        text['text'] = 'идя по улицам вы заходите в училище,молодой учитель берёт вас под своё крыло'
        var += 1
    elif var == 3:
        text['text'] = 'После чего вы отправляетесь на расспределение  по классам'
        global name_oryj
        if name_oryj == 'лук':
            xp = 300
            yr = 80
            b1 = yr
            if bonys == 'яд василиска в банке':
                yr += 40
        elif name_oryj == 'меч':
            xp = 500
            yr = 40
            b1 = yr
            if bonys == 'кристалл мощи':
                yr += 40
        else:
            xp = 400
            yr = 60
            b1 = yr
            if bonys == 'кожанная накидка':
                bron += 20
        var += 1
    elif var == 4:
        text['text'] = 'спустя долгые 5 лет обучения вас выпускают с новыми знаниями'
        var += 1
    elif var == 5:
        text[
            'text'] = 'теперь вы готовы ко всему(как вам кажется),осталось лишь найти дракона и заставить его заплатить за свои деяния'
        var += 1
    elif var == 6:
        text['text'] = 'Вы решаете пойти в деревню'
        var += 1
    elif var == 7:
        text['text'] = 'пройдя несколько дней вы замечаете знакомые дома'
        var += 1
    elif var == 8:
        text['text'] = 'жители радостно кричат увидев вас'
        var += 1
    elif var == 9:
        text['text'] = 'От жителей вы узнаёте что дракон давно покинул эти края'
        var += 1
    elif var == 10:
        text['text'] = 'тут вы слышите грохот и туча стрел падает у ваших ног'
        var += 1
    elif var == 11:
        text['text'] = 'шайка бандитов видна на горизонте'
        var += 1
    elif var == 12:
        text['text'] = 'вы без особого труда побеждаете их'
        var += 1
    elif var == 13:
        text['text'] = 'осмотрев их трупы и сумки вы находите карту'
        var += 1
    elif var == 14:
        text['text'] = 'на ней чётко показанна пещера ,где и обитает дракон'
        var += 1
    elif var == 15:
        text['text'] = 'уже поздно и вы решаете поспать и на утро пойти в путь'
        var += 1
    elif var == 16:
        text['text'] = 'зайдя в какой - то домик вы ложитесь на кровать и засыпаете'
        var += 1
    elif var == 17:
        text['text'] = 'проспав 8 , а то и 10 часов вы просыпаетесь'
        var += 1
    elif var == 18:
        text['text'] = 'полные решимости вы идёте по карте'
        var += 1
    elif var == 19:
        text['text'] = 'пройдя несколько дней вы видите пещеру '
        var += 1
    elif var == 20:
        text['text'] = 'А вот и он'
        var += 1
    elif var == 21:
        text['text'] = 'вы слышите только одно'
        var += 1
    elif var == 22:
        text['text'] = 'я ждал тебя'
        var += 1
    elif var == 23:
        global name

        text['text'] = name
        var += 1
        lab_xp_dragon = Label(text = "Хп дракона: " + str(dragon_xp))
        lab_xp_dragon.pack()
        lab_xp_hero = Label(text = "Ваше хп: " + str(xp))
        lab_xp_hero.pack()
    elif var == 24:
        global dragon
        global dragon_yr
        global dragon_bron
        global g1
        global g2
        global g3
        global g4
        global g5
        global dr1
        global dr2
        global dr3
        global dr4
        global dr5
        global n
        global num
        n += 1
        if xp > 0 and dragon_xp > 0:
            if rounds % 2 == 0:
                dragon_yr = b
                dragon_bron = b2
                g1 = Button(text='обычная атака', command=j)
                g2 = Button(text=vibor, command=h)
                g3 = Button(text=vibor1, command=h1)
                g4 = Button(text=vibor2, command=h2)
                g5 = Button(text=vibor3, command=h3)
                num = Label(text="Ход номер: "+ str(n))
                lab_xp_hero['text'] = "Хп героя: " + str(xp)
                lab_xp_dragon['text'] = "Хп дракона: " + str(dragon_xp)
                g1.pack()
                g2.pack()
                g3.pack()
                g4.pack()
                g5.pack()
                num.pack()
            else:

                dr1 = Button(text='удар когтями', command=d1)
                dr2 = Button(text='рёв', command=d2)
                dr3 = Button(text='защита крыльями', command=d3)
                dr4 = Button(text='сон', command=d4)
                dr5 = Button(text='хвост-молот', command=d5)
                num = Label(text="Ход номер: " + str(n))
                lab_xp_hero['text'] = "Хп героя: " + str(xp)
                lab_xp_dragon['text'] = "Хп дракона: " + str(dragon_xp)
                dr1.pack()
                dr2.pack()
                dr3.pack()
                dr4.pack()
                dr5.pack()
                num.pack()

                yr = b1

        if xp <= 0:
            text['text'] = 'вы погибли'
        if dragon_xp <= 0:
            text['text'] = 'вы победили,на этом и закончилось ваше приключение'
        rounds += 1

g()
text = Button(text='нажмите чтобы начать', command=osnov)
text.pack()
root.mainloop()