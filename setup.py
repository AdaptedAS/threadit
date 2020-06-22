from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='threadit',
      version='1.2.2',
      description='Takes the hassle away from threading functions and getting their results',
      url='https://github.com/AdaptedAS/threadit',
      author='Odd Jøren Røland',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author_email='odd@adapted.no',
      license='MIT',
      packages=['threadit'],
      platforms=['any'],
      keywords=['threading', 'threads'],
      include_package_data=True,
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      zip_safe=False
      )
