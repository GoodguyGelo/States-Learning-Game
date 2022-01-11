import turtle
import pandas
from state_creator import StatesCreator

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state = StatesCreator()

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
guesses = []
while len(guesses) < 50:
    answer_state = screen.textinput(title=f"Score: {state.score}/50", prompt="What is another state?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in states_list if state not in guesses]

        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer_state in guesses:
        game_is_on = False
    elif answer_state in states_list:
        chosen_state = data[data.state == answer_state]
        x_cor = int(chosen_state.x)
        y_cor = int(chosen_state.y)
        location = (x_cor, y_cor)
        state.write_state(answer_state, location)
        state.add_to_score()
        guesses.append(answer_state)

# will subtract the contents of one list to another



screen.exitonclick()
