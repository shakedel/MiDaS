from setuptools import setup, find_packages

packages = ['MiDaS', 'MiDaS.tf'] +\
           ['MiDaS.midas'] + ['MiDaS.midas.'+p for p in find_packages('midas')]

setup(
    name='MiDaS',
    version='0.0.1',
    description='',
    packages=packages,
    package_dir={p: p.replace('.', '/').replace('MiDaS', '.') for p in packages},
    install_requires=[
        'torch',
        'torchvision',
        'numpy',
        'opencv-python',
        'imutils',
        'timm',
        'einops'
    ],
)
