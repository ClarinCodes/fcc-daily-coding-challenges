#13-02-2026 | 13-02-2026

#Given an array of five numbers, each representing the time (in seconds) it took a luger to complete a segment of a track, determine which segment had the fastest speed and what that speed was.

def get_fastest_speed(times):
    i=0
    j=0
    fastest=0
    fast=[]
    segment = [320, 280, 350, 300, 250]
    for i in range(len(segment)):
        speed = segment[i]/times[i]
        fast.append(speed)
        j=j+1
        if fastest < speed:
            fastest = speed
            x = j
    return  f"The luger's fastest speed was {fastest:.2f} m/s on segment {x}."
