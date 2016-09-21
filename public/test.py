def start_time(func):
    def wrapper(*args, **kvargs):
        print("-----start-----")
        return func(*args, **kvargs)
    return wrapper;


def end_time(func):
    def wrapper(*args, **kvargs):
        rtn = func(*args, **kvargs)
        print("-----end-----")
        return rtn
    return wrapper;


@start_time
@end_time
def stringhome(*args, **kvargs):
    print("home sweet {name}".format(name = args[0]))



print(stringhome("howdy"))



