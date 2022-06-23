from setuptools import setup, find_packages

version = '0.0.1'

install_requires = [
    'setuptools~=57.0.0',
    'aiohttp~=3.8.1',
    'aiodns~=3.0.0',
    'pydantic~=1.9.0',
    'orjson~=3.6.7',
    'oauthlib~=3.2.0',
    'aiohttp-session[secure]~=2.11.0'
]

setup(
    name='aiohttp-oauth',
    version=version,
    description='OAuth async typed framework based on aiohttp, aouthlib libs',
    url='https://',
    author='Leonid Kuzin',
    author_email='dg.inc.lcf@gmail.com',
    license='MIT',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: System :: Networking',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),
    install_requires=install_requires,
    )
