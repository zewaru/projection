# Code for getting sky projection
# Matplotlib does not allow change in x axis limits without a lot of changes and 
# rewriting of how the projection is made. So I am going to keep the x limits fro -180
# to  +180. But since my data goes from 0 to 360, I am changing how it is displayed.
# Data with RA 0 to 180 is not transposed. Data with RA from 180 to 360 is  transposed
# to -180 to 0.I make plots with ra and dec and L and b. Also a final plot with no colors
# so as to make comparison with Huchra's plots easier.


from matplotlib.pyplot import subplot
from matplotlib.pyplot import savefig
import matplotlib.pyplot as plt
import matplotlib.pylab
from matplotlib.backends.backend_pdf import PdfPages
import math
import random
from pylab import subplot,savefig,grid,plot, legend

def zplot(z):
    if z <= 0.01:
        plt.plot(ra, dec, marker = "o", mfc = 'red', mec = 'red', ms = 1.8, linestyle = "none", label = "z <= 0.01")
    elif 0.01 <= z <= 0.02:
        plt.plot(ra, dec, marker = "o", mfc = 'green', mec = 'green', ms = 1.8, linestyle = "none", label = "0.01 <= z <= 0.02")
    elif 0.02 <= z <= 0.03:
        plt.plot(ra, dec, marker = "o", mfc = 'blue', mec = 'blue', ms = 1.8, linestyle = "none", label = "0.02 <=z <= 0.03")
    elif 0.03 <= z <= 0.04:
        plt.plot(ra, dec, marker = "o", mfc = 'black', mec = 'black', ms = 1.8, linestyle = "none", label = "0.03 <= z <= 0.04")
    else:
        plt.plot(ra, dec, marker = "o", mfc = 'white', mec = 'black', ms = 1.8, linestyle = "none", label = "0.04 <= z ")

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




f = open("sky-distribution.dat", 'r')

f.seek(0)

Fast = 0
dF = 0
NED = 0
SDSS = 0

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection = 'hammer')
plt.suptitle('Full Sample')
grid(True)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection = 'hammer')
plt.suptitle('Fast + CTIO + ZCAT + McDonald ')
grid(True)
fig3 = plt.figure()
ax3 = fig3.add_subplot(111, projection = 'hammer')
plt.suptitle('6dF')
grid(True)
fig4 = plt.figure()
ax4 = fig4.add_subplot(111, projection = 'hammer')
plt.suptitle('NED')
grid(True)
fig5 = plt.figure()
ax5 = fig5.add_subplot(111, projection = 'hammer')
plt.suptitle('SDSS')
grid(True)
fig6 = plt.figure()
ax6 = fig6.add_subplot(111, projection = 'hammer')
plt.suptitle('Full Sample Z distribution')
grid(True)
fig7 = plt.figure()
ax7 = fig7.add_subplot(111, projection = 'hammer')
plt.suptitle('Fast + CTIO + ZCAT + McDonald  Z distribution')
grid(True)
fig8 = plt.figure()
ax8 = fig8.add_subplot(111, projection = 'hammer')
plt.suptitle('6dF Z distribution')
grid(True)
fig9 = plt.figure()
ax9 = fig9.add_subplot(111, projection = 'hammer')
plt.suptitle('NED Z distribution')
grid(True)
fig10 = plt.figure()
ax10 = fig10.add_subplot(111, projection = 'hammer')
plt.suptitle('SDSS Z distribution')
grid(True)

#mec_choice = ['black', 'red', 'green', 'blue', 'magenta', 'white']

pp = PdfPages('hammer-eq-col.pdf')


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
        plt.figure(fig2.number)
        plt.plot(ra, dec, marker = "o", mfc = 'red', mec = 'red', ms = 1, linestyle = "none")
        plt.figure(fig1.number)
        plt.plot(ra, dec, marker = "o", mfc = 'red', mec = 'red', linestyle = "none", ms = 1, label = "FAST")
        plt.figure(fig6.number)
        zplot(z)
        plt.figure(fig7.number)
        zplot(z)
        Fast += 1
    elif source == '6':
        plt.figure(fig3.number)
        plt.plot(ra, dec, marker = "o", mfc = 'green', mec = 'green', ms = 1, linestyle = "none")
        plt.figure(fig1.number)
        plt.plot(ra, dec, marker = "o", mfc = 'green', mec = 'green', ms = 1, linestyle = "none", label = "6dF")
        plt.figure(fig6.number)
        zplot(z)
        plt.figure(fig8.number)
        zplot(z)
        dF += 1
    elif source == 'N' or source == 'M':
        plt.figure(fig4.number)
        plt.plot(ra, dec, marker = "o", mfc = 'blue', mec = 'blue', ms = 1, linestyle = "none")
        plt.figure(fig1.number)
        plt.plot(ra, dec, marker = "o", mfc = 'blue', mec = 'blue', ms = 1, linestyle = "none", label = "NED")
        plt.figure(fig6.number)
        zplot(z)
        plt.figure(fig9.number)
        zplot(z)
        NED += 1
    elif source == 'S':
        plt.figure(fig5.number)
        plt.plot(ra, dec, marker = "o", mfc = 'magenta', mec = 'magenta', ms = 1, linestyle = "none")
        plt.figure(fig1.number)
        plt.plot(ra, dec, marker = "o", mfc = 'magenta', mec = 'magenta', ms = 1, linestyle = "none", label = "SDSS")
        plt.figure(fig6.number)
        zplot(z)
        plt.figure(fig10.number)
        zplot(z)
        SDSS += 1

plt.figure(fig1.number)
handles, labels = ax1.get_legend_handles_labels()
h, l =  legend_line(handles, labels, 4)
ax1.legend(h, l, fontsize = 'xx-small', bbox_to_anchor=(0, 0, 1, 1), loc = "upper right")

plt.figure(fig6.number)
handles6, labels6 = ax6.get_legend_handles_labels()
h6, l6 = legend_line(handles6, labels6, 5)
ax6.legend(h6, l6, fontsize = 'xx-small', bbox_to_anchor=(0, 0, 1, 1), loc = "upper right")

plt.figure(fig7.number)
handles7, labels7 = ax7.get_legend_handles_labels()
h7, l7 = legend_line(handles7, labels7, 5)
ax7.legend(h7, l7, fontsize = 'xx-small', bbox_to_anchor=(0, 0, 1, 1), loc = "upper right")

plt.figure(fig8.number)
handles8, labels8 = ax8.get_legend_handles_labels()
h8, l8 = legend_line(handles8, labels8, 5)
ax8.legend(h8, l8, fontsize = 'xx-small', bbox_to_anchor=(0, 0, 1, 1), loc = "upper right")

plt.figure(fig9.number)
handles9, labels9 = ax9.get_legend_handles_labels()
h9, l9 = legend_line(handles9, labels9, 5)
ax9.legend(h9, l9, fontsize = 'xx-small', bbox_to_anchor=(0, 0, 1, 1), loc = "upper right")

plt.figure(fig10.number)
handles10, labels10 = ax10.get_legend_handles_labels()
h10, l10 = legend_line(handles10, labels10, 5)
ax10.legend(h10, l10, fontsize = 'xx-small', bbox_to_anchor=(0, 0, 1, 1), loc = "upper right")




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

print "6dF =", dF, "FLWO + CTIO + ZCAT + McDonald=", Fast, "SDSS =", SDSS, "NED + NEd-alt =", NED

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
#savefig("hammer-NED.png")
#savefig("hammer-SDSS.png")

