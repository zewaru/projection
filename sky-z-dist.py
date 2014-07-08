# histograms for various purposes.
# for redshift cutoff, change upper limit in z in line 38 (?)
# to make histograms for redshift distribution for different telescopes
# change code for selection in line ()
# Ned-z-dist.out gives the list of sources with their coordinates and redshifts
# this should really come only from NED_references.out


import sys
import matplotlib.pyplot as plt
import matplotlib.pylab
from matplotlib.backends.backend_pdf import PdfPages
import math
import random
from pylab import subplot, savefig, grid, plot, legend

def zselect(z, n, ydata):
    if 0.00 <= z < n:
        ydata.append(z)
    elif z <= 0.00:
        ydata.append(0.0001)


f = open("sky-distribution.dat",'r')

n = 0.042
histbins = [0.001*i for i in range(0, int(n*1000))]


bar0 = plt.figure()
plt.suptitle('Full Sample Z distribution < 0.04')
bar1 = plt.figure()
plt.suptitle('Fast + CTIO + ZCAT + McDonald  Z distribution < 0.04')
bar2 = plt.figure()
plt.suptitle('6dF Z distribution < 0.04')
bar3 = plt.figure()
plt.suptitle('NED Z distribution < 0.04')
bar4 = plt.figure()
plt.suptitle('SDSS Z distribution < 0.04')
bar5 = plt.figure()
plt.suptitle('NED Z distribution < 0.04 in 6dF footprint')

pp = PdfPages('z-dist-0-04.pdf')


ydata = []
ydata_FAST = []
ydata_SDSS = []
ydata_6dF = []
ydata_NED = []
ydata_NED6dF =[]

for line in f:
    data = line.split()
    z = float(data[6])/300000 
    source = data[7]
    zselect(z, n, ydata)
    if source == 'F' or source == 'C' or source == 'O' or source == 'D': 
        zselect(z, n, ydata_FAST)
    elif source == 'S':
        zselect(z , n, ydata_SDSS)
    elif source == '6':
        zselect(z, n, ydata_6dF)
    elif source == 'N' or source == 'M':
        zselect(z, n ,ydata_NED)
        if math.fabs(float(data[4])) > 10:
            zselect(z, n, ydata_NED6dF)

print len(ydata)
print len(ydata_FAST)
print len(ydata_SDSS)
print len(ydata_6dF)
print len(ydata_NED)
print len(ydata_NED6dF)

plt.figure(bar0.number)
plt.hist(ydata, bins = histbins)
plt.figure(bar1.number)
plt.hist(ydata_FAST, bins = histbins)
plt.figure(bar2.number)
plt.hist(ydata_6dF, bins = histbins)
plt.figure(bar3.number)
plt.hist(ydata_NED, bins = histbins)
plt.figure(bar4.number)
plt.hist(ydata_SDSS, bins = histbins)
plt.figure(bar5.number)
plt.hist(ydata_NED6dF, bins = histbins)

pp.savefig(bar0)
pp.savefig(bar1)
pp.savefig(bar2)
pp.savefig(bar3)
pp.savefig(bar4)
pp.savefig(bar5)

pp.close()



f.close()
