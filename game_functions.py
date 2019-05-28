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

def update_aliens(settings, aliens):
    # 检查是否有外星人位于屏幕边缘，并调整位置
    check_fleet_edges(settings, aliens)
    # 更新所有外星人的位置
    aliens.update()
    

def fire_bullet(setting, screen, ship, bullets):
    # 创建一颗子弹并加入编组bullets
        if len(bullets) < setting.bullets_allowed:
            new_bullet = Bullet(setting, screen, ship)
            bullets.add(new_bullet)

        
def get_number_aliens_x(settings, alien_width):
    # 计算每行可容纳外星人数量
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(settings, ship_height, alien_height):
    # 计算屏幕能容纳多少行外星人
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(settings, screen, aliens, alien_number, row_number):
    # 创建一个外星人并放在当前行
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(settings, screen, ship, aliens):
    # 创建一个外星人， 并计算一行可容纳外星人数
    alien = Alien(settings, screen)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(settings, aliens):
    # 有外星人到达边缘时采取措施
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def change_fleet_direction(settings, aliens):
    # 将外星人群向下移动。并改变他们的方向
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1