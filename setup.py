from setuptools import setup

setup(name='citrine_point_sampler',
      version='0.1',
      description='Efficient generation of high dimensional points subject to constraints.',
      url='http://github.com/LeanAndMean/citrine_point_sampler',
      author='Kevin Ryan',
      author_email='KevinRyan7926+citrine_point_sampler@gmail.com',
      license='MIT',
      packages=['citrine_point_sampler'],
      install_requires=["numpy"],
      setup_requires=["pytest-runner"],
      tests_require=["pytest"],
      entry_points = {
        'console_scripts': ['citrine_point_sampler-sampler=citrine_point_samplier.sampler.main'],
      },
      include_package_data=True,
      zip_safe=False)