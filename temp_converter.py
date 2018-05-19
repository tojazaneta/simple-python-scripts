"""Temperature converter. Convert Celsius to Fahrenheit."""

celsius = input("Celsius: ")

def c_t_f():
    if float(celsius) < -273.15:
        print("Really, too cold")
    else:
        fahrenheit = float(celsius) * 9/5 + 32
        print(celsius, "degrees Celsius =", fahrenheit, "degrees Fahrenheit")
        print("---------------")

c_t_f()
