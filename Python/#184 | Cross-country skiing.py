#10-02-2026 | 14-02-2026

'''given: an array of HH:MM:SS which are the finishing time n players
   return: the time gap between the first and completed n players
   example: given ["1:25:32", "1:25:10", "1:27:05"]) should return ["0", "+0:22", "+1:33"].'''

def get_relative_results(times_arr):
    time_secs=[]
      #converting each element into seconds 
    for i in range(len(times_arr)):
        hrs, mins, secs = map(int,times_arr[i].split(":"))
        total_secs = (hrs*3600)+(mins*60)+secs
        time_secs.append(total_secs)
      
    #finding the difference
    time_diff_arr=[]
    for i in range(len(time_secs)):
        time_diff = time_secs[i]-time_secs[0]
        if time_diff == 0:
            lap_time="0"
        else:
            mins = time_diff//60
            secs = time_diff%60
            lap_time = f"+{mins}:{secs:02d}"
        #adding the difference to the list
        time_diff_arr.append(lap_time)

    return time_diff_arr
