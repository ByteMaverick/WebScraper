from setuptools import setup, find_packages

setup(
    name='image_downloader',
    version='1.0.0',
    author='Your Name',
    author_email='your_email@example.com',
    description='A library for downloading images from the web.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/image_downloader',  # Replace with your repo link
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
