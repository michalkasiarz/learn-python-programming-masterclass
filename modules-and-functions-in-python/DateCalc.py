import time

# Data calculator

print(time.gmtime(0))

# using localtime method
time_here = time.localtime()
print(time)

# Two ways of printing year, month and day
print("Year: ", time_here[0], time_here.tm_year)
print("Month: ", time_here[1], time_here.tm_mon)
print("Day: ", time_here[2], time_here.tm_mday)
