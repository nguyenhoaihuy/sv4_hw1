from lib.game import Lesson1Game

###
# Thay doi ham sau de vuot qua thu thach dau tien
# Giup Trau tra loi cau hoi "What's your name?" cua Sieu May Tinh
###
def answer_what_is_your_name():
    return None

###
# Thay doi ham sau de vuot qua thu thach thu 2
# Giup Trau tra loi cau hoi "x + y = ?" cua Sieu May Tinh
###
def answer_x_plus_y(x, y):
    return 0

###
# Thay doi ham sau de vuot qua thu thach thu 3
# Giup Trau ve mot kim tu thap voi so tang bang
# voi bien level
###
def answer_draw_a_pyramid(level):
    return []

game = Lesson1Game(
        lecture1_challenge1_solution=answer_what_is_your_name,
        lecture1_challenge2_solution=answer_x_plus_y,
        lecture1_homework1_solution=answer_draw_a_pyramid,
        )
game.start()
