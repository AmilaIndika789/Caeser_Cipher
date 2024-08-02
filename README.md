![Build](https://github.com/AmilaIndika789/Caeser_Cipher/actions/workflows/build_and_test.yml/badge.svg?branch=main&event=push) [![codecov](https://codecov.io/gh/AmilaIndika789/Caeser_Cipher/graph/badge.svg?token=U2X98VLBZT)](https://codecov.io/gh/AmilaIndika789/Caeser_Cipher) 

# Caeser Cipher 

A simple command line [Caeser Cipher](https://en.wikipedia.org/wiki/Caesar_cipher) implemented using Python.

## Instructions

1. Install required python dependencies

    ~~~zsh
    pip install -r requirements.txt
    ~~~

2. Run the following command from the root directory

    ~~~zsh
    python -m src.pkg.caeser_cipher src/pkg/caeser_cipher.py
    ~~~

3. [Optional] Run unit tests with coverage and pytest

    ~~~bash
    coverage run --source src.pkg --module pytest --verbose tests
    ~~~

## Example Usage

### Encoding

![Example of encoding using caeser cipher](images/encoding.png)

### Decoding

![Example of decoding using caeser cipher](images/decoding.png)
