from tabulate import tabulate
import matplotlib.pyplot as plt


def show_table(xs, ys, precision=4):
    rows = [
        (round(x, precision), round(y, precision))
        for x, y in zip(xs, ys)
    ]
    print(tabulate(rows, headers=["X", "Y"], tablefmt="grid"))


def draw_plot(xs, ys, title="График функции"):
    plt.figure(figsize=(9, 4.5))
    plt.plot(xs, ys, "o-")
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(title)
    plt.show()
