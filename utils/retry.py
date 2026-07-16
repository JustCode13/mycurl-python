import random
import time
from .exceptions import RetryLimitExceededError


def calculate_backoff_delay(attempt: int, base_delay: float, maximum_delay: float) -> float:
    if (attempt < 0):
        raise ValueError("attempt must be greater than or equal to 0")
    
    if (base_delay <= 0):
        raise ValueError("base_delay must be greater than 0")
    
    if (maximum_delay <= 0):
        raise ValueError("maximum_delay must be greater than 0")
    
    if (base_delay > maximum_delay):
        raise ValueError("maximum_delay must be greater than or equal to base_delay")
    
    calculated_delay = base_delay * (2 ** attempt)

    if (calculated_delay > maximum_delay):
        return maximum_delay
    
    return calculated_delay


def add_retry_jitter(delay: float) -> float:
    if not isinstance(delay,float):
        raise ValueError("delay must be float")
    
    if (delay < 0):
        raise ValueError("delay must be greater than zero")
    
    start_value = -0.5
    end_value = 0.5

    jitter = random.uniform(start_value,end_value)

    final_delay = delay + jitter

    if (final_delay <= 0):
        raise ValueError("final delay cannot be negative")
    
    return final_delay


def sleep_before_retry(attempt: int, base_delay: float, maximum_delay: float) -> None:
    if not isinstance(attempt,int):
        raise ValueError("attempt must be int")
    
    if (attempt < 1):
        raise ValueError("attempt must be greater than zero")
    
    max_retries = 10

    if (attempt > max_retries):
        raise RetryLimitExceededError("maximum retry limits exceeded")

    try:
        delay = calculate_backoff_delay(attempt, base_delay, maximum_delay)
        
        final_delay = add_retry_jitter(delay)
    except ValueError:
        raise

    time.sleep(final_delay)
