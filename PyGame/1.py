import pygame

pygame.init() #инициализация игры

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

dis = pygame.display.set_mode((800, 500)) #создание экрана, ширина 800, высота 500
pygame.display.set_caption("Snake") #создание названия игры, отражается сверху

game_over = False #указатель на окончание игры

x1 = 300 #координаты где будет стоять точка при запуске
y1 = 400

x1_change = 0
y1_change = 0

clock =pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN: #кнопка вниз
            if event.key == pygame.K_LEFT: #кнопка влево
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT: #кнопка вправо
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    if x1>=800 or x1<0 or y1>=600 or y1<0: #завершение игры, если точка дойдет до конца экрана
        game_over = True

    x1+=x1_change
    y1+=y1_change
    dis.fill(white) #закрашивание экрана в белый

    pygame.draw.rect(dis, blue, [x1,y1,10,10]) #рисуем змейку
    pygame.display.update() #

    clock.tick(30)

pygame = quit()
quit()
