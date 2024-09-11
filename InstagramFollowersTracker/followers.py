#!pip install instagrapi

from instagrapi import Client
import os

USERNAME = input('username: ')
PASSWORD = input('password: ')
PATH_TO_FOLLOWERS_LIST = input('path to the followers list (just enter if there is not one): ')
# suppose that the same path is to record all the unfollows
print()

cl = Client()
print('Try to connect...')
cl.login(USERNAME, PASSWORD)

user_id = cl.user_info(cl.user_id).pk
print('Hi, your user id is', user_id)

print('Let\'s gather your actual followers...')
followers = cl.user_followers(cl.user_id)
followers_usernames = [followers[el].username for el in followers]

if os.path.exists(PATH_TO_FOLLOWERS_LIST+"followers.txt"):
    
    f = open(PATH_TO_FOLLOWERS_LIST+"followers.txt")
    g = open(PATH_TO_FOLLOWERS_LIST+"unfollowers.txt", "a")
    
    old_followers = f.readlines()
    
    for el in old_followers:
        el = el[:len(el)-1]
        if el != "" and el != "\n" and el not in followers_usernames:
            g.write(el)
            g.write('\n')
            print(el, 'unfollowed you (or maybe they changed username...)')
    f.close()
    g.close()
    
    f = open(PATH_TO_FOLLOWERS_LIST+"followers.txt", "w") # write over the old file with the new list
    
else:
    print("No follower list found. Let's write it down for the first time in the current dir...")
    f = open("followers.txt", "a") # create the file
    
for el in followers_usernames:
    f.write(el)
    f.write('\n')
f.close()
