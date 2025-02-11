import time
import random
from tqdm import tqdm
from functools import singledispatch

@singledispatch
def smart_sleep(duration, description="Sleeping"):
    """Generic sleep function that accepts different types of input."""
    raise TypeError(f"Unsupported argument type for sleep: {type(duration)}")

@smart_sleep.register
def _(duration: int, description="Sleeping"):
    """Handles fixed integer sleep time."""
    sleep_time = duration + random.random()
    _show_progress(sleep_time, description)

@smart_sleep.register
def _(duration: float, description="Sleeping"):
    """Handles fixed float sleep time."""
    sleep_time = duration + random.random()
    _show_progress(sleep_time, description)

@smart_sleep.register
def _(duration: tuple, description="Sleeping"):
    """Handles a tuple range (min_time, max_time) for random sleep."""
    min_time, max_time = duration
    sleep_time = random.uniform(min_time, max_time)
    _show_progress(sleep_time, description)

def _show_progress(sleep_time, description):
    """Displays a progress bar with a custom description."""
    for _ in tqdm(range(int(sleep_time * 10)), desc=description, unit="ticks", ncols=80):
        time.sleep(0.1)
