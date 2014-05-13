import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

DEPENDENCYLINKS = []
REQUIRES = []


setup(
    name='orgalytics',
    description='Github Contribution for Organizations',
    keywords='github',
    version="0.0.1",
    author='Caleb Groom',
    author_email='caleb@calebgroom.com',
    dependency_links=DEPENDENCYLINKS,
    install_requires=REQUIRES,
    entry_points={
        'console_scripts': [
            'orgalytics=orgalytics.entry_points:start'
        ]
    },
    tests_require=['tox'],
    packages=find_packages(exclude=['bin', 'ez_setup']),
    include_package_data=True,
    namespace_packages=['orgalytics'],
    license='Apache License (2.0)',
    classifiers=["Programming Language :: Python"],
    url='http://github.com/calebgroom/orgalytics'
)
