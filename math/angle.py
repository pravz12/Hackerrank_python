import math
c = int(raw_input())
a = int(raw_input())

p = math.sqrt((c*c)+(a*a))/2

thet = math.asin(c/(2*p))
        
q = math.sqrt(p*p+a*a-2*p*a*(math.cos(thet)))

theta = math.asin(p*math.sin(thet)/q)*180/(math.pi)
print str(int(round(theta)))+'°'

