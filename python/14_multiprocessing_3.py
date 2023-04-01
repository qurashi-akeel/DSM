from multiprocessing import Process
import time

start = time.perf_counter()

def do_smtg(seconds):
    print(f'Sleeping for {seconds} second(s).')
    time.sleep(seconds)
    print('Done sleeping.')

processes = []

if __name__ == "__main__":
    for _ in range(5):
        p = Process(target=do_smtg, args=[_])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

finish = time.perf_counter()

print(f"finished in {round(finish - start, 2)} second(s).")
