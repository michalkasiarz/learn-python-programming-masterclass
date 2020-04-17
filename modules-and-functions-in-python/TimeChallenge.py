# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.

import time

time1 = time.get_clock_info("time")
time2 = time.get_clock_info("perf_counter")
time3 = time.get_clock_info("monotonic")
time4 = time.get_clock_info("process_time")

times = {"Time": time1, "Perf_counter": time2, "Monotonic": time3, "Process_time": time4}

for key, value in times.items():
    print(key + ": " + str(value))
