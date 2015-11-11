# code-timer
A way to see how much time it took a particular block of code to execute

Sure almost every time I happen to always use the general approach (The only my dumb as could think of).

This is the:

<code> import time

start_time = time.time()

...
..        '''block of code to be timed'''
.

end_time = time.time()

'''And then'''

total_time = start_time - end_time '''The same approach I use in every other lang. as well'''<\code>

The above wouldn't look tiresome until you have check the execution time of different blocks of code.

So what if there was a better way to do this, well thing is I didn't try checking,
I think I've seen someone use a better approach with matlab, but then I decided to write something I could call my own, though not perfect but yea it kindof feels better (maybe because it came from me).

Implented in python and can be done in any other language:

#Summary

- It takes the object time(), and a process (name)
  - <code> tm = timer() <\code>
  - <code> tm.s_time([process name])   '''process name is optional if s_time would be used just once'''<\code>

- 'process name' and 'start time' are stored in a list and tuple respectively

- If tm.s_time() is called again this time with a process name the step directly above is repeated

- The block of code is executed

- Then <code> tm.total_time([pNum]) </code>, this is also called with an optional parameter (the number of proc. name we are trying to get the total of)





