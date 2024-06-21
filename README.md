### Goldbach's Conjecture Checker

A Python script to test Goldbach's Conjecture within a given range. It uses custom functions to check for prime numbers and even numbers.

## Features

- Tests whether every even number within a specified range can be expressed as the sum of two prime numbers.
- Prints each valid sum for even numbers.
- Reports any exceptions found where the conjecture does not hold.

## Requirements

- Custom `tools` module containing `prime` and `even` functions.

## Usage

1. Run the script:
   ```bash
   python goldbach_checker.py
   ```

2. Input the range when prompted to test Goldbach's Conjecture for even numbers within that range.

## Notes

- Ensure the `tools` module is in the same directory as your script or installed in your Python environment.
- The script only considers even numbers and checks them for Goldbach's Conjecture.

## Disclaimer

This script is for educational purposes. The implementation of the `prime` and `even` functions in the `tools` module should be verified for accuracy and performance as needed.
