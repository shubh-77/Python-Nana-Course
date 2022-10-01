from user import User
from post import Post

app_user_one = User("shubh@l&t.com", "Shubham P", "pwd1", "Software Engineer")
app_user_one.get_user_info()

app_user_two = User("shubh@ltts.com", "Shubham P", "pwd2", "Delivery Head")
app_user_two.get_user_info()

post_one = Post("on a secret mission today",app_user_two.name)
post_one.get_post_info()