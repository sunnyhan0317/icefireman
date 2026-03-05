import pygame
import sys
import math

# 顏色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0,191,255)
SKYBLUE = (187,255,255)

# 寬度與長度
WIDTH = 400
HEIGHT = 400

# 遊戲初始化
pygame.init()

# 創建視窗
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 遊戲的標題
pygame.display.set_caption("My game")

# 遊戲迴圈
# 創建一個時鐘
clock = pygame.time.Clock()
while True:
    # 處理遊戲的幀數
    clock.tick(60)  
    # 取得使用者的所有輸入
    for event in pygame.event.get():
        # 當使用者按下關閉視窗，便退出遊戲
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 視窗顏色
    screen.fill(WHITE)

    # 臉
    pygame.draw.ellipse(screen, BLUE,[150, 200, 80, 90])
    pygame.draw.ellipse(screen, BLACK,[150, 200, 80, 90],3)

    # 眼睛(左)
    pygame.draw.ellipse(screen, SKYBLUE,[165, 227, 20, 30])
    pygame.draw.ellipse(screen, BLACK,[165, 227, 20, 30],3)
    pygame.draw.rect(screen,BLUE,[165,245,20,17])
    pygame.draw.line(screen, BLACK, (165,243), (185,243),3)
    pygame.draw.circle(screen, BLACK, (176,237), 2)

    # 眼睛(右)
    pygame.draw.ellipse(screen, SKYBLUE,[192, 227, 20, 30])
    pygame.draw.ellipse(screen, BLACK,[192, 227, 20, 30],3)
    pygame.draw.rect(screen,BLUE,[192,245,20,17])
    pygame.draw.line(screen, BLACK, (192,243), (210,243),3)
    pygame.draw.circle(screen, BLACK, (202,237), 2)

    # 嘴巴
    rect = pygame.Rect(182, 250, 18, 18)
    start_angle = 180
    end_angle = 0
    line_thickness = 2
    start_angle_rad = math.radians(start_angle)
    end_angle_rad = math.radians(end_angle)
    pygame.draw.arc(screen, BLACK, rect, start_angle_rad, end_angle_rad, line_thickness)


    #頭髮中間
    pygame.draw.circle(screen, BLUE, (190,194), 12)


    rect = pygame.Rect(175, 182, 33, 33)
    start_angle = 0
    end_angle = 180
    line_thickness = 2
    start_angle_rad = math.radians(start_angle)
    end_angle_rad = math.radians(end_angle)
    pygame.draw.arc(screen, BLACK, rect, start_angle_rad, end_angle_rad, line_thickness)

    



    #頭髮左上
    pygame.draw.circle(screen, BLUE, (168,206), 9)
    pygame.draw.circle(screen, BLUE, (163,210), 9)
    pygame.draw.circle(screen, BLUE, (175,207), 9)
    pygame.draw.circle(screen, BLUE, (168,206), 9)
    pygame.draw.circle(screen, BLUE, (175,205), 9)
    pygame.draw.circle(screen, BLUE, (173,205), 9)
    pygame.draw.circle(screen, BLUE, (163,210), 9)
    pygame.draw.circle(screen, BLUE, (162,205), 9)
    pygame.draw.circle(screen, BLUE, (156,207), 9)



    rect = pygame.Rect(145, 195, 45, 30)
    start_angle = 60
    end_angle = 195
    line_thickness = 2
    start_angle_rad = math.radians(start_angle)
    end_angle_rad = math.radians(end_angle)
    pygame.draw.arc(screen, BLACK, rect, start_angle_rad, end_angle_rad, line_thickness)


    #頭髮左下
    rect = pygame.Rect(145, 195, 45, 25)
    start_angle = 195
    end_angle = 420
    line_thickness = 2
    start_angle_rad = math.radians(start_angle)
    end_angle_rad = math.radians(end_angle)
    pygame.draw.arc(screen, BLACK, rect, start_angle_rad, end_angle_rad, line_thickness)


    #頭髮右上
    pygame.draw.circle(screen, BLUE, (200,205), 9)
    pygame.draw.circle(screen, BLUE, (205,208), 9)
    pygame.draw.circle(screen, BLUE, (213,215), 9)
    pygame.draw.circle(screen, BLUE, (205,203), 9)
    pygame.draw.circle(screen, BLUE, (209,204), 9)
    pygame.draw.circle(screen, BLUE, (213,207), 12)
    pygame.draw.circle(screen, BLUE, (220,205), 9)
    pygame.draw.circle(screen, BLUE, (225,210), 9)
    


    rect = pygame.Rect(185, 195, 53, 33)
    start_angle = -30
    end_angle = 150
    line_thickness = 2
    start_angle_rad = math.radians(start_angle)
    end_angle_rad = math.radians(end_angle)
    pygame.draw.arc(screen, BLACK, rect, start_angle_rad, end_angle_rad, line_thickness)

    #頭髮右下
    rect = pygame.Rect(185, 195, 53, 28)
    start_angle = 150
    end_angle = 330
    line_thickness = 2
    start_angle_rad = math.radians(start_angle)
    end_angle_rad = math.radians(end_angle)
    pygame.draw.arc(screen, BLACK, rect, start_angle_rad, end_angle_rad, line_thickness)

    
                                   
    pygame.display.update()
