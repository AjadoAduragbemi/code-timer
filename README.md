# code-timer
A way to see how much time it took a particular block of code to execute

Sure almost every time I happen to always use the general approach (The only my dumb as could think of),
This is the:

import time

start_time = time.time()

...
..        '''block of code to be timed'''
.

end_time = time.time()

#And then

total_time = start_time - end_time

The above code wouldn't look tire some until you have 
