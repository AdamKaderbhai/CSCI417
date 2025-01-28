import time


def calc_sum_1(n):
    return n * (n + 1) // 2

sum_1 = calc_sum_1(100000)
print(sum_1)

start_time = time.time()
sum_1 = calc_sum_1(100000)
end_time = time.time()

print(f"Sum: {sum_1}")
print(f"Time taken: {end_time - start_time} seconds")