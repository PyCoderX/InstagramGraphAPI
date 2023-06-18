import requests
import pandas as pd
from datetime import date

class InstaApi:
    def __init__(self, credentials):
        """
        Initializes the InstaApi class and loads the credentials from the insta_cred.py file.
        """
       
        self.app_id = credentials['app_id']
        self.app_secret = credentials['app_secret']
        self.facebook_page_id = credentials['facebook_page_id']
        self.instagram_page_id = credentials['instagram_page_id']
        self.access_token = credentials['access_token']
        self.url = 'https://graph.facebook.com/v16.0/{}'

    # Rest of the class code...

    
    def _post_request(self, url, params):
        """
        Makes a POST request to the specified URL with the given parameters.

        Args:
            url (str): The URL to make the request to.
            params (dict): The request parameters.

        Returns:
            dict: The response JSON data.
        """
        response = requests.post(url, params=params)
        data = response.json()
        return data
    
    def _get_request(self, url, params):
        """
        Makes a GET request to the specified URL with the given parameters.

        Args:
            url (str): The URL to make the request to.
            params (dict): The request parameters.

        Returns:
            dict: The response JSON data.
        """
        response = requests.get(url, params=params)
        data = response.json()
        return data

    def get_long_access_token(self, short_access_token):
        """
        Converts a short-lived access token to a long-lived access token.

        Args:
            short_access_token (str): The short-lived access token.

        Raises:
            FileNotFoundError: If the credential file is not found or cannot be read.
        """
        params = {
            'grant_type': 'fb_exchange_token',
            'client_id': self.app_id,
            'client_secret': self.app_secret,
            'fb_exchange_token': short_access_token
        }
        data = self._post_request(self.url.format('oauth/access_token'), params=params)
        self.access_token = data['access_token']
    
    def get_media_id_list(self):
        """
        Retrieves a list of all media IDs.

        Returns:
            list: The list of media IDs.
        """
        url = self.url.format(f'{self.instagram_page_id}/media')
        params = {
            'access_token': self.access_token,
        }
        data = self._get_request(url, params=params)
        id_list = [elem['id'] for elem in data['data']]
        return id_list
    
    def get_media_info(self, media_id):
        """
        Retrieves information about a specific media.

        Args:
            media_id (str): The media ID.

        Returns:
            dict: The media information.
        """
        url = self.url.format(media_id)
        params = {
            'fields': 'timestamp,comments_count,like_count,media_type',
            'access_token': self.access_token,
        }
        media_info = self._get_request(url, params=params)

        url = self.url.format(f"{media_id}/insights")
        params = {
            'metric': 'engagement,impressions,reach',
            'access_token': self.access_token,
        }
        data = self._get_request(url, params=params)
        for element in data['data']:
            media_info[element['name']] = element['values'][0]['value']
        return media_info

    def generate_media_report(self):
        """
        Generates a media report based on the available media.

        Returns:
            pandas.DataFrame: The media report as a DataFrame.
        """
        id_list = self.get_media_id_list()
        info_list = [self.get_media_info(media_id) for media_id in id_list]
        dataframe = pd.DataFrame.from_records(info_list)
        dataframe['timestamp'] = pd.to_datetime(dataframe['timestamp'], format='%Y-%m-%d').dt.date
        return dataframe
    
    def get_user_info(self):
        """
        Retrieves information about the Instagram user.

        Returns:
            dict: The user information.
        """
        url = self.url.format(self.instagram_page_id)
        params = {
            'fields': 'followers_count,follows_count,media_count',
            'access_token': self.access_token,
        }
        data = self._get_request(url, params=params)
        data['date'] = date.today().strftime("%Y-%m-%d")
        return data
    
    def post_image(self, image_url, caption=''):
        """
        Posts an image to the Instagram page.

        Args:
            image_url (str): The URL of the image to post.
            caption (str, optional): The caption for the image. Defaults to ''.

        Returns:
            dict: The response data.
        """
        url = self.url.format(f"{self.instagram_page_id}/media")
        params = {
            'image_url': image_url,
            'caption': caption,
            'access_token': self.access_token,
        }
        data = self._post_request(url, params=params)
        return data
    
    def generate_detail_report(self):
        """
        Generates a detailed report by retrieving user info and generating a media report.
        Rearranges the information dictionary based on the specified key order.
        Returns the reordered dictionary representing the detailed report.
        """
        user_info = self.get_user_info()  # Retrieve user info
        dataframe = self.generate_media_report()  # Generate media report
        info_dict = dataframe.sum().to_dict()  # Convert the dataframe to a dictionary
        del info_dict['media_type'], info_dict['id']  # Remove unnecessary keys

        for key in ['date','followers_count', 'follows_count', 'media_count']:
            info_dict[key] = user_info[key]
            
        key_order = ['date', 'followers_count', 'follows_count', 'media_count', 'impressions', 'reach', 'engagement', 'like_count', 'comments_count']
        reordered_dict = {key: info_dict[key] for key in key_order if key in info_dict}
        return reordered_dict

