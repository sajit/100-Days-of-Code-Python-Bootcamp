from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)


map_turtle = Turtle()

map_turtle.shape(image)


state_data = pandas.read_csv("50_states.csv")



score = 0
guessed_states = []
while score < 50:
    answer = screen.textinput(
        title="Guess a state",
        prompt="Name a state (or type 'Exit' to end the game):",
    )
    if answer is None or answer.strip().lower() == "exit":
        break

    state_from_file = state_data[state_data["state"] == answer]
    if answer not in guessed_states:
        if not state_from_file.empty:
            state = Turtle()
            state.penup()
            state.hideturtle()
            x = state_from_file.iloc[0]["x"]
            y = state_from_file.iloc[0]["y"]
            state_name = state_from_file.iloc[0]["state"]
            state.goto(x,y)
            state.write(state_name)
            guessed_states.append(answer)
            score += 1
    else:
        print(f"Repeat guess: {answer}")


print(f"Game over! Your score: {score}/50")
screen.exitonclick()

