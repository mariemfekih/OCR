# pattern matcher


## Getting Started

To use this code, follow the steps below to set up the environment:

### Prerequisites

- Python 3.x

### Clone the Repository

```bash
git clone https://github.com/mohamedsaoud7/ocr.git
cd ocr
```
### choose what version you want to choose(main(the fields that are gonna get extracted are in groups based on the selected domain) or secondVersion(here you have fine grained control over the fields that you want to extract)) so for example to use the secondVersion:
```bash
git checkout secondVersion
```
### Install the virtual environment

```bash
python3 -m pip install virtualenv
```
### Create a virtual environment

Create a new virtual environment named .venv/inventoryMatcher

```bash
python3 -m venv .venv/ocr
```

### Activate the virtual environment
On macOS and Linux:

```bash
source .venv/inventoryMatcher/bin/activate
```
On Windows:
```bash
.venv/inventoryMatcher\Scripts\activate
```


### Install dependencies
Once the virtual environment is activated, use the following command to install the required dependencies:

```bash
python3 -m pip install -r requirements.txt
```

### Running the project
```bash
streamlit run ocr.py
```
