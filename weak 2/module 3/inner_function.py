def duble_decker():
    print("stared duble decker")
    def inner_fun():
        print("inside a stard")
        return 3000
    return inner_fun

# print(duble_decker())
print(duble_decker()())

def do_samtings(work):
    print('working started')
    work()
    print("working end")

def coding():
    print("coding start Now ")

do_samtings(coding)
