def add(func):

    def wrapper(*args,**kwargs):

        result=func(*args,**kwargs)
        print(f"Total :{result}")
        return result
    return wrapper    

@add
def add_two_numbers(a,b):
    return a + b
(add_two_numbers(10,20))



@add

def sub_two_numbers(a,b):
    return a - b

(sub_two_numbers(100,20))


@add

def mul_two_numbers(a,b):
    return a * b
(mul_two_numbers(10,20))

@add
def div_two_numbers(a,b):
    return a/b
(div_two_numbers(100,20))
