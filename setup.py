from setuptools import setup
from setuptools import find_packages


# Remember to update local-oldest-requirements.txt when changing the minimum
# acme/certbot version.

version='0.1'

docs_extras = [
    'Sphinx>=1.0',  # autodoc_member_order = 'bysource', autodoc_default_flags
    'sphinx_rtd_theme',
]

setup(
    name='certbot-dns-vultr',
    version=version,
    description="Vultr DNS Authenticator plugin for Certbot",
    url='https://github.com/bsorahan/certbot-dns-vultr.git',
    author="Ben Sorahan",
    license='MIT License',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires = [
        'acme>=0.21.1',
        'certbot>=0.21.1',
        'dns-lexicon>=3.6.0', # Support for >1 TXT record per name
        'mock',
        'setuptools',
        'zope.interface',
    ],
    packages=find_packages(),
    include_package_data=True,
    extras_require={
        'docs': docs_extras,
    },
    entry_points={
        'certbot.plugins': [
            'dns-vultr = certbot_dns_vultr.dns_vultr:Authenticator',
        ],
    }
)
