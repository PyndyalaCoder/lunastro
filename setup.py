import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pynocturnal',
    version='0.0.1',
    author='Siddhu Pendyala',
    author_email='elcientifico.pendyala@hotmail.com',
    description='python package for lunar information',
    long_description = long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/PyndyalaCoder/pynocturnal',
    project_urls = {
        "Bug Tracker": "https://github.com/PyndyalaCoder/pynocturnal/issues"
    },
    license='MIT',
    packages=['lunarinfo'],
    install_requires=['requests'],
)
