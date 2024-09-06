# Brute Force Password Hacker

This Python script demonstrates a simple brute-force password hacker that I wrote in high school that attempts to find a password by generating all possible combinations of characters up to a specified length. It uses the SHA-256 hashing algorithm to compare guessed passwords against a known hash.

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Limitations](#limitations)
- [Disclaimer](#disclaimer)

## Overview

The brute-force password hacker generates all possible combinations of characters (letters and digits) up to a maximum length and checks if the hash of each combination matches the target hashed password. This script is for educational purposes only, to demonstrate how brute-force attacks work in a controlled environment.

## Usage

1. Clone the repository or download the script.
2. Make sure you have Python installed (version 3.x recommended).
3. Run the script using a terminal or command prompt:

    ```bash
    python brute_force_password_hacker.py
    ```

4. Modify the script to change the target password, maximum length, or character set as desired.

## Installation

1. **Install Python**: Ensure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone this repository to your local machine using:

    ```bash
    git clone https://github.com/yourusername/brute-force-password-hacker.git
    ```

3. **Navigate to the Project Directory**:

    ```bash
    cd brute-force-password-hacker
    ```

## How It Works

1. **Hashing Function**: The script includes a function (`hash_password`) that takes a password as input and returns its SHA-256 hash.

2. **Brute-Force Function**: The `brute_force_password` function generates all possible combinations of characters up to the specified maximum length. It compares each generated hash against the target hash.

3. **Character Set**: The default character set includes lowercase letters (`a-z`) and digits (`0-9`). You can modify the character set to include uppercase letters, special characters, or any other characters you want.

## Limitations

- **Performance**: Brute-force attacks are highly inefficient and can take a very long time for longer passwords or larger character sets.
- **Legal and Ethical Concerns**: Brute-force techniques should not be used to attack systems or applications without explicit permission.

## Disclaimer

This script is for educational purposes only. Unauthorized use of this tool to gain access to any system, server, or application is illegal and unethical. The author is not responsible for any misuse or damage caused by this script.
