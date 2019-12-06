import facebook, requests, datetime

token= 'EAAGBYgZA1RQcBAMlqCglGOpsMDKxjWlpTGQSq5jZB1NfSUZAW3MXPmVqRRI6zaPDO8jiBMYosrd0aZAQQXMniRp6HCGVSJq2KpSLNlZCaNAr09rWUtxZAaVze794IGZCw6aBL4M8ENrf6Mtbfqtboh6PWWoW3DuO9z9vnbZA3iKc0UDWTvpfc0jtZBpoyLkHhjlDVa6MgAkfGdlTDMZAKELMBTdXb8ltL76ArGYSMkp3BUmwZDZD'
graph = facebook.GraphAPI(access_token=token, version = 2.8)

user = 'me'

#birthday = a reference to the database?
birthday = '2000-01-01'

def parse_date(post):
    post_date = datetime.datetime.striptime(
        post['created_time'], '%Y-%m-%dT%H:%M:S+0000')
    return post_date.date()

def like_comment(post):
    message = "Appreciated"

    graph.put_like(post['id'])
    graph.put_comment(post['id'], message)

birth = datetime.datetime.strptime(birthday, '%Y-%m-%d')

graph = facebook.GraphAPI(token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'feed')

birthday_posts = [
    post for post in posts['data'] if parse_date(post) == birth.date()]

for idx, post in enumerate(birthday_posts):
    like_comment(post)
    print('Post %d successfully processed.' % idx)