
from setuptools import setup, find_packages

setup(
    name='test_scene',
    version=1.0,
    author='smironenko',
    company='topcon',
    author_email='smironenko@topcom.com',
    packages=find_packages(),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'test_scene = test_scene.scene_view:main'

        ],
    },
    package_data={
        'test_scene': [
            '*.ui']
    },
)
