from boxsdk import OAuth2, Client
CLIENT_ID='x2cg84xsrrjr3p694d0jgssk5fx1ubbn'
CLIENT_SECRET = 'tR27oOJ1mdZkvFUM2TW6EOcM6jjqFBXB'
ACESS_TOKEN = 'xDRl9ZM7ICLW9KEn27rwqhg1o2fx1Vh2'
auth = OAuth2(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    access_token=ACESS_TOKEN
)
client = Client(auth)

user = client.user().get()
print(f'The current user ID is {user.id}')