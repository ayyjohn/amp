from setuptools import setup, find_packages

setup(
    name='amp-player',
    version='0.1.3',
    description='Asynchronous command-line YouTube interface',
    keywords=["music", "audio", "video", "stream", "youtube"],
    url='https://github.com/nivekuil/amp',
    download_url='https://github.com/nivekuil/amp/tarball/master',
    author='Kevin Liu',
    author_email='mail@nivekuil.com',
    license='GPL3',
    entry_points={'console_scripts': ['amp = amp.main:main']},
    package_dir = {'': 'amp'},
    packages = ['amp'],
    install_requires=['pafy >= 0.3.74', 'psutil'],
    classifiers = [
        'Programming Language :: Python :: 3',
    ],

)