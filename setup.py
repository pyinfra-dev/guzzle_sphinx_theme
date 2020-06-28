from setuptools import setup

setup(
    name='pyinfra-guzzle_sphinx_theme',
    version='0.1',
    description='Sphinx theme used by Guzzle, with customisations for pyinfra.',
    author='Michael Dowling (modified by Nick Barrett)',
    author_email='pointlessrambler@gmail.com',
    url='https://github.com/Fizzadar/guzzle_sphinx_theme',
    packages=['guzzle_sphinx_theme'],
    include_package_data=True,
    install_requires=['Sphinx>1.3'],
    license="MIT",
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ),
)
