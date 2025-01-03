# #pip install mechanize
# #pip install bs4 -> BeautifulSoup
# #using a from page from findandtrace website to scrap data

# import mechanize as mech
# from bs4 import BeautifulSoup 

# url = "https://www.findandtrace.com/trace-mobile-number-location"
# brow = mech.Browser()  # you can even use selenium
# brow.set_handle_robots(False)  #false because some websites dosent allow us to scrap data
# brow.open(url)      
# brow.select_form(name='trace') #the name of form on website is trace
# brow['mobilenumber'] = str(input("Enter the mobile number to get Info: ")) #the name of input field on website is mobilenumber
# result = brow.submit() #submit the form and record the response as result

# soup =  BeautifulSoup (result.read(),'html.parser')
# table_extr = soup.find_all('table',id='customers')  #table id is cutomers in the website
# print(len(table_extr)) #it will give numbers of tables in website



#failed => showing forbidden error
