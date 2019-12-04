# http://stackoverflow.com/questions/13583153/how-to-zoomed-a-portion-of-image-and-insert-in-the-same-plot-in-matplotlib
#  https://github.com/NelleV/jhepc/tree/master/2013/entry10
#  https://ocefpaf.github.io/python4oceanographers/blog/2013/12/09/zoom/

#  https://pythonhosted.org/plottools/generated/plottools.zoom_axes.html
# http://btabibian.com/notebooks/learnpython/scientific-computing/lecture-4-matplotlib/
#
# # http://akuederle.com/matplotlib-zoomed-up-inset
# fig, ax = plt.subplots() # create a new figure with a default 111 subplot
# ax.plot(overview_data_x, overview_data_y)
#
# from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
# axins = zoomed_inset_axes(ax, 2.5, loc=2) # zoom-factor: 2.5, location: upper-left
#
# axins.plot(overview_data_x, overview_data_y)
#
# x1, x2, y1, y2 = 47, 60, 3.7, 4.6 # specify the limits
# axins.set_xlim(x1, x2) # apply the x-limits
# axins.set_ylim(y1, y2) # apply the y-limits
#
# plt.yticks(visible=False)
# plt.xticks(visible=False)
#
#
# from mpl_toolkits.axes_grid1.inset_locator import mark_inset
# mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")
#

# https://stackoverflow.com/questions/26223937/matplotlib-pandas-zoom-part-of-a-plot-with-time-series
from collections import Counter

from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, inset_axes

# https://stackoverflow.com/questions/24035118/different-x-and-y-scale-in-zoomed-inset-matplotlib
# # Load the time series
#  https://matplotlib.org/3.1.0/gallery/axes_grid1/inset_locator_demo2.html#sphx-glr-gallery-axes-grid1-inset-locator-demo2-py
# ts = pd.read_csv('EUR_CHF_daily.csv',sep=';', parse_dates=['time'], index_col = 'time',decimal=',')
# ts = ts['EUR/CHF']
# ts = ts.sort_index(ascending=True)
from legacy.feature_extraction import load_pickle_data

#
# # plt.subplot(2,3,i+1)  # plt.subplot(131)
srcIP = '192.168.10.5'
bins = 10000
input_file = f'input_data/CICIDS2017/Merged-WorkingHours/5_bots_20170707-09_00-12_00-srcIP_{srcIP}.pcap_IAT_flows_len.txt'
print(f'input_file: {input_file}')
IAT_arr = load_pickle_data(input_file)
print(f'{Counter(IAT_arr)}')
# plt.figure()
# plt.hist(IAT_arr, bins='auto')
# plt.show()
# # print(f'{Counter(IAT_arr)}')
# quant = 0.9
# thres= int(np.quantile(IAT_arr, q=quant))
# print(f'thres: {thres}, quantile = {quant}')
# stat_data(np.array(IAT_arr).reshape(-1,1))
# if rescale_flg:
#     IAT_arr = [value for value in IAT_arr if value < 25]
#     bins = 30
# # plot_histgram(IAT_arr, title=f'srcIP:{srcIP}, quantile:{quant}, length_IAT:{thres}')
# title = f'srcIP:{srcIP}, \nquantile:{quant}, \nlength_IAT:{thres}'

# # plt.title(f"{title}")
# # plt.ylabel('Counts')
# # # plt.xlabel('Number of packets in each flow')
# # plt.xlabel('Flow length')
# # plt.show()
# # Plot
# fig, ax = plt.subplots() # create a new figure with a default 111 subplot
# # ax = plt.axes()
# ax.plot(IAT_arr)
# # ax.hist(IAT_arr, bins=bins)  # arguments are passed to np.histogram
#
# # Label the axis
# ax.set_xlabel('')
# ax.set_ylabel('EUR/CHF')
#
# #I want to select the x-range for the zoomed region. I have figured it out suitable values
# # by trial and error. How can I pass more elegantly the dates as something like
# x1 = 1.00
# x2 = 10.0
#
# # select y-range for zoomed region
# y1 = 0
# y2 = 3000
# # Make the zoom-in plot:
# axins = zoomed_inset_axes(ax, 1.5, loc=1) # zoom-factor: 2.5, location: upper-left
# axins.plot(IAT_arr)
# # axins.hist(IAT_arr, bins=bins)
# axins.set_xlim(x1, x2)
# axins.set_ylim(y1, y2)
# plt.xticks(visible=True)
# plt.yticks(visible=True)
# #
# # # draw a bbox of the region of the inset axes in the parent axes and
# # # connecting lines between the bbox and the inset axes area
# # mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")
# # # plt.draw()
# # plt.show()
# import matplotlib.pyplot as plt
#
# from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset
# from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
#
# import numpy as np
#
#
# def get_demo_image():
#     from matplotlib.cbook import get_sample_data
#     import numpy as np
#     f = get_sample_data("axes_grid/bivariate_normal.npy", asfileobj=False)
#     z = np.load(f)
#     # z is a numpy array of 15x15
#     return z, (-3, 4, -4, 3)

# fig, (ax, ax2) = plt.subplots(ncols=2, figsize=[6, 3])
fig, ax2 = plt.subplots(figsize=[6, 3])
#
# # First subplot, showing an inset with a size bar.
# ax.set_aspect(1)
#
# axins = zoomed_inset_axes(ax, zoom=0.5, loc='upper right')
# # fix the number of ticks on the inset axes
# axins.yaxis.get_major_locator().set_params(nbins=7)
# axins.xaxis.get_major_locator().set_params(nbins=7)
#
# plt.setp(axins.get_xticklabels(), visible=False)
# plt.setp(axins.get_yticklabels(), visible=False)
#
#
# def add_sizebar(ax, size):
#     asb = AnchoredSizeBar(ax.transData,
#                           size,
#                           str(size),
#                           loc=8,
#                           pad=0.1, borderpad=0.5, sep=5,
#                           frameon=False)
#     ax.add_artist(asb)

# add_sizebar(ax, 0.5)
# add_sizebar(axins, 0.5)

#
# # Second subplot, showing an image with an inset zoom
# # and a marked inset
# Z, extent = get_demo_image()
# Z2 = np.zeros([150, 150], dtype="d")
# ny, nx = Z.shape
# # Z2[30:30 + ny, 30:30 + nx] = Z
#
# # extent = [-3, 4, -4, 3]
# ax2.imshow(Z, extent=extent, interpolation="nearest",
#           origin="lower")

ax2.hist(IAT_arr, bins=bins)
ax2.set_ylim(0, 8000)

axins2 = zoomed_inset_axes(ax2, 10, loc=4)  # zoom = 6
axins2 = inset_axes(ax2, 2, 1, loc=2, bbox_to_anchor=(0.2, 0.55), bbox_transform=ax2.figure.transFigure)  # no zoom
# axins2.imshow(Z, extent=extent, interpolation="nearest",
#               origin="lower")

axins2.hist(IAT_arr, bins=bins)
# sub region of the original image
x1, x2, y1, y2 = 0, 10, 0, 8000
axins2.set_xlim(x1, x2)
axins2.set_ylim(y1, y2)
# fix the number of ticks on the inset axes
axins2.yaxis.get_major_locator().set_params(nbins=7)
axins2.xaxis.get_major_locator().set_params(nbins=7)

plt.setp(axins2.get_xticklabels(), visible=True)
plt.setp(axins2.get_yticklabels(), visible=True)

# draw a bbox of the region of the inset axes in the parent axes and
# connecting lines between the bbox and the inset axes area
mark_inset(ax2, axins2, loc1=2, loc2=4, fc="none", ec="0.5")

plt.show()
