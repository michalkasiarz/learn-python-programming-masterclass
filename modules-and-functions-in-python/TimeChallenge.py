# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.

from time import time
from time import perf_counter
from time import monotonic
from time import process_time

time1 = time()
time2 = perf_counter()
time3 = monotonic()
time4 = process_time()

times = time1, time2, time3, time4

for time in times:
    print(time)

