#  Metacode

## Overview

Metacode is a blockchain-based system designed for secure data sharing. It utilizes cryptographic techniques, including Shamir Secret Sharing for request transmission and Pro-ORAM for data storage. The system is engineered to protect metadata and ensure robustness against up to n−1 malicious servers, making it an ideal choice for environments requiring high security and data integrity.

## Features

- **Blockchain-Based Secure Sharing**: Leverages blockchain technology for secure and transparent data transactions.
- **Shamir Secret Sharing**: Implements Shamir Secret Sharing for secure request transmission, enhancing privacy and security.
- **Pro-ORAM for Data Storage**: Utilizes Pro-ORAM (Oblivious RAM) for efficient and secure data storage, protecting against unauthorized access and data breaches.
- **Robust Against Malicious Servers**: Designed to be resilient against a high number of malicious servers, ensuring data integrity and reliability.

## Requirements

- Python 3.x

## Installation

Download and extract the Metacode package to your desired directory.

## Usage

The system consists of various Python modules, each serving a specific function in the Metacode framework:

- `main.py`: The main script to run the Metacode system.
- `config.py`: Contains configuration settings for the system.
- `crypto.py`: Implements cryptographic functions and utilities.
- `init.py`: Initializes the system and sets up necessary parameters.
- `nodes.py`: Defines the node structure and interactions within the blockchain.
- `proxy.py`: Manages proxy functionalities for data requests and responses.
- `shuffle.py`: Handles data shuffling to enhance security.
- `target.py`: Target module for data storage and retrieval.
- `test.py`: Contains tests for validating the functionality of the system.

To start the Metacode system, run the `main.py` script:

```python
python main.py
```

## Testing

Run the `test.py` script to perform unit tests and ensure the system is functioning correctly:

```python
python test.py
```
