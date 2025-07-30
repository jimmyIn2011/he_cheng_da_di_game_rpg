import pygame as pg
import random as rd


def move(arr):
    k = []
    for sb in arr:
        if sb != 0:
            k.append(sb)
    while len(k) < 4:
        k.append(0)
    for sb in [0, 1, 2]:
        if k[sb] == k[sb + 1] and k[sb] != 0:
            k[sb] *= 2
            k[sb + 1] = 0
    jj = []
    for sb in k:
        if sb != 0:
            jj.append(sb)
    while len(jj) < 4:
        jj.append(0)
    k = jj
    for sb in [0, 1, 2]:
        if k[sb] == k[sb + 1] and k[sb] != 0:
            k[sb] *= 2
            k[sb + 1] = 0
    jj = []
    for sb in k:
        if sb != 0:
            jj.append(sb)
    while len(jj) < 4:
        jj.append(0)
    k = jj
    for sb in [0, 1, 2]:
        if k[sb] == k[sb + 1] and k[sb] != 0:
            k[sb] *= 2
            k[sb + 1] = 0
    jj = []
    for sb in k:
        if sb != 0:
            jj.append(sb)
    while len(jj) < 4:
        jj.append(0)
    k = jj
    for sb in [0, 1, 2]:
        if k[sb] == k[sb + 1] and k[sb] != 0:
            k[sb] *= 2
            k[sb + 1] = 0
    return k


def gen_jj(num):
    if num == 2:
        return "练气"
    elif num == 4:
        return "筑基"
    elif num == 8:
        return "金丹"
    elif num == 16:
        return "元婴"
    elif num == 32:
        return "化神"
    elif num == 64:
        return "炼虚"
    elif num == 128:
        return "仙王"
    elif num == 256:
        return "仙皇"
    elif num == 512:
        return "仙尊"
    elif num == 1024:
        return "仙圣"
    else:
        return "仙帝"


pg.init()
pg.display.init()
screen = pg.display.set_mode([800, 800])
pg.display.set_caption("合成大帝")
# 境界：练气、筑基、金丹、元婴、化神、炼虚、仙王、仙皇、仙尊、仙圣、仙帝
board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
dest_board = [[40, 40], [40, 40 + 190], [40, 40 + 190 * 2], [40, 40 + 190 * 3], [40 + 190, 40], [40 + 190, 40 + 190],
              [40 + 190, 40 + 190 * 2],
              [40 + 190, 40 + 190 * 3], [40 + 190 * 2, 40], [40 + 190 * 2, 40 + 190 * 1], [40 + 190 * 2, 40 + 190 * 2],
              [40 + 190 * 2, 40 + 190 * 3],
              [40 + 190 * 3, 40], [40 + 190 * 3, 40 + 190], [40 + 190 * 3, 40 + 190 * 2], [40 + 190 * 3, 40 + 190 * 3]]
k1 = rd.choice([0, 1, 2, 3])
k2 = rd.choice([0, 1, 2, 3])
board[k1][k2] = 2
startbtn = pg.Rect(250, 400, 300, 62)
scene = 2
running = True
tm = 0
win = False
while running:
    screen.fill([221, 169, 98])
    tm += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if scene == 2:
            if startbtn.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN:
                scene = 1
                win = False
        if scene == 3:
            if startbtn.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN:
                scene = 2
        if scene == 1:
            # 先移后并
            if pg.key.get_pressed()[pg.K_w] or pg.key.get_pressed()[pg.K_UP]:
                w1 = move([board[0][0], board[1][0], board[2][0], board[3][0]])
                board[0][0] = w1[0]
                board[1][0] = w1[1]
                board[2][0] = w1[2]
                board[3][0] = w1[3]
                w1 = move([board[0][1], board[1][1], board[2][1], board[3][1]])
                board[0][1] = w1[0]
                board[1][1] = w1[1]
                board[2][1] = w1[2]
                board[3][1] = w1[3]
                w1 = move([board[0][2], board[1][2], board[2][2], board[3][2]])
                board[0][2] = w1[0]
                board[1][2] = w1[1]
                board[2][2] = w1[2]
                board[3][2] = w1[3]
                w1 = move([board[0][3], board[1][3], board[2][3], board[3][3]])
                board[0][3] = w1[0]
                board[1][3] = w1[1]
                board[2][3] = w1[2]
                board[3][3] = w1[3]
                if tm >= 90:
                    tm = 0
                    k1 = rd.choice([0, 1, 2, 3])
                    k2 = rd.choice([0, 1, 2, 3])
                    js = 0
                    while board[k1][k2] != 0:
                        k1 = rd.choice([0, 1, 2, 3])
                        k2 = rd.choice([0, 1, 2, 3])
                        js += 1
                        if js >= 1000000000:
                            win = False
                            scene = 3
                    board[k1][k2] = rd.choice([2, 2, 2, 2, 4, 4, 8])
            elif pg.key.get_pressed()[pg.K_s] or pg.key.get_pressed()[pg.K_DOWN]:
                w1 = move([board[3][0], board[2][0], board[1][0], board[0][0]])
                board[0][0] = w1[3]
                board[1][0] = w1[2]
                board[2][0] = w1[1]
                board[3][0] = w1[0]
                w1 = move([board[3][1], board[2][1], board[1][1], board[0][1]])
                board[0][1] = w1[3]
                board[1][1] = w1[2]
                board[2][1] = w1[1]
                board[3][1] = w1[0]
                w1 = move([board[3][2], board[2][2], board[1][2], board[0][2]])
                board[0][2] = w1[3]
                board[1][2] = w1[2]
                board[2][2] = w1[1]
                board[3][2] = w1[0]
                w1 = move([board[3][3], board[2][3], board[1][3], board[0][3]])
                board[0][3] = w1[3]
                board[1][3] = w1[2]
                board[2][3] = w1[1]
                board[3][3] = w1[0]
                if tm >= 90:
                    tm = 0
                    js = 0
                    k1 = rd.choice([0, 1, 2, 3])
                    k2 = rd.choice([0, 1, 2, 3])
                    while board[k1][k2] != 0:
                        k1 = rd.choice([0, 1, 2, 3])
                        k2 = rd.choice([0, 1, 2, 3])
                        js += 1
                        if js >= 1000000000:
                            win = False
                            scene = 3
                    board[k1][k2] = rd.choice([2, 2, 2, 2, 4, 4, 8])
            elif pg.key.get_pressed()[pg.K_a] or pg.key.get_pressed()[pg.K_LEFT]:
                board[0] = move(board[0])
                board[1] = move(board[1])
                board[2] = move(board[2])
                board[3] = move(board[3])
                if tm >= 90:
                    tm = 0
                    k1 = rd.choice([0, 1, 2, 3])
                    k2 = rd.choice([0, 1, 2, 3])
                    js = 0
                    while board[k1][k2] != 0:
                        k1 = rd.choice([0, 1, 2, 3])
                        k2 = rd.choice([0, 1, 2, 3])
                        js += 1
                        if js >= 1000000000:
                            win = False
                            scene = 3
                    board[k1][k2] = rd.choice([2, 2, 2, 2, 4, 4, 8])
            elif pg.key.get_pressed()[pg.K_d] or pg.key.get_pressed()[pg.K_RIGHT]:
                w1 = move([board[0][3], board[0][2], board[0][1], board[0][0]])
                board[0][0] = w1[3]
                board[0][1] = w1[2]
                board[0][2] = w1[1]
                board[0][3] = w1[0]
                w1 = move([board[1][3], board[1][2], board[1][1], board[1][0]])
                board[1][0] = w1[3]
                board[1][1] = w1[2]
                board[1][2] = w1[1]
                board[1][3] = w1[0]
                w1 = move([board[2][3], board[2][2], board[2][1], board[2][0]])
                board[2][0] = w1[3]
                board[2][1] = w1[2]
                board[2][2] = w1[1]
                board[2][3] = w1[0]
                w1 = move([board[3][3], board[3][2], board[3][1], board[3][0]])
                board[3][0] = w1[3]
                board[3][1] = w1[2]
                board[3][2] = w1[1]
                board[3][3] = w1[0]
                if tm >= 90:
                    tm = 0
                    k1 = rd.choice([0, 1, 2, 3])
                    k2 = rd.choice([0, 1, 2, 3])
                    js = 0
                    while board[k1][k2] != 0:
                        k1 = rd.choice([0, 1, 2, 3])
                        k2 = rd.choice([0, 1, 2, 3])
                        js += 1
                        if js >= 1000000000:
                            win = False
                            scene = 3
                    board[k1][k2] = rd.choice([2, 2, 2, 2, 4, 4, 8])
    # (226, 234, 87)
    if scene == 1:
        for i in dest_board:
            pg.draw.rect(screen, (226, 234, 87), (i[0], i[1], 150, 150))
        for i in [0, 1, 2, 3]:
            for j in [0, 1, 2, 3]:
                if board[i][j] != 0:
                    screen.blit(pg.font.SysFont("华文楷体", 75).render(gen_jj(board[i][j]),
                                                                       True, [0, 0, 0]), dest_board[i + j * 4])
                if board[i][j] == 2048:
                    scene = 3
                    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
                    k1 = rd.choice([0, 1, 2, 3])
                    k2 = rd.choice([0, 1, 2, 3])
                    board[k1][k2] = 2
                    win = True
    else:
        pg.draw.rect(screen, [255, 0, 0], startbtn)
        screen.blit(pg.font.SysFont("华文楷体", 50).render("开始-合成大帝" if scene == 2 else "你%s了" %
                                                                                              (
                                                                                                  "赢" if win == True else "输"),
                                                           True, [0, 0, 0]), [250, 400])
    pg.display.flip()
pg.quit()
