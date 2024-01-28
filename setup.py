from setuptools import setup, find_packages

setup(
    name='lyzr-experimental-automata',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'openai',
        'asyncio', # If you're using any non-standard library packages
    ],
    author='Siva Surendira',
    author_email='siva@lyzr.ai',
    description='A prompt based agent workflow that integrates with other Lyzr agents',
    long_description=open('README.md').read(),
    long_description_content_type='check Readme file',
    url='https://github.com/lyzrcore/lyzr-experimental-automata',
    license='MIT',
)
