from setuptools import setup, find_packages

setup(
    name='Xunit2 plugin',
    # ...
    entry_points={
        'nose.plugins.0.10': [
            'xunit2 = xunit2:Xunit2'
        ]
    },
    packages=find_packages(),
    # ...
)
