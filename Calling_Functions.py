def function1():
    global var1
    var1 = "Hello from function 1!"
    function2(var1)
    
def function2(var1):
    print(var1)
    
# Call function1
function1()