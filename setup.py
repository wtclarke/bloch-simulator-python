from setuptools import Extension, setup
import numpy

setup(
    ext_modules=[
        Extension(
            name="bloch.bloch_simulator",
            sources = ["src/bloch/bloch_simulator.c"],
            include_dirs=[numpy.get_include()]
        ),
    ]
)
