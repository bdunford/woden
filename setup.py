from setuptools import setup

setup(name='woden',
    version='0.1',
    description='Just some python helpers for doing a few things. Some stuff is pointless I agree.',
    url='http://github.com/bdunford/woden',
    author='Frustrated User',
    author_email='birch.dunford@gmail.com',
    license='MIT',
    packages=[
        'woden',
        'woden/web', 
        'woden/network', 
        'woden/system', 
        'woden/exploit',  
        'woden/utility'
    ],
    zip_safe=False,
    install_requires=[
        'future',
        'pyOpenSSL',
        'requests',
        'requests_ntlm',
        'dnspython'
    ]
)
