import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PiAleatorio", # Replace with your own username
    version="0.0.1",
    author="Raphael Frajuca",
    author_email="raphaelcfrajuca@gmail.com",
    description="Programa simples feito em Python para obter números aleatórios com o calculo do Pi ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RaphaelCFrajuca/PiAleatorio",
    packages=setuptools.find_packages(),
    python_requires='>=3.3',
)