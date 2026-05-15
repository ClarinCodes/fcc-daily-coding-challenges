#19-02-2026 | 19-02-2026

#1st code in this series without the help of AI
def avalanche_risk(snow_depth, slope):
    if snow_depth == 'Shallow' or slope == 'Gentle':
        return 'Safe'
    else:
        return 'Risky'
