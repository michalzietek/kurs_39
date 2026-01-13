import time
import datetime

def monitor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_datetime = datetime.datetime.now()
        try:
            result = func(*args, **kwargs)
            status = "Success"
            return result
        except Exception as e:
            status = f"Error: {e}"
        finally:
            end_time = time.time()
            duration = end_time - start_time
            log_info = (f"{start_datetime} - Function {func.__name__}"
                        f"executed in {duration} seconds."
                        f"Arguments: {args}, {kwargs},"
                        f"Status: {status}")
            with open("monitoring.log", "a") as file:
                file.write(log_info + "\n")
    return wrapper