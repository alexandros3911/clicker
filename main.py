#pgzero

#more [...]
WIDTH = 500 # Ширина окна
HEIGHT = 500 # Высота окна
TITLE = "clicer infineti" # Заголовок окна игры
FPS = 90 # Количество кадров в секунду
count = 0
price3 = 90

#Объекты
wing = Actor('wing', size=(90,90), center=(250,300))
bonus  = Actor('gas',   center=(270,80))


#Отрисовка объектов
def draw():
    screen.fill((32, 197, 777))
    wing.draw()
    bonus .draw()
    screen.draw.text(count, center=(150, 300), color="white", fontsize = 50)
    if count > -1 and count < 100:
        screen.draw.text("noob", center=(250, 200), color="white", fontsize = 50)
    if count > 99 and count < 300:
        screen.draw.text("pro", center=(250, 200), color="white", fontsize = 50)
    if count > 299 and count < 600:
        screen.draw.text("cheeter", center=(250, 200), color="white", fontsize = 50)
    if count > 599 and count < 120000:
        screen.draw.text("god", center=(250, 200), color="white", fontsize = 50)
    if count > 110099:
        screen.draw.text("master clicer", center=(150, 200), color="white", fontsize = 50)
    screen.draw.text("bonus /", center=(250, 80), color="white", fontsize = 50)
    screen.draw.text(price3, center=(390, 80), color="black", fontsize = 50)
        
#for bonuse
def for_bonus_2():
    global count
    count += 5  

    
 #Функция обработки кликов   
def on_mouse_down(button, pos):
    global count, price3
    if button == mouse.LEFT and wing.collidepoint(pos):
        count = count + 1
    elif  button == mouse.LEFT and bonus.collidepoint(pos):
            if count >= price3:
                schedule_interval(for_bonus_2, 1)
                count -= price3
                price3 *= 2
