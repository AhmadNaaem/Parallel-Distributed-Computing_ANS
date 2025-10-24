from Code import testCode
import time
import multiprocessing
import threading

if __name__ == "__main__":
    size = 10000000
    counts = [5, 10, 15]

    print("\n=== Multithreading Test with Lock ===")
    for threads in counts:
        lock = threading.Lock()
        jobs = []
        start_time = time.time()

        def sf_testCode(size, out_list):
            with lock:
                testCode(size, out_list)

        for i in range(threads):
            out_list = []
            thread = threading.Thread(target=sf_testCode, args=(size, out_list))
            jobs.append(thread)

        for t in jobs:
            t.start()
        for t in jobs:
            t.join()

        end_time = time.time()
        print(f"Threads (Lock): {threads}, Time taken = {end_time - start_time:.4f} seconds")

    print("\nAll processing complete.")
