from functools import wraps
from time import sleep


def waiting_sim():
    print("How long would you like to wait? (In seconds)")
    answer = input("-> ")
    done_waiting()


def timer(func, num):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(num)

    return wrapper

@timer
def done_waiting():
    print("Thanks for waiting! Carry on now.")

