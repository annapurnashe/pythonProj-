def  decorator(fun):
    def wrapper():
        print("something is happening before the function is called.")
        fun()
        print("something is happening after the function calling.")
    return wrapper
@decorator
def hello():
    print("hello.")

hello()

