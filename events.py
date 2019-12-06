import urllib3,facebook,requests

token= 'EAAGBYgZA1RQcBAMlqCglGOpsMDKxjWlpTGQSq5jZB1NfSUZAW3MXPmVqRRI6zaPDO8jiBMYosrd0aZAQQXMniRp6HCGVSJq2KpSLNlZCaNAr09rWUtxZAaVze794IGZCw6aBL4M8ENrf6Mtbfqtboh6PWWoW3DuO9z9vnbZA3iKc0UDWTvpfc0jtZBpoyLkHhjlDVa6MgAkfGdlTDMZAKELMBTdXb8ltL76ArGYSMkp3BUmwZDZD'
graph = facebook.GraphAPI(access_token=token, version = 2.8)

args = {'fields' : 'birthday,name' }
friends = graph.get_object("me/friends",**args)

#print(friends)

from facebook import GraphAPI
profile = graph.get_all_connections(id='me', connection_name='friends')
profile = graph.get_object('me',**args)

print(profile)