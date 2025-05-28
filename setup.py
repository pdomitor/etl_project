from setuptools import setup, find_packages

setup(
    name='product_revenue',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    extras_require={
        'dev': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'generate-revenue=run:main',
        ],
    },
)
