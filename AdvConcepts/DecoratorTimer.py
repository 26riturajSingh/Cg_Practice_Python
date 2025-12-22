n = [1,2,3,4,5]
import time
def timer_decor(func):
    def wrapper(*args):
        start_time = time.time()
        r = func(*args)
        end_time = time.time()
        print("TT: ", round(end_time - start_time, 5))
        return r
    return wrapper

@timer_decor
def sample_method(a):
    return list(map(lambda x:x*x, a))

print(sample_method(n))