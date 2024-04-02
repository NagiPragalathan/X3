from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = '0.1.0'
DESCRIPTION = 'X3: The Decentralized Programming Language'

setup(
    name='X3Lang',
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://example.com',  # Update with your project URL
    author='NagiPragalathan N',
    author_email='nagiptagalathan@gmail.com',
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
   KEYWORDS = [
    'X3', 'decentralized', 'programming-language', 'blockchain', 'DApps',
    'smart contracts', 'cryptocurrency', 'web3', 'Ethereum', 'solidity',
    'smart contract development', 'decentralized applications', 'crypto',
    'blockchain technology', 'distributed ledger', 'consensus mechanism',
    'tokenization', 'decentralized finance', 'smart contract security',
    'blockchain development', 'crypto development', 'blockchain integration',
    'distributed applications', 'blockchain solutions', 'blockchain platforms',
    'blockchain protocol', 'blockchain architecture', 'decentralized systems',
    'crypto ecosystem', 'blockchain innovations', 'smart contract auditing',
    'blockchain consensus', 'blockchain scalability', 'blockchain interoperability',
    'blockchain governance', 'decentralized governance', 'blockchain privacy',
    'decentralized identity', 'blockchain regulation', 'blockchain use cases',
    'blockchain adoption', 'blockchain projects', 'decentralized networks',
    'blockchain security', 'blockchain transactions', 'decentralized storage',
    'blockchain consensus algorithms', 'blockchain token', 'blockchain ecosystem',
    'decentralized exchange', 'blockchain infrastructure', 'blockchain applications',
    'blockchain innovation', 'blockchain technology trends', 'blockchain research',
    'blockchain education', 'blockchain community', 'blockchain programming',
    'blockchain architecture', 'blockchain governance models', 'blockchain scalability solutions',
    'blockchain regulation', 'blockchain use cases', 'blockchain consulting',
    'blockchain as a service', 'blockchain analytics', 'blockchain interoperability protocols',
    'decentralized application development', 'decentralized application platforms',
    'decentralized finance (DeFi)', 'decentralized autonomous organizations (DAOs)',
    'decentralized identity solutions', 'decentralized data management',
    'decentralized governance models', 'decentralized storage solutions',
    'decentralized consensus mechanisms', 'decentralized tokenomics',
    'decentralized marketplace', 'decentralized protocol', 'decentralized technology',
    'decentralized ecosystem', 'decentralized development', 'decentralized innovation'
],
    packages=find_packages(),
    install_requires=[
        'web3',
        'pymongo',
        'arweave-python-client'
    ],
    entry_points={
        'console_scripts': [
            'x3 = X3Program.shell:main'
        ]
    },
    project_urls={
        'Documentation': 'https://manis-organization-2.gitbook.io/untitled-1',
        'Source': 'https://github.com/nagipragalathan/X3',
    },
)
