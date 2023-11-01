#Name: Evan Woods    Date Assigned: Sept. 11, 2023
#
#Course: 2000-       Date Due: Sept. 18, 2023
#
#File name: sept. 16 code assing 1
#
#Program Description: The preogram asks the for the user for their email adaress and phone number. It then showcases the domain, user name, and phone number.

email=input("Enter email:")
phone_number=input("Enter phone number:")
print(email)
username, Domain = (email.split('@'))
print(username)
print(Domain)
print("("+phone_number[:3]+") " +phone_number[3:6]+"-"+phone_number[6:])
