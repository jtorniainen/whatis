from setuptools import setup

setup(name='whatis',
      version='0.0.1',
      description='A diagnostic tool for inspecting variables',
      author='Jari Torniainen, Quantified Employee at the Finnish Institute of Occupational Health',
      author_email='jari.torniainen@ttl.fi',
      url='https://github.com/jtorniainen/whatis',
      license='MIT',
      packages=['whatis'],
      package_dir={'whatis': 'whatis'},
      include_package_data=False,
)
