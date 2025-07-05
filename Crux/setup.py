from setuptools import setup, find_packages

setup(
    name='crux-aes',
    version='1.0.0',
    author='aesneverhere',
    author_email='aesh.n@outlook.com',
    description='A lightweight, modular Python utility library for aes-co projects.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aes-co/crux', # Assuming a GitHub repo will be created
    packages=find_packages(where='.'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Utility Modules',
    ],
    python_requires='>=3.10',
    install_requires=[
        'aiohttp',
    ],
)
