import setuptools


setuptools.setup(
    name='stardust-rpg',
    version='0.0.1',

    description='',
    long_description=open('README.rst').read(),
    keywords='stardust role-playing d20',

    author='John Hagen',
    author_email='johnthagen@gmail.com',
    url='https://github.com/johnthagen/stardust-rpg',
    license='MIT',
    install_requires=open('requirements.txt').readlines(),

    zip_safe=False,

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Topic :: Games/Entertainment :: Role-Playing',
    ],
)
