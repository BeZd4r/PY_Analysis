from random import choice

class Random_walk:

    def __init__(self,num_points=5000):
        self.num_points = num_points
        
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        
        while len(self.x_values) < self.num_points:

            x_direction = choice([-1,1])
            x_distance = choice(range(5))
            x_step = x_direction * x_distance

            y_direction = choice([-1,1])
            y_distance = choice(range(5))
            y_step = y_direction * y_distance

            if x_step and y_step:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)