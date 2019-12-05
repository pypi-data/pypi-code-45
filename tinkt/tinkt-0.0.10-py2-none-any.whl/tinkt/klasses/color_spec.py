# -*- coding:utf-8 -*-

import six
from konfluence import Konfluence
import numpy as np
from matplotlib import colors as mpl_colors
from matplotlib import pyplot as plt

from krux.types.check import is_integer, is_seq
from tinkt.cmap_utils import get_cmap


class ColorSpec(object):
    konf = Konfluence()

    def __init__(self, name='unknown', cmap=plt.cm.jet, norm=None, vmin=None, vmax=None, levels=None, categories=None, label=None, **kwargs):
        self.name = name
        try:
            if isinstance(cmap, mpl_colors.Colormap):
                self.cmap = cmap
            elif isinstance(cmap, six.string_types):
                if cmap.startswith('colormap/'):
                    self.cmap = self.konf.get(cmap, 'default')
                else:
                    self.cmap = get_cmap(cmap)
            elif isinstance(cmap, (list, tuple, np.ndarray)):
                self.cmap = mpl_colors.ListedColormap(cmap)
            else:
                raise ValueError
        except Exception as e:
            raise ValueError(u'Cannot parse cmap: {}'.format(cmap))

        try:
            if norm is None or isinstance(norm, mpl_colors.Normalize):
                self.norm = norm
            elif isinstance(norm, six.string_types):
                self.norm = self.konf[norm]
            elif isinstance(norm, (list, tuple, np.ndarray)):
                self.norm = mpl_colors.BoundaryNorm(norm, len(norm)-1, clip=False)
            else:
                raise ValueError
        except Exception as e:
            raise ValueError(u'Cannot parse norm: {}'.format(norm))

        self._vmin = vmin
        self._vmax = vmax
        self._levels = levels
        self.categories = categories
        self.label = label

    def colorbar(self, fig, cax=None, label=None, orientation=None, **kwargs):
        if orientation is None:
            fig_w, fig_h = fig.get_size_inches()
            orientation = 'horizontal' if fig_w >= fig_h else 'vertical'

        if not cax:
            if orientation == 'horizontal':
                cax = fig.add_axes((0.1, 0.35, 0.8, 0.15))
            else:
                cax = fig.add_axes((0.2, 0.15, 0.15, 0.75))

        data_ax = fig.add_axes((1.1, 1.1, 0, 0))
        data = np.linspace(self.vmin, self.vmax, 12).reshape(3, 4)

        if label is None:
            label = self.label

        if not self.norm:
            pc = data_ax.pcolormesh(data, cmap=self.cmap)
        else:
            pc = data_ax.pcolormesh(data, cmap=self.cmap, norm=self.norm)

        clb = plt.colorbar(mappable=pc, cax=cax, ax=data_ax, orientation=orientation, **kwargs)

        if label:
            if orientation == 'horizontal':
                x, y = 0.5, 0.75
            else:
                x, y = 0.5, 0.1
            plt.figtext(x, y, label, figure=fig, ha='center', va='top')

        if isinstance(self.norm, mpl_colors.BoundaryNorm):
            if self.categories:
                pass  # TODO

        return clb

    @property
    def vmin(self):
        if self._vmin is not None:
            return self._vmin
        elif self.norm is not None:
            return self.norm.vmin
        else:
            return None

    @property
    def vmax(self):
        if self._vmax is not None:
            return self._vmax
        elif self.norm is not None:
            return self.norm.vmax
        else:
            return None

    @property
    def levels(self):
        if isinstance(self.norm, mpl_colors.BoundaryNorm):
            return self.norm.boundaries
        else:
            if not self._levels:
                return None

            if is_integer(self._levels):
                vmin = self.vmin
                vmax = self.vmax
                if vmin is None or vmax is None:
                    return None

                if self.norm is None:
                    return np.linspace(vmin, vmax, self._levels)
                else:
                    if isinstance(self.norm, (mpl_colors.PowerNorm, mpl_colors.LogNorm, mpl_colors.SymLogNorm)):
                        raise NotImplementedError()
                    else:
                        return np.linspace(vmin, vmax, self._levels)

            elif is_seq(self._levels):
                return self._levels

    def copy(self):
        return self.__class__(
            name=self.name,
            cmap=self.cmap, norm=self.norm,
            vmin=self._vmin, vmax=self._vmax, levels=self._levels,
            categories=self.categories,
            label=self.label
        )

    def get_contour_opts(self):
        # TODO: handle levels and other stuffs
        return {
            "cmap": self.cmap,
            "norm": self.norm,
            "vmin": self._vmin,
            "vmax": self._vmax
        }

    def get_pcolor_opts(self):
        # TODO: handle levels
        return {
            "cmap": self.cmap,
            "norm": self.norm,
            "vmin": self._vmin,
            "vmax": self._vmax
        }
