import time
import random
from tqdm import tqdm
from functools import singledispatch
import os

miniters_lookup = {
    (1, 2): 1,                  # very short sleep times (up to 2 seconds)
    (3, 10): 2,                 # short sleep times (3 to 10 seconds)
    (11, 20): 5,                # moderate sleep times (11 to 20 seconds)
    (21, 60): 10,               # moderate sleep times (21 to 60 seconds)
    (61, 600): 60,              # longer sleep times (1 to 10 minutes, update every 60 seconds)
    (601, float('inf')): 120    # very long sleep times (over 10 minutes, update every 2 minutes)
}

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

    disable_tqdm = os.getenv('GITHUB_ACTIONS') == 'true'

    total_ticks = int(sleep_time * 10)
    miniters = next(miniters_value for (start, end), miniters_value in miniters_lookup.items()
                    if start <= total_ticks <= end)    
    
    if total_ticks > 60:
        total_ticks = max(1, int(sleep_time / 60)) 
    
    for _ in tqdm(range(total_ticks), desc=description, unit="ticks", ncols=80, miniters=miniters, disable=disable_tqdm):
        time.sleep(sleep_time / total_ticks)
