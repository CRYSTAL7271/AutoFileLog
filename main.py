from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Samsung:: Tablet :: GalaxyTabS6Lite',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='CrystalStudios',
  version='0.0.1',
  description='Creates a file log for you, easy and fast.',
  long_description=open('README.md').read(),
  url='',  
  author='CrystalStudios',
  author_email='sebastian.lentini210@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='calculator', 
  packages=find_packages(),
  install_requires=[''] 
)	
