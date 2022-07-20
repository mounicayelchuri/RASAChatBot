from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def allocate_category(x):
    if x < 300:
     return 'low'
    elif x > 700:
       return 'high'
    else:
       return 'medium'

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
ZomatoData=ZomatoData.sort_values(by=['Aggregate rating'],ascending=False)
ZomatoData['Average cost category'] = ZomatoData['Average Cost for two'].apply(lambda x : allocate_category(x))
WeOperate = ZomatoData.City.unique()

def RestaurantSearch(City,Cuisine,Budget):
	TEMP = ZomatoData[ZomatoData['Average cost category'] == Budget][(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

def IsValidLocation(Location):
    if Location.lower() in map(lambda x:x.lower(),WeOperate):
        temp_df=ZomatoData[ZomatoData['City'].apply(lambda x: Location.lower() in x.lower())]
        if len(temp_df)>=5:
            return True
        else:
            return False
    else:
        return False


def sendmail(MailID,response):
    mail_content = 'Please find the top restaurants from your recent search'
    mail_content= mail_content+'\n\n\n'+response
    sender_address = 'dummytosendmail@gmail.com'
    sender_pass = 'Test@1234'
    receiver_address = MailID
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Here is your restaurant list..Bon appetit!'   #The subject line
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()		


class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('budget')
		
		is_restaurant_exist = False
		results = RestaurantSearch(City=loc,Cuisine=cuisine,Budget=price)
		response=""
		if results.shape[0] == 0:
			response= "no results"
		else:
			is_restaurant_exist = True
			for restaurant in results.iloc[:5].iterrows():
				restaurant = restaurant[1]
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']}  has been rated {restaurant['Aggregate rating']} \n"
				
		dispatcher.utter_message("-----"+response)
		return [SlotSet('is_restaurant_exist',is_restaurant_exist)]

class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price= tracker.get_slot('budget')
		results = RestaurantSearch(City=loc,Cuisine=cuisine,Budget=price)
		MailID = tracker.get_slot('email')
		response=""
		if results.shape[0] == 0:
			response= "no results"
		else:
			for restaurant in results.iloc[:10].iterrows():
				restaurant = restaurant[1]
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']}  has been rated {restaurant['Aggregate rating']} \n\n"
		sendmail(MailID,response)
		print("in mail send")

class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):
		location = tracker.get_slot('location')
		res = IsValidLocation(location)
		return [SlotSet('is_valid_location',res)]

