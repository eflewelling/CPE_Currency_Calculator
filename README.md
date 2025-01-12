# CPE Currency Calculator

The CPE Currency Calculator is a Python script that checks if a given Common Platform Enumeration (CPE) string is up to date by comparing it with the latest versions available in the NIST National Vulnerability Database (NVD).

## Features

- Fetches the latest versions of software products from the NVD API.
- Compares the provided CPE string with the latest versions.
- Outputs whether the CPE string is up to date or outdated.

## Requirements

- Python 3.6 or higher
- `requests` library
- `packaging` library

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/eflewelling/CPE_Currency_Calculator.git
   cd CPE_Currency_Calculator
