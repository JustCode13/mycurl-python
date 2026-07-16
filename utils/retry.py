import random
import time
from .exceptions import RedirectLimitExceededError


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


def add_retry_jitter(delay: float):
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



