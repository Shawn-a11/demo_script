import time
def stopwatch():
    input("Ready")
    start_time = time.time()
    input("Stopwatch running... Press Enter to stop it")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time elapsed: {elapsed_time:.2f} seconds")

stopwatch()