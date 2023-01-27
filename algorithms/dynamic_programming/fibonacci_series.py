import time


def r_fib(n):
    if n <= 2:
        return 1
    return r_fib(n-1) + r_fib(n-2)

start = time.time()
print(f'recursive result: {r_fib(35)} --> {time.time() - start} (sec)')


F = [None]*1000
def mem_fib(n):
    if n <= 1:
        return n
    
    if F[n] is None:
        F[n] = mem_fib(n-1) + mem_fib(n-2)

    return F[n]

start = time.time()
print(f'dynamic memorization result: {mem_fib(100)} --> {time.time() - start} (sec)')


def tab_fib(n):
    F = [-1]*(n+1)
    F[0] = 0
    F[1] = 1
    for i in range(2, n+1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]

start = time.time()
print(f'dynamic tabulation result: {tab_fib(100)} --> {time.time() - start} (sec)')
