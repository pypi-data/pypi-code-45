# Copyright 2018-2019 CNRS, Ecole Polytechnique and Safran.
#
# This file is part of nullspace_optimizer.
#
# nullspace_optimizer is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# nullspace_optimizer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# A copy of the GNU General Public License is included below.
# For further information, see <http://www.gnu.org/licenses/>.

import setuptools

long_description = r"""
# Null space optimizer
`nullspace_optimizer` is a package implementing the null space algorithm for nonlinear constrained
optimization.

Please cite the following references when using this source:

FEPPON, Florian, ALLAIRE, Grégoire, et DAPOGNY, Charles.
*Null space gradient flows for constrained optimization with applications to
 shape optimization.* 2019. HAL preprint [hal-01972915](https://hal.archives-ouvertes.fr/hal-01972915/document).

FEPPON, Florian. *Shape and topology optimization of multiphysics systems.* 2019.
Université Paris-Saclay. Thèse préparée à l'École polytechnique.

# Installation

```bash
# Light version
pip install nullspace_optimizer

# Full dependencies including colored output and plotting features
pip install nullspace_optimizer[colored,matplotlib]
```

# Running examples
A few examples of 2-d inequality constrained optimization are available in the `examples' folder.
They can be run from command line with

```bash
python -m nullspace_optimizer.examples.ex0
python -m nullspace_optimizer.examples.ex1
python -m nullspace_optimizer.examples.ex2
```
and so on. 

For instance, running `python -m nullspace_optimizer.examples.ex1` should produce the following figure:
<img src="https://gitlab.com/florian.feppon/null-space-optimizer/raw/public-master/nullspace.png" align="center" alt="Null space gradient flow trajectories" width="40%">

# Requirements
Runs with python 3.6 and the following libraries:
* numpy (>=1.12.1)
* scipy (>=0.19.1)
* cvxopt (>=1.2.1)

Optional dependencies:
* colored (>=1.3.93)   *(for colored output)*
* matplotlib (>=2.0.2) *(for displaying figures while running examples)*
"""

setuptools.setup(
    name="nullspace_optimizer",
    version="1.0.0",
    author="Florian Feppon",
    author_email="florian.feppon@polytechnique.edu",
    license="GNU GPL version 3",
    description="Null space algorithm for nonlinear constrained optimization",
    keywords="nonlinear constrained optimization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/florian.feppon/null-space-optimizer",
    packages=['nullspace_optimizer','nullspace_optimizer.examples'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    install_requires=['numpy>=1.12.1',
                      'scipy>=0.19.1',
                      'cvxopt>=1.2.1',
                      ],
    extras_require={'colored': ['colored>=1.3.93'],
                    'matplotlib': ['matplotlib>=2.0.2']},
    python_requires='>=3.6',
)
