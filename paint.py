import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker


test_SNR = np.arange(0, 22, 2)
AER = np.abs(np.random.randn(3, 11)/1e3)
xtick = np.arange(0, 21, 5)
fontsmall = 12
fontbig = 15
width = .8

rc = {"font.family" : "serif", "mathtext.fontset" : "stix"}
plt.rcParams.update(rc)
plt.rcParams["font.serif"] = ["Times New Roman"] + plt.rcParams["font.serif"]
fig, ax = plt.subplots()
fig.set_size_inches(6.3, 5.25)
kw = dict(markersize=11.3, markerfacecolor='none', markeredgewidth=1, linewidth=.8, clip_on=False)    # clip: outside marker
ax.semilogy(test_SNR, AER[0], 'b-o', label=r'Proposed $\mathit{k}$ = 5' , **kw)
ax.semilogy(test_SNR, AER[1], 'r-->', label=r'Proposed $\mathit{k}$ = 10', **kw)
ax.semilogy(test_SNR, AER[2], 'k:s', label=r'Proposed $\mathit{k}$ = 15', **kw)
legend = ax.legend(loc='lower left', fontsize=fontsmall, markerscale=.8, framealpha=1, edgecolor='black', fancybox=False, borderpad=.25)
legend.get_frame().set_linewidth(width)
ax.set_xlabel('SNR (dB)', fontsize=fontbig)
ax.set_ylabel('ADEP', fontsize=fontbig)
ax.grid(which='major', alpha=.6)
ax.grid(which='minor', linestyle = ':', alpha=.5)
ax.set_xticks(xtick)
ax.set_xlim(test_SNR[0], test_SNR[-1])
ax.set_yscale('log',nonpositive='mask')
ax.tick_params(axis="x", which='both', direction="in", pad=6, labelsize=fontsmall)    # pad: distance to border
ax.tick_params(axis="y", which='both', direction="in", pad=6, labelsize=fontsmall)
# ax.yaxis.set_minor_formatter(ticker.ScalarFormatter())    # scalar not power
# ax.yaxis.set_minor_formatter(ticker.FormatStrFormatter('%.1f'))    # float number
# ax.yaxis.set_major_formatter(ticker.ScalarFormatter())
# ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

# box and arrow
ymax = np.min(AER)
xmax = np.argmin(AER[np.where(AER==ymax)[0][0]])
text = "min: {:.1f}e-2\n{:.1f}e-2\n{:.1f}e-4".format(min(AER[2])*1e2, min(AER[1])*1e2, min(AER[0])*1e4)
xytext = (0.53,0.155)    # box location
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=width)    # pad: box size
arrowprops=dict(arrowstyle="->")
kw = dict(xycoords='data',textcoords="axes fraction",
            bbox=bbox_props, ha="right", va="top", arrowprops=arrowprops)
ax.annotate(text, xy=(test_SNR[xmax], ymax), xytext=xytext, fontsize=fontsmall, **kw)    # xy: arrow destination

# upper left scale
ax.text(-0.002, 1.02, r'$\times 10^{3}$',    # xy loc, text
        fontsize=fontsmall,
        horizontalalignment='center',
        verticalalignment='center',
        rotation=0,
        transform=ax.transAxes)
plt.savefig('snr.pdf')
plt.show()
