import multiprocessing
import time

# Using multiprocessing.
# attached flow diagram for this as `../assets/14_flow_diagram_parallel.png`

start = time.perf_counter()


def do_smtg():
    print('Sleeping for a second')
    time.sleep(1)
    print('Done sleeping')

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=do_smtg)
    p2 = multiprocessing.Process(target=do_smtg)

    for p in [p1, p2]:
        p.start()

    for p in [p1, p2]:
        p.join()

finish = time.perf_counter()

print(f"finished in {round(finish - start, 2)} second(s).")



'''
Before even sleeping the statements:
start = time.perf_counter()
finish = time.perf_counter()

print(f"finished in {round(finish - start, 2)} second(s).")

got executed.

That' why we saw the print statement before all other code.

now to solve that we need to use .join() method.
'''
