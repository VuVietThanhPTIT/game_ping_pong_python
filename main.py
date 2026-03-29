import pygame
import define 
from player import Player
from ball import Ball

pygame.init()


screen = pygame.display.set_mode((define.window_width, define.window_height))
#set title
pygame.display.set_caption("Game pingpong")

# set icon of game 
img = pygame.image.load('D:asset\image\Table-tennis_35746.png')
pygame.display.set_icon(img) 

# set font
score_font = pygame.font.SysFont("comisans" , 50)
#set color
window_color = define.color_black
# change the window 
screen.fill(window_color)

# init player 
player_left = Player(0, (define.window_height - define.player_height) / 2 , define.color_red)
player_right = Player( define.window_width - define.player_width ,(define.window_height - define.player_height     ) / 2  , define.color_blue )
ball = Ball(define.window_width / 2 , define.window_height/ 2 , define.color_yellow,        define.ball_size  , define.ball_velocity , 0 )


def reset_ball(direction):
    ball.x = define.window_width / 2
    ball.y = define.window_height / 2
    ball.vy = 0
    ball.vx = abs(define.ball_velocity) * direction

def keyboard_input():
    global window_color  , running 
     #catch the button 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
                # checking if key "A" was pressed
                if event.key == pygame.K_UP:
                    player_right.move_up()
                if event.key == pygame.K_DOWN:
                    player_right.move_down()

                if event.key == pygame.K_s:
                    player_left.move_down()
                if event.key == pygame.K_w:
                    player_left.move_up()
                

def handle_collision( ):
    if ball.y - ball.radius <= 0 :
        # xử lý khi va chạm bên trên thành trên
        ball.vy *= -1
    if ball.y + ball.radius >= define.window_height:
        ball.vy *= -1 
        # xử lý khi va chạm bên trên thành dưới
    if ball.vx >= 0 and ball.x + ball.radius >= define.window_width - define.player_width:
        # cham nguoi choi ben phai
        
        # người chơi viết từ điểm y đến y + height
       
     
        if ball.y + ball.radius > player_right.y and  ball.y + ball.radius <=  player_right.y + define.player_height // 2:
            ball.vy -=  0.05
            ball.vx *= -1 
        elif ball.y + ball.radius >=  player_right.y + define.player_height // 2 and  ball.y + ball.radius <=  player_right.y + define.player_height: 
            ball.vy +=  0.05
            ball.vx *= -1 
        
    if ball.vx < 0 and ball.x - ball.radius <=  define.player_width:
        # cham nguoi choi ben trai
        
        if ball.y + ball.radius > player_left.y and  ball.y + ball.radius <=  player_left.y + define.player_height // 2:
            ball.vy -=  0.05
            ball.vx *= -1 
        elif ball.y + ball.radius >=  player_left.y + define.player_height // 2 and  ball.y + ball.radius <=  player_left.y + define.player_height: 
            ball.vy +=  0.05
            ball.vx *= -1  
        
running = True
def main():    
    
    left_score = 0 
    right_score = 0 
    
    while running:
        
        screen.fill(window_color)
        # draw a line 
        pygame.draw.line(screen, define.color_white, ( define.window_width / 2  , 0 ), (  define.window_width / 2,  define.window_height ), width= define.line_width)
        
        left_score_text  = score_font.render(f"{left_score}", True, define.color_white)
        right_score_text  = score_font.render(f"{right_score}", True, define.color_white)
        screen.blit(left_score_text , (define.window_width//4 -left_score_text.get_width() , 20))
        screen.blit(right_score_text , (define.window_width* 0.75 -right_score_text.get_width() , 20))

        # show player 
        player_left.show(  screen )
        player_right.show( screen)
        ball.show(screen)
        keyboard_input()
        ball.move()

        # Score ngay khi bong ra khoi man hinh va reset ve giua
        if ball.x + ball.radius < 0:
            right_score += 1
            reset_ball(direction=1)
            continue
        if ball.x - ball.radius > define.window_width:
            left_score += 1
            reset_ball(direction=-1)
            continue

        handle_collision()
        # update the display 
        pygame.display.update()
            
    pygame.quit()

if __name__ == '__main__':
    main()