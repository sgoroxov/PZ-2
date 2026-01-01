import calculations
import visualization
from decorators import measure_time, log_call


@measure_time
@log_call
def compute(fn, a, b, step):
    xs, ys = [], []
    x = a

    while x <= b + 1e-9:
        xs.append(x)
        ys.append(fn(x))
        x += step

    return xs, ys


# ───── ВЫБОР ФУНКЦИИ ПО НОМЕРУ ─────

func_names = list(calculations.functions.keys())

print("Доступные функции:")
for i, name in enumerate(func_names, start=1):
    print(f"{i} — {name}")

choice = input("\nВведите номер функции: ").strip()

# проверка, что введено число
if not choice.isdigit():
    print("Ошибка: нужно ввести номер, а не текст.")
    exit()

choice = int(choice)

# проверка диапазона номеров
if choice < 1 or choice > len(func_names):
    print("Ошибка: функции с таким номером нет.")
    exit()

selected_name = func_names[choice - 1]
func = calculations.functions[selected_name]


# ───── ВВОД ИНТЕРВАЛА ─────

a = float(input("Начало интервала a = "))
b = float(input("Конец интервала b = "))
h = float(input("Шаг = "))

xs, ys = compute(func, a, b, h)


# ───── ВЫВОД РЕЗУЛЬТАТОВ ─────

print("\nТаблица значений:")
visualization.show_table(xs, ys)

print("\nГрафик функции:")
visualization.draw_plot(xs, ys, f"Функция — {selected_name}")
