import matplotlib
matplotlib.use('QT5Agg')
import matplotlib.pyplot as plt
import os, datetime
from scipy import misc, ndimage
from skimage import color
import skimage.measure
from core.Tint_Matlab import getpos, centerBox, remBadTrack
import numpy as np
import scipy
import scipy.signal
from core.GUI_Utils import print_msg
import pandas as pd
import math


def speed2d(x, y, t):
    dx = np.diff(x.flatten())
    dy = np.diff(y.flatten())
    dt = np.diff(t.flatten())

    speed = np.sqrt(dx ** 2 + dy ** 2) / dt

    return speed


def findArenaShape(posx, posy, arena_shape, self=None):
    # calculating if the arena is a circle or not
    points = np.hstack((posx.reshape((len(posx), 1)),
                        posy.reshape((len(posy), 1))))  # making an array [x1, y1;x2,y2,...]

    if arena_shape is None:

        msg = '[%s %s]: Determining the shape of the arena!' % (
                    str(datetime.datetime.now().date()),
                    str(datetime.datetime.now().time())[:8])

        print_msg(self, msg)

        # check if it is a square or a circle arena by looking at the corners
        bin_x = np.linspace(np.amin(posx), np.amax(posx), 11)
        bin_y = np.linspace(np.amin(posx), np.amax(posx), 11)

        corners = np.array([[bin_x[-2], bin_y[-2]], [bin_x[1], bin_y[-2]],
                            [bin_x[1], bin_y[1]], [bin_x[-2], bin_y[1]]])

        plot_corners = False
        if plot_corners:
            # plots to see the test if it is a square or cirlce. I essentially
            # determine if there is data at the corners of the arena
            fig_corners = plt.figure(figsize=(5, 5))
            ax_corners = fig_corners.add_subplot(111)
            ax_corners.plot(posx, posy, 'r-')
            ax_corners.plot(corners[0:2, 0], corners[0:2, 1], 'g')
            ax_corners.plot(corners[1:3, 0], corners[1:3, 1], 'g')
            ax_corners.plot(corners[[0, 3], 0], corners[[0, 3], 1], 'g')
            ax_corners.plot(corners[[2, 3], 0], corners[[2, 3], 1], 'g')

        circle_bool = []
        for corner in range(4):
            # for each corner, see if there is data in the corners
            if corner == 0:  # NE corner
                bool_val = (points[:, 0] >= 0) * (points[:, 1] >= 0)
                current_points = points[bool_val, :]

                circle_bool.append(np.sum((current_points[:, 0] >= corners[corner, 0]) *
                                          (current_points[:, 1] >= corners[corner, 1])))

            elif corner == 1:  # NW Corner
                bool_val = (points[:, 0] < 0) * (points[:, 1] >= 0)
                current_points = points[bool_val, :]

                circle_bool.append(np.sum((current_points[:, 0] < corners[corner, 0]) *
                                          (current_points[:, 1] >= corners[corner, 1])))

            elif corner == 2:  # SW Corner
                bool_val = (points[:, 0] < 0) * (points[:, 1] < 0)
                current_points = points[bool_val, :]

                circle_bool.append(np.sum((current_points[:, 0] <= corners[corner, 0]) *
                                          (current_points[:, 1] < corners[corner, 1])))

            else:  # SE corner
                bool_val = (points[:, 0] > 0) * (points[:, 1] < 0)
                current_points = points[bool_val, :]

                circle_bool.append(np.sum((current_points[:, 0] > corners[corner, 0]) *
                                          (current_points[:, 1] < corners[corner, 1])))

        if sum(circle_bool) >= 1:
            shape = 'Rectangular'

            msg = '[%s %s]: Arena detected as being rectangular.' % (
                        str(datetime.datetime.now().date()),
                        str(datetime.datetime.now().time())[:8])
            print_msg(self, msg)

        else:
            shape = 'Circle'

            msg = '[%s %s]: Arena detected as being circular.' % (
                    str(datetime.datetime.now().date()),
                    str(datetime.datetime.now().time())[:8])

            print_msg(self, msg)
    else:
        shape = arena_shape

    return shape


def getPosValues(set_filename, ppm=None, center=None, self=None):

    directory = os.path.dirname(set_filename)

    session = os.path.splitext(os.path.basename(set_filename))[0]  # get the session name (basename of .set file)

    posfile = os.path.join(directory, session + '.pos')  # defining the position filename

    if not os.path.exists(posfile):
        msg = '[%s %s]: the following position file does not exist, skipping: %s.' % (
                str(datetime.datetime.now().date()),
                str(datetime.datetime.now().time())[:8], posfile)
        print_msg(self, msg)
        raise FileNotFoundError

    msg = '[%s %s]: Loading position data.' % (
            str(datetime.datetime.now().date()),
            str(datetime.datetime.now().time())[:8])
    print_msg(self, msg)

    posx, posy, post, Fs_pos = getpos(posfile, ppm=ppm, center=center, flip_y=False)  # getting the mouse position

    if center is None:
        # then we will use the behavior to center
        # centering the positions
        center = centerBox(posx, posy)
        posx = posx - center[0]
        posy = posy - center[1]

    posy = -posy  # flip the y like we do in Tint, wanted to make sure we flip after we center

    # Threshold for how far a mouse can move (100cm/s), in one sample (sampFreq = 50 Hz
    threshold = 100 / 50  # defining the threshold

    posx, posy, post = remBadTrack(posx, posy, post, threshold)  # removing bad tracks (faster than threshold)

    nonNanValues = np.where(np.isnan(posx) == False)[0]
    # removing any NaNs
    post = post[nonNanValues]
    posx = posx[nonNanValues]
    posy = posy[nonNanValues]

    if len(posx) == 0:
        msg = '[%s %s]: There are no valid positions (all NaNs)' % (
                str(datetime.datetime.now().date()),
                str(datetime.datetime.now().time())[:8])

        print_msg(self, msg)
        raise Exception("No valid positions!")

    msg = '[%s %s]: Smoothing the position data' % (
            str(datetime.datetime.now().date()),
            str(datetime.datetime.now().time())[:8])

    print_msg(self, msg)

    # box car smoothing, closest we could get to replicating Tint's speeds
    B = np.ones((int(np.ceil(0.4 * Fs_pos)), 1)) / np.ceil(0.4 * Fs_pos)
    posx = scipy.ndimage.convolve(posx, B, mode='nearest')
    posy = scipy.ndimage.convolve(posy, B, mode='nearest')

    return posx, posy, post, Fs_pos, center


def runAnalysis(session_path, save_directory, geometry=None, ppm=None, center=None, arena_shape='Auto',
                bin_label=None, radii=None, outer_radius=None, rect_arena_length=None, rect_arena_width=None,
                self=None):

    session = os.path.splitext(os.path.basename(session_path))[0]  # get the session name (basename of .set file)

    msg = '[%s %s]: Analyzing the following session: %s!' % (
        str(datetime.datetime.now().date()),
        str(datetime.datetime.now().time())[:8], session)

    print_msg(self, msg)

    # get position

    posx, posy, post, Fs_pos, center = getPosValues(session_path, ppm=ppm, center=center, self=self)

    center_original = center

    # since we have moved the center to 0,0. We will define this as the new center
    center = [0, 0]

    # find the arena shape
    if arena_shape is None and self is not None:
        arena_shape = self.arena_shape.currentText()

    if arena_shape == 'Auto':
        arena_shape = None

    arena_shape = findArenaShape(posx, posy, arena_shape, self=self)

    if geometry is None and self is not None:
        if arena_shape == 'Circle':
            geometry = (int(self.settings_window.num_inner.text()),
                        int(self.settings_window.num_outer.text()))
        elif arena_shape == 'Rectangular':
            geometry = (int(self.settings_window.num_rows.text()),
                        int(self.settings_window.num_cols.text()))
        else:
            raise Exception("Invalid Arena Shape!")
    elif geometry is not None:
        pass
    else:
        raise Exception("Invalid Arena Shape!")

    if radii is None and self is not None:
        radii = [float(self.settings_window.inner_rad.text())]
    else:
        if arena_shape == 'Circle':
            raise Exception("Invalid Radius value!")

    original_radii = radii[0]

    # get the arena bounds and labels
    x_bounds = None
    y_bounds = None
    if arena_shape == 'Rectangular':
        if rect_arena_length is None:
            if self is not None:
                rect_arena_length = self.settings_window.rect_length.text()
                if rect_arena_length == '':
                    # use the behavior boundaries to find the x value boundaries
                    rect_arena_length = 2 * np.max(np.abs([np.min(posx), np.max(posx)]))
                else:
                    try:
                        rect_arena_length = float(rect_arena_length)
                    except:
                        raise Exception("rect_arena_length cannot be converted to a float!")

                    rect_arena_length_behavior = 2 * np.max(np.abs([np.min(posx), np.max(posx)]))
                    if rect_arena_length_behavior > rect_arena_length:
                        msg = '[%s %s]: The provided Arena Length is smaller than what is found in the behavior (%f), using the behavior value instead!#Red' % (
                            str(datetime.datetime.now().date()),
                            str(datetime.datetime.now().time())[:8], rect_arena_length_behavior)
                        print_msg(self, msg)

                        rect_arena_length = rect_arena_length_behavior

            else:
                # use the behavior boundaries to find the x value boundaries
                rect_arena_length = 2 * np.max(np.abs([np.min(posx), np.max(posx)]))

        # the user provided a length, use this as well as the center value to determine the
        # x boundaries
        x_bounds = [center[0] - rect_arena_length / 2, center[0] + rect_arena_length / 2]

        if rect_arena_width is None:
            if self is not None:
                rect_arena_width = self.settings_window.rect_width.text()
                if rect_arena_width == '':
                    # use the behavior to find the y value boundaries
                    rect_arena_width = 2 * np.max(np.abs([np.min(posy), np.max(posy)]))
                else:
                    try:
                        rect_arena_width = float(rect_arena_width)
                    except:
                        raise ValueError

                    rect_width_behavior = 2 * np.max(np.abs([np.min(posy), np.max(posy)]))
                    if rect_width_behavior > rect_arena_width:
                        msg = '[%s %s]: The provided Arena Width is smaller than what is found in the behavior (%f), using the behavior value instead!#Red' % (
                            str(datetime.datetime.now().date()),
                            str(datetime.datetime.now().time())[:8], rect_width_behavior)
                        print_msg(self, msg)

                        rect_arena_width = rect_width_behavior

            else:
                # use the behavior to find the y value boundaries
                rect_arena_width = 2 * np.max(np.abs([np.min(posy), np.max(posy)]))

        # the user provided a width, use this as well as the center value to determine the
        # y boundaries
        y_bounds = [center[1] - rect_arena_width / 2, center[1] + rect_arena_width / 2]

    elif arena_shape == 'Circle':

        if outer_radius is None:
            if self is not None:
                outer_radius = self.settings_window.circle_radius.text()

                if outer_radius == '':
                    # get the radius from the behavior
                    rad_pos = np.sqrt((posx) ** 2 + (posy) ** 2).flatten()

                    # determine the outer_radius to be the max of the radii array
                    outer_radius = np.amax(rad_pos)
                else:
                    # user set the radius value
                    try:
                        outer_radius = float(outer_radius)
                    except:
                        raise ValueError

                    # get the radius from the behavior
                    rad_pos = np.sqrt((posx) ** 2 + (posy) ** 2).flatten()
                    outer_radius_behavior = np.amax(rad_pos)

                    if outer_radius_behavior > outer_radius:
                        msg = '[%s %s]: The provided Arena Radius is smaller than what is found in the behavior (%f), using the behavior value instead!#Red' % (
                            str(datetime.datetime.now().date()),
                            str(datetime.datetime.now().time())[:8], outer_radius_behavior)
                        print_msg(self, msg)

                        outer_radius = outer_radius_behavior
            else:
                # get the radius from the behavior
                rad_pos = np.sqrt((posx) ** 2 + (posy) ** 2).flatten()

                # determine the outer_radius to be the max of the radii array
                outer_radius = np.amax(rad_pos)
        else:
            # get the radius from the behavior
            rad_pos = np.sqrt((posx) ** 2 + (posy) ** 2).flatten()

            # determine the outer_radius to be the max of the radii array
            outer_radius = np.amax(rad_pos)

        x_bounds = [center[0] - outer_radius, center[0] + outer_radius]
        y_bounds = [center[1] - outer_radius, center[1] + outer_radius]

        # radii is a list of inner radii that are fractions of the outer radius, convert them to cm values
        for i, rad in enumerate(radii):
            radii[i] = rad * outer_radius

        # append the outer radius to radii
        radii = sorted(radii) + [outer_radius]

    save_settings = {'ppm': ppm, 'arena_shape': arena_shape, 'center': str(center_original)}

    if arena_shape == 'Rectangular':
        save_settings['rect_arena_width'] = rect_arena_width
        save_settings['rect_arena_length'] = rect_arena_length

    elif arena_shape == 'Circle':
        save_settings['outer_radius'] = radii[-1]

    # analyze the quadrants
    QuadrantAnalysis(session, posx, posy, post, Fs_pos, save_directory, x_bounds=x_bounds, y_bounds=y_bounds,
                     arena_shape=arena_shape, radii=radii, save_settings=save_settings, self=self)

    if bin_label is None and self is not None:
        if arena_shape == 'Circle':
            bin_label = self.settings_window.circular_labels
        elif arena_shape == 'Rectangular':
            bin_label = self.settings_window.rectangle_labels
        else:
            raise Exception("Invalid Arena Shape!")
    else:
        raise Exception("No Bin Label Provided!")

    if arena_shape == 'Circle':
        save_settings['inner_radii'] = radii[0]
        save_settings['inner_radii(%)'] = original_radii

    InnerVOuter(session_path, posx, posy, post, Fs_pos, bin_label, geometry, arena_shape=arena_shape,
                radii=radii, x_bounds=x_bounds, y_bounds=y_bounds, save_settings=save_settings, self=self)

    msg = '[%s %s]: Finished analyzing the following session: %s!' % (
        str(datetime.datetime.now().date()),
        str(datetime.datetime.now().time())[:8], session)

    print_msg(self, msg)


def getLimits(posx, posy, x_bounds=None, y_bounds=None, plot_linewidth=5.334):
    """
    This method will simply provide the x and y limits for the plotting, we want to ensure that all the plots have
    the same limits since we will be dealing with pixels.

    :param posx:
    :param posy:
    :param x_bounds:
    :param y_bounds:
    :param plot_linewidth:
    :return:
    """
    if x_bounds is None and y_bounds is None:
        dimensions = np.array([np.amin(posx), np.amax(posx), np.amin(posy), np.amax(posy)])
    else:
        dimensions = np.array([x_bounds[0], x_bounds[1], y_bounds[0], y_bounds[1]])

    xlim_values = [dimensions[0] - 2*plot_linewidth-1, dimensions[1] + 2*plot_linewidth]
    ylim_values = [dimensions[2] - 2*plot_linewidth-1, dimensions[3] + 2*plot_linewidth]

    return xlim_values, ylim_values


def getTotalArea(save_figures_directory, session, posx, posy, arena_shape, self=None, x_bounds=None, y_bounds=None,
                 plot_linewidth=5.334, debug_fig=False):

    coverage_figure = plt.figure(figsize=(5, 5))
    ax_coverage = coverage_figure.add_subplot(111)

    # get the plot xlim and ylim values
    xlim_values, ylim_values = getLimits(posx, posy, x_bounds=x_bounds, y_bounds=y_bounds)

    if arena_shape == 'Rectangular':
        # if there is data in the corners it is a square

        # find the average height and average width

        # bins = np.linspace(np.amin(posx), np.amax(posx), 20)
        # bin_edges = np.hstack((bins[0:-1].reshape((len(bins[0:-1]), 1)), bins[1:].reshape((len(bins[1:]), 1))))

        # graphing rectangle representing the arena border

        rectangle_points = np.array([[np.amin(posx), np.amax(posy)],  # NW
                                     [np.amax(posx), np.amax(posy)],  # NE
                                     [np.amax(posx), np.amin(posy)],  # SE
                                     [np.amin(posx), np.amin(posy)],  # SW
                                     [np.amin(posx), np.amax(posy)]  # NW
                                     ])

        border = ax_coverage.plot(rectangle_points[:, 0], rectangle_points[:, 1], 'b', lw=plot_linewidth)
        ax_coverage.plot(posx, posy, 'r-', lw=plot_linewidth)

        # Length * Width
        total_area_cm2 = (np.abs(np.amin(posx)) + np.amax(posx)) * (np.abs(np.amin(posy) + np.amax(posy)))

    elif arena_shape == 'Circle':
        # there were no position values in the corner, must be a circle

        bins = np.linspace(np.amin(posx), np.amax(posx), 50)

        bin_edges = np.hstack((bins[0:-1].reshape((len(bins[0:-1]), 1)),
                               bins[1:].reshape((len(bins[1:]), 1))))

        rad_pos = np.sqrt((posx) ** 2 + (posy) ** 2).flatten()

        radii = np.max(rad_pos)

        # equivalent to ang = 0:0.01:4*pi in matlab
        step = 0.001
        ang = np.arange(np.round((4 * np.pi + step) / step)) / (1 / step)

        xp, yp = circle_vals(0, 0, 2 * radii, ang)

        border = ax_coverage.plot(xp, yp, 'b', lw=plot_linewidth)
        ax_coverage.plot(posx, posy, 'r', lw=plot_linewidth)

        total_area_cm2 = np.pi * (radii ** 2)  # area = pr^2

    else:
        print('The arena_shape: %s has not be setup yet!' % arena_shape)
        return np.NaN

    ax_coverage.set_xlim(xlim_values)
    ax_coverage.set_ylim(ylim_values)

    cover_png_total = os.path.join(save_figures_directory, '%s_total.png' % session)

    if not os.path.exists(os.path.dirname(cover_png_total)):
        os.makedirs(os.path.dirname(cover_png_total))

    ax_coverage.axis('off')
    coverage_figure.savefig(cover_png_total, bbox_inches='tight', dpi=300)  # saving figure with the arena trace
    plt.close(coverage_figure)
    # now reload the image so that we can use edge detection and region props to calculate the area

    # finding the total area
    msg = '[%s %s]: Finding the total area of the arena!' % (
            str(datetime.datetime.now().date()),
            str(datetime.datetime.now().time())[:8])

    print_msg(self, msg)

    RGBA = misc.imread(cover_png_total)
    try:
        RGB = color.rgba2rgb(RGBA)
    except ValueError:
        RGB = RGBA

    I = rgb2gray(RGB)

    I = np.round(I).astype('int32')

    # create a binary gradient mask of image
    BWs_x = ndimage.sobel(I, 0)  # horizontal derivative
    BWs_y = ndimage.sobel(I, 1)  # vertical derivative
    BWs = np.hypot(BWs_x, BWs_y)  # magnitude

    BWs *= 255.0 / np.amax(BWs)  # normalize (Q&D)

    # create a dilated gradient mask
    # BWsdil = ndimage.morphology.binary_dilation(BWs)  # used to use this, but found it unnecessary
    BWdfill = ndimage.morphology.binary_fill_holes(BWs)

    area = []

    label_img = skimage.measure.label(BWdfill)
    regions = skimage.measure.regionprops(label_img)
    pixels_per_cm = None
    for prop in regions:
        area.append(prop.area)
        bbox = prop.bbox  # [miny, minx, maxy, maxx]
        dy_pixels = bbox[2] - bbox[0]
        dx_pixels = bbox[3] - bbox[1]

        pixels_per_cm_values = [dx_pixels / (np.amax(posx) - np.amin(posx)),
                                dy_pixels / (np.amax(posy) - np.amin(posy))]

        pixels_per_cm = np.mean(pixels_per_cm_values)

    total_area = max(area)

    # debug_fig = True
    if debug_fig:
        debug_fig = plt.figure(figsize=(5, 5))
        ax_debug = debug_fig.add_subplot(111)
        ax_debug.imshow(BWdfill, cmap=plt.cm.gray)
        debug_fig.show()

    os.remove(cover_png_total)

    return total_area, pixels_per_cm


def getFileArea(filename, delete_file=False, debug_figs=False, fill=False):
    """
    This method is used to find the area of a shape from a png file.

    :param filename:
    :param delete_file:
    :param debug_figs:
    :param fill:
    :return:
    """
    RGBA = misc.imread(filename)
    try:
        RGB = color.rgba2rgb(RGBA)
    except ValueError:
        RGB = RGBA

    I = rgb2gray(RGB)
    I = np.round(I).astype('int32')

    # check if the user wants to fill in the holes, used for calculating total possible area
    if fill:
        # create a binary gradient mask of image
        BWs_x = ndimage.sobel(I, 0)  # horizontal derivative
        BWs_y = ndimage.sobel(I, 1)  # vertical derivative
        BWs = np.hypot(BWs_x, BWs_y)  # magnitude

        BWs *= 255.0 / np.amax(BWs)  # normalize (Q&D)

        # create a dilated gradient mask
        # BWsdil = ndimage.morphology.binary_dilation(BWs)  # used to use this, but found it unnecessary
        BWdfill = ndimage.morphology.binary_fill_holes(BWs)
    else:
        if np.amax(I) <= 1:
            # then the image was saved from numpy
            BWdfill = I < 1
        else:
            BWdfill = I < 255

    area = []

    label_img = skimage.measure.label(BWdfill)
    regions = skimage.measure.regionprops(label_img)
    for prop in regions:
        area.append(prop.area)

    if debug_figs:
        coverage_fill_figure = plt.figure(figsize=(5, 5))
        ax_coverage_fill = coverage_fill_figure.add_subplot(111)
        ax_coverage_fill.imshow(BWdfill, cmap=plt.cm.gray)

    total_area = max(area)

    if delete_file:
        os.remove(filename)

    return total_area


def weighted_avg_and_std(values, weights):
    """
    Return the weighted average and standard deviation.

    values, weights -- Numpy ndarrays with the same shape.
    """
    average = np.average(values, weights=weights)
    # Fast and numerically precise:
    variance = np.average((values-average)**2, weights=weights)
    return (average, math.sqrt(variance))


def QuadrantAnalysis(session, posx, posy, post, Fs_pos, save_directory, x_bounds=None, y_bounds=None, arena_shape=None,
                     plot_linewidth=5.334, radii=None, debug_figs=False, save_settings=None, self=None):
    """

    :param session:
    :param posx:
    :param posy:
    :param post:
    :param Fs_pos:
    :param save_directory:
    :param x_bounds:
    :param y_bounds:
    :param arena_shape:
    :param plot_linewidth:
    :param radii:
    :param debug_figs:
    :param save_settings:
    :param self:
    :return:
    """

    # creates the excel filename
    excel_filename = os.path.join(save_directory, '%s_quadrant.xlsx' % session)

    # the file has already been analyzed
    if os.path.exists(excel_filename):
        self.LogAppend.myGUI_signal.emit(
            '[%s %s]: The following excel filename has already been analyzed, skipping: %s' % (
                str(datetime.datetime.now().date()),
                str(datetime.datetime.now().time())[:8], excel_filename))
        return

    # adds a figures directory to that QuadrantAnalysis directory to save the figures
    save_figures_directory = os.path.join(save_directory, 'Figures')

    # get the plot xlim and ylim values
    xlim_values, ylim_values = getLimits(posx, posy, x_bounds=x_bounds, y_bounds=y_bounds)

    # since we are doing quadrants, we will break this into a 2x2 arena
    geometry = (2, 2)  # break it up into quadrants
    binBounds = getBinBounds(x_bounds, y_bounds, 'Rectangular', geometry=geometry)

    # find the total area
    _, pixels_per_cm = getTotalArea(save_figures_directory, session, posx, posy, arena_shape, self=self,
                                    x_bounds=x_bounds, y_bounds=y_bounds, plot_linewidth=plot_linewidth)

    # now we will break the image up into quadrants.

    self.LogAppend.myGUI_signal.emit(
        '[%s %s]: Breaking up arena into quadrants!' % (
            str(datetime.datetime.now().date()),
            str(datetime.datetime.now().time())[:8]))

    # finding boundary lines

    possible_labels = []
    for row in range(geometry[0]):
        for col in range(geometry[1]):
            possible_labels.append(1. * (row+1) + (col+1)/100)

    # we will be forcing Rectangular arena_shape so that we get the square/rectangular bins
    labels = track_to_xylabels(posx, posy, arena_shape='Rectangular', geometry=geometry,
                               x_bounds=x_bounds, y_bounds=y_bounds)

    # labels = track_to_xylabels(posx, posy, geometry=geometry, arena_shape=arena_shape)

    # initializing the figure to plot the quadrants
    quadrant_figure = plt.figure(figsize=(5, 5))
    ax_quadrant = quadrant_figure.add_subplot(111)

    # plotting the quadrants
    plot_map_labels(posx, posy, labels, ax=ax_quadrant)

    ax_quadrant.plot(posx, posy, "k-", alpha=0.2)

    # acquiring the x tick and y tick values (the boundaries for the quadrants)
    x_ticks = np.linspace(x_bounds[0], x_bounds[1], geometry[0] + 1)
    y_ticks = np.linspace(y_bounds[0], y_bounds[1], geometry[1] + 1)

    if arena_shape == 'Rectangular':
        # then it's a rectangular arena, plot the boundaries as square/rectangular bins
        ax_quadrant.vlines(x_ticks, y_bounds[0], y_bounds[1], linestyles='dashed')
        ax_quadrant.hlines(y_ticks, x_bounds[0], x_bounds[1], linestyles='dashed')

    elif arena_shape == 'Circle':
        # plot a circular trace representing the arena, and then plot the quadrant boundaries
        # equivalent to ang = 0:0.01:4*pi in matlab
        step = 0.001

        ang = np.arange(np.round((2 * np.pi + step) / step)) / (1 / step)

        # rad_pos = np.sqrt((posx) ** 2 + (posy) ** 2).flatten()

        radii = np.amax(radii)

        xp, yp = circle_vals(0, 0, 2 * radii, ang)
        ax_quadrant.plot(xp, yp, 'k--')

        # plot the center lines
        ax_quadrant.vlines(x_ticks[1], y_bounds[0], y_bounds[1], linestyles='dashed')
        ax_quadrant.hlines(y_ticks[1], x_bounds[0], x_bounds[1], linestyles='dashed')
    else:

        msg = '[%s %s]: The arena_shape: %s has not be setup yet!' % (str(datetime.datetime.now().date()),
                                                                      str(datetime.datetime.now().time())[:8],
                                                                      arena_shape)
        print_msg(self, msg)
        return

    # setting the minimum x and y values for this figure
    ax_quadrant.set_xlim(xlim_values)
    ax_quadrant.set_ylim(ylim_values)

    # removing the x and y axis
    ax_quadrant.axis('off')
    quadrant_figurename = os.path.join(save_figures_directory, '%s_quadrants.png' % session)

    msg = '[%s %s]: Saving .png of quadrants at the following location: %s!' % (
            str(datetime.datetime.now().date()),
            str(datetime.datetime.now().time())[:8], quadrant_figurename)

    print_msg(self, msg)

    # saving the figure
    quadrant_figure.savefig(quadrant_figurename, bbox_inches='tight', dpi=300)
    plt.close(quadrant_figure)

    quadrant_number = 1

    bin_time = {}  # time (seconds) in each bin
    bin_n_entered = {}  # number of times this bin was entered
    bin_vel_avg = {}  # average velocity of each bin
    bin_vel_std = {}  # standard deviation of each bin
    bin_distance = {}  # the distance travelled in each bin
    bin_total_area = {}  # the total_area of each bin
    bin_coverage_percentage = {}

    angle_bounds = {1.01: [180, 270],  # 3rd quad
                    1.02: [90, 180],  # 2nd quad
                    2.01: [270, 360],  # 4th quad
                    2.02: [0, 90],  # 1st quad
                    }

    for label in sorted(possible_labels):
        msg = '[%s %s]: Analyzing quadrant %d!' % (
                str(datetime.datetime.now().date()),
                str(datetime.datetime.now().time())[:8], quadrant_number)
        print_msg(self, msg)

        quadrant_number += 1

        msg = '[%s %s]: Analyzing amount of time spent within the quadrant!' % (
                str(datetime.datetime.now().date()),
                str(datetime.datetime.now().time())[:8])

        print_msg(self, msg)

        label_bool = np.where(labels == label)[0]

        if len(label_bool) == 0:
            bin_time[label] = 0
            bin_n_entered[label] = 0
            bin_vel_avg[label] = 0
            bin_vel_std[label] = 0
            bin_distance[label] = 0
            bin_total_area[label] = 0
            bin_coverage_percentage[label] = 0
            continue

        consecutive_points = find_consec(label_bool)

        # bin_time[label] = len(label_bool) / Fs_pos  # the amount of time in seconds within this sector

        msg = '[%s %s]: Analyzing the number of times the animal entered this quadrant!' % (
                str(datetime.datetime.now().date()),
                str(datetime.datetime.now().time())[:8])

        print_msg(self, msg)

        bin_n_entered[label] = len(consecutive_points)  # the amount of times that the animal entered the sector

        v_total = np.array([])
        weights = np.array([])
        distance = 0
        time = 0

        msg = '[%s %s]: Analyzing the average (and standard deviation) of mouse velocity within this quadrant!' % (
                str(datetime.datetime.now().date()),
                str(datetime.datetime.now().time())[:8])

        print_msg(self, msg)

        # initializing the quadrant coverage figure
        quadrant_positions = plt.figure(figsize=(5, 5))
        quadrant_axis = quadrant_positions.add_subplot(111)

        for run in consecutive_points:

            runx = posx[run]
            runy = posy[run]
            runt = post[run]

            if len(runx) <= 2:
                continue

            # I decided to calculate time on each run as well. Used to just find how many samples are within the bin
            # and take that as the time, but the vel = distance/time relationship does not work out in that case since
            # we will be missing the distance/velocity points from when the mouse leaves one bin and enters another
            # therefore we will just calculate the time below. I subtract 1 from the length so we will start the time
            # at t=0 for each bin.

            # dTime
            dTime = np.diff(runt.flatten())

            # adding up dTime to get total time (add to time variable)
            time += np.sum(dTime)

            # difference in distances betwen points
            dDistance = np.sqrt(np.diff(runx.flatten()) ** 2 +
                                np.diff(runy.flatten()) ** 2)

            distance += np.sum(dDistance)

            v_i = dDistance/dTime
            if len(v_total) != 0:
                v_total = np.concatenate((v_total, v_i.flatten()))
            else:
                v_total = v_i.flatten()

            if len(weights) != 0:
                weights = np.concatenate((weights, dTime.flatten()))
            else:
                weights = dTime.flatten()

            # we will plot all the runs individually, won't need it for the 2x2 grid, but we do it just to ensure
            # that we have the same method as the inner vs outer method.
            quadrant_axis.plot(runx, runy, 'r-', lw=plot_linewidth)

        # setting the total time in the bin
        bin_time[label] = time  # unit: seconds

        # setting the total distance in the bin
        bin_distance[label] = distance / 100  # units: meters

        # here we will be doing a weighted average and standard dev so that we take in account the fact that there
        # will be instances where the positions are invalid, and thus the difference between points might not be
        # uniform.
        v_avg, v_sd = weighted_avg_and_std(v_total, weights)

        # v_avg = np.mean(v_total)  # finding the average velocity in this sector
        # v_sd = np.std(v_total)  # finding the standard deviation of the sector

        bin_vel_avg[label] = v_avg
        bin_vel_std[label] = v_sd

        quadrant_axis.set_xlim(xlim_values)
        quadrant_axis.set_ylim(ylim_values)

        quadrant_position_filename = os.path.join(save_figures_directory, '%s_quadrant_%s.png' % (session, label))

        quadrant_axis.axis('off')
        quadrant_positions.savefig(quadrant_position_filename, bbox_inches='tight', dpi=300)
        plt.close(quadrant_positions)

        # plotting total possible quadrant area
        label_str = str(label).replace('.', '_')
        bin_total = plt.figure(figsize=(5, 5))
        bin_total_filename = os.path.join(save_figures_directory, '%s_quad%s_total.png' % (
            session, label_str))
        bin_total_ax = bin_total.add_subplot(111)

        bin_total_ax.set_xlim(xlim_values)
        bin_total_ax.set_ylim(ylim_values)

        if arena_shape == 'Rectangular':
            plotSquareBin(*binBounds[label][:], ax=bin_total_ax)
        elif arena_shape == 'Circle':
            plotCircularSector(0, radii, angle_bounds[label][0], angle_bounds[label][1], ax=bin_total_ax, lw=5.334)

        bin_total_ax.axis('off')
        bin_total.savefig(bin_total_filename, bbox_inches='tight', dpi=300)
        plt.close(bin_total)

        # getting total possible bin area
        total_possible_bin_area = getFileArea(bin_total_filename, delete_file=True, debug_figs=False,
                                              fill=True)  # units: pixels^2

        # finding the coverage of the animal within this quadrant
        msg = '[%s %s]: Analyzing coverage within the quadrant!' % (
                str(datetime.datetime.now().date()),
                str(datetime.datetime.now().time())[:8])

        print_msg(self, msg)

        # get the quadrant coverage (area in pixels)
        quadrant_area_covered = getFileArea(quadrant_position_filename, delete_file=True, fill=False,
                                            debug_figs=debug_figs)

        # percentage of the total area that was covered in the quadrant
        bin_coverage_percentage[label] = 100 * (quadrant_area_covered / total_possible_bin_area)  # units: percent

        # quadrant area conversion to cm^2
        total_possible_bin_area = total_possible_bin_area / pixels_per_cm  # units cm^2

        # the total area of the bin
        bin_total_area[label] = total_possible_bin_area

    # save all values in an excel sheet

    data = {'Label': list(sorted(possible_labels)),
            'Time (sec)': [value for key, value in sorted(bin_time.items())],
            'N Entered': [value for key, value in sorted(bin_n_entered.items())],
            'Avg. Velocity (cm/s)': [value for key, value in sorted(bin_vel_avg.items())],
            'SD. Velocity (cm/s)': [value for key, value in sorted(bin_vel_std.items())],
            'Distance (m)': [value for key, value in sorted(bin_distance.items())],
            'Quadrant Coverage (% Quadrant Total)': [value for key, value in sorted(bin_coverage_percentage.items())],
            'Quadrant Area (cm^2)': [value for key, value in sorted(bin_total_area.items())],
            }

    # create a new worksheet

    data_df = pd.DataFrame.from_dict(data)

    # find the coverage for each quadrant, and add them up to get the total coverage
    total_coverage = sum(data_df['Quadrant Coverage (% Quadrant Total)'] * data_df['Quadrant Area (cm^2)'])  # units cm^2

    # now take the quadrant coverage, and divide them by total coverage to get the percent relative to the
    # total coverage of the mouse.
    data_df['Quadrant Coverage (% of total coverage)'] = 100 * (data_df['Quadrant Coverage (% Quadrant Total)'] *
                                                           data_df['Quadrant Area (cm^2)']) / total_coverage

    # find the total area (in cm^2)
    total_area = sum(data_df['Quadrant Area (cm^2)'])

    # normalize the quadrant area by the total area
    data_df['Quadrant Area (% of total)'] = 100 * data_df['Quadrant Area (cm^2)'] / total_area

    # adding totals
    total_label = {'Label': 'Total', 'Time (sec)': data_df['Time (sec)'].sum(),
                   'Distance (m)': data_df['Distance (m)'].sum(),
                   'Quadrant Area (cm^2)': total_area}

    data_df = data_df.append(total_label, ignore_index=True)

    # exporting to excel
    data_df.to_excel(excel_filename, index=False)

    if save_settings is not None:
        save_settings['geometry'] = str(geometry)
        for key, value in save_settings.items():
            if type(value) != list:
                save_settings[key] = [value]
        settings_df = pd.DataFrame.from_dict(save_settings)
        with pd.ExcelWriter(excel_filename, mode='a') as writer:
            settings_df.to_excel(writer, index=False, sheet_name='settings')

    msg = '[%s %s]: Quadrant analysis excel file saved at the following location: %s!' % (
                str(datetime.datetime.now().date()),
                str(datetime.datetime.now().time())[:8], excel_filename)

    print_msg(self, msg)


def new_atan2(y, x):
    """angles from 0 to 360"""

    if isinstance(y, (int, float, complex)):
        y = [y]

    if isinstance(x, (int, float, complex)):
        x = [x]

    if len(y) > 1:

        angles = np.zeros(len(y))

        neg_y = np.where(y < 0)[0]
        pos_y = np.where(y >= 0)[0]

        # setting the adding 360 degrees to the angles that are in the 3rd and 4th quadrant
        angles[neg_y] = np.arctan2(y[neg_y], x[neg_y]) * (180 / np.pi) + 360

        # regular arctan2 for those values that are in the 1st and 2nd quadrant
        angles[pos_y] = np.arctan2(y[pos_y], x[pos_y]) * (180 / np.pi)

    elif len(y) == 1:

        if y[0] < 0:
            angles = np.arctan2(y[0], x[0]) * (180 / np.pi) + 360
        else:
            angles = np.arctan2(y[0], x[0]) * (180 / np.pi)

    else:

        angles = []

    return angles


def getBinBounds(x_bounds, y_bounds, arena_shape, geometry=None, radii=None):
    """
    This function will get the boundary information for each of hte bins. This is essentially for plotting the bins
    so that we can get the area of the bin.

    :param x_bounds:
    :param y_bounds:
    :param arena_shape:
    :param geometry:
    :param radii:
    :return:
    """
    bounds = {}

    if arena_shape == 'Rectangular':

        if geometry is None:
            raise Exception("Invalid Geometry!")

        x_ticks = np.linspace(x_bounds[0], x_bounds[1], geometry[0] + 1)
        y_ticks = np.linspace(y_bounds[0], y_bounds[1], geometry[1] + 1)

        for row in np.arange(geometry[0]):
            for col in np.arange(geometry[1]):
                label = 1. * (col + 1) + (row + 1) / 100
                bounds[label] = [x_ticks[col], x_ticks[col + 1], y_ticks[row], y_ticks[row + 1]]

    elif arena_shape == 'Circle':
        if geometry is None:
            raise Exception("Invalid Geometry!")

        if radii is None:
            raise Exception("Invalid Radii value!")

        rad_limits = np.r_[0, radii].flatten()

        for i in range(len(geometry)):
            rad_lab = i + 1
            angle_limits = np.linspace(0, 360, num=geometry[i] + 1)

            rad_start = rad_limits[i]
            rad_stop = rad_limits[i + 1]

            for x in range(len(angle_limits) - 1):
                angle_lab = x + 1
                label = 1. * rad_lab + angle_lab / 100

                angle_start = angle_limits[x]
                angle_stop = angle_limits[x + 1]

                bounds[label] = [rad_start, rad_stop, angle_start, angle_stop]

    else:
        raise Exception("Invalid arena_shape")

    return bounds


def InnerVOuter(set_file, posx, posy, post, Fs_pos, bin_label, geometry, arena_shape=None,
                x_bounds=None, y_bounds=None, radii=None, plot_linewidth=5.334, save_settings=None, self=None):
    """

    :param set_file:
    :param posx:
    :param posy:
    :param post:
    :param Fs_pos:
    :param bin_label:
    :param geometry:
    :param arena_shape:
    :param x_bounds:
    :param y_bounds:
    :param radii:
    :param plot_linewidth:
    :param save_settings:
    :param self:
    :return:
    """
    directory = os.path.dirname(set_file)

    session = os.path.splitext(os.path.basename(set_file))[0]

    # puts a QuadrantAnalysis directory in the directory
    save_directory = os.path.join(directory, 'QuadrantAnalysis')

    excel_filename = os.path.join(save_directory, '%s_inVout.xlsx' % session)

    # adds a figures directory to that QuadrantAnalysis directory to save the figures
    save_figures_directory = os.path.join(save_directory, 'Figures')

    msg = '[%s %s]: Performing the Inner vs Outer analysis on the following session: %s!' % (
        str(datetime.datetime.now().date()),
        str(datetime.datetime.now().time())[:8], set_file)

    print_msg(self, msg)

    # Bin the positions based on the arena shape
    labels = None

    _, pixels_per_cm = getTotalArea(save_figures_directory, session, posx, posy, arena_shape, self=self,
                                    x_bounds=x_bounds, y_bounds=y_bounds, plot_linewidth=plot_linewidth)

    # get the plot xlim and ylim values
    xlim_values, ylim_values = getLimits(posx, posy, x_bounds=x_bounds, y_bounds=y_bounds)

    if arena_shape == 'Rectangular':

        labels = track_to_xylabels(posx, posy, arena_shape=arena_shape, geometry=geometry,
                                   x_bounds=x_bounds, y_bounds=y_bounds)

        binBounds = getBinBounds(x_bounds, y_bounds, arena_shape, geometry=geometry)

    elif arena_shape == 'Circle':

        # divide the position data into their specific bins based upon the number of bins
        labels = track_to_xylabels(posx, posy, arena_shape=arena_shape, geometry=geometry,
                                   radii=radii)

        # get the boundaries for the bins so we can plot them later
        binBounds = getBinBounds(x_bounds, y_bounds, arena_shape, geometry=geometry,
                                 radii=radii)

    x_ticks = np.linspace(x_bounds[0], x_bounds[1], geometry[0] + 1)
    y_ticks = np.linspace(y_bounds[0], y_bounds[1], geometry[1] + 1)

    # plot the bins
    bins_fig = plt.figure(figsize=(5, 5))
    bin_ax = bins_fig.add_subplot(111)
    # plot the labels
    bin_ax = plot_map_labels(posx, posy, labels, ax=bin_ax)
    # overlay the position in an opaque black
    bin_ax.plot(posx, posy, "k-", alpha=0.2)
    bin_ax.set_xlim(xlim_values)
    bin_ax.set_ylim(ylim_values)

    if arena_shape == 'Rectangular':
        # then it's a rectangular arena
        bin_ax.vlines(x_ticks, y_bounds[0], y_bounds[1], linestyles='dashed')
        bin_ax.hlines(y_ticks, x_bounds[0], x_bounds[1], linestyles='dashed')

    elif arena_shape == 'Circle':
        # plot a circular trace representing the arena, and then plot the quadrant boundaries
        # equivalent to ang = 0:0.01:4*pi in matlab
        step = 0.001
        ang = np.arange(np.round((2 * np.pi + step) / step)) / (1 / step)
        # rad_pos = np.sqrt((posx) ** 2 + (posy) ** 2).flatten()

        for rad_plot in radii:
            xp, yp = circle_vals(0, 0, 2 * rad_plot, ang)
            bin_ax.plot(xp, yp, 'k--')

    bin_fig_filename = os.path.join(save_figures_directory, '%s_ivo_all_bins.png' % (session))
    bin_ax.axis('off')
    bins_fig.savefig(bin_fig_filename, bbox_inches='tight', dpi=300)  # saving figure with the arena trace
    plt.close(bins_fig)

    # plot inner vs outer
    colors = []
    for label in sorted(bin_label.keys()):
        colors.append(get_plot_color(bin_label[label]))

    ivo_fig = plt.figure(figsize=(5, 5))
    ivo_ax = ivo_fig.add_subplot(111)
    ivo_ax = plot_map_labels(posx, posy, labels, ax=ivo_ax, colors=colors)
    # overlay the position in an opaque black
    ivo_ax.plot(posx, posy, "k-", alpha=0.2)
    ivo_ax.set_xlim(xlim_values)
    ivo_ax.set_ylim(ylim_values)

    if arena_shape == 'Rectangular':
        # then it's a rectangular arena
        ivo_ax.vlines(x_ticks, y_bounds[0], y_bounds[1], linestyles='dashed')
        ivo_ax.hlines(y_ticks, x_bounds[0], x_bounds[1], linestyles='dashed')
    elif arena_shape == 'Circle':
        # plot a circular trace representing the arena, and then plot the quadrant boundaries
        # equivalent to ang = 0:0.01:4*pi in matlab
        step = 0.001
        ang = np.arange(np.round((2 * np.pi + step) / step)) / (1 / step)
        # rad_pos = np.sqrt((posx) ** 2 + (posy) ** 2).flatten()
        for rad_plot in radii:
            xp, yp = circle_vals(0, 0, 2 * rad_plot, ang)
            ivo_ax.plot(xp, yp, 'k--')

    ivo_ax.axis('off')
    ivo_fig_filename = os.path.join(save_figures_directory, '%s_ivo_bins.png' % (session))
    ivo_fig.savefig(ivo_fig_filename, bbox_inches='tight', dpi=300)  # saving figure with the arena trace
    plt.close(ivo_fig)

    # analyze bins
    bin_time = {}  # time (seconds) in each bin
    bin_vel_avg = {}  # average velocity of each bin
    bin_vel_std = {}  # standard deviation of each bin
    bin_distance = {}  # the distance travelled in each bin
    bin_total_area = {}  # the total_area of each bin
    bin_coverage_percentage = {}

    for label in sorted(bin_label.keys()):
        msg = '[%s %s]: Analyzing the following bin: %s' % (
            str(datetime.datetime.now().date()),
            str(datetime.datetime.now().time())[:8], label)

        print_msg(self, msg)

        label_bool = np.where(labels == label)[0]

        if len(label_bool) == 0:
            bin_time[label] = 0
            bin_vel_avg[label] = 0
            bin_vel_std[label] = 0
            bin_distance[label] = 0
            bin_total_area[label] = 0
            bin_coverage_percentage[label] = 0
            continue

        consecutive_points = find_consec(label_bool)

        # the amount of time in seconds within this sector
        # bin_time[label] = (len(label_bool)-1) / Fs_pos

        # calculating velocities
        v_total = np.array([])
        weights = np.array([])
        distance = 0
        time = 0
        # calculate the velocities for each run within this bin

        # creating a figure for plotting the bin
        bin_positions = plt.figure(figsize=(5, 5))
        bin_ax = bin_positions.add_subplot(111)

        # iterate through each run and calculate various metrics (and plot the run)
        # we will also plot each run. This will remove any weird discontinuity issues
        # from plotting the between run points (it will plot from the end of the last run
        # to the beginning of the next run which could theoretically create a line through
        # another bin in the case of a circular plot.
        for run_i, run in enumerate(consecutive_points):

            runx = posx[run]
            runy = posy[run]
            runt = post[run]

            if len(runx) <= 2:
                continue

            # I decided to calculate time on each run as well. Used to just find how many samples are within the bin
            # and take that as the time, but the vel = distance/time relationship does not work out in that case since
            # we will be missing the distance/velocity points from when the mouse leaves one bin and enters another
            # therefore we will just calculate the time below. I subtract 1 from the length so we will start the time
            # at t=0 for each bin.

            # dTime
            dTime = np.diff(runt.flatten())

            # adding up dTime to get total time (add to time variable)
            time += np.sum(dTime)

            # difference in distances betwen points
            dDistance = np.sqrt(np.diff(runx.flatten()) ** 2 +
                                np.diff(runy.flatten()) ** 2)

            distance += np.sum(dDistance)

            v_i = dDistance / dTime
            if len(v_total) != 0:
                v_total = np.concatenate((v_total, v_i.flatten()))
            else:
                v_total = v_i.flatten()

            if len(weights) != 0:
                weights = np.concatenate((weights, dTime.flatten()))
            else:
                weights = dTime.flatten()

            bin_ax.plot(runx, runy, 'r-', lw=plot_linewidth)

        # setting the total time in the bin
        bin_time[label] = time  # units: sec

        # setting the total distance in the bin
        bin_distance[label] = distance / 100  # units: meters

        # here we will be doing a weighted average and standard dev so that we take in account the fact that there
        # will be instances where the positions are invalid, and thus the difference between points might not be
        # uniform.
        v_avg, v_sd = weighted_avg_and_std(v_total, weights)

        # v_avg = np.mean(v_total)  # finding the average velocity in this sector
        # v_sd = np.std(v_total)  # finding the standard deviation of the sector

        bin_vel_avg[label] = v_avg
        bin_vel_std[label] = v_sd

        bin_ax.set_xlim(xlim_values)
        bin_ax.set_ylim(ylim_values)

        label_str = str(label).replace('.', '_')

        bin_position_filename = os.path.join(save_figures_directory, '%s_bin%s.png' % (
            session, label_str))

        bin_ax.axis('off')
        bin_positions.savefig(bin_position_filename, bbox_inches='tight', dpi=300)
        plt.close(bin_positions)

        bin_area_covered = getFileArea(bin_position_filename, delete_file=True, fill=False)

        # get total possible bin area
        bin_total = plt.figure(figsize=(5, 5))
        bin_total_filename = os.path.join(save_figures_directory, '%s_bin%s_total.png' % (
            session, label_str))
        bin_total_ax = bin_total.add_subplot(111)

        bin_total_ax.set_xlim(xlim_values)
        bin_total_ax.set_ylim(ylim_values)

        fill_plot = True
        if arena_shape == 'Rectangular':
            plotSquareBin(*binBounds[label][:], ax=bin_total_ax)
        elif arena_shape == 'Circle':
            fill_plot = plotCircularSector(*binBounds[label][:], ax=bin_total_ax)

        bin_total_ax.axis('off')
        bin_total.savefig(bin_total_filename, bbox_inches='tight', dpi=300)
        plt.close(bin_total)

        # read the figure in so we can get the area in pixels
        total_possible_bin_area = getFileArea(bin_total_filename, delete_file=True,
                                              debug_figs=False, fill=fill_plot)  # units: pixels^2

        bin_coverage_percentage[label] = 100 * (bin_area_covered / total_possible_bin_area)  # units: percent

        total_possible_bin_area = total_possible_bin_area / pixels_per_cm  # units cm^2
        bin_total_area[label] = total_possible_bin_area

    data = {'Label': list(sorted(bin_label.keys())),
            'Time (sec)': [value for key, value in sorted(bin_time.items())],
            'Avg. Velocity (cm/s)': [value for key, value in sorted(bin_vel_avg.items())],
            'SD. Velocity (cm/s)': [value for key, value in sorted(bin_vel_std.items())],
            'Distance (m)': [value for key, value in sorted(bin_distance.items())],
            'Bin Coverage (% bin total)': [value for key, value in sorted(bin_coverage_percentage.items())],
            'Bin Area (cm^2)': [value for key, value in sorted(bin_total_area.items())],
            'Inner/Outer': [getIOfromState(value) for key, value in sorted(bin_label.items())]
            }

    data_df = pd.DataFrame.from_dict(data)

    # find the coverage for each bin, and add them up to get the total coverage
    total_coverage = sum(data_df['Bin Coverage (% bin total)'] * data_df['Bin Area (cm^2)'])  # units cm^2

    # now take the bin coverage, and divide them by total coverage to get the percent relative to the
    # total coverage of the mouse.
    data_df['Bin Coverage (% of total coverage)'] = 100 * (data_df['Bin Coverage (% bin total)'] *
                                                           data_df['Bin Area (cm^2)']) / total_coverage

    # find the total area (in cm^2)
    total_area = sum(data_df['Bin Area (cm^2)'])

    # normalize the bin area by the total area
    data_df['Bin Area (% of total)'] = 100 * data_df['Bin Area (cm^2)'] / total_area

    # moving the inner/outer to the end

    ivo = data_df['Inner/Outer']
    data_df = data_df.drop(columns='Inner/Outer')

    data_df['Inner/Outer'] = ivo

    # adding the totals
    total_label = {'Label': 'Total', 'Time (sec)': data_df['Time (sec)'].sum(),
                   'Distance (m)': data_df['Distance (m)'].sum(),
                   'Bin Area (cm^2)': total_area}
    data_df = data_df.append(total_label, ignore_index=True)

    # export to excel
    data_df.to_excel(excel_filename, index=False)

    if save_settings is not None:
        save_settings['geometry'] = str(geometry)
        for key, value in save_settings.items():
            if type(value) != list:
                save_settings[key] = [value]
        settings_df = pd.DataFrame.from_dict(save_settings)
        with pd.ExcelWriter(excel_filename, mode='a') as writer:
            settings_df.to_excel(writer, index=False, sheet_name='settings')

    msg = '[%s %s]: Inner vs Outer results saved to the following file: %s!' % (
        str(datetime.datetime.now().date()),
        str(datetime.datetime.now().time())[:8], excel_filename)

    print_msg(self, msg)

    return labels, data_df


def track_to_xylabels(x_pos, y_pos, arena_shape='Rectangular', geometry=None, radii=None,
                      x_bounds=None, y_bounds=None):
    """
    returns the list of labels for each data point

    parameters:
    x_pos: x position
    y_pos: y position
    arena_shape: shape of the arena
    geometry: if arena_shape is "Rectangular", then it is a tuple of the following
        (number of rows, number of columns). If the arena_shape is "Circle", then it is a tuple
        of the following (number of inner bins, number of outer bins)
    radii: if the arena_shape is circular you will need to provide a radii argument which is
        a list of radius values, from smallest to largest (corresponding to the geometry values)

    Rectangular Example:

    For example: 2x2 grid (geometry = (2,2))

              y=100 -------------------------------------------
                    |                    |                     |
                    |                    |                     |
                    |   Label = 1.02      |   Label = 2.02       |    y
                    |                    |                     |    |
                    |                    |                     |    a
               y=50 -------------------------------------------     x
                    |                    |                     |    i
                    |                    |                     |    s
                    |  Label = 1.01       |   Label = 2.01       |
                    |                    |                     |
                    |                    |                     |
                y=0 -------------------------------------------|
                    x=0                 x=50                  x=100
                                x-axis

    """

    if arena_shape == 'Rectangular':
        if x_bounds is None:
            x_bounds = [np.min(x_pos), np.max(x_pos)]
        if y_bounds is None:
            y_bounds = [np.min(y_pos), np.max(y_pos)]

        x_ticks = np.linspace(x_bounds[0], x_bounds[1], geometry[0] + 1)[:-1]
        y_ticks = np.linspace(y_bounds[0], y_bounds[1], geometry[1] + 1)[:-1]

        x_lab = np.sum([x_pos >= t for t in x_ticks], 0)
        y_lab = np.sum([y_pos >= t for t in y_ticks], 0)

        return 1. * x_lab + y_lab / 100

    elif arena_shape == 'Circle':
        if geometry is None:
            raise Exception("Invalid geometry")

        if radii is None:
            raise Exception("Invalid radii")

        # get the angle for each position
        rad_pos = np.sqrt((x_pos) ** 2 + (y_pos) ** 2).flatten()
        rad_limits = np.r_[0, radii].flatten()

        angle_pos = new_atan2(y_pos.flatten(), x_pos.flatten())

        rad_lab = np.sum([rad_pos >= r for r in rad_limits[:-1]], 0)

        angle_lab = np.zeros_like(rad_lab).astype(int)

        # iterate through each of the radius values and bin the data based off of angle limits
        for i in range(len(geometry)):
            if i < len(geometry) - 1:
                rad_bool = np.where((rad_pos >= rad_limits[i]) * (rad_pos < rad_limits[i + 1]))[0]
            else:
                rad_bool = np.where(rad_pos >= rad_limits[i])[0]

            angle_limits = np.linspace(0, 360, num=geometry[i] + 1)[:-1]

            angle_lab[rad_bool] = np.sum([angle_pos[rad_bool] >= theta for theta in angle_limits],
                                         0)

        return 1. * rad_lab + angle_lab / 100

    else:
        raise Exception("Invalid geometry")


def plot_map_labels(x_pos, y_pos, labels, ax=None, colors=None, **args):
    if ax is None:
        fig = plt.figure(figsize=(5, 5))
        ax = fig.add_subplot(111)

    if colors is None:
        colors = plt.cm.rainbow(np.linspace(0, 1, len(np.unique(labels))))

    for l, c in zip(np.unique(labels), colors):
        ax.scatter(x_pos[labels == l], y_pos[labels == l], color=c, **args)

    return ax


def get_plot_color(state):
    if state == 0:
        return 'b'
    elif state == 1:
        return 'r'
    elif state == 2:
        return 'k'


def find_consec(data):
    """finds the consecutive numbers and outputs as a list"""
    consecutive_values = []  # a list for the output
    current_consecutive = [data[0]]

    if len(data) == 1:
        return [[data[0]]]

    for index in range(1, len(data)):

        if data[index] == data[index - 1] + 1:
            current_consecutive.append(data[index])

            if index == len(data) - 1:
                consecutive_values.append(current_consecutive)

        else:
            consecutive_values.append(current_consecutive)
            current_consecutive = [data[index]]

            if index == len(data) - 1:
                consecutive_values.append(current_consecutive)
    return consecutive_values


def plotSquareBin(xmin, xmax, ymin, ymax, ax, lw=5.334):
    ax.vlines([xmin, xmax], ymin, ymax, lw=lw)
    ax.hlines([ymin, ymax], xmin, xmax, lw=lw)


def getIOfromState(state):
    if state == 0:
        return 'Outer'
    elif state == 1:
        return 'Inner'
    else:
        return 'Other'


def plotCircularSector(inner_radius, outer_radius, start_theta, stop_theta, ax,
                       lw=5.334):
    """

    This will plot the circles/circular sectors given an inner/outer radius of the bin,
    the start and stop angle (theta) of the sector, and the plot axis.

    We will return if the plot should be filled in or not (for calculating the area of the
    plot). The only situation where you need to fill in the plot would be if there are two
    concentric circles plotted (1 outer bin and 1 inner bin essentially). This is because
    when you fill the plot, it will fill in the entire area within the outer circle's radius.

    """
    start_theta *= (np.pi / 180)
    stop_theta *= (np.pi / 180)

    theta = np.linspace(start_theta, stop_theta, num=100)
    theta2 = np.linspace(stop_theta, start_theta, num=100)

    if stop_theta - start_theta == 2 * np.pi:
        # then it is a circle
        x_values_out = outer_radius * np.cos(theta)
        y_values_out = outer_radius * np.sin(theta)
        ax.plot(x_values_out, y_values_out, 'r-', lw=lw)

        if inner_radius != 0:
            # fill in the circle because having the inner radius plotted wiill just
            # simply find all the area of the outer circle (not outer - inner)
            n_plots = np.ceil((outer_radius - inner_radius) / (lw / 20))

            for rad in np.linspace(inner_radius, outer_radius, num=n_plots):
                x_values_rad = rad * np.cos(theta)
                y_values_rad = rad * np.sin(theta)
                ax.plot(x_values_rad, y_values_rad, 'r-', lw=lw)
            return False
    else:
        # it is a circular sector
        x_values = np.hstack(
            (outer_radius * np.cos(theta),  # outer radius
             outer_radius * np.cos(stop_theta),  # connect outer to inner
             inner_radius * np.cos(stop_theta),
             inner_radius * np.cos(theta2),  # inner radius
             inner_radius * np.cos(start_theta),
             outer_radius * np.cos(start_theta),
             ))

        y_values = np.hstack(
            (outer_radius * np.sin(theta),  # outer radius
             outer_radius * np.sin(stop_theta),  # connect outer to inner
             inner_radius * np.sin(stop_theta),
             inner_radius * np.sin(theta2),  # inner radius
             inner_radius * np.sin(start_theta),
             outer_radius * np.sin(start_theta),
             ))

        ax.plot(x_values, y_values, 'r-', lw=lw)

    return True


def circle_vals(x, y, d, ang):
    """x and y are the coordinates of the center o the circle with radius,r"""
    r = d / 2

    xp = np.multiply(r, np.cos(ang))
    yp = np.multiply(r, np.sin(ang))

    xp = np.add(xp, x)
    yp = np.add(yp, y)

    return xp.reshape((len(xp), 1)), yp.reshape((len(yp), 1))


def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray


def flood_fill(test_array, h_max=255):
    input_array = np.copy(test_array)
    el = scipy.ndimage.generate_binary_structure(2, 2).astype(np.int)
    inside_mask = scipy.ndimage.binary_erosion(~np.isnan(input_array), structure=el)
    output_array = np.copy(input_array)
    output_array[inside_mask] = h_max
    output_old_array = np.copy(input_array)
    output_old_array.fill(0)
    el = scipy.ndimage.generate_binary_structure(2, 1).astype(np.int)
    while not np.array_equal(output_old_array, output_array):
        output_old_array = np.copy(output_array)
        output_array = np.maximum(input_array, scipy.ndimage.grey_erosion(output_array, size=(3, 3), footprint=el))
    return output_array

