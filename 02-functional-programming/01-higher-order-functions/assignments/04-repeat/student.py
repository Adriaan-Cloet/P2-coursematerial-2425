def repeat(function, n):
    for _ in range(n):
        function()

def say_hello():
    print("Hello!")

print(repeat(say_hello, 5))