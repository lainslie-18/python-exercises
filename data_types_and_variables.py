''' You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay? ''' 

movie_price_per_day = 3.0
little_mermaid_days_rented = 3
brother_bear_days_rented = 5
hercules_days_rented = 1

total_price = (little_mermaid_days_rented + brother_bear_days_rented + hercules_days_rented) * movie_price_per_day

''' Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon. ''' 

google_pay_per_hr = 400
amazon_pay_per_hr = 380
facebook_pay_per_hr = 350

google_hrs_worked = 6
amazon_hrs_worked = 4
facebook_hrs_worked = 10

total_payment = (google_pay_per_hr * google_hrs_worked) + (amazon_pay_per_hr * amazon_hrs_worked) + (facebook_pay_per_hr * facebook_hrs_worked)

''' A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.''' 

class_is_full = False
schedule_conflict = False

can_enroll_to_class = (not class_is_full) and (not schedule_conflict)

''' A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.''' 

offer_not_expired = True
bought_more_than_2_items = True
premium_member = False

product_offer_can_be_applied = offer_not_expired and (bought_more_than_2_items or premium_member)

# username, password exercise

username = 'codeup'
password = 'notastrongpassword'

password_at_least_5_char = len(password) >= 5
username_no_more_than_20_char = len(username) <= 20
password_diff_than_username = password != username
begins_or_ends_with_whitespace = username != username.strip() or password != password.strip()

valid_username_password = password_at_least_5_char and username_no_more_than_20_char and password_diff_than_username and not begins_or_ends_with_whitespace


