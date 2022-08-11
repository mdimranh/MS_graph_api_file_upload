import requests

from ms_graph import *

APP_ID = 'Your-app-id'
SCOPES = ['Files.ReadWrite.All']

access_token = generate_access_token(APP_ID, SCOPES)

headers = {
    'Authorization': 'Bearer ' + access_token['access_token']
}

file_path = r'C:\Users\Md Imran Hossain\Desktop\imran.png'
file_name = os.path.basename(file_path)


with open(file_path, 'rb') as upload:
    media_content = upload.read()

response = requests.put(
    GRAPH_API_ENDPOINT + f'/me/drive/items/root:/{file_name}:/content',
    headers = headers,
    data = media_content
)
print(response.json())
