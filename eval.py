res=eval('4+7*4')
print(res)

user_input = input("Enter an expression: ")
result = eval(user_input)
print(f"Result: {result}")


result = eval("x + y", {"x": 10, "y": 15})
print(result) 

config = {
    'value1': '15 * 7 / 5',
    'value2' : '6 + 8 - 3 * 2'
}
result = eval(config['value1'])
print(result)
result = eval(config['value2'])
print(result)

def run_expression(code):
    return eval(code)

print(run_expression("3 / 4")) 

class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(99)
attr_name = "value"
print(eval("obj." + attr_name))

condition = "x > 10"
x = 15
if eval(condition):
    print("Condition met")  


eval("print('Bonjour!!')")

data = "{'a': 1, 'b': 2}"
result = eval(data)
print(result)  

user_formula = "price * quantity + tax"
context = {'price': 100, 'quantity': 5, 'tax': 20}
total = eval(user_formula, context)
print(total)  

