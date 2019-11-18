
def _get_version(version_info):
    """
    converts version info tuple to version string
    example:
        (0, 1, 2, 'beta', 3) returns '0.1.2-beta.3'
    """
    vi = [str(e) for e in version_info]
    suffix = ''
    if len(vi) > 3:
        suffix = '-' + '.'.join(vi[3:])
    version = '.'.join(vi[:3]) + suffix
    return version


# meta data

__name__ = 'ipyhc'
name_url = __name__.replace('_', '-')


version_info = (0, 0, 0, 'alpha', 5)
__version__ = _get_version(version_info) # https://www.highcharts.com/

# must be MANUALLY synced wih js.package.json.version
version_js_info = (0, 0, 0, 'alpha', 5)
__version_js__ = _get_version(version_js_info)


__description__ = 'Jupyter widget - highcharts in the notebook'
__long_description__ = 'See repo README'
__author__ = 'DGothrek'
__author_email__ = 'louisraison1@gmail.com'

# gitlab template
__url__ = 'https://gitlab.com/{}/{}'.format(__author__, name_url)
__download_url__ = 'https://gitlab.com/{}/{}/repository/archive.tar.gz?ref={}'.format(__author__,
                                                                                      name_url+"-dev",
                                                                                      __version__)

__keywords__ = ['ipyhc',
                'javascript',
                'highcharts',
                ]
__license__ = 'MIT'
__classifiers__ = ['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'
                   ]
__include_package_data__ = True
__package_data__ = {}
__data_files__ = [
    ('share/jupyter/nbextensions/ipyhc', [
        'ipyhc/static/extension.js',
        'ipyhc/static/index.js',
        'ipyhc/static/index.js.map',
    ]),
    # classic notebook extension
    ('etc/jupyter/nbconfig/notebook.d', [
        'ipyhc/ipyhc.json'
    ]),
]
__zip_safe__ = False
__entry_points__ = {}
