from setuptools import setup, find_packages

setup(
    name='film_ranking',
    version='0.1',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'pandas',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'film_ranking=main:main',
        ],
    },
)
