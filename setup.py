from setuptools import setup, find_packages


setup(
    name="ClassPy",  # Nome do pacote
    version="1.0.0",    # Versão inicial
    author="Felipe Catao",
    author_email="cataofelipe@formigatech.com",
    description="O Classpy é um pacote para aprimorar a orientação a objetos em projetos Python, oferecendo maior controle de fluxo e performance. Com suporte a métodos privados, protegidos e interfaces, ele expande as capacidades nativas da linguagem, tornando o design de software mais robusto e modular.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/FelipeKatao/ClassPy",
    packages=find_packages(),
    install_requires=[
        "numpy",  # Dependências necessárias
        "pandas"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

