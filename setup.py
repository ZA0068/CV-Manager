from setuptools import setup, find_packages

setup(
    name="MyApp",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PyQt5',
        'reportlab',
        'python-docx',
    ],
    entry_points={
        'console_scripts': [
            'myapp = myapp:main',
        ],
    },
)
