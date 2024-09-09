# Simple API fuzzer

this is a simple API fuzzer written in Python using the requests and sys libraries.

## Features

- Send requests to the API endpoint.
- Built with common and standard python libraries for easy setup and usage.

## Getting Started

### Prerequisites

1. Python 3.x is installed on your system.
2. Install the 'requests' and 'sys' libraries in your system if you don't have them already
   - pip install requests (for windows systems)
   - apt-get install requests (for debian based systems)

### Linux Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/rlcosta177/simple_api_fuzzer.git
   ```
2. `cd` into the directory:
   ```bash
   cd simple_api_fuzzer
   ```
3. Run the program with the following syntax:
   ```bash
   cat small.txt | python3 fuzzer.py
   ```
  - Change `https://example.com/api/` into your target API

4. The fuzzer will start sending the requests to the specified API and display the responses/errors.

---

### Windows Installation

1. Clone the repository to your local machine using Powershell:

   ```bash
   git clone https://github.com/rlcosta177/simple_api_fuzzer.git
   ```
2. `cd` into the directory:
   ```bash
   cd .\simple_api_fuzzer
   ```

3. Run the program with the following syntax:
   ```bash
   Get-Content small.txt | python3 fuzzer.py
   ```

4. The fuzzer will start sending the requests to the specified API and display the responses/errors.
