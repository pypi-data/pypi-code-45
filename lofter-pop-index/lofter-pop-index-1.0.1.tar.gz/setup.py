#     LOFTER-POP-INDEX, an automatic tool used for increase LOFTER blogs' popular index.
#     Copyright (C) 2019  PengFCB
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lofter-pop-index",  # Replace with your own username
    version="1.0.1",
    author="PengFCB",
    author_email="peng_fcb@qq.com",
    description="An automatic tool used for increasing LOFTER blogs' popular index.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PengFCB/lofter_pop_index",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    python_requires='>=3.6',
    install_requires=[
        "selenium"
    ]
)
