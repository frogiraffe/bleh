import matplotlib.pyplot as plt
import random
from sympy.solvers import solve
from sympy import Symbol


class Math:
    def solve_equation(self, probability_value):
        x = Symbol("x")
        solution_list = solve(
            ((3600 - (3600 - 120 * x + x**2)) / 3600) - probability_value
        )
        return solution_list


class List:
    def __init__(self):
        pass

    def compare_list(self, sample, wait_val):
        samples_x = []
        samples_y = []
        x_l1 = []
        y_l1 = []
        for n in range(sample):
            a = random.uniform(0, 60)
            b = random.uniform(0, 60)
            if a - b <= wait_val and b - a <= wait_val:
                samples_x.append(a)
                samples_y.append(b)
            else:
                x_l1.append(a)
                y_l1.append(b)
        return samples_x, samples_y, x_l1, y_l1


class Graph:
    def create_graph(self, x, y):
        plt.scatter(x, y, s=2)

    def show_graph(self):
        plt.show()


class Method(Math):
    def __init__(self):
        self.natural_prompt = "Sample size: "
        self.natural_prompt_error = "Please enter a natural number."
        self.process_prompt = "Probability or Num Process: p/n"
        self.prob_prompt = "Probability value: "
        self.wait_value_prompt = "Enter wait value"
        self.prob_value = "P"
        self.num_value = "N"

    def get_sample_size(self):
        while True:
            value = input(self.natural_prompt)
            try:
                return int(value)
            except ValueError:
                print(self.natural_prompt_error)

    def get_process(self):
        while True:
            value = input(self.process_prompt).upper()
            return value

    def get_prob(self):
        while True:
            try:
                value = float(input((self.prob_prompt)))
                return value
            except ValueError:
                print("Please enter a number")
                continue

    def get_wait_value(self):
        while True:
            try:
                value = eval(input(self.wait_value_prompt))
                return value
            except ValueError:
                print("Please enter a number")
                continue

    def values_prob(self):
        prob = self.get_prob()
        time = self.solve_equation(prob)
        sample = self.get_sample_size()
        return time[0], sample

    def values_num(self):
        time = self.get_wait_value()
        sample = self.get_sample_size()
        return time, sample

    def print_results(self, time, samples_x, sample):
        self.wait_val_result_prompt = print(f"Time waited: {time}")
        self.probability_result_prompt = print(
            f"Probability: {len(samples_x) / sample}"
        )

    def probability_process(self):
        time, sample = self.values_prob()
        samples_x, samples_y, x_l1, y_l1 = List().compare_list(sample, time)
        self.print_results(time, samples_x, sample)
        Graph().create_graph(samples_x, samples_y)
        Graph().create_graph(x_l1, y_l1)
        Graph().show_graph()

    def num_process(self):
        time, sample = self.values_num()
        samples_x, samples_y, x_l1, y_l1 = List().compare_list(sample, time)
        self.print_results(time, samples_x, sample)
        Graph().create_graph(samples_x, samples_y)
        Graph().create_graph(x_l1, y_l1)
        Graph().show_graph()


if __name__ == "__main__":
    while True:
        process = Method().get_process()
        if process == Method().prob_value:
            Method().probability_process()
        elif process == Method().num_value:
            Method().num_process()
