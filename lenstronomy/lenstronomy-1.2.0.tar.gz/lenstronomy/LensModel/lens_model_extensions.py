import numpy as np
import lenstronomy.Util.util as util
import lenstronomy.Util.mask_util as mask_util
import lenstronomy.Util.param_util as param_util


class LensModelExtensions(object):
    """
    class with extension routines not part of the LensModel core routines
    """
    def __init__(self, lensModel):
        """

        :param lensModel: instance of the LensModel() class, or with same functionalities.
        In particular, the following definitions are required to execute all functionalities presented in this class:
        def ray_shooting()
        def magnification()
        def kappa()
        def alpha()
        def hessian()

        """
        self._lensModel = lensModel

    def magnification_finite(self, x_pos, y_pos, kwargs_lens, source_sigma=0.003, window_size=0.1, grid_number=100,
                             shape="GAUSSIAN", polar_grid=False, aspect_ratio=0.5):
        """
        returns the magnification of an extended source with Gaussian light profile
        :param x_pos: x-axis positons of point sources
        :param y_pos: y-axis position of point sources
        :param kwargs_lens: lens model kwargs
        :param source_sigma: Gaussian sigma in arc sec in source
        :param window_size: size of window to compute the finite flux
        :param grid_number: number of grid cells per axis in the window to numerically comute the flux
        :return: numerically computed brightness of the sources
        """

        mag_finite = np.zeros_like(x_pos)
        deltaPix = float(window_size)/grid_number
        if shape == 'GAUSSIAN':
            from lenstronomy.LightModel.Profiles.gaussian import Gaussian
            quasar = Gaussian()
        elif shape == 'TORUS':
            import lenstronomy.LightModel.Profiles.ellipsoid as quasar
        else:
            raise ValueError("shape %s not valid for finite magnification computation!" % shape)
        x_grid, y_grid = util.make_grid(numPix=grid_number, deltapix=deltaPix, subgrid_res=1)

        if polar_grid is True:
            a = window_size*0.5
            b = window_size*0.5*aspect_ratio
            ellipse_inds = (x_grid*a**-1) **2 + (y_grid*b**-1) **2 <= 1
            x_grid, y_grid = x_grid[ellipse_inds], y_grid[ellipse_inds]

        for i in range(len(x_pos)):
            ra, dec = x_pos[i], y_pos[i]

            center_x, center_y = self._lensModel.ray_shooting(ra, dec, kwargs_lens)

            if polar_grid is True:
                theta = np.arctan2(dec,ra)
                xcoord, ycoord = util.rotate(x_grid, y_grid, theta)
            else:
                xcoord, ycoord = x_grid, y_grid

            betax, betay = self._lensModel.ray_shooting(xcoord + ra, ycoord + dec, kwargs_lens)

            I_image = quasar.function(betax, betay, 1., source_sigma, center_x, center_y)
            mag_finite[i] = np.sum(I_image) * deltaPix**2
        return mag_finite

    def zoom_source(self, x_pos, y_pos, kwargs_lens, source_sigma=0.003, window_size=0.1, grid_number=100,
                             shape="GAUSSIAN"):
        """
        computes the surface brightness on an image with a zoomed window

        :param x_pos: angular coordinate of center of image
        :param y_pos: angular coordinate of center of image
        :param kwargs_lens: lens model parameter list
        :param source_sigma: source size (in angular units)
        :param window_size: window size in angular units
        :param grid_number: number of grid points per axis
        :param shape: string, shape of source, supports 'GAUSSIAN' and 'TORUS
        :return: 2d numpy array
        """
        deltaPix = float(window_size) / grid_number
        if shape == 'GAUSSIAN':
            from lenstronomy.LightModel.Profiles.gaussian import Gaussian
            quasar = Gaussian()
        elif shape == 'TORUS':
            import lenstronomy.LightModel.Profiles.ellipsoid as quasar
        else:
            raise ValueError("shape %s not valid for finite magnification computation!" % shape)
        x_grid, y_grid = util.make_grid(numPix=grid_number, deltapix=deltaPix, subgrid_res=1)
        center_x, center_y = self._lensModel.ray_shooting(x_pos, y_pos, kwargs_lens)
        betax, betay = self._lensModel.ray_shooting(x_grid + x_pos, y_grid + y_pos, kwargs_lens)
        image = quasar.function(betax, betay, 1., source_sigma, center_x, center_y)
        return util.array2image(image)

    def critical_curve_tiling(self, kwargs_lens, compute_window=5, start_scale=0.5, max_order=10):
        """

        :param kwargs_lens:
        :param compute_window:
        :param tiling_scale:
        :return:
        """
        numPix = int(compute_window / start_scale)
        x_grid_init, y_grid_init = util.make_grid(numPix, deltapix=start_scale, subgrid_res=1)
        mag_init = util.array2image(self._lensModel.magnification(x_grid_init, y_grid_init, kwargs_lens))
        x_grid_init = util.array2image(x_grid_init)
        y_grid_init = util.array2image(y_grid_init)

        ra_crit_list = []
        dec_crit_list = []
        # iterate through original triangles and return ra_crit, dec_crit list
        for i in range(numPix-1):
            for j in range(numPix-1):
                edge1 = [x_grid_init[i, j], y_grid_init[i, j], mag_init[i, j]]
                edge2 = [x_grid_init[i+1, j+1], y_grid_init[i+1, j+1], mag_init[i+1, j+1]]
                edge_90_1 = [x_grid_init[i, j+1], y_grid_init[i, j+1], mag_init[i, j+1]]
                edge_90_2 = [x_grid_init[i+1, j], y_grid_init[i+1, j], mag_init[i+1, j]]
                ra_crit, dec_crit = self._tiling_crit(edge1, edge2, edge_90_1, max_order=max_order,
                                                      kwargs_lens=kwargs_lens)
                ra_crit_list += ra_crit  # list addition
                dec_crit_list += dec_crit  # list addition
                ra_crit, dec_crit = self._tiling_crit(edge1, edge2, edge_90_2, max_order=max_order,
                                                      kwargs_lens=kwargs_lens)
                ra_crit_list += ra_crit  # list addition
                dec_crit_list += dec_crit  # list addition
        return np.array(ra_crit_list), np.array(dec_crit_list)

    def _tiling_crit(self, edge1, edge2, edge_90, max_order, kwargs_lens):
        """
        tiles a rectangular triangle and compares the signs of the magnification

        :param edge1: [ra_coord, dec_coord, magnification]
        :param edge2: [ra_coord, dec_coord, magnification]
        :param edge_90: [ra_coord, dec_coord, magnification]
        :param max_order: maximal order to fold triangle
        :return:
        """
        ra_1, dec_1, mag_1 = edge1
        ra_2, dec_2, mag_2 = edge2
        ra_3, dec_3, mag_3 = edge_90
        sign_list = np.sign([mag_1, mag_2, mag_3])
        if sign_list[0] == sign_list[1] and sign_list[0] == sign_list[2]:  # if all signs are the same
            return [], []
        else:
            # split triangle along the long axis
            # execute tiling twice
            # add ra_crit and dec_crit together
            # if max depth has been reached, return the mean value in the triangle
            max_order -= 1
            if max_order <= 0:
                return [(ra_1 + ra_2 + ra_3)/3], [(dec_1 + dec_2 + dec_3)/3]
            else:
                # split triangle
                ra_90_ = (ra_1 + ra_2)/2  # find point in the middle of the long axis to split triangle
                dec_90_ = (dec_1 + dec_2)/2
                mag_90_ = self._lensModel.magnification(ra_90_, dec_90_, kwargs_lens)
                edge_90_ = [ra_90_, dec_90_, mag_90_]
                ra_crit, dec_crit = self._tiling_crit(edge1=edge_90, edge2=edge1, edge_90=edge_90_, max_order=max_order,
                                                      kwargs_lens=kwargs_lens)
                ra_crit_2, dec_crit_2 = self._tiling_crit(edge1=edge_90, edge2=edge2, edge_90=edge_90_, max_order=max_order,
                                                          kwargs_lens=kwargs_lens)
                ra_crit += ra_crit_2
                dec_crit += dec_crit_2
                return ra_crit, dec_crit

    def critical_curve_caustics(self, kwargs_lens, compute_window=5, grid_scale=0.01):
        """

        :param kwargs_lens: lens model kwargs
        :param compute_window: window size in arcsec where the critical curve is computed
        :param grid_scale: numerical grid spacing of the computation of the critical curves
        :return: lists of ra and dec arrays corresponding to different disconnected critical curves and their caustic counterparts

        """
        numPix = int(compute_window / grid_scale)
        x_grid_high_res, y_grid_high_res = util.make_grid(numPix, deltapix=grid_scale, subgrid_res=1)
        mag_high_res = util.array2image(self._lensModel.magnification(x_grid_high_res, y_grid_high_res, kwargs_lens))

        ra_crit_list = []
        dec_crit_list = []
        ra_caustic_list = []
        dec_caustic_list = []

        import matplotlib.pyplot as plt
        cs = plt.contour(util.array2image(x_grid_high_res), util.array2image(y_grid_high_res), mag_high_res, [0],
                         alpha=0.0)
        paths = cs.collections[0].get_paths()
        for i, p in enumerate(paths):
            v = p.vertices
            ra_points = v[:, 0]
            dec_points = v[:, 1]
            ra_crit_list.append(ra_points)
            dec_crit_list.append(dec_points)
            ra_caustics, dec_caustics = self._lensModel.ray_shooting(ra_points, dec_points, kwargs_lens)
            ra_caustic_list.append(ra_caustics)
            dec_caustic_list.append(dec_caustics)
        plt.cla()
        return ra_crit_list, dec_crit_list, ra_caustic_list, dec_caustic_list

    def hessian_eigenvectors(self, x, y, kwargs_lens, diff=None):
        """
        computes magnification eigenvectors at position (x, y)

        :param x: x-position
        :param y: y-position
        :param kwargs_lens: lens model keyword arguments
        :return: radial stretch, tangential stretch
        """
        f_xx, f_xy, f_yx, f_yy = self._lensModel.hessian(x, y, kwargs_lens, diff=diff)
        if isinstance(x, int) or isinstance(x, float):
            A = np.array([[1-f_xx, f_xy], [f_yx, 1-f_yy]])
            w, v = np.linalg.eig(A)
            v11, v12, v21, v22 = v[0, 0], v[0, 1], v[1, 0], v[1, 1]
            w1, w2 = w[0], w[1]
        else:
            w1, w2, v11, v12, v21, v22 = np.empty(len(x), dtype=float), np.empty(len(x), dtype=float), np.empty_like(x), np.empty_like(x), np.empty_like(x), np.empty_like(x)
            for i in range(len(x)):
                A = np.array([[1 - f_xx[i], f_xy[i]], [f_yx[i], 1 - f_yy[i]]])
                w, v = np.linalg.eig(A)
                w1[i], w2[i] = w[0], w[1]
                v11[i], v12[i], v21[i], v22[i] = v[0, 0], v[0, 1], v[1, 0], v[1, 1]
        return w1, w2, v11, v12, v21, v22

    def radial_tangential_stretch(self, x, y, kwargs_lens, diff=None):
        """
        computes the radial and tangential stretches at a given position

        :param x: x-position
        :param y: y-position
        :param kwargs_lens: lens model keyword arguments
        :param diff: float or None, finite average differential scale
        :return: radial stretch, tangential stretch
        """
        w0, w1, v11, v12, v21, v22 = self.hessian_eigenvectors(x, y, kwargs_lens, diff=diff)
        if isinstance(x, int) or isinstance(x, float):
            if w0 > w1:
                radial_stretch = 1. / w0
                tangential_stretch = 1. / w1
                v_rad1, v_rad2 = v11, v12
                v_tang1, v_tang2 = v21, v22
            else:
                radial_stretch = 1. / w1
                tangential_stretch = 1. / w0
                v_rad1, v_rad2 = v21, v22
                v_tang1, v_tang2 = v11, v12
        else:
            radial_stretch, tangential_stretch, v_rad1, v_rad2, v_tang1, v_tang2 = np.empty(len(x), dtype=float), np.empty(len(x), dtype=float), np.empty_like(x), np.empty_like(x), np.empty_like(x), np.empty_like(x)
            for i in range(len(x)):
                if w0[i] > w1[i]:
                    radial_stretch[i] = 1. / w0[i]
                    tangential_stretch[i] = 1. / w1[i]
                    v_rad1[i], v_rad2[i] = v11[i], v12[i]
                    v_tang1[i], v_tang2[i] = v21[i], v22[i]
                else:
                    radial_stretch[i] = 1. / w1[i]
                    tangential_stretch[i] = 1. / w0[i]
                    v_rad1[i], v_rad2[i] = v21[i], v22[i]
                    v_tang1[i], v_tang2[i] = v11[i], v12[i]

        return radial_stretch, tangential_stretch, v_rad1, v_rad2, v_tang1, v_tang2

    def radial_tangential_differentials(self, x, y, kwargs_lens, center_x=0, center_y=0, smoothing_3rd=0.001, smoothing_2nd=None):
        """
        computes the differentials in stretches and directions

        :param x: x-position
        :param y: y-position
        :param kwargs_lens: lens model keyword arguments
        :param center_x: x-coord of center towards which the rotation direction is defined
        :param center_y: x-coord of center towards which the rotation direction is defined
        :param smoothing_3rd: finite differential length of third order in units of angle
        :param smoothing_2nd: float or None, finite average differential scale of Hessian
        :return:
        """
        radial_stretch, tangential_stretch, v_rad1, v_rad2, v_tang1, v_tang2 = self.radial_tangential_stretch(x, y, kwargs_lens, diff=smoothing_2nd)
        x0 = x - center_x
        y0 = y - center_y
        dx_tang = x + smoothing_3rd * v_tang1
        dy_tang = y + smoothing_3rd * v_tang2
        rad_dt, tang_dt, v_rad1_dt, v_rad2_dt, v_tang1_dt, v_tang2_dt = self.radial_tangential_stretch(dx_tang, dy_tang, kwargs_lens, diff=smoothing_2nd)

        d_tang_d_tang = (tang_dt - tangential_stretch) / smoothing_3rd * np.sign(v_tang1 * y0 - v_tang2 * x0)
        cos_delta = v_tang1 * v_tang1_dt + v_tang2 * v_tang2_dt # / (np.sqrt(v_tang1**2 + v_tang2**2) * np.sqrt(v_tang1_dt**2 + v_tang2_dt**2))
        norm = np.sqrt(v_tang1**2 + v_tang2**2) * np.sqrt(v_tang1_dt**2 + v_tang2_dt**2)
        cos_delta /= norm
        arc_cos = np.arccos(np.abs(np.minimum(cos_delta, 1)))
        d_angle_d_tang = arc_cos / smoothing_3rd

        dx_rad = x + smoothing_3rd * v_rad1
        dy_rad = y + smoothing_3rd * v_rad2
        rad_dr, tang_dr, v_rad1_dr, v_rad2_dr, v_tang1_dr, v_tang2_dr = self.radial_tangential_stretch(dx_rad, dy_rad, kwargs_lens, diff=smoothing_2nd)
        cos_delta = v_rad1 * v_rad1_dr + v_rad2 * v_rad2_dr / (np.sqrt(v_rad1**2 + v_rad2**2) * np.sqrt(v_rad1_dr**2 + v_rad2_dr**2))

        cos_delta = np.minimum(cos_delta, 1)
        d_angle_d_rad = np.arccos(cos_delta) / smoothing_3rd
        d_rad_d_rad = (rad_dr - radial_stretch) / smoothing_3rd * np.sign(v_rad1 * x0 + v_rad2 * y0)

        d_tang_d_rad = (tang_dr - tangential_stretch) / smoothing_3rd * np.sign(v_rad1 * x0 + v_rad2 * y0)

        cos_angle = (v_tang1 * x0 + v_tang2 * y0) / np.sqrt((x0**2 + y0**2) * (v_tang1**2 + v_tang2**2)) * np.sign(v_tang1 * y0 - v_tang2 * x0)
        angle = np.arccos(cos_angle) - np.pi / 2
        return radial_stretch, tangential_stretch, d_tang_d_tang, d_tang_d_rad, d_angle_d_tang, d_rad_d_rad, d_angle_d_rad, angle

    def curved_arc_estimate(self, x, y, kwargs_lens, smoothing=None, smoothing_3rd=0.001):
        """
        performs the estimation of the curved arc description at a particular position of an arbitrary lens profile

        :param x: float, x-position where the estimate is provided
        :param y: float, y-position where the estimate is provided
        :param kwargs_lens: lens model keyword arguments
        :return: keyword argument list corresponding to a CURVED_ARC profile at (x, y) given the initial lens model
        """
        radial_stretch, tangential_stretch, v_rad1, v_rad2, v_tang1, v_tang2 = self.radial_tangential_stretch(x, y, kwargs_lens, diff=smoothing)
        dx_tang = x + smoothing_3rd * v_tang1
        dy_tang = y + smoothing_3rd * v_tang2
        rad_dt, tang_dt, v_rad1_dt, v_rad2_dt, v_tang1_dt, v_tang2_dt = self.radial_tangential_stretch(dx_tang, dy_tang,
                                                                                                       kwargs_lens,
                                                                                                       diff=smoothing)
        d_tang1 = v_tang1_dt - v_tang1
        d_tang2 = v_tang2_dt - v_tang2
        delta = np.sqrt(d_tang1**2 + d_tang2**2)
        if delta > 1:
            d_tang1 = v_tang1_dt + v_tang1
            d_tang2 = v_tang2_dt + v_tang2
            delta = np.sqrt(d_tang1 ** 2 + d_tang2 ** 2)
        curvature = delta / smoothing_3rd
        direction = np.arctan2(v_rad2 * np.sign(v_rad1 * x + v_rad2 * y), v_rad1 * np.sign(v_rad1 * x + v_rad2 * y))
        kwargs_arc = {'radial_stretch': radial_stretch,
                      'tangential_stretch': tangential_stretch,
                      'curvature': curvature,
                      'direction': direction,
                      'center_x': x, 'center_y': y}
        return kwargs_arc
