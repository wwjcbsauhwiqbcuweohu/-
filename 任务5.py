import random
player = input("请输入要出的选项:剪刀(4)/石头(0)/布(2)/蜥蜴(3)/史博克(1)")
if player.isdigit() and int(player) >= 1 and int(player) <= 5:
    player = int(player)
com = random.randint(1, 5)
if player == 4:
    player1 = "剪刀"
if player == 0:
    player1 = "石头"
if player == 2:
    player1 = "布"
if player == 3:
    player1 = "蜥蜴"
if player == 1:
    player1 = "史博克"
if com == 4:
    com1 = "剪刀"
if com == 0:
    com1 = "石头"
if com == 2:
    com1 = "布"
if com == 3:
    com1 = "蜥蜴"
if com == 1:
    com1 = "史博克"
print("您出拳为:", player, "机器出拳为:", com)
#
if (player == 0 and com == 3 or com == 4) \
or (player == 1 and com == 0 or com == 4) \
or (player == 2 and com == 0 or com == 1) \
or (player == 3 and com == 1 or com == 2) \
or (player == 4 and com == 2 or com == 3):
    print("您胜利")
elif (player == 3 or player == 4 and com == 0) \
or (player == 0 or player == 4 and com == 1) \
or (player == 0 or player == 1 and com == 2) \
or (player == 1 or player == 2 and com == 3) \
or (player == 2 or player == 3 and com == 4):
    print("机器胜利")
elif (player == 0 and com == 0) \
or (player == 1 and com == 1) \
or (player == 2 and com == 2) \
or (player == 3 and com == 3) \
or (player == 4 and com == 4):
    print("平局")
else:
    print("出拳有误")
