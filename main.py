#Barbaric approach at /r/place timelapese program using pygame for visualization

import pygame, sys

#I could've put everything into a single list, but idk, this feels cleaner
time = []
coord = []
color = []
color_list = [
    (255, 255, 255),
    (228, 228, 228),
    (136, 136, 136),
    (34, 34, 34),
    (255, 167, 209),
    (229, 0, 0),
    (229, 149, 0),
    (160, 106, 66),
    (229, 217, 0),
    (148, 224, 68),
    (2, 190, 1),
    (0, 229, 240),
    (0, 131, 199),
    (0, 0, 234),
    (224, 74, 255),
    (130, 0, 128),
    ]

running = True
length = 0
speed = 10000
current_time = 0

#Loading the file and seperating it into different lists
path = "data/place.csv"
with open(path) as f:
    content = f.readlines()
    for x in content:
        temp = x.strip() #remove unnecessary things from string
        temp = temp.split(",") #seperate the string by ","
        #Adding the seperated string into the lists
        time.append(int(temp[0]))
        coord.append((int(temp[1]), int(temp[2])))
        color.append(int(temp[3]))
        length += 1

#Pygame initialisation stuff
pygame.init()
window = pygame.display.set_mode((1200,1000))
pygame.display.set_caption("/r/place")
font = pygame.font.SysFont('Arial', 30)
pygame.key.set_repeat(1,1)

#Function for writing text on screen
def text(string, coords):
    string = str(string) + "          "
    temp = font.render(string, True, (0,0,0), (255,255,255))
    window.blit(temp, coords)

#Fill the screen with white once at start
window.fill((255, 255, 255))

#Recalculates frame, insanely slow, probably going to add some key frames
def recalculate():
    window.fill((255, 255, 255))
    for i in range(0, current_time):
        window.set_at(coord[i], color_list[color[i]])

#Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_PLUS: speed += 2
            if event.key == pygame.K_KP_MINUS: speed -= 2
            if event.key == pygame.K_KP1: speed = 1000
            if event.key == pygame.K_KP2: speed = 20000
            if event.key == pygame.K_KP0: #Resets to zero
                current_time = 0
                recalculate()
            if event.key == pygame.K_LEFT: #If you go backwards it has to recalculate everything
                current_time -= speed
                if current_time < 0: current_time = 0
                recalculate()
            if event.key == pygame.K_RIGHT: #Going forwards
                current_time += speed
                if current_time > length: current_time = length
                for i in range(current_time - speed, current_time):
                    window.set_at(coord[i], color_list[color[i]])

    text("Time:", (1020,20))
    text(current_time, (1020,60))
    text("Speed:", (1020, 120))
    text(speed, (1020, 160))

    pygame.display.update()