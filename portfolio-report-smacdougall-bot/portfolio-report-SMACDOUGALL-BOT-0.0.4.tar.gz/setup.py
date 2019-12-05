# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0330
# pylint: disable=C0303



import setuptools


setuptools.setup(
    name="portfolio-report-SMACDOUGALL-BOT", # Replace with your own username
    version="0.0.4",
    author="Steve MacDougall",
    author_email="sgmacdougall@gmail.com",
    description="Generates a CSV of portfilio holdings and their performance",
    packages=['portfolio'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
	'console_scripts': ['portfolio_report=portfolio.portfolio_report:main']
    },
    install_requires=[
	"pytest>=4.3.1"
	"pylint>=2.3.1"
	"six>=1.12"
	"requests>=2.22"
	"requests-mock>=1.7"
	]	
)
