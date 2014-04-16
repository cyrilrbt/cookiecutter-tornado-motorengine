from setuptools import setup, find_packages


setup(
    name='{{ cookiecutter.project }}',
    version=0.0,
    author='{{ cookiecutter.ful_name }}',
    author_email='{{ cookiecutter.email }}',
    url='http://67labs.com',
    install_requires=[
        'setuptools',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    namespace_packages=['{{ cookiecutter.project }}', ],
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project }} = {{ cookiecutter.project }}.main:run',
        ]},
)
