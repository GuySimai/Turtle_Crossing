from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUM_OF_CARS = 25


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.create_cars()

    def create_cars(self):
        for car in range(NUM_OF_CARS):
            self.create_car()

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(random.randint(-300, 300), random.randint(-250, 250))
        new_car.move_speed = STARTING_MOVE_DISTANCE
        self.all_cars.append(new_car)

    def move_cars(self):
        for num_car in range(NUM_OF_CARS):
            if self.all_cars[num_car].xcor() < -320:
                self.reset_car_position(num_car)
            new_x = self.all_cars[num_car].xcor() - self.all_cars[num_car].move_speed
            self.all_cars[num_car].goto(new_x, self.all_cars[num_car].ycor())

    def reset_car_position(self, num_of_cars):
        self.all_cars[num_of_cars].goto(320, random.randint(-250, 250))

    def speed_up(self):
        for num_car in range(NUM_OF_CARS):
            self.all_cars[num_car].move_speed += MOVE_INCREMENT
