from multiprocessing import Process
import time

start = time.perf_counter()

def do_smtg():
    print('Sleeping for a second')
    time.sleep(1)
    print('Done sleeping')

processes = []

if __name__ == "__main__":
    # _ below is the throw away variable.
    for _ in range(50):
        p = Process(target=do_smtg)
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

finish = time.perf_counter()

print(f"finished in {round(finish - start, 2)} second(s).")
