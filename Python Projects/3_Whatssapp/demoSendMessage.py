#Whatsapp Message send
# pip install pywhatkit
# pip install keyboard

import pywhatkit as kit
import datetime
import time
import keyboard

# Country code for India (change as needed)
country = "+91"

# Get the phone number from the user
while True:
    num = str(input("Enter Number : "))
    # Validate the phone number (should be 10 digits)
    if len(num) == 10 and num.isdigit():
        break
    else:
        print("Invalid phone number. Please enter a 10-digit number.")

# Get the message from the user
message = str(input("Enter Message : "))

# Get the current date and time
now = datetime.datetime.now()
hour = now.hour
minute = now.minute

# Wait for 10 seconds to ensure WhatsApp Web interface is loaded
print("Waiting for 10 seconds to load WhatsApp Web interface...")
time.sleep(10)

# Send the WhatsApp message
print("Sending WhatsApp message...")
try:
    kit.sendwhatmsg(country + num, message, hour, minute + 1) # increase to +2 if call time error
    print("Message sent successfully!")
except:
    print("Error sending WhatsApp message. Please try again later.")

# Close the tab and browser
print("Closing tab and browser...")
time.sleep(5)  # wait for 5 seconds
keyboard.press_and_release('ctrl+w')  # close the current tab




# time.sleep(1)  # wait for 1 second
# keyboard.press_and_release('alt+f4')  # close the browser
# print("Tab and browser closed!")




# kit.sendwhatmsg("+91xxxxxxxxx", "Hello", 12, 30,
#                 auto_close=True, wait_time=10, tab_close=True, close_time=10,
#                 close_tab=True, close_browser=True, close_app=True, close_pc=True)
#kit.sendwhatmsg('+91XXXXXXXXXX',"This is Message",17,30)



