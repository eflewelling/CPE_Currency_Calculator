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

2. **Create a virtual environment (optional but recommended)**:
 ```sh
python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```

3. **Install the required libraries**:
```sh
pip install requests packaging
```

## Usage
1. Run the script:
```sh
python CPEcurrencycalculator.py
```

2. Enter the CPE string when prompted:
```sh
cpe:2.3:a:adobe:acrobat_reader_dc:2019.010.20098:*:*:*:*:*:*:*
```

3. View the result: The script will output whether the provided CPE string is up to date or outdated.

Example
```sh
$ python CPEcurrencycalculator.py
Enter the CPE to check: cpe:2.3:a:adobe:acrobat_reader_dc:2019.010.20098:*:*:*:*:*:*:*
cpe:2.3:a:adobe:acrobat_reader_dc:2019.010.20098:*:*:*:*:*:*:* is outdated. Latest version is 2021.001.20145.
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
