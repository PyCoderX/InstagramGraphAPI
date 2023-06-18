# Instagram API Wrapper

This project provides a Python wrapper for the Instagram API, allowing you to easily interact with the Instagram platform and retrieve data from your Instagram account.

## Prerequisites

Before using this wrapper, make sure you have the following:

- Python 3.x installed on your system
- Instagram Developer Account: Obtain the necessary credentials from the Instagram Developer portal. You'll need the App ID, App Secret, Facebook Page ID, Instagram Page ID, and Access Token.

## Installation

1. Clone the project repository:

```python
git clone https://github.com/PyCoderX/InstagramGraphAPI.git
```

2. Install the required dependencies:
```python
pip install -r requirements.txt
```

## Usage

1. Import the `InstaApi` class and `insta_credentials` module:

```python
from src import InstaApi 
from src import insta_credentials as credentials
```

2. Create an instance of the InstaApi class using the provided credentials:
```python
insta = InstaApi(credentials)
```
3. Fetch User Info:
```python
user_info = insta.get_user_info()
print(user_info)
```
4. To retrieve the IDs of all the published media items on the Instagram page, use the `get_media_id_list` method.
```python
media_ids = insta.get_media_id_list()
media_insights = insta.get_media_info('your_media_id')
media_report = insta.generate_media_report()
```


