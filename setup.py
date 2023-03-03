import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='lunastro',
    version='0.0.13',
    author='Siddhu Pendyala',
    author_email='elcientifico.pendyala@hotmail.com',
    description='python package for lunar and solar information',
    long_description = long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/PyndyalaCoder/lunastro',
    project_urls = {
        "Bug Tracker": "https://github.com/PyndyalaCoder/lunastro/issues"
    },
    license='MIT',
    packages=['lunastro'],
    install_requires=['requests', 'pytz'],
)
