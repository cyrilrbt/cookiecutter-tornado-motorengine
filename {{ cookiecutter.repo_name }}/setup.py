from setuptools import setup, find_packages


setup(
    name='youtube.playlists',
    version=0.0,
    author='Cyril Robert',
    author_email='cyril@hippie.io',
    url='http://67labs.com',
    install_requires=[
        'setuptools',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    namespace_packages=['youtube.playlists', ],
    entry_points={
        'console_scripts': [
            'youtube.playlists = youtube.playlists.main:run',
        ]},
)
