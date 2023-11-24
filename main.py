import tkinter as tk


class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator2")

        self.label_height = tk.Label(root, text="身長（cm）：")
        self.label_height.pack()

        self.entry_height = tk.Entry(root)
        self.entry_height.pack()

        self.label_weight = tk.Label(root, text="体重（kg）：")
        self.label_weight.pack()

        self.entry_weight = tk.Entry(root)
        self.entry_weight.pack()

        self.button_calculate = tk.Button(root, text="計算", command=self.calculate_bmi)
        self.button_calculate.pack()

        self.label_result = tk.Label(root, text="")
        self.label_result.pack()

    def calculate_bmi(self):
        height = float(self.entry_height.get())
        weight = float(self.entry_weight.get())

        bmi = weight / ((height / 100) ** 2)

        result = f"あなたのBMIは {bmi:.2f} です。"

        self.label_result.config(text=result)


root = tk.Tk()
bmi_calculator = BMICalculator(root)
root.mainloop()
