# coding:utf-8
# Created by Equator at 2019/12/6
import pygame
import sys
import random
import math


def get_center_position(_x, _y, _width, _height):
    return _x + _width / 2, _y + _height / 2


def point_distance(p1, p2):
    return math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))


if __name__ == '__main__':
    pygame.init()
    color = (0, 0, 0)
    size = width, height = 640, 480
    screen = pygame.display.set_mode(size)
    screen_rect = screen.get_rect()

    robot = pygame.image.load('robot.png')
    robot_rect = robot.get_rect()
    robot_target_x = 0
    robot_target_y = 0
    robot_moving = False
    robot_speed = [5, 5]
    danger = False
    # 允许误差值
    robot_diff = 16
    trap = pygame.image.load('trap.png')
    trap_rect = trap.get_rect()
    # 初始化位置
    trap_rect.bottom = screen_rect.bottom
    trap_rect.right = screen_rect.right
    trap_moving = False
    trap_moving_counter = 0
    trap_speed = [3, 3]
    clock = pygame.time.Clock()
    while True:
        trap_moving_counter = trap_moving_counter + 1
        if trap_moving_counter % 360 == 0:
            trap_moving = not trap_moving
        clock.tick(60)
        # 当前圆心
        current_x, current_y = get_center_position(robot_rect.x, robot_rect.y, robot_rect.width, robot_rect.height)
        print("robot", robot_rect.x, robot_rect.y, robot_moving, danger, robot_speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                robot_target_x, robot_target_y = mouse_x, mouse_y
                print("click", mouse_x, mouse_y)
                robot_speed[0] = (mouse_x - current_x) / 50
                robot_speed[1] = (mouse_y - current_y) / 50
                robot_moving = True
        if robot_moving:
            robot_rect = robot_rect.move(robot_speed)
        if trap_moving:
            trap_rect = trap_rect.move(trap_speed)
        # 判断是否到达目标附近
        if not danger and robot_moving and abs(current_x - robot_target_x) <= robot_diff \
                and abs(current_y - robot_target_y) <= robot_diff:
            print("到达目标附近")
            robot_moving = False
        # 避开障碍物（陷阱）
        distance = point_distance(get_center_position(robot_rect.x, robot_rect.y, robot_rect.width, robot_rect.height),
                                  get_center_position(trap_rect.x, trap_rect.y, trap_rect.width, trap_rect.height))
        if distance <= 8 * robot_diff:
            print("碰撞", robot_moving, danger, robot_speed)
            if robot_moving:
                robot_speed[0] = random.randint(0, 10)
                robot_speed[1] = random.randint(0, 10)
            else:
                robot_moving = True
                danger = True
                robot_speed[0] = random.randint(0, 10)
                robot_speed[1] = random.randint(0, 10)
        else:
            danger = False
        # 越界检查
        if robot_rect.left < 0:
            robot_rect.left = 0
            robot_speed[0] = -trap_speed[0]
        if robot_rect.right > width:
            robot_rect.right = width
            robot_speed[0] = -trap_speed[0]
        if robot_rect.top < 0:
            robot_rect.top = 0
            robot_speed[1] = -trap_speed[1]
        if robot_rect.bottom > height:
            robot_rect.bottom = height
            robot_speed[1] = -trap_speed[1]
        if trap_rect.left < 0 or trap_rect.right > width:
            trap_speed[0] = -trap_speed[0]
        if trap_rect.top < 0 or trap_rect.bottom > height:
            trap_speed[1] = -trap_speed[1]
        screen.fill(color)
        screen.blit(robot, robot_rect)
        screen.blit(trap, trap_rect)
        pygame.display.flip()
    pygame.quit()
