import urllib3
import facebook

token = 'EAAGBYgZA1RQcBAMlqCglGOpsMDKxjWlpTGQSq5jZB1NfSUZAW3MXPmVqRRI6zaPDO8jiBMYosrd0aZAQQXMniRp6HCGVSJq2KpSLNlZCaNAr09rWUtxZAaVze794IGZCw6aBL4M8ENrf6Mtbfqtboh6PWWoW3DuO9z9vnbZA3iKc0UDWTvpfc0jtZBpoyLkHhjlDVa6MgAkfGdlTDMZAKELMBTdXb8ltL76ArGYSMkp3BUmwZDZD'

graph = facebook.GraphAPI(access_token=token, version=5.0)
posts = graph.request('/search?q=Birthday&type=post&limit=10000')

postList = posts['data']

postid = postList[1]['id']

post1 = graph.get_object(id=postid,
    fields='first_name,last_name,birthday')
firstName = post1['first_name']
lastName = post1['last_name']
birthday = post1['birthday']

