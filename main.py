from src import InstaApi 
from src import insta_credentials as credentials
insta = InstaApi(credentials)
print(insta.generate_detail_report())