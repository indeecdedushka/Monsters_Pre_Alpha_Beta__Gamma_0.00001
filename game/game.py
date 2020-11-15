from PyQt5 import  QtWidgets,QtGui
import time,sys
from random import *
#приложение
app = QtWidgets.QApplication(sys.argv)
ico = QtGui.QIcon("icon.JPG")
app.setWindowIcon(ico)
#окно
window = QtWidgets.QWidget()
window.setWindowTitle("Monsters!Monsters!")
window.resize(800,600)
#меню
grid = QtWidgets.QGridLayout()
start = QtWidgets.QPushButton('УБИВАТЬ УБИВАТЬ УБИВАТЬ')
ex = QtWidgets.QPushButton('Выход')
grid.addWidget(start,0,0)
grid.addWidget(ex,1,0)
window.setLayout(grid)
#Проброс
a = [0,0,0]
for i in range(3):
    a[i] = randint(1,6)+randint(1,6)+randint(1,6)
#переход к игровому окну
def prep():
    #смена
    global ex
    global start
    global grid
    ex.setHidden(True)
    start.setHidden(True)
    grid.removeWidget(ex)
    grid.removeWidget(start)
    #Проброс
    seq = ['Хлынов','Хлебов','Глобов','Жлобов','Рома Желудь',
           'Глобекс','Глайдер','Глыба','Глоб','Глоба','Глеб',
           'Глеба','Глобула','Весьма глобально','Глобалист',
           'Глобальное потепление','Марк Глебов','Хлеб','ГЛОНАСС',
           'Глютен','Проглоб','Протопоп А(вакуум)','Гемоглобин',
           'Горбачев','Глобешник','Глобус','Глыбень','Иммуноглобулин',
           'Бычий цепень','Свиной ебень']
    #Характеристики
    global a
    strength = QtWidgets.QLabel('Сила:'+str(a[0]))
    con = QtWidgets.QLabel('Телосложение:'+str(a[1]))
    dex = QtWidgets.QLabel('Ловкость:'+str(a[2]))
    name = QtWidgets.QLabel('Имя:'+choice(seq))
    race = QtWidgets.QLabel('''Раса: кряква
Расовая способность: может плавать на поверхности воды
даже в доспехах, утиный акцент не позволяет остальным нормально
понимать вас. Ничего из этого не пригодится в подземелье.''')
    char = QtWidgets.QLabel()
    char.setPixmap(QtGui.QPixmap("start1.jpg"))
    #Контейнеры слева
    box = QtWidgets.QGroupBox('Инфо')
    vbox = QtWidgets.QVBoxLayout()
    vbox.addWidget(name)
    vbox.addWidget(race)
    vbox.addWidget(char)
    vbox.addWidget(strength)
    vbox.addWidget(con)
    vbox.addWidget(dex)
    box.setLayout(vbox)
    grid.addWidget(box,0,0)
    # Контейнеры справа
    attack = QtWidgets.QPushButton('Атака')
    defence = QtWidgets.QPushButton('Защита')
    text = QtWidgets.QLabel(' Добро пожаловать в подземелье')
    grid.addWidget(text,0,1)
    grid.addWidget(attack, 1, 1)
    grid.addWidget(defence, 2, 1)
#заставка
splash = QtWidgets.QSplashScreen(QtGui.QPixmap("splash.jpg"))
splash.show()
time.sleep(0.6)
splash.deleteLater()
#запуск
ex.clicked.connect(app.quit)
start.clicked.connect(prep)
window.show()
sys.exit(app.exec_())