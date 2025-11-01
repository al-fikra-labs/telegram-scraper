import time
import functools

def measure_execution_time_async(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        end_time = time.perf_counter()
        time_elapsed = end_time - start_time
        formatted = time.strftime("%M min %S sec", time.gmtime(time_elapsed))
        print(f"Execution time: {formatted}")
        return result
    return wrapper
