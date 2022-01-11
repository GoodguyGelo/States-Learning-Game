from turtle import Turtle


class StatesCreator(Turtle):
    """will create a turtle to write the state onto a specified location"""
    def __init__(self):
        super().__init__()
        self.score = 0

    def write_state(self, answer, location):
        """will write the state onto a specified location"""
        self.hideturtle()
        self.penup()
        self.goto(location)
        self.write(f"{answer}", align="center", font=("Courier", 7, "normal"))

    def add_to_score(self):
        self.score += 1

