from lib.game import Lesson1Game


def answer_what_is_your_name():
    return "Zi"

def answer_x_plus_y(x, y):
    return x + y

def answer_draw_a_pyramid(level):
    return []

game = Lesson1Game(
        lecture1_challenge1_solution=answer_what_is_your_name,
        lecture1_challenge2_solution=answer_x_plus_y,
        lecture1_homework1_solution=answer_draw_a_pyramid,
        )
game.start()
