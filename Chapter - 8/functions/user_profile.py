def build_profile(first,last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

data = build_profile('anwar','basha',location = 'chennai',occupation = 'nursing', hobby = 'natural lover')
print(data)
