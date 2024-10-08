def ways(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    onesteps = 0
    twosteps = 0
     
    onesteps = ways(stairs -1)
    if stairs >= 2:
        twosteps = ways(stairs -2)
    return onesteps + twosteps

print(ways(4))