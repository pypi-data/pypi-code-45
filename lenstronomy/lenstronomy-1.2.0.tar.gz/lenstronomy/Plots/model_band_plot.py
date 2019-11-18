
import lenstronomy.Util.util as util
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
from lenstronomy.ImSim.MultiBand.single_band_multi_model import SingleBandMultiModel
from lenstronomy.LensModel.lens_model_extensions import LensModelExtensions
from lenstronomy.Data.coord_transforms import Coordinates
from lenstronomy.Plots import plot_util


class ModelBandPlot(object):
    """
    class to plot a single band given the modeling results

    """
    def __init__(self, multi_band_list, kwargs_model, model, error_map, cov_param, param, kwargs_params,
                 likelihood_mask_list=None, band_index=0, arrow_size=0.02, cmap_string="gist_heat"):

        self.bandmodel = SingleBandMultiModel(multi_band_list, kwargs_model,
                                                  likelihood_mask_list=likelihood_mask_list, band_index=band_index)
        self._kwargs_special_partial = kwargs_params.get('kwargs_special', None)
        kwarks_lens_partial, kwargs_source_partial, kwargs_lens_light_partial, kwargs_ps_partial, self._kwargs_extinction_partial = self.bandmodel.select_kwargs(**kwargs_params)
        self._kwargs_lens_partial, self._kwargs_source_partial, self._kwargs_lens_light_partial, self._kwargs_ps_partial = self.bandmodel.update_linear_kwargs(param, kwarks_lens_partial, kwargs_source_partial, kwargs_lens_light_partial, kwargs_ps_partial)
        self._norm_residuals = self.bandmodel.reduced_residuals(model, error_map=error_map)
        self._reduced_x2 = self.bandmodel.reduced_chi2(model, error_map=error_map)
        print("reduced chi^2 of data ", band_index, "= ", self._reduced_x2)

        self._model = model
        self._cov_param = cov_param
        self._param = param

        self._lensModel = self.bandmodel.LensModel
        self._lensModelExt = LensModelExtensions(self._lensModel)
        log_model = np.log10(model)
        log_model[np.isnan(log_model)] = -5
        self._v_min_default = max(np.min(log_model), -5)
        self._v_max_default = min(np.max(log_model), 10)
        self._coords = self.bandmodel.Data
        self._data = self._coords.data
        self._deltaPix = self._coords.pixel_width
        self._frame_size = np.max(self._coords.width)
        x_grid, y_grid = self._coords.pixel_coordinates
        self._x_grid = util.image2array(x_grid)
        self._y_grid = util.image2array(y_grid)

        if isinstance(cmap_string, str):
            cmap = plt.get_cmap(cmap_string)
        else:
            cmap = cmap_string
        cmap.set_bad(color='k', alpha=1.)
        cmap.set_under('k')
        self._cmap = cmap
        self._arrow_size = arrow_size

    def _critical_curves(self):
        if not hasattr(self, '_ra_crit_list') or not hasattr(self, '_dec_crit_list'):
            self._ra_crit_list, self._dec_crit_list = self._lensModelExt.critical_curve_tiling(self._kwargs_lens_partial,
                                                                                        compute_window=self._frame_size,
                                                                                        start_scale=self._deltaPix / 5.,
                                                                                        max_order=10)
        return self._ra_crit_list, self._dec_crit_list

    def _caustics(self):
        if not hasattr(self, '_ra_caustic_list') or not hasattr(self, '_dec_caustic_list'):
            ra_crit_list, dec_crit_list = self._critical_curves()
            self._ra_caustic_list, self._dec_caustic_list = self._lensModel.ray_shooting(ra_crit_list,
                                                                                     dec_crit_list, self._kwargs_lens_partial)
        return self._ra_caustic_list, self._dec_caustic_list

    def data_plot(self, ax, v_min=None, v_max=None, text='Observed',
                  font_size=15, colorbar_label=r'log$_{10}$ flux', **kwargs):
        """

        :param ax:
        :return:
        """
        if v_min is None:
            v_min = self._v_min_default
        if v_max is None:
            v_max = self._v_max_default
        im = ax.matshow(np.log10(self._data), origin='lower',
                        extent=[0, self._frame_size, 0, self._frame_size], cmap=self._cmap, vmin=v_min, vmax=v_max)  # , vmin=0, vmax=2

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.autoscale(False)

        plot_util.scale_bar(ax, self._frame_size, dist=1, text='1"', font_size=font_size)
        plot_util.text_description(ax, self._frame_size, text=text, color="w",
                         backgroundcolor='k', font_size=font_size)

        if 'no_arrow' not in kwargs or not kwargs['no_arrow']:
            plot_util.coordinate_arrows(ax, self._frame_size, self._coords, color='w',
                              arrow_size=self._arrow_size, font_size=font_size)

        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        cb = plt.colorbar(im, cax=cax, orientation='vertical')
        cb.set_label(colorbar_label, fontsize=font_size)
        return ax

    def model_plot(self, ax, v_min=None, v_max=None, image_names=False,
                   colorbar_label=r'log$_{10}$ flux',
                   font_size=15, text='Reconstructed', **kwargs):
        """

        :param ax:
        :param model:
        :param v_min:
        :param v_max:
        :return:
        """
        if v_min is None:
            v_min = self._v_min_default
        if v_max is None:
            v_max = self._v_max_default
        im = ax.matshow(np.log10(self._model), origin='lower', vmin=v_min, vmax=v_max,
                        extent=[0, self._frame_size, 0, self._frame_size], cmap=self._cmap)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.autoscale(False)
        plot_util.scale_bar(ax, self._frame_size, dist=1, text='1"', font_size=font_size)
        plot_util.text_description(ax, self._frame_size, text=text, color="w",
                         backgroundcolor='k', font_size=font_size)
        if 'no_arrow' not in kwargs or not kwargs['no_arrow']:
            plot_util.coordinate_arrows(ax, self._frame_size, self._coords,
                              color='w', arrow_size=self._arrow_size,
                              font_size=font_size)
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        cb = plt.colorbar(im, cax=cax)
        cb.set_label(colorbar_label, fontsize=font_size)

        #plot_line_set(ax, self._coords, self._ra_caustic_list, self._dec_caustic_list, color='b')
        #plot_line_set(ax, self._coords, self._ra_crit_list, self._dec_crit_list, color='r')
        if image_names is True:
            ra_image, dec_image = self.bandmodel.PointSource.image_position(self._kwargs_ps_partial, self._kwargs_lens_partial)
            plot_util.image_position_plot(ax, self._coords, ra_image, dec_image)
        #source_position_plot(ax, self._coords, self._kwargs_source)

    def convergence_plot(self, ax, text='Convergence', v_min=None, v_max=None,
                         font_size=15, colorbar_label=r'$\log_{10}\ \kappa$',
                         **kwargs):
        """

        :param x_grid:
        :param y_grid:
        :param kwargs_lens:
        :param kwargs_else:
        :return:
        """
        if not 'cmap' in kwargs:
            kwargs['cmap'] = self._cmap

        kappa_result = util.array2image(self._lensModel.kappa(self._x_grid, self._y_grid, self._kwargs_lens_partial))
        im = ax.matshow(np.log10(kappa_result), origin='lower',
                        extent=[0, self._frame_size, 0, self._frame_size],
                        cmap=kwargs['cmap'], vmin=v_min, vmax=v_max)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.autoscale(False)
        plot_util.scale_bar(ax, self._frame_size, dist=1, text='1"', color='w', font_size=font_size)
        if 'no_arrow' not in kwargs or not kwargs['no_arrow']:
            plot_util.coordinate_arrows(ax, self._frame_size, self._coords, color='w',
                              arrow_size=self._arrow_size, font_size=font_size)
            plot_util.text_description(ax, self._frame_size, text=text,
                         color="w", backgroundcolor='k', flipped=False,
                         font_size=font_size)
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        cb = plt.colorbar(im, cax=cax)
        cb.set_label(colorbar_label, fontsize=font_size)
        return ax

    def normalized_residual_plot(self, ax, v_min=-6, v_max=6, font_size=15, text="Normalized Residuals",
                                 colorbar_label=r'(f${}_{\rm model}$ - f${}_{\rm data}$)/$\sigma$',
                                 no_arrow=False, **kwargs):
        """

        :param ax:
        :param v_min:
        :param v_max:
        :param kwargs: kwargs to send to matplotlib.pyplot.matshow()
        :return:
        """
        if not 'cmap' in kwargs:
            kwargs['cmap'] = 'bwr'
        im = ax.matshow(self._norm_residuals, vmin=v_min, vmax=v_max,
                        extent=[0, self._frame_size, 0, self._frame_size], origin='lower',
                        **kwargs)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.autoscale(False)
        plot_util.scale_bar(ax, self._frame_size, dist=1, text='1"', color='k',
                  font_size=font_size)
        plot_util.text_description(ax, self._frame_size, text=text, color="k",
                         backgroundcolor='w', font_size=font_size)
        if not no_arrow:
            plot_util.coordinate_arrows(ax, self._frame_size, self._coords, color='w',
                              arrow_size=self._arrow_size, font_size=font_size)
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        cb = plt.colorbar(im, cax=cax)
        cb.set_label(colorbar_label,
                     fontsize=font_size)
        return ax

    def absolute_residual_plot(self, ax, v_min=-1, v_max=1, font_size=15,
                               text="Residuals",
                               colorbar_label=r'(f$_{model}$-f$_{data}$)'):
        """

        :param ax:
        :param residuals:
        :return:
        """
        im = ax.matshow(self._model - self._data, vmin=v_min, vmax=v_max,
                        extent=[0, self._frame_size, 0, self._frame_size], cmap='bwr', origin='lower')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.autoscale(False)
        plot_util.scale_bar(ax, self._frame_size, dist=1, text='1"', color='k',
                  font_size=font_size)
        plot_util.text_description(ax, self._frame_size, text=text, color="k",
                         backgroundcolor='w', font_size=font_size)
        plot_util.coordinate_arrows(ax, self._frame_size, self._coords,
                          font_size=font_size,
                          color='k',
                          arrow_size=self._arrow_size)
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        cb = plt.colorbar(im, cax=cax)
        cb.set_label(colorbar_label, fontsize=font_size)
        return ax

    def source(self, numPix, deltaPix, center=None, image_orientation=True):
        """

        :param numPix: number of pixels per axes
        :param deltaPix: pixel size
        :param image_orientation: bool, if True, uses frame in orientation of the image, otherwise in RA-DEC coordinates
        :return: 2d surface brightness grid of the reconstructed source and Coordinates() instance of source grid
        """
        if image_orientation is True:
            Mpix2coord = self._coords.transform_pix2angle * deltaPix / self._deltaPix
            x_grid_source, y_grid_source = util.make_grid_transformed(numPix, Mpix2Angle=Mpix2coord)
            ra_at_xy_0, dec_at_xy_0 = x_grid_source[0], y_grid_source[0]
        else:
            x_grid_source, y_grid_source, ra_at_xy_0, dec_at_xy_0, x_at_radec_0, y_at_radec_0, Mpix2coord, Mcoord2pix = util.make_grid_with_coordtransform(
            numPix, deltaPix)

        center_x = 0
        center_y = 0
        if center is not None:
            center_x, center_y = center[0], center[1]
        elif len(self._kwargs_source_partial) > 0:
            center_x = self._kwargs_source_partial[0]['center_x']
            center_y = self._kwargs_source_partial[0]['center_y']
        x_grid_source += center_x
        y_grid_source += center_y

        coords_source = Coordinates(transform_pix2angle=Mpix2coord,
                                    ra_at_xy_0=ra_at_xy_0 + center_x,
                                    dec_at_xy_0=dec_at_xy_0 + center_y)

        source = self.bandmodel.SourceModel.surface_brightness(x_grid_source, y_grid_source,
                                                               self._kwargs_source_partial)
        source = util.array2image(source) * deltaPix ** 2
        return source, coords_source

    def source_plot(self, ax, numPix, deltaPix_source, center=None, v_min=None,
                    v_max=None, with_caustics=False, caustic_color='yellow',
                    font_size=15, plot_scale='log',
                    scale_size=0.1,
                    text="Reconstructed source",
                    colorbar_label=r'log$_{10}$ flux', point_source_position=True,
                    **kwargs):
        """

        :param ax:
        :param numPix:
        :param deltaPix_source:
        :param center: [center_x, center_y], if specified, uses this as the center
        :param v_min:
        :param v_max:
        :param with_caustics:
        :param caustic_color:
        :param font_size:
        :param plot_scale: string, log or linear, scale of surface brightness plot
        :param kwargs:
        :return:
        """
        if v_min is None:
            v_min = self._v_min_default
        if v_max is None:
            v_max = self._v_max_default
        d_s = numPix * deltaPix_source
        source, coords_source = self.source(numPix, deltaPix_source, center=center)
        if plot_scale == 'log':
            source[source < 10**(v_min)] = 10**(v_min) # to remove weird shadow in plot
            source_scale = np.log10(source)
        elif plot_scale == 'linear':
            source_scale = source
        else:
            raise ValueError('variable plot_scale needs to be "log" or "linear", not %s.' % plot_scale)
        im = ax.matshow(source_scale, origin='lower', extent=[0, d_s, 0, d_s],
                        cmap=self._cmap, vmin=v_min, vmax=v_max)  # source
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.autoscale(False)
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        cb = plt.colorbar(im, cax=cax)
        cb.set_label(colorbar_label, fontsize=font_size)

        if with_caustics is True:
            ra_caustic_list, dec_caustic_list = self._caustics()
            plot_util.plot_line_set(ax, coords_source, ra_caustic_list,
                          dec_caustic_list, color=caustic_color)
            plot_util.scale_bar(ax, d_s, dist=scale_size, text='{:.1f}"'.format(scale_size),
                  color='w',
                  flipped=False,
                  font_size=font_size)
        if 'no_arrow' not in kwargs or not kwargs['no_arrow']:
            plot_util.coordinate_arrows(ax, self._frame_size, self._coords, color='w',
                              arrow_size=self._arrow_size, font_size=font_size)
            plot_util.text_description(ax, d_s, text=text, color="w", backgroundcolor='k',
                         flipped=False, font_size=font_size)
        if point_source_position is True:
            ra_source, dec_source = self.bandmodel.PointSource.source_position(self._kwargs_ps_partial, self._kwargs_lens_partial)
            plot_util.source_position_plot(ax, coords_source, ra_source, dec_source)
        return ax

    def error_map_source_plot(self, ax, numPix, deltaPix_source, v_min=None,
                              v_max=None, with_caustics=False, font_size=15, point_source_position=True):
        x_grid_source, y_grid_source = util.make_grid_transformed(numPix,
                                                                  self._coords.transform_pix2angle * deltaPix_source / self._deltaPix)
        x_center = self._kwargs_source_partial[0]['center_x']
        y_center = self._kwargs_source_partial[0]['center_y']
        x_grid_source += x_center
        y_grid_source += y_center
        coords_source = Coordinates(self._coords.transform_pix2angle * deltaPix_source / self._deltaPix, ra_at_xy_0=x_grid_source[0],
                                    dec_at_xy_0=y_grid_source[0])
        error_map_source = self.bandmodel.error_map_source(self._kwargs_source_partial, x_grid_source, y_grid_source, self._cov_param)
        error_map_source = util.array2image(error_map_source)
        d_s = numPix * deltaPix_source
        im = ax.matshow(error_map_source, origin='lower', extent=[0, d_s, 0, d_s],
                        cmap=self._cmap, vmin=v_min, vmax=v_max)  # source
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.autoscale(False)
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        cb = plt.colorbar(im, cax=cax)
        cb.set_label(r'error variance', fontsize=font_size)
        if with_caustics:
            ra_caustic_list, dec_caustic_list = self._caustics()
            plot_util.plot_line_set(ax, coords_source, ra_caustic_list, dec_caustic_list, color='b')
        plot_util.scale_bar(ax, d_s, dist=0.1, text='0.1"', color='w', flipped=False, font_size=font_size)
        plot_util.coordinate_arrows(ax, d_s, coords_source,
                          arrow_size=self._arrow_size, color='w', font_size=font_size)
        plot_util.text_description(ax, d_s, text="Error map in source", color="w",
                         backgroundcolor='k', flipped=False, font_size=font_size)
        if point_source_position is True:
            ra_source, dec_source = self.bandmodel.PointSource.source_position(self._kwargs_ps_partial, self._kwargs_lens_partial)
            plot_util.source_position_plot(ax, coords_source, ra_source, dec_source)
        return ax

    def magnification_plot(self, ax, v_min=-10, v_max=10,
                           image_name_list=None, font_size=15, no_arrow=False,
                           text="Magnification model",
                           colorbar_label=r"$\det\ (\mathsf{A}^{-1})$",
                           **kwargs):
        """

        :param ax: matplotib axis instance
        :param v_min: minimum range of plotting
        :param v_max: maximum range of plotting
        :param kwargs: kwargs to send to matplotlib.pyplot.matshow()
        :return:
        """
        if not 'cmap' in kwargs:
            kwargs['cmap'] = self._cmap
        if not 'alpha' in kwargs:
            kwargs['alpha'] = 0.5
        mag_result = util.array2image(self._lensModel.magnification(self._x_grid, self._y_grid, self._kwargs_lens_partial))
        im = ax.matshow(mag_result, origin='lower', extent=[0, self._frame_size, 0, self._frame_size],
                        vmin=v_min, vmax=v_max, **kwargs)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.autoscale(False)
        plot_util.scale_bar(ax, self._frame_size, dist=1, text='1"', color='k', font_size=font_size)
        if not no_arrow:
            plot_util.coordinate_arrows(ax, self._frame_size, self._coords, color='k', arrow_size=self._arrow_size,
                                        font_size=font_size)
        plot_util.text_description(ax, self._frame_size, text=text, color="k",
                         backgroundcolor='w', font_size=font_size)
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        cb = plt.colorbar(im, cax=cax)
        cb.set_label(colorbar_label, fontsize=font_size)
        ra_image, dec_image = self.bandmodel.PointSource.image_position(self._kwargs_ps_partial, self._kwargs_lens_partial)
        plot_util.image_position_plot(ax, self._coords, ra_image, dec_image, color='k', image_name_list=image_name_list)
        return ax

    def deflection_plot(self, ax, v_min=None, v_max=None, axis=0,
                        with_caustics=False, image_name_list=None,
                        text="Deflection model", font_size=15,
                        colorbar_label=r'arcsec'):
        """

        :param kwargs_lens:
        :param kwargs_else:
        :return:
        """

        alpha1, alpha2 = self._lensModel.alpha(self._x_grid, self._y_grid, self._kwargs_lens_partial)
        alpha1 = util.array2image(alpha1)
        alpha2 = util.array2image(alpha2)
        if axis == 0:
            alpha = alpha1
        else:
            alpha = alpha2
        im = ax.matshow(alpha, origin='lower', extent=[0, self._frame_size, 0, self._frame_size],
                        vmin=v_min, vmax=v_max, cmap=self._cmap, alpha=0.5)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.autoscale(False)
        plot_util.scale_bar(ax, self._frame_size, dist=1, text='1"', color='k', font_size=font_size)
        plot_util.coordinate_arrows(ax, self._frame_size, self._coords, color='k',
                          arrow_size=self._arrow_size, font_size=font_size)
        plot_util.text_description(ax, self._frame_size, text=text, color="k",
                         backgroundcolor='w', font_size=font_size)
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        cb = plt.colorbar(im, cax=cax)
        cb.set_label(colorbar_label, fontsize=font_size)
        if with_caustics is True:
            ra_crit_list, dec_crit_list = self._critical_curves()
            ra_caustic_list, dec_caustic_list = self._caustics()
            plot_util.plot_line_set(ax, self._coords, ra_caustic_list, dec_caustic_list, color='b')
            plot_util.plot_line_set(ax, self._coords, ra_crit_list, dec_crit_list, color='r')
        ra_image, dec_image = self.bandmodel.PointSource.image_position(self._kwargs_ps_partial, self._kwargs_lens_partial)
        plot_util.image_position_plot(ax, self._coords, ra_image, dec_image, image_name_list=image_name_list)
        return ax

    def decomposition_plot(self, ax, text='Reconstructed', v_min=None, v_max=None,
                           unconvolved=False, point_source_add=False,
                           font_size=15,
                           source_add=False, lens_light_add=False, **kwargs):
        """

        :param ax:
        :param text:
        :param v_min:
        :param v_max:
        :param unconvolved:
        :param point_source_add:
        :param source_add:
        :param lens_light_add:
        :param kwargs: kwargs to send matplotlib.pyplot.matshow()
        :return:
        """
        model = self.bandmodel.image(self._kwargs_lens_partial, self._kwargs_source_partial, self._kwargs_lens_light_partial,
                                          self._kwargs_ps_partial, unconvolved=unconvolved, source_add=source_add,
                                          lens_light_add=lens_light_add, point_source_add=point_source_add)
        if v_min is None:
            v_min = self._v_min_default
        if v_max is None:
            v_max = self._v_max_default
        if not 'cmap' in kwargs:
            kwargs['cmap'] = self._cmap
        im = ax.matshow(np.log10(model), origin='lower', vmin=v_min, vmax=v_max,
                        extent=[0, self._frame_size, 0, self._frame_size], **kwargs)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.autoscale(False)
        plot_util.scale_bar(ax, self._frame_size, dist=1, text='1"', font_size=font_size)
        plot_util.text_description(ax, self._frame_size, text=text, color="w", backgroundcolor='k')
        plot_util.coordinate_arrows(ax, self._frame_size, self._coords,
                          arrow_size=self._arrow_size, font_size=font_size)
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        cb = plt.colorbar(im, cax=cax)
        cb.set_label(r'log$_{10}$ flux', fontsize=font_size)
        return ax

    def subtract_from_data_plot(self, ax, text='Subtracted', v_min=None,
                                v_max=None, point_source_add=False,
                                source_add=False, lens_light_add=False,
                                font_size=15
                                ):
        model = self.bandmodel.image(self._kwargs_lens_partial, self._kwargs_source_partial, self._kwargs_lens_light_partial,
                                          self._kwargs_ps_partial, unconvolved=False, source_add=source_add,
                                          lens_light_add=lens_light_add, point_source_add=point_source_add)
        if v_min is None:
            v_min = self._v_min_default
        if v_max is None:
            v_max = self._v_max_default
        im = ax.matshow(np.log10(self._data - model), origin='lower', vmin=v_min, vmax=v_max,
                        extent=[0, self._frame_size, 0, self._frame_size], cmap=self._cmap)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.autoscale(False)
        plot_util.scale_bar(ax, self._frame_size, dist=1, text='1"', font_size=font_size)
        plot_util.text_description(ax, self._frame_size, text=text, color="w",
                         backgroundcolor='k', font_size=font_size)
        plot_util.coordinate_arrows(ax, self._frame_size, self._coords,
                          arrow_size=self._arrow_size, font_size=font_size)
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        cb = plt.colorbar(im, cax=cax)
        cb.set_label(r'log$_{10}$ flux', fontsize=font_size)
        return ax

    def plot_main(self, with_caustics=False):
        """
        print the main plots together in a joint frame

        :return:
        """

        f, axes = plt.subplots(2, 3, figsize=(16, 8))
        self.data_plot(ax=axes[0, 0])
        self.model_plot(ax=axes[0, 1], image_names=True)
        self.normalized_residual_plot(ax=axes[0, 2], v_min=-6, v_max=6)
        self.source_plot(ax=axes[1, 0], deltaPix_source=0.01, numPix=100, with_caustics=with_caustics)
        self.convergence_plot(ax=axes[1, 1], v_max=1)
        self.magnification_plot(ax=axes[1, 2])
        f.tight_layout()
        f.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0., hspace=0.05)
        return f, axes

    def plot_separate(self):
        """
        plot the different model components separately

        :return:
        """
        f, axes = plt.subplots(2, 3, figsize=(16, 8))

        self.decomposition_plot(ax=axes[0, 0], text='Lens light', lens_light_add=True, unconvolved=True)
        self.decomposition_plot(ax=axes[1, 0], text='Lens light convolved', lens_light_add=True)
        self.decomposition_plot(ax=axes[0, 1], text='Source light', source_add=True, unconvolved=True)
        self.decomposition_plot(ax=axes[1, 1], text='Source light convolved', source_add=True)
        self.decomposition_plot(ax=axes[0, 2], text='All components', source_add=True, lens_light_add=True,
                                    unconvolved=True)
        self.decomposition_plot(ax=axes[1, 2], text='All components convolved', source_add=True,
                                    lens_light_add=True, point_source_add=True)
        f.tight_layout()
        f.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0., hspace=0.05)
        return f, axes

    def plot_subtract_from_data_all(self):
        """
        subtract model components from data

        :return:
        """
        f, axes = plt.subplots(2, 3, figsize=(16, 8))

        self.subtract_from_data_plot(ax=axes[0, 0], text='Data')
        self.subtract_from_data_plot(ax=axes[0, 1], text='Data - Point Source', point_source_add=True)
        self.subtract_from_data_plot(ax=axes[0, 2], text='Data - Lens Light', lens_light_add=True)
        self.subtract_from_data_plot(ax=axes[1, 0], text='Data - Source Light', source_add=True)
        self.subtract_from_data_plot(ax=axes[1, 1], text='Data - Source Light - Point Source', source_add=True,
                                         point_source_add=True)
        self.subtract_from_data_plot(ax=axes[1, 2], text='Data - Lens Light - Point Source', lens_light_add=True,
                                         point_source_add=True)
        f.tight_layout()
        f.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0., hspace=0.05)
        return f, axes

    def plot_extinction_map(self, ax, v_min=None, v_max=None, **kwargs):
        """

        :param ax:
        :param v_min:
        :param v_max:
        :return:
        """
        model = self.bandmodel.extinction_map(self._kwargs_extinction_partial, self._kwargs_special_partial)
        if v_min is None:
            v_min = 0
        if v_max is None:
            v_max = 1

        im = ax.matshow(model, origin='lower', vmin=v_min, vmax=v_max,
                        extent=[0, self._frame_size, 0, self._frame_size], **kwargs)
        return ax