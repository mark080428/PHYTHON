color = "red" 
shape = 'table'

def function(shape="привет"):
    global color
    color = "green"
    print(f"Внутри функции цвет - {color}")
    print(shape)


# print(shape)
# print(f"В основной программе цвет - {color}")
# function('привет')
# print(f"В основной программе цвет - {color}")


def information(a=7, b=2):
    print(a + b)
    function()
information(b=7)
print(shape)