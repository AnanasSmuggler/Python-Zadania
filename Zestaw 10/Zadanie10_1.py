import tkinter as tk
import random

def main() -> None:
    root = tk.Tk()
    root.title("Rzut kostką")
    root.geometry("400x400")
    result_label_text = tk.StringVar()

    def roll_the_dice() -> None:
        result = random.randint(1,6)
        result_label_text.set(result)


    main_label = tk.Label(text = "Wynik rzutu kostką: ", font=("Arial", 25), pady=10)
    result_label = tk.Label(textvariable=result_label_text, font=("Arial", 35), pady=10)
    button = tk.Button(text = "Rzuć kostką!", font=("Arial", 25), pady=10, command=roll_the_dice)

    main_label.pack()
    result_label.pack()
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()