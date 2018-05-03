from setuptools import setup


setup(
    name='morsetalk',
    version='1.0.2',
    install_requires=[
    ],
    packages=[
        'morsetalk'
    ],
    entry_points={
        'console_scripts': [
            'morsetalk = morsetalk.bin:run'
        ]
    }
)
