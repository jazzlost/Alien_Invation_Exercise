import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # 飞船向右移动
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 飞船向左移动
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # 飞船停止向右移动
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 飞船停止向左移动
        ship.moving_left = False

def check_events(setting, screen, ship, bullets):
    # 键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, setting, screen, ship, bullets)
                
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(settings, screen, ship, aliens, bullets):
    # 更新屏幕并绘制图形
    screen.fill(settings.bg_color)
    # 绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip()


def update_bullets(bullets):           
    # 更新子弹位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)


def fire_bullet(setting, screen, ship, bullets):
    # 创建一颗子弹并加入编组bullets
        if len(bullets) < setting.bullets_allowed:
            new_bullet = Bullet(setting, screen, ship)
            bullets.add(new_bullet)

        
def create_fleet(settings, screen, aliens):
    # 创建一个外星人， 并计算一行可容纳外星人数
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    # 创建第一行外星人
    for alien_number in range(number_aliens_x):
        # 创建一个外星人并加入当前行
        alien = Alien(settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)