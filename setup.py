# -*- coding: utf-8 -*-
"""
Created on Sun May  9 10:59:55 2021

@author: Maria
"""
from setuptools import find_packages, setup

import sys

cv_ver = ""
keras_ver = ">=2.0.0"
if sys.version_info.major < 3:
      cv_ver = "<=4.2.0.32" 
      keras_ver = "<=2.3.0"


setup(name="keras_segmentation",
      version="0.3.0",
      description="Image Segmentation of Bones from CT for keras",
      author="Maria Albu",
      author_email='albu.madalina85@gmail.com',
      platforms=["any"],  # "win64", 
      license="GPLv3",
      url="https://github.com/mba15mma/CT-segmentation",
      packages=find_packages(exclude=["test"]),
      entry_points={
            'console_scripts': [
                  'bone_segmentation = bone_segmentation.__main__:main'
            ]
      },
      install_requires=[
            "Keras"+keras_ver,
            "imageio==2.5.0",
            "imgaug==0.2.9",
            "opencv-python"+cv_ver,
            "tqdm"],
      extras_require={
            # These requires provide different backends available with Keras
            "tensorflow": ["tensorflow"],
            "cntk": ["cntk"],
            "theano": ["theano"],
            # Default testing with tensorflow
            "tests-default": ["tensorflow", "pytest"]
      }
)