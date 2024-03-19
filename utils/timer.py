class Timer:
    def __init__(self, message):
        self.message = message

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            import time
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{self.message}: {end_time - start_time:.2f} seconds")
            return result

        return wrapper
