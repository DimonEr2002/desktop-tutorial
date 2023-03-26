import pygame
import random
import ast
import time
pygame.init()

size = 1440,900
Screen = pygame.display.set_mode(size) # Для отображения окна
pygame.display.set_caption('Sudoku')

### Colors ###
Red = 255,0,0
Black = 0,0,0
Gray = 128, 128, 128
DarkGray = 169, 169, 169
DimGrey	= 105, 105, 105
Silver = 220, 220, 220
Silver1 = 180, 180, 180
White =	255, 255, 255
LightYellow	= 255, 255, 224
PeachPuff =	255, 218, 185
Orange = 255, 165, 0
Green = 0,255,0
Blue = 0,0,255
OrangeRed = 255, 69, 0
Cornsilk = 255, 248, 220
BlanchedAlmond = 255, 235, 205

def Check_MousePos(MP,Pos,S): # Функция проверяет находится ли курсор на нужных координатах
    if Pos[1]+S[1] >= MP[1] >= Pos[1] and Pos[0]+S[0] >= MP[0] >= Pos[0]:
        return True
def CheckPressed(Locate,Click,Check,i): # Функция проверяет нажатую клавишу, если клавиша нажата, возврощает определённое значение для следующих действий
    if Locate == 1: # От меню
        if Check == True and Click[0] == True:
            if i == (10, 10):
                return 1
            if i == (10,65):
                return 2
            if i == (10,120):
                return 3
            if i == (215,10):
                return 4
    if Locate == 2: # От кнопки возврата в меню и сохранения
        if Check == True and Click[0] == True:
            if i == (10, 840):
                return 1
            if i == (215, 840):
                return 2
    if Locate == 4: # От настроек
        if Check == True and Click[0] == True:
            if i == (300, 100):
                return 1
            if i == (500, 100):
                return 2
            if i == (700, 100):
                return 3
def Draw_menu(MP,Click): # Отображение экрана меню
    pygame.font.init()
    font = pygame.font.Font(None, 48)
    text = font.render("Sudoku", False,(Black))
    text1 = font.render("Settings", False, (Black))
    text2 = font.render("Exit", False, (Black))
    text3 = font.render("Load save", False, (Black))
    Pos = [(10, 10),(10, 65),(10, 120),(215,10)]
    TPos = [(15, 10), (15, 66), (15, 120),(217,10)]
    Bs = 200,50
    for i in Pos: # Цикл отображает кнопки и текст в меню так же отвечает за смену цвета на кнопках, когда курсор на кнопке
        color = DimGrey
        Check = Check_MousePos(MP,i,Bs) # Проверка положения курсора
        Com = CheckPressed(1,Click,Check,i) # Проверка нажатой клавиши
        if Check == True:
            color = Silver
        pygame.draw.rect(Screen,(color),((i),(Bs))) # Отрисовка кнопки
        # Отрисовка текста
        Screen.blit(text, (TPos[0]))
        Screen.blit(text1, (TPos[1]))
        Screen.blit(text2, (TPos[2]))
        Screen.blit(text3, (TPos[3]))
        if Com == 1 or Com == 2 or Com == 3 or Com == 4: # Возврат команды от нажатой кнопки, если кнопка нажата
            return Com
def Exit_B(MP,Click): # Отображение кнопок Menu и Save
    pygame.font.init()
    font1 = pygame.font.Font(None, 48)
    text = font1.render("Menu", False,(Black))
    text1 = font1.render("Save", False,(Black))
    Pos = [(10,size[1]-60),(215,size[1]-60)]
    TPos = [(15,size[1]-60),(220,size[1]-60)]
    Bs = 200,50
    for i in Pos:
        if Sudoku == True: # Если игра запущена отображает кнопку Save и Menu
            color = DimGrey
            Check = Check_MousePos(MP, i, Bs)
            Com = CheckPressed(2, Click, Check, i)
            if Check == True:
                color = Silver
            pygame.draw.rect(Screen,(color),((i),(Bs)))
            Screen.blit(text, (TPos[0]))
            Screen.blit(text1, (TPos[1]))
            if Com != None: # Возврощает команду если конпка была нажата
                return Com
        if Settings == True and i == Pos[0]: # Если запущены настройки отображает только одну кнопку
            color = DimGrey
            Check = Check_MousePos(MP, i, Bs)
            Com = CheckPressed(2, Click, Check, i)
            if Check == True:
                color = Silver
            pygame.draw.rect(Screen, (color), ((i), (Bs)))
            Screen.blit(text, (TPos[0]))
            if Com != None: # Возврощает команду если конпка была нажата
                return Com
def Sudoku_draw(MP,Click): # отрисовка игрового поля и вычисление координат игрового поля
    global Selected,SelN
    Rect_pos = [(360,100),(357,97)] # Координаты начальной точки
    Rect_Size = [(720,720),(725,725)] # Размер игрового поля
    pygame.draw.rect(Screen, (Black), ((Rect_pos[1]), (Rect_Size[1])))  # Отрисовка контура игрового поля
    pygame.draw.rect(Screen,(Silver), ((Rect_pos[0]),(Rect_Size[0]))) # Отрисовка самого игрового поля
    Cx = 0
    Cy = 0
    X = []
    Y = []
    XY = []
    for x in range(359,1081,80): # Вычисляет Х от 359 до 1081 с шагом 80
        Cx += 1
        if Cx == 4 or Cx == 7:
            pygame.draw.line(Screen, (Black), (x, 99), (x, 820),3) # Отрисовка Вертикальных линий на игровом поле
        pygame.draw.line(Screen, (Black), (x, 99), (x, 820)) # Отрисовка Вертикальных линий на игровом поле
        if len(X) <= 8:
            X.append(x+11) # Сохранение Х в список
        for y in range(99,821,80): # Тоже самое что и для Х
            xy = x,y
            Cy += 1
            if Cy == 4 or Cy == 7:
                pygame.draw.line(Screen, (Black), (359, y), (1080, y),3) # Отрисовка горизонтальных линий на игровом поле
            pygame.draw.line(Screen,(Black),(359,y),(1080,y)) # Отрисовка горизонтальных линий на игровом поле
            if len(Y) <= 8:
                Y.append(y+11) # Сохранение Y в список
            if len(XY) <= 80 and not y == 819:
                xy1 = x,y
                XY.append(xy1) # Сохранение обоих координат в список
            js = 80,80
            Mop = Check_MousePos(MP,xy,js) # Проверка положеня курсора, для изменения цвета в клетке под курсором
            if Mop == True and xy[0] < 1001 and xy[1] <= 739:
                pygame.draw.rect(Screen, (Silver1), ((xy), (80,80)))
            if Mop == True and Click == (True,False,False): # Если кнопка нажата выделяет выделеную клетку
                X1 = xy[0]
                Y1 = xy[1]
                Selected = xy # Сохраняет координату выделеной клетки

    XY = XY,X,Y  # Возврощает координаты клеток в основной цикл
    return XY
def Numbers(X,Y,XY): # Эта функция генерирует числа в клетках используя сложность игры
    global dif,I
    for i in range(dif):
        Rand = random.randint(0, 80) # Случайно генерирует числа которые будут скрыты
        if not Rand in I:
            I.append(Rand) # Сохраняет скрытые числа
    Col = [(1, 4, 7, 2, 5, 8, 3, 6, 9), # Игровая сетка до перестановки чисел случайным образом
           (2, 5, 8, 3, 6, 9, 4, 7, 1),
           (3, 6, 9, 4, 7, 1, 5, 8, 2),
           (4, 7, 1, 5, 8, 2, 6, 9, 3),
           (5, 8, 2, 6, 9, 3, 7, 1, 4),
           (6, 9, 3, 7, 1, 4, 8, 2, 5),
           (7, 1, 4, 8, 2, 5, 9, 3, 6),
           (8, 2, 5, 9, 3, 6, 1, 4, 7),
           (9, 3, 6, 1, 4, 7, 2, 5, 8)]

    def dif1(dif): # функция случайно перемешивает числа в сетке
        for i in range(dif):
            i = random.randint(0, 8)
            i1 = random.randint(0, 8)
            Col[i], Col[i1] = Col[i1], Col[i]
        return Col # Выдаёт перемешенную сетку
    Col = dif1(dif)
    def Rajc(Col): # Находит значения всех районов сетки
        Raj = [] # используется для проверки сетки на одинаковые числа
        R = []
        for i in range(9):
            for c in Col:
                if i in [0, 3, 6]:
                    c = c[0:3]
                    for k in c:
                        R.append(k)
                        if len(R) == 9:
                            Raj.append(tuple(R))
                            R = []
                            break
        return Raj # Выдаёт значения районов сетки
    Raj = Rajc(Col)
    H = True
    while H: # Проверяет наличие одинаковых чисел в районе, если есть одинаковые числа, то снова перемешивает числа до момента пока в во всех районах числа не будут повторяться
        o = 0
        for i in range(9):
            L = Raj[i]
            for j in L:
                ii = L.count(j)
                if ii >= 2:
                    Col = dif1(dif)
                    Raj = Rajc(Col)
                if ii == 1:
                    o += 1
        if o == 81:
            break

    num = [] # используется для записи всех чисел в один список
    for c in Col:
        for i in range(9):
            num.append(c[i])
    xyc = [] # Используется за записи всех чисел с координатами клеток игрового поля
    for i in XY:
        for n in num:
            XYC = i,n # Присваивает числам сетки координату по порядку
            xyc.append(XYC)
            ni = num.index(n)
            del num[ni] # Удаляет числа которые уже записаны с координатой
            break
    return xyc # Возврощает числа с координатой
def Set(MP,Click): # Отображает окно настроек
    global dif
    Rect_pos = [(300, 100),(500,100),(700,100),(100,100)]
    Rect_Size = 200, 55
    for i in Rect_pos: # Отображает кнопки
        MC = Check_MousePos(MP,i,Rect_Size)
        if MC == True:
            pygame.draw.rect(Screen, (Silver), ((90,90), (815,75)))
    for i in Rect_pos[0:3]:
        MC = Check_MousePos(MP, i, Rect_Size) # Проверка положения курсора
        if MC == True and Click == (True,False,False):
            Com = CheckPressed(4,Click,MC,i) # Проверка нажатой клавиши мыши, проверяет кнопки изменения сложности игры
            if Com == 1:
                dif = dif_min
            if Com == 2:
                dif = Defualt_dif
            if Com == 3:
                dif = dif_max
    #### Отображает текст в окне настроек ####
    Text11 = 'Current difficult - '+str(dif)
    font = pygame.font.SysFont('serif', 48)
    text = font.render('difficult', False, (Black))
    Screen.blit(text, (100, 100))
    font = pygame.font.SysFont('serif', 48)
    text = font.render(Text11, False, (Black))
    Screen.blit(text, (400, 40))
    pygame.draw.rect(Screen, (LightYellow), ((Rect_pos[0]), (Rect_Size)))
    pygame.draw.rect(Screen, (Orange), ((Rect_pos[1]), (Rect_Size)))
    pygame.draw.rect(Screen, (Red), ((Rect_pos[2]), (Rect_Size)))
    font = pygame.font.SysFont('serif', 48)
    text = font.render('Easy', False, (Black))
    Screen.blit(text, (310, 100))
    font = pygame.font.SysFont('serif', 48)
    text = font.render('Medium', False, (Black))
    Screen.blit(text, (510, 100))
    font = pygame.font.SysFont('serif', 48)
    text = font.render('Hard', False, (Black))
    Screen.blit(text, (710, 100))
    ############################################
def Win(): # Отображает надписть "Victory# когда игрок все сделал верно, завершает игру
    x = 650
    y = 40
    font = pygame.font.SysFont('serif', 48)
    text = font.render('Victory', False, (Red))
    Screen.blit(text, (x , y))
    return True
def Save(I, UI, DIF, NUM): # Сохранение
    try:
        f = open('Save.txt','w') # Открывает файл "save.txt"
    except IOError:
        f = open('Save.txt', 'w+') # Если файл не был найден, то создаёт его и открывает

    #### Меняет тип основных переменных в строки и записывает в список ####
    I = str(I)+'\n'
    UI = str(UI)+'\n'
    DIF = str(DIF)+'\n'
    NUM = str(NUM)+'\n'
    SaveData = [I, UI, DIF, NUM]
    ###################################
    for i in SaveData: # Сохраняет по одному элементу списка
        f.write(i)
    f.close() # Закрывает файл
def LoadSave(): # Загрузка сохранений
    Load = [] # В эту переменную будут записаны сохранённые данные
    try:
        f = open('Save.txt', 'r') # открывает файл сохранения
    except IOError:
        return # Если файл отсутствует, ничего не делает
    for i in range(4): # Выводит данные из файла по одной строчке и сохраняет в переменную
        L = f.readline()
        L = ast.literal_eval(L) # Делает из строки список
        Load.append(L)
    return Load # Возврощает данные из сохранения
#### Переменные для отображения того или иного окна ####
Menu = True
Sudoku = False
Settings = False
########################################
Main = True # Основной цикл
number = False # Для одноразовой генерации чисел
Mouse_press = (False,False,False)  # Кнопки мыши (ЛКМ, ПКМ, СКМ)
#### Сложность игры ####
dif = 80
dif_min = 50
Defualt_dif = 80
dif_max = 150
########################
Selected = 0 # В этой переменно будут храниться выделенные игроком клетки
SelN = 0
Num = []
I = [] # Для хранения индексов скрытых чисел
UserInput = [] # Числа которые ввёл игрок
TrueInput = [] # Верные числа которые ввёл игрок
keys = [49,50,51,52,53,54,55,56,57, # Keys 1-9
    1073741913,1073741914,1073741915,1073741916,1073741917,1073741918,1073741919,1073741920,1073741921] # keys NUM 1-9
while Main: # Основной цикл
    Input = 0 # Число которое вводит игрок (0 - для того что бы старое число не сохранилось)
    Nums = [] # Временно сохраняет координаты без чисел (Нужен для отображения выделеной клетки)
    Com = None # Принимает команду от функции CheckPressed()
    Screen.fill((DarkGray)) # Отображает фон окна
    events = pygame.event.get() # Действия игрока
    Mouse_pos = pygame.mouse.get_pos() # Координаты курсора
    for event in events: # Проверка действий игрока
        if event.type == pygame.KEYDOWN: # Проверка нажатую кнопку на клавиатуре
            key = event.key # Кнопка которая была нажата игроком
            #### Сравнение нажатой кнопки с кнопками в списке ###
            if key in keys:
                if key == 49 or key == 1073741913:
                    Input = 1
                if key == 50 or key == 1073741914:
                    Input = 2
                if key == 51 or key == 1073741915:
                    Input = 3
                if key == 52 or key == 1073741916:
                    Input = 4
                if key == 53 or key == 1073741917:
                    Input = 5
                if key == 54 or key == 1073741918:
                    Input = 6
                if key == 55 or key == 1073741919:
                    Input = 7
                if key == 56 or key == 1073741920:
                    Input = 8
                if key == 57 or key == 1073741921:
                    Input = 9
                ################################
        if event.type == pygame.MOUSEBUTTONDOWN: # Проверка нажатой кнопки мыши
            Mouse_press = pygame.mouse.get_pressed() # Нажатая кнопка мыши
        if event.type == pygame.QUIT: # Проверка выхода из игры (Нажатый крестик на самом окне игры)
            Sudoku = False
            Menu = False
            Settings = False
            Main = False

    if Menu == True: # Отображение меню игры
        #### Обнулить данные игры ####
        I = []
        TrueInput = []
        UserInput = []
        ##############
        Com = Draw_menu(Mouse_pos,Mouse_press) # Вызов функции отображения меню
        if Com == 1: # Запускает игру если была нажата кнопка "Судоку" и закрывает меню, так же включает случайную генерацию чисел
            Menu = False
            Sudoku = True
            number = True
        if Com == 2: # Запускает настройки если была нажата кнопка "Настройки" и закрывает меню
            Menu = False
            Settings = True
        if Com == 3: # Кнопка выхода из игры
            Main = False
        if Com == 4: # Кнопка загрузки данных из сохранения
            LoadData = LoadSave()
            if LoadData != None: # Если данных нету ничего не делает
                #### Присваивает переменным сохранённые значения ####
                I = LoadData[0]
                UserInput = LoadData[1]
                dif = LoadData[2]
                Num = LoadData[3]
                ####################
                #### Запускает игру ####
                Menu = False
                Sudoku = True
                number = False
                ##############
        Mouse_press = (False, False, False) # Скидывает нажатую кнопку мыши на не нажатую кнопку
    elif Menu == False: # Включает кнопки сохранения и выхода в меню
        Com = Exit_B(Mouse_pos,Mouse_press)
        if Com == 1: # Если нажата кнопка выхода в меню, выключает игру и открывает меню
            Menu = True
            Sudoku = False
            Settings = False
        if Com == 2 and Sudoku == True: # Если нажата кнопка сохранения, сохраняет данные с помощью функции Save()
            Save(I, UserInput, dif, Num)

    if Settings == True: # Открывает настройки
        seting = Set(Mouse_pos,Mouse_press)

    if Sudoku == True: # Запускает игру
        XY = Sudoku_draw(Mouse_pos,Mouse_press) # Отображает игровое поле и получает координаты игрового поля
        X = XY[1]
        Y = XY[2]
        XY = XY[0]
        if number == True:
            Num = Numbers(X,Y,XY) # Генерирует сетку чисел и закрывается, что бы числа не были сгенерированы повторно. Выдаёт координату и число
            number = False
        for i in Num: # Берет по одной координате с числом
            xy = i[0]
            n = i[1]
            ii = Num.index(i) # Узнаёт индекс числа
            if not ii in I: # Проверяет нужно ли отображать текущее число
                font = pygame.font.SysFont('serif', 48)
                text = font.render(str(n), False, (Black)) # Отображение текущего числа
                x = xy[0]
                y = xy[1]
                Screen.blit(text, (x+26,y+18))
                xy = x, y
                Nums.append(xy) # Добавляет координату числа для проверки выделеной клетки
        if Selected != 0: # Проверяет есть ли выделеная клетка
            if not Selected in Nums: # Проверяет, не совпадает ли выделеная клетка с координатой числа
                pygame.draw.rect(Screen, (Silver1), ((Selected), (80, 80))) # Отображает выделеную клетку
                if not Input == 0: # Проверяет, ввёл ли игрок число
                    User = Selected,Input # Присваивает числу игрока координату выделеной клетки
                    UserInput.append(User) # Сохраняет число игрока в список
                    for i in UserInput: # Проверяет поменял ли игрок число в этой же клетке, если поменял, удаляет старое число
                        ii = UserInput.index(i)
                        Sel = i[0]
                        inp = i[1]
                        IS = Sel,inp
                        if Sel == Selected and inp != Input:
                            UserInput.remove(IS)

        for u in UserInput: # Отображает число игрока
            xy1 = u[0]
            x,y = xy1
            n1 = u[1]
            font = pygame.font.SysFont('serif', 48)
            text = font.render(str(n1), False, (Red))
            Screen.blit(text, (x+26,y+18))
            if u in Num: # Сравнивает число игрока с верным числом
                if not u in TrueInput: # Если число верное, добавляет его в список верных чисел
                    TrueInput.append(u)
                if len(TrueInput) == len(I): # Если все числа введены верно, вызывает функцию Win()
                    Settings = False
                    Sudoku = False
                    Menu = Win()
                    pygame.display.update() # Обновляет экран что бы появилась надпись "Победа"
                    time.sleep(2) # Задерживает цикл на 2 секунды


    Mouse_press = (False, False, False) # Скидывает нажатыве кнопки мыши
    pygame.init()
    pygame.display.flip() # Обновляет экран для отображения новых данных

pygame.quit()