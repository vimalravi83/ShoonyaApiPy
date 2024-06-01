from setuptools import setup, find_packages

setup(
    name='ShoonyaApiPy',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
        # e.g., 'numpy', 'requests',
    ],
    entry_points={
        'console_scripts': [
            # Define scripts that should be available as command-line executables
            # 'command-name=package.module:function',
        ],
    },
    author='Ravi',  # Your name or the author's name
    author_email='vimalravi@hotmail.com',  # Your email or the author's email
    description='Shoonya API trading',
    url='https://github.com/vimalravi83/ShoonyaApiPy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python version requirements
)
