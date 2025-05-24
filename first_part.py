from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLabel, QVBoxLayout

with open("file_for_zapis.txt", "w", encoding="UTF-8") as file:
    file.write("")
app = QApplication([])

window = QWidget()
window.setWindowTitle('История')
window.resize(1300, 800)

label = QLabel("Вы родились в деревне ")



v = QVBoxLayout()
v.addWidget(label)
window.setLayout(v)
died = False


def vvod(vopros_text, my_text, zapis = False):
    global died
    if not died:
        vvod_name, ok = QInputDialog.getText(window, "Вопрос", vopros_text)
        if ok and vvod_name != '':
            label.setText(label.text() + vvod_name + my_text)
        if zapis:
            with open("file_for_zapis.txt", "a", encoding="UTF-8") as file:
                file.write(vvod_name + "\n")


def variants(variants_text,variants, posledstviya, my_text, zapis = False):
    global died
    if not died:
        vvod_name, ok = QInputDialog.getText(window, "Вопрос", variants_text)
        if ok and vvod_name != '':
            find = False
            for i in range(len(variants)):
                if variants[i] == vvod_name:
                    find = True
                    if posledstviya[i] == 'смерть':
                        died = True
                        label.setText(label.text() + 'Вы умерли')
                    elif posledstviya[i] == '+20 монет':
                        label.setText(label.text() + vvod_name + " вы получаете 20 монет ")
                        with open("file_for_zapis.txt", "a", encoding="UTF-8") as file:
                            file.write('+20 монет' + "\n")
                    elif posledstviya[i] == 'свиток':
                        label.setText(label.text() + vvod_name + " вы получаете свиток с ледяной стрелой")
                        with open("file_for_zapis.txt", "a", encoding="UTF-8") as file:
                            file.write('свиток' + "\n")
                    elif posledstviya[i] == 'ничего':
                        with open("file_for_zapis.txt", "a", encoding="UTF-8") as file:
                            file.write('ничего' + "\n")
                    else:
                        label.setText(label.text() + vvod_name + my_text)
            if not find:
                variants(variants_text,variants, posledstviya, my_text, zapis)
            if zapis == True:
                with open("file_for_zapis.txt", "a", encoding="UTF-8") as file:
                    file.write(vvod_name + "\n")

window.show()
vvod("Название деревни: ", " вокруг вас ходят люди и вы замечаете красивую женщину ")
vvod("Введите имя женщины: ", " это ваша мама,она обращается к вам ")
vvod("Ваше имя: ", ", после чего вас берут на руки и убаюкивают.Так проходят ваши первые дни жизни,в тишине и спокойствии. \nОднажды вы просыпаетесь от криков горожан,выглядывая в окно вы видите огромного дракона ", True)
vvod("Имя дракона: ", ", он ", True)
variants("Дракон: лазурный, огнедышащий, ледяной. Выберите и напишите вариант ответа", ['лазурный', "огнедышащий", "ледяной"], ["жизнь", "жизнь", "жизнь"], ", его огромный хвост ломает телеги ,а пасть съедает каждого прохожего,в ужасе вы хватаете ")
variants("Оружие: лук,меч,волшебная палочка. Выберите и напишите вариант ответа", ["лук", "меч", "волшебная палочка"], ["жизнь", "жизнь", "жизнь"], " и убегаете в", True)
variants("Куда? лес, пещера, замок. Выберите и напишите вариант ответа", ['лес', "пещера", "замок"], ["смерть", "смерть", "жизнь"], " пройдя 3 дня\nбез сна и покояъ вы подходите к воротам замка, стражник с верху открывает вам путь и вы заходите в замок, вам надо придумать что делать дальше ")
variants("Что делать? пойти устроиться в стражу, пойти на рынок, попытаться выкрасть оружие из оружейни", ["пойти устроиться в стражу", "пойти на рынок", "попытаться выкрасть оружие из оружейни"], ["смерть", "жизнь", "смерть"], " вы спрашиваете у прохожего как дойти до рынка и он показывает рукой\nкуда надо идти. На рынке вы осматриваете прилавки и видите как у одного торговца пытаются выкрасть товар ")
variants("Что будете делать? остановить воров,ничего не делать,подождать пока они украдут и украсть у них товар после", ['остановить воров','ничего не делать','подождать пока они украдут и украсть у них товар после'], ["+20 монет", "ничего", "свиток"], ",после инцидента вас подзывает торговец и предлагает товары ")
variants("Выберите товар: кожанная накидка, кристалл мощи, яд василиска в банке", ["кожанная накидка", "кристалл мощи", "яд василиска в банке"], ["жизнь", "жизнь", "жизнь"], " после покупки вы идете молиться в церковь", True)

app.exec_()