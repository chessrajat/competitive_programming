'''
/*
 * @Author: Rajat  
 * @Date: 2020-12-22 16:41:30 
 * @Last Modified by: Rajat
 * @Last Modified time: 2020-12-22 17:10:31
 */
'''

def timeConversion(s):
    #
    # Write your code here.
    zone = s[-2:]
    time = s[:-2]
    a = time.split(":")
    if zone == "PM":
        if int(a[0]) != 12:
            a[0] = str((int(a[0])+12))
        if a[0] == "0":
            a[0] = "00" 
        return(":".join(a))
    if zone == "AM":
        if int(a[0]) > 12:
            a[0] = str(abs(int(a[0]) - 12))
        if int(a[0]) == 12:
            a[0] = "00"
        
        if a[0] == "0":
            a[0] = "00" 
        
        return(":".join(a))


def timeConversion2(s):
    h = int(s[0:2])
    if s[-2:] == "PM":
        if h != 12:
            h += 12
    else:
        if h == 12:
            h = 0
    return f"{h:02d}{s[2:-2]}"

if __name__ == '__main__':

    s = input()

    result = timeConversion2(s)

    print(result)