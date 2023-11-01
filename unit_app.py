import tkinter as tk
from tkinter import messagebox

class UnitConvertor(tk.Tk):
    def __init__(self, root):
        self.root = root
        self.root.title("UNIT CONVERTER")
        
        self.main_menu()
        
        self.length_choice = tk.IntVar()
        self.result = tk.StringVar()
        self.weight_choice = tk.IntVar()
        self.temperature_choice = tk.IntVar()

    def main_menu(self):
        self.label = tk.Label(text="Welcome to unit converter", font=(None, 16), bg="black", fg="white")
        self.label.grid(row=0, column=2)

        self.select_label = tk.Label(text="Select the converter to choose:", font=(None, 12))
        self.select_label.grid(row=2, column=2)

        self.length_button = tk.Button(text="LENGTH", command=self.length)
        self.length_button.grid(row=6, column=0)
        self.weight_button = tk.Button(text="WEIGHT",command=self.weight)
        self.weight_button.grid(row=6, column=2)
        self.temperature_button = tk.Button(text="TEMPERATURE",command=self.temperature)
        self.temperature_button.grid(row=6, column=4)

    def clear(self):
        self.label.destroy()
        self.select_label.destroy()
        self.weight_button.destroy()
        self.temperature_button.destroy()
        self.length_button.destroy()

    def clear_converter(self):
        self.select_label.destroy()
        self.length_choice.set(1)
        for widget in self.root.winfo_children():
            widget.destroy()
        
    def length(self):
        self.clear()
        self.length_label = tk.Label(text="LENGTH CONVERTER", font=(None, 16), bg="black", fg="white")
        self.length_label.grid(row=0, column=2)

        self.select_label = tk.Label(text="Choose the conversion:", font=(None, 12))
        self.select_label.grid(row=2, column=2)

        self.length_choice.set(1)  

        length_radio_options = [
            ("Meters to Feet", 1),
            ("Feet to Meters", 2),
            ("Inches to Centimeters", 3),
            ("Centimeters to Inches", 4),
            ("Kilometers to Meters", 5),
            ("Meters to Kilometers", 6)
        ]

        for option, value in length_radio_options:
            length_radio = tk.Radiobutton(text=option, variable=self.length_choice, value=value)
            length_radio.grid(column=2)

        self.length_entry = tk.Entry(self.root, width=20)
        self.length_entry.grid(column=2)

        length_button = tk.Button(self.root, text="Convert Length", command=self.length_convert)
        length_button.grid(column=2)

        exit_button = tk.Button(self.root, text="EXIT", command=self.exit)
        exit_button.grid(column=2)

        back_button = tk.Button(self.root,text="BACK" , command=self.back)
        back_button.grid(column=2)

    def weight(self):
        self.clear()
        self.length_label = tk.Label(text="WEIGHT CONVERTER", font=(None, 16), bg="black", fg="white")
        self.length_label.grid(row=0, column=2)

        self.select_label = tk.Label(text="Choose the conversion:", font=(None, 12))
        self.select_label.grid(row=2, column=2)

        self.weight_choice.set(1)  

        weight_radio_options = [
            ("grams to pound", 1),
            ("pounds to grams", 2),
            ("grams to Kilogram", 3),
            ("kilogram to grams", 4),
            ("kilogram to pounds", 5),
            ("pounds to kilogram", 6)
        ]

        for option, value in weight_radio_options:
            weight_radio = tk.Radiobutton(text=option, variable=self.weight_choice, value=value)
            weight_radio.grid(column=2)

        self.weight_entry = tk.Entry(self.root, width=20)
        self.weight_entry.grid(column=2)

        weight_button = tk.Button(self.root, text="Convert Length", command=self.weight_convert)
        weight_button.grid(column=2)

        exit_button = tk.Button(self.root, text="EXIT", command=self.exit)
        exit_button.grid(column=2)

        back_button = tk.Button(self.root,text="BACK" , command=self.back)
        back_button.grid(column=2)

    def temperature(self):
        self.clear()
        self.texperature_label = tk.Label(text="TEMPERATURE CONVERTER", font=(None, 16), bg="black", fg="white")
        self.texperature_label.grid(row=0, column=2)

        self.select_label = tk.Label(text="Choose the conversion:", font=(None, 12))
        self.select_label.grid(row=2, column=2)

        self.temperature_choice.set(1)  

        temperature_radio_options = [
            ("Celsius to Fahrenheit", 1),
            ("Fahrenheit to Celsius", 2)
        ]

        for option, value in temperature_radio_options:
            temperature_radio = tk.Radiobutton(text=option, variable=self.temperature_choice, value=value)
            temperature_radio.grid(column=2)

        self.temperature_entry = tk.Entry(self.root, width=20)
        self.temperature_entry.grid(column=2)

        temperature_button = tk.Button(self.root, text="Convert Length", command=self.temperature_convert)
        temperature_button.grid(column=2)

        exit_button = tk.Button(self.root, text="EXIT", command=self.exit)
        exit_button.grid(column=2)

        back_button = tk.Button(self.root,text="BACK" , command=self.back)
        back_button.grid(column=2)

    def exit(self):
        self.root.destroy()

    def back(self):
        self.clear_converter()
        self.main_menu()

    def weight_convert(self):
        choice = self.weight_choice.get()
        value = self.weight_entry.get()
        self.result.set("")
        result_text = ""

        try:
            value = float(value)
            if choice == 1:
                result_text = f"{value} grams is equal to {value * 0.00220462} pounds."
            elif choice == 2:
                result_text =f"{value} pounds is equal to {value / 0.00220462} grams :"
            elif choice == 3:
                result_text =f"{value} grams is equal to {value /1000 } kilograms :"
            elif choice == 4:
                result_text =f"{value} kilograms is equal to {value* 1000} grams :"
            elif choice == 5:
                result_text =f"{value} kilograms is equal to {value *2.20462} pounds."
            elif choice == 6:
                result_text =f"{value} pounds is equal to {value / 2.20462} kilograms." 
            else:
                result_text = "Invalid conversion choice."
        except ValueError:
            result_text = "Invalid input. Please enter a valid number."

        messagebox.showinfo("Result", result_text)


    def length_convert(self):
        choice = self.length_choice.get()
        value = self.length_entry.get()
        self.result.set("")
        result_text = ""

        try:
            value = float(value)  
            if choice == 1:
                result_text = f"{value} meters is equal to {value * 3.28084} feet."
            elif choice == 2:
                result_text = f"{value} feet is equal to {value / 3.28084} meters."
            elif choice == 3:
                result_text = f"{value} inches is equal to {value * 2.54} centimeters."
            elif choice == 4:
                result_text = f"{value} centimeters is equal to {value / 2.54} inches."
            elif choice == 5:
                result_text = f"{value} kilometers is equal to {value * 1000} meters."
            elif choice == 6:
                result_text = f"{value} meters is equal to {value / 1000} kilometers."
            else:
                result_text = "Invalid conversion choice."
        except ValueError:
            result_text = "Invalid input. Please enter a valid number."

        messagebox.showinfo("Result", result_text)

    def temperature_convert(self):
        choice = self.temperature_choice.get()
        value = self.temperature_entry.get()
        self.result.set("")
        result_text = ""

        try:
            value = float(value)
            if choice == 1:
                result_text =f"{value} celsius is equal to {(value * 9/5)+32} fahrenheit."
            elif choice == 2:
                result_text =f"{value} fahrenheit is equal to {(value - 32)*5/9} celsius."
            else:
                result_text = "Invalid conversion choice."
        except ValueError:
            result_text = "Invalid input. Please enter a valid number."

        messagebox.showinfo("Result", result_text)
            
if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConvertor(root)
    root.mainloop()
