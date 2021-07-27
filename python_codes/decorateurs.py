def verbose(fn):       # fonction → fonction décorée

    def decorated(*args, **kwargs):
        print("Function:  ", fn.__name__)
        print("Arguments: ", args, kwargs)
        result = fn(*args, **kwargs)
        print("Result:    ", result)

        return result

    return decorated

verbose_sum = verbose(sum)
# print(verbose_sum([1, 2, 3]))

def p_decorate(func):
    def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
    return func_wrapper

@p_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

# print(get_text("John"))



def add(f):
    
    def _addition(_a,b):
        return _a+b
    return _addition


@add
def myfun():
    return "Start"

print(myfun(10,2))