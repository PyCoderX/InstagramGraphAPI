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
```
5. You can fetch insights for a specific media item by providing its ID to the `get_media_info` method:
```python
media_insights = insta.get_media_info('your_media_id')
```
6. To generate a report with insights for all the published media items on the Instagram page, use the `generate_media_report` method:
```python
media_report = insta.generate_media_report()
```
The `generate_media_report` method returns a Pandas DataFrame containing the insights for all the media items. The DataFrame includes columns such as timestamp, comments count, like count, media type, engagement, impressions, and reach. Feel free to explore other methods provided by the InstaAPI library to suit your specific requirements and use cases.

## Contribution
Contributions to the InstaAPI library are welcome! If you encounter any issues, have feature requests, or would like to contribute code improvements, please submit an issue or a pull request on the GitHub repository.

## License
The InstaAPI library is open-source and released under the MIT License. See the LICENSE file for more details.

