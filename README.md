# Instagram API Wrapper

This project provides a Python wrapper for the Instagram API, allowing you to easily interact with the Instagram platform and retrieve data from your Instagram account.

## Prerequisites

Before using this wrapper, make sure you have the following:

- Python 3.x installed on your system
- Instagram Developer Account: Obtain the necessary credentials from the Instagram Developer portal. You'll need the App ID, App Secret, Facebook Page ID, Instagram Page ID, and Access Token.

## Installation

1. Clone the project repository:

```python
git clone https://github.com/PyCoderX/InstagramGraphAPI
```

2. Install the required dependencies:
```python
pip install -r requirements.txt
```

## Usage

1. Import the `InstaApi` class and `insta_credentials` module:

```python
from lib.insta_api import InstaApi
from credentials.insta_credentials import credentials
```

2. Create an instance of the InstaApi class using the provided credentials:
```python
insta = InstaApi(credentials)
```

