## complete path 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": true}
    - utter_ask_email
* email_send{"email": "abc12332@domain.com"}
    - slot{"email": "abc12332@domain.com"}
    - action_send_mail
    - utter_mail_sent_confirm

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"is_valid_location": false}
    - utter_we_dont_operate
    - utter_goodbye


## interactive 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": true}
    - utter_ask_email
* email_send{"email": "dfsdf342@domain.com"}
    - slot{"email": "dfsdf342@domain.com"}
    - action_send_mail
    - utter_mail_sent_confirm

## interactive 2
* greet
    - utter_greet
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye

## interactive 3
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_check_location
    - slot{"is_valid_location": false}
    - utter_we_dont_operate
    - utter_ask_location_again
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": true}
    - utter_ask_email
* email_send{"email": "xyz@dsd.edu"}
    - slot{"email": "xyz@dsd.edu"}
    - action_send_mail
    - utter_mail_sent_confirm

## interactive 4
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email
* email_send{"email": "jddk.2313sdfe@fs.co.in"}
    - slot{"email": "jddk.2313sdfe@fs.co.in"}
    - action_send_mail
    - utter_mail_sent_confirm

## interactive 5
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "punjab"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "punjab"}
    - action_check_location
    - slot{"is_valid_location": false}
    - utter_we_dont_operate
    - utter_ask_location_again
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_check_location
    - slot{"is_valid_location": false}
    - utter_we_dont_operate
    - utter_goodbye

## interactive 6
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "punjab"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "punjab"}
    - action_check_location
    - slot{"is_valid_location": false}
    - utter_we_dont_operate
    - utter_ask_location_again
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye

## interactive 7
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "New Delhi"}
    - slot{"cuisine": "american"}
    - slot{"location": "New Delhi"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": true}
    - utter_ask_email
* email_send{"email": "dsdfsdf@dfsf.in"}
    - slot{"email": "dsdfsdf@dfsf.in"}
    - action_send_mail
    - utter_mail_sent_confirm

## interactive 8
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "gujarat"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "gujarat"}
    - action_check_location
    - slot{"is_valid_location": false}
    - utter_we_dont_operate
    - utter_ask_location_again
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye

## interactive 9
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "allahabad"}
    - slot{"cuisine": "american"}
    - slot{"location": "allahabad"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": true}
    - utter_ask_email
* email_send{"email": "rete343.43df@yopmail.com"}
    - slot{"email": "rete343.43df@yopmail.com"}
    - action_send_mail
    - utter_mail_sent_confirm

## interactive 10
* greet
    - utter_greet
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye

## interactive 11
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": true}
    - utter_ask_email
* email_send{"email": "ksds23_324@wewewe.in"}
    - slot{"email": "ksds23_324@wewewe.in"}
    - action_send_mail
    - utter_mail_sent_confirm

## interactive 12
* greet
    - utter_greet
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": false}
    - utter_goodbye

## interactive 13
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "budget": "low", "location": "chandigarh"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "chandigarh"}
    - slot{"budget": "low"}
    - action_check_location
    - slot{"is_valid_location": true}
    - action_search_restaurants
    - slot{"is_restaurant_exist": false}
    - utter_goodbye

## interactive 14
* greet
    - utter_greet
* restaurant_search{"location": "bhopal", "budget": "medium"}
    - slot{"location": "bhopal"}
    - slot{"budget": "medium"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": true}
    - utter_ask_email
* email_send{"email": "gargshivani3093@gmail.com"}
    - slot{"email": "gargshivani3093@gmail.com"}
    - action_send_mail
    - utter_mail_sent_confirm

## interactive 15
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "budget": "high", "location": "mohali"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "mohali"}
    - slot{"budget": "high"}
    - action_check_location
    - slot{"is_valid_location": true}
    - action_search_restaurants
    - slot{"is_restaurant_exist": false}
    - utter_goodbye

## interactive 16
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "mangalore"}
    - slot{"location": "mangalore"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": false}
    - utter_goodbye

## interactive 17
* greet
    - utter_greet
* restaurant_search{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": true}
    - utter_ask_email
* email_send{"email": "gargshivani3093@gmail.com"}
    - slot{"email": "gargshivani3093@gmail.com"}
    - action_send_mail
    - utter_mail_sent_confirm

## interactive 18
* greet
    - utter_greet
* restaurant_search{"location": "vvfeieqewl"}
    - slot{"location": "vvfeieqewl"}
    - action_check_location
    - slot{"is_valid_location": false}
    - utter_we_dont_operate
    - utter_ask_location_again
* restaurant_search{"cuisine": "mexican", "location": "New Delhi"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "New Delhi"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": true}
    - utter_ask_email
* email_send{"email": "ddsfsfee@yopmail.com"}
    - slot{"email": "ddsfsfee@yopmail.com"}
    - action_send_mail
    - utter_mail_sent_confirm

* greet
    - utter_greet
* restaurant_search{"location": "Bangalore", "budget": "low"}
    - slot{"location": "Bangalore"}
    - slot{"budget": "low"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": false}
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Puducherry"}
    - slot{"location": "Puducherry"}
    - action_check_location
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"is_restaurant_exist": true}
    - utter_ask_email
* email_send
    - utter_ask_email
* email_send{"email": "gargshivani3093@gmail.com"}
    - slot{"email": "gargshivani3093@gmail.com"}
    - action_send_mail
    - utter_mail_sent_confirm
