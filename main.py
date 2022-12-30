import turtle
import pandas
from tkinter import messagebox

# Creating a turtle screen and add blank states image
screen = turtle.Screen()
screen.setup(725, 491)
screen.title(f"THE U.S STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# TODO: Read in states csv. State Location and State Name
state_data = pandas.read_csv("50_states.csv")
state_names = state_data.state.to_list()
state_cor = list(zip(state_data.x, state_data.y))

# TODO: Check if the guess is among the 50 states
# TODO: Create a while loop
correct_guess = []
current_score = 0
while len(correct_guess) < 50:
    # TODO: Taking user guess
    answer = screen.textinput(title=f"{current_score}/50 States Correct",
                              prompt="What's another state's name?").title()

    if answer == "Exit":
        missed_states = [state for state in state_names if state not in correct_guess]
        missing_data = pandas.DataFrame(missed_states)
        missing_data.to_csv("states_to_learn.csv")
        break
    if answer in state_names and answer not in correct_guess:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        cor_state = state_data[state_data.state == f'{answer}']
        t.goto(int(cor_state.x), int(cor_state.y))
        t.write(arg=f"{answer}", font=("sans serif", 9, "bold"))
        correct_guess.append(answer)
        current_score += 1
    elif answer not in state_names or answer == "":
        messagebox.showerror(title="Invalid Input", message="Not a correct state name or\nField was empty.")
        current_score -= 1

game_end_text = turtle.Turtle()
game_end_text.hideturtle()
game_end_text.penup()
game_end_text.goto(-220, 200)
game_end_text.color('blue')
messagebox.showinfo(title="Program Ended", message=f"Your final score: {current_score}/50")


