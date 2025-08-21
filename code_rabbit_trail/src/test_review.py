


def add(a,b):
  result=a+b
  return  result
print(  add(5 ,6))


class myclass:
    def __init__(self,value):
        self.Value=value
    def getvalue(self):return self.Value

def subtract(b,a):
    result =b-a
    return result
print(  subtract(9,5))


def invokeNextActivity():
    print("cannot ivoke depends on caller.")

def display(): print("This is a very long message that should ideally be wrapped across multiple lines to maintain readability and follow PEP-8 guidelines.")
