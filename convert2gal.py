import math


# RA(radians),Dec(radians) of Galactic Northpole in J2000
Galactic_Northpole_Equatorial=(math.radians(192.859508), math.radians(27.128336))

# #######################################################################
# Convert Equatorial coordinates to Galactic coordinates in the epoch J2000 
# #########################################################################
def eq2gal(ra,dec):

#    Convert Equatorial coordinates to Galactic Coordinates in the epch J2000.
    
#    Keywords arguments:
#    ra  -- Right Ascension (in radians)
#    dec -- Declination (in radians)

#    Return a tuple (l, b):
#    l -- Galactic longitude (in radians)
#    b -- Galactic latitude (in radians)


    alpha = Galactic_Northpole_Equatorial[0]
    delta = Galactic_Northpole_Equatorial[1]
    la = math.radians(33.0)
    
    b = math.asin(math.sin(dec) * math.sin(delta) +
                  math.cos(dec) * math.cos(delta) * math.cos(ra - alpha))

    l = math.atan2(math.sin(dec) * math.cos(delta) - 
                   math.cos(dec) * math.sin(delta) * math.cos(ra - alpha), 
                   math.cos(dec) * math.sin(ra - alpha)
                   ) + la

    l = l if l >= 0 else (l + math.pi * 2.0)

#    l = l % (2.0 * math.pi)

    return l, b
# by MQQ @ Vanderbilt   
# last modified: Nov 09 2011
###############################################################################
# #The end of eq2gal   ###################################################

f1 = open('sky-distribution.dat','r')

for line in f1:
    row = line.split(' ')
    ra = float(row[1])
    dec = float(row[2])
    l = float(row[3])
    b = float(row[4])
    gal = eq2gal(ra, dec)
    print ("%s %s %s %s\n" % (math.degrees(gal[0]) , math.degrees(gal[1]), l, b))

f1.close()
