#throw catch
#cron job and get data from REST API
import schedule
import time
import requests
response = requests.get("https://randomuser.me/api/")
data=response.json()

def get_user_interactions():
    print("getting user interactions...")
    #get user interaction data dn process here

def reading_hashtags():
     print("reading hashtags...")
     hash=data['results']
     print(hash)
     #?trending hashtag problem
     #add new hashtahs foor hashtag metrix
     #also hashtag storing and processing

     schedule.every(5).seconds.do(get_user_interactions)
     schedule.every().day.at("23:59").do(reading_hashtags)

     while True:
         schedule.run_pending()
         time.sleep(1)
########################################################end ###############################
# store hashtag list from API
# list=['category1','category2','category3','category4']
#code for indiviodual user

# ??#each media id rows, each variable columns #########
# ??#author and hashtag array enougj



# userA_hashtags=[0,0,0,0]
# userA_publishers=[0,0,0,0,0]
#
# # last watch vid category ['']==
#
# watch_time=int()
# like=bool()
# dislike=bool()
# comment=bool()
# #comment yes no, and comment content, also consider user is a frequent commenter or not
# share=bool()
# catch=bool()
# reject=bool()
# throw=bool()
#with thrown from wallet without expiration

#
# # if list[0] == "fashion":
#
#     if watch_time=>80:
#         userA_hashtags[0]=userA_hashtags[0]+50
#     elif watch_time=>50:
#         userA_hashtags[0]=userA_hashtags[0]+30
#     else:
# if like==True:
# userA_hashtags[0]= userA_hashtags[0]+1

#sync time 10 mins
#new hashtags new array, or just



