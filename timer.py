
'''Time a particular process'''

from time import time
from sys import exit

class timer:
    __proc = []
    __st_time, l_st_time = (), []
    __d_time = {}
    
    #constructor removed
    
    def s_time(self, tag=None): #start watch
        if(tag == None):
            tag = 'process'
        self.__proc.append(tag)
        self.l_st_time = list(self.__st_time)
        self.l_st_time.append(time())
        self.__st_time = tuple(self.l_st_time)
        
        return self.__st_time
        
    def fmt_time(self, t_taken=0.0):
            sec_t, min_t, hour_t, day_t = t_taken, 0, 0, 0
            
            if sec_t >= 0 and sec_t < 60:
                sec_t = sec_t
                
            elif sec_t >= 60 and sec_t < 3600:
                min_t = int(sec_t//60)
                sec_t = sec_t%60
                
            elif sec_t >= 3600 and sec_t < 84000:
                hour_t, sec_t = int(sec_t//3600), sec_t%3600
                min_t, sec_t = int(sec_t//60), sec_t%60
                
            elif sec_t >= 84000:
                day_t, sec_t = int(sec_t//84000), sec_t%84000
                hour_t, sec_t = int(sec_t//3600), sec_t%3600
                min_t, sec_t = int(sec_t//60), sec_t%60
        
            return (day_t, hour_t, min_t, sec_t)
    
    def __t_time(self, time_d, proc, fmt=True):
        if time_d >= 0 and fmt:
            self.__d_time[proc] = "{}".format("%.2d:%.2d:%.2d:%.2d"%(self.fmt_time(time_d) ))
        elif time_d >= 0 and not fmt:
            self.__d_time[proc] = "%s sec(s)"%(time_d)
        else:
            self.__d_time[proc] = "Invalid time: couldn't process"
            exit()
        return self.__d_time
        
    #stop watch and give result
    def total_time(self, tagNum=0):
        end_time = time()
        try:
            time_t = end_time - self.__st_time[tagNum]
        except Exception as msg:
            print "An error occurred: ",
            print msg
            exit()
        else:
            d_tm = self.__t_time(time_t, self.__proc[tagNum])
        proc = self.__proc[tagNum]
        return "Total Time taken by \'{}\': {}".format(proc, d_tm.get(proc))
