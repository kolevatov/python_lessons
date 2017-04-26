# How to read global variable, change and hide variable
def read_global():
    print (gl_var)

def change_global():
    global gl_var
    gl_var += 1
    print(gl_var)

def hide_global():
    gl_var = 0
    print(gl_var)

gl_var = 100
read_global()
change_global()
hide_global()