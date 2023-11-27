import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
correct = 0
guessed_states = []
missing_states = []
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

while correct < 50:
    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        missed_states = pandas.DataFrame(missing_states)
        missed_states.to_csv("states_you_missed.csv")
        break
    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        cor = data[data.state == answer_state]
        t.goto(int(cor.x), int(cor.y))
        t.write(answer_state)
        correct += 1
    answer_state = screen.textinput(title=f"{correct}/50 States Correct", prompt="What's another state's name?").title()
