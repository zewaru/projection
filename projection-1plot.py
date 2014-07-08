# Code for getting sky projection
# Matplotlib does not allow change in x axis limits without a lot of changes and 
# rewriting of how the projection is made. So I am going to keep the x limits fro -180
# to  +180. But since my data goes from 0 to 360, I am changing how it is displayed.
# Data with RA 0 to 180 is not transposed. Data with RA from 180 to 360 is  transposed
# to -180 to 0.I make plots with ra and dec and L and b. Also a final plot with no colors
# so as to make comparison with Huchra's plots easier.


from datetime import datetime

starttime = datetime.now()

from matplotlib.pyplot import subplot
from matplotlib.pyplot import savefig
import matplotlib.pyplot as plt
import matplotlib.pylab
from matplotlib.backends.backend_pdf import PdfPages
import math
import random
from pylab import subplot, savefig, grid, plot, legend

def zplot(ra, dec, z):
    for i in range(0, len(ra)):
        if z[i] <= 0.01:
            p1, = plt.plot(ra[i], dec[i], marker = "o", mfc = 'red', mec = 'red', ms = 1.8, linestyle = "none", label = "z <= 0.01")
        elif 0.01 <= z[i] <= 0.02:
            p2, = plt.plot(ra[i], dec[i], marker = "o", mfc = 'green', mec = 'green', ms = 1.8, linestyle = "none", label = "0.01 <= z <= 0.02")
        elif 0.02 <= z[i] <= 0.03:
            p3, = plt.plot(ra[i], dec[i], marker = "o", mfc = 'blue', mec = 'blue', ms = 1.8, linestyle = "none", label = "0.02 <=z <= 0.03")
        elif 0.03 <= z[i] <= 0.04:
            p4, = plt.plot(ra[i], dec[i], marker = "o", mfc = 'black', mec = 'black', ms = 1.8, linestyle = "none", label = "0.03 <= z <= 0.04")
        else:
            p5, = plt.plot(ra[i], dec[i], marker = "o", mfc = 'white', mec = 'black', ms = 1.8, linestyle = "none", label = "0.04 <= z ")

def legend_line(handles, labels, q):
    n = len(labels)
    h = []
    l = []
    for i in range(0, n):
        if labels[i] not in l:
            h.append(handles[i])    
            l.append(labels[i])
        if len(l) == q:
            break
    return h, l


#mec_choice = ['black', 'red', 'green', 'blue', 'magenta', 'white']

pp = PdfPages('hammer-eq-col-plot1.pdf')

f = open("sky-distribution.dat", 'r')

f.seek(0)

Fast = []
df = []
Ned = []
SDSS = []


for line in f:
    line = line.strip()
    columns = line.split(' ')
#    ra = math.radians(float(columns[1]))
    ra_0_to_360 = float(columns[1])
    ra = math.radians(ra_0_to_360 if ra_0_to_360 <= 180 else ra_0_to_360 - 360)
    dec = math.radians(float(columns[2]))
    l_0_to_360 = float(columns[3])
    l = math.radians(l_0_to_360 if l_0_to_360 <= 180 else l_0_to_360 - 360)
    b = math.radians(float(columns[4]))
    K_s = float(columns[5])
    z = float(columns[6]) / 300000
    source = columns[7]
    if source == 'F' or source == 'C' or source == 'O' or source == 'D': 
        Fast.append((ra,dec,z))
    elif source == '6':
        df.append((ra,dec,z))
    elif source == 'N' or source == 'M':
        Ned.append((ra,dec,z))
    elif source == 'S':
        SDSS.append((ra,dec,z))



fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection = 'hammer')
plt.suptitle('Full Sample')
grid(True)
plt.figure(fig1.number)
p1, = plt.plot([float(coord[0]) for coord in Fast], [float(coord[1]) for coord in Fast], marker = "o", mfc = 'red', mec = 'red', linestyle = "none", ms = 1, label = "FAST")
p2, = plt.plot([float(coord[0]) for coord in df], [float(coord[1]) for coord in df], marker = "o", mfc = 'green', mec = 'green', ms = 1, linestyle = "none", label = "6dF")
p3, = plt.plot([float(coord[0]) for coord in Ned], [float(coord[1]) for coord in Ned], marker = "o", mfc = 'blue', mec = 'blue', ms = 1, linestyle = "none", label = "Ned")
p4, = plt.plot([float(coord[0]) for coord in SDSS], [float(coord[1]) for coord in SDSS], marker = "o", mfc = 'magenta', mec = 'magenta', ms = 1, linestyle = "none", label = "SDSS")
#plt.figure(fig1.number)
#handles, labels = ax1.get_legend_handles_labels()
#h, l =  legend_line(handles, labels, 4)
ax1.legend(numpoints= 1, fontsize = 'xx-small', bbox_to_anchor=(0, 0, 1, 1), loc = "upper right")


fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection = 'hammer')
plt.suptitle('Fast + CTIO + ZCAT + McDonald ')
grid(True)
plt.figure(fig2.number)
plt.plot([float(coord[0]) for coord in Fast], [float(coord[1]) for coord in Fast], marker = "o", mfc = 'red', mec = 'red', ms = 1, linestyle = "none")
        
fig3 = plt.figure()
ax3 = fig3.add_subplot(111, projection = 'hammer')
plt.suptitle('6dF')
grid(True)
plt.figure(fig3.number)
plt.plot([float(coord[0]) for coord in df], [float(coord[1]) for coord in df], marker = "o", mfc = 'green', mec = 'green', ms = 1, linestyle = "none")

fig4 = plt.figure()
ax4 = fig4.add_subplot(111, projection = 'hammer')
plt.suptitle('Ned')
grid(True)
plt.figure(fig4.number)
plt.plot([float(coord[0]) for coord in Ned], [float(coord[1]) for coord in Ned], marker = "o", mfc = 'blue', mec = 'blue', ms = 1, linestyle = "none")

fig5 = plt.figure()
ax5 = fig5.add_subplot(111, projection = 'hammer')
plt.suptitle('SDSS')
grid(True)
plt.figure(fig5.number)
plt.plot([float(coord[0]) for coord in SDSS], [float(coord[1]) for coord in SDSS], marker = "o", mfc = 'magenta', mec = 'magenta', ms = 1, linestyle = "none")

fig6 = plt.figure()
ax6 = fig6.add_subplot(111, projection = 'hammer')
plt.suptitle('Full Sample Z distribution')
grid(True)
zplot([float(coord[0]) for coord in SDSS], [float(coord[1]) for coord in SDSS], [float(coord[2]) for coord in SDSS])
zplot([float(coord[0]) for coord in Ned], [float(coord[1]) for coord in Ned], [float(coord[2]) for coord in Ned])
zplot([float(coord[0]) for coord in df], [float(coord[1]) for coord in df], [float(coord[2]) for coord in df])
zplot([float(coord[0]) for coord in Fast], [float(coord[1]) for coord in Fast], [float(coord[2]) for coord in Fast])
#plt.figure(fig6.number)
#handles6, labels6 = ax6.get_legend_handles_labels()
#h6, l6 = legend_line(handles6, labels6, 5)
ax6.legend(numpoints = 1, fontsize = 'xx-small', bbox_to_anchor=(0, 0, 1, 1), loc = "upper right")

fig7 = plt.figure()
ax7 = fig7.add_subplot(111, projection = 'hammer')
plt.suptitle('Fast + CTIO + ZCAT + McDonald  Z distribution')
grid(True)
#fast_ra = [float(coord[0]) for coord in Fast]
#fast_dec = [float(coord[1]) for coord in Fast]
#fast_z = [float(coord[2]) for coord in Fast]
#zplot(fast_ra, fast_dec, fast_z)
zplot([float(coord[0]) for coord in Fast], [float(coord[1]) for coord in Fast], [float(coord[2]) for coord in Fast])
#plt.figure(fig7.number)
#handles7, labels7 = ax7.get_legend_handles_labels()
#h7, l7 = legend_line(handles7, labels7, 5)
ax7.legend(numpoints = 1, fontsize = 'xx-small', bbox_to_anchor=(0, 0, 1, 1), loc = "upper right")



fig8 = plt.figure()
ax8 = fig8.add_subplot(111, projection = 'hammer')
plt.suptitle('6dF Z distribution')
grid(True)
zplot([float(coord[0]) for coord in df], [float(coord[1]) for coord in df], [float(coord[2]) for coord in df])
#plt.figure(fig8.number)
#handles8, labels8 = ax8.get_legend_handles_labels()
#h8, l8 = legend_line(handles8, labels8, 5)
ax8.legend(numpoints = 1, fontsize = 'xx-small', bbox_to_anchor=(0, 0, 1, 1), loc = "upper right")


fig9 = plt.figure()
ax9 = fig9.add_subplot(111, projection = 'hammer')
plt.suptitle('Ned Z distribution')
grid(True)
zplot([float(coord[0]) for coord in Ned], [float(coord[1]) for coord in Ned], [float(coord[2]) for coord in Ned])
#plt.figure(fig9.number)
#handles9, labels9 = ax9.get_legend_handles_labels()
#h9, l9 = legend_line(handles9, labels9, 5)
ax9.legend(numpoints = 1, fontsize = 'xx-small', bbox_to_anchor=(0, 0, 1, 1), loc = "upper right")


fig10 = plt.figure()
ax10 = fig10.add_subplot(111, projection = 'hammer')
plt.suptitle('SDSS Z distribution')
grid(True)
zplot([float(coord[0]) for coord in SDSS], [float(coord[1]) for coord in SDSS], [float(coord[2]) for coord in SDSS])
#plt.figure(fig10.number)
#handles10, labels10 = ax10.get_legend_handles_labels()
#h10, l10 = legend_line(handles10, labels10, 5)
ax10.legend(numpoints = 1, fontsize = 'xx-small', bbox_to_anchor=(0, 0, 1, 1), loc = "upper right")




# Based on coordinate systems, these statements can be substituted above.
#
#    ra = float(columns[1])
#    dec = float(columns[2])
#    l_0_to_360 = float(columns[3])
#    l = math.radians(l_0_to_360 if l_0_to_360 <= 180 else l_0_to_360 - 360)
#    b = math.radians(float(columns[4]))
#
#    ra_0_to_360 = float(columns[1])
#    ra = math.radians(ra_0_to_360 if ra_0_to_360 <= 180 else ra_0_to_360 - 360)
#    dec = math.radians(float(columns[2]))
#    l = float(columns[3])
#    b = float(columns[4])
#    clr = "#%02x%02x%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#   plot(l, b, marker = "o", mfc = 'black', ms = 1, linestyle = "none")

f.close()

print "6dF =", len(df), "FLWO + CTIO + ZCAT + McDonald=", len(Fast), "SDSS =", len(SDSS), "Ned + Ned-alt =", len(Ned)

#plt.show()


pp.savefig(fig1)
pp.savefig(fig6)
pp.savefig(fig2)
pp.savefig(fig7)
pp.savefig(fig3)
pp.savefig(fig8)
pp.savefig(fig4)
pp.savefig(fig9)
pp.savefig(fig5)
pp.savefig(fig10)
pp.close()
#savefig("hammer-Fast.png")
#savefig("hammer-6dF.png")
#savefig("hammer-Ned.png")
#savefig("hammer-SDSS.png")

print(datetime.now()- starttime)