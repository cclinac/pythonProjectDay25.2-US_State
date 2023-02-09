import turtle
import pandas

the_screen = turtle.Screen()
the_screen.title("US State Game")
image = "blank_states_img.gif"
the_screen.addshape(image)
background = turtle.Turtle()
background.shape(image)
data = pandas.read_csv("50_states.csv")
the_pen = turtle.Turtle()

guessed_state = []
state_list = data["state"].to_list()
learning_state = []
is_exit = False
while len(guessed_state) < 50 and not is_exit:
    answer_state = the_screen.textinput(title=f"Guess the State ({len(guessed_state)}/50)",
                                        prompt="What's another state's name?").title()
    if answer_state == "Exit":
        for i in state_list:
            if i not in guessed_state:
                learning_state.append(i)
        new_data = pandas.DataFrame(learning_state)
        new_data.to_csv("pandas_learning.csv")
        is_exit = True

    if (answer_state in state_list) and (answer_state not in guessed_state):
        # print("OK")
        guessed_state.append(answer_state)
        the_pen.penup()
        position = (int(data[data.state == answer_state]['x']), int(data[data.state == answer_state]['y']))
        the_pen.goto(position)
        the_pen.write(answer_state)

the_pen.goto(0, 0)
the_pen.write("Click to Exit")
the_screen.exitonclick()
