#Created by Xiavage

import os
import time
import smtplib, ssl


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


appointmentFound = False
#selenium into the cvs appointment webpage
count = 0
#send email to client
def send_email(name, url):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = ""  # Enter your address
    receiver_email = ''  # Enter receiver address
    password = '' #Enter email password here
    message = """\  
    Subject: COVID 19 Appointment

    An appointment is available at """ + name #message for the email recipient
    message = message + '\nSign up using this link: ' + url
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    appointmentFound = True
    print('appointment found!')

#email if there is an available appointment 
if __name__ == '__main__':
    # driver = webdriver.Chrome(executable_path="chromedriver", options = chrome_options)
    driver = webdriver.Chrome()
    url = 'https://www.cvs.com/immunizations/covid-19-vaccine'
    driver.get(url)
    #click on texas
    while(1):
        try:
            no_thanks_button = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/a[1]')
            no_thanks_button.click()           
            time.sleep(5)
        except NoSuchElementException:
            print("no thanks button not found, continue on")
 
        time.sleep(1)
        texas = driver.find_element_by_xpath('/html/body/content/div/div/div/div[3]/div/div/div[2]/div/div[5]/div/div/div/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/ul/li[11]/div/a/span')
        texas.click()
        time.sleep(1)
    #look for cities based on your location (this is the cities nearby houston and austin texas)
        austin_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[7]/td[1]/span').text
        austin_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[7]/td[2]/span').text
        if(austin_status == 'Available'):
            send_email(austin_name, url)

        # cleveland_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[16]/td[1]/span').text
        # cleveland_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[16]/td[2]/span').text
        # if(cleveland_status == 'Available'):
        #     send_email(cleveland_name, url)

        cypress_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[19]/td[1]/span').text
        cypress_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[19]/td[2]/span').text
        if(cypress_status == 'Available'):
            send_email(cypress_name, url)

        elgin_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[23]/td[1]/span').text
        elgin_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[23]/td[2]/span').text
        if(elgin_status == 'Available'):
            send_email(elgin_name, url)

        georgetown_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[28]/td[1]/span').text
        georgetown_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[28]/td[2]/span').text
        if(georgetown_status == 'Available'):
            send_email(georgetown_name, url)
        
        houston_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[33]/td[1]/span').text
        houston_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[33]/td[2]/span').text
        if(houston_status == 'Available'):
            send_email(houston_name, url)

        huntsville_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[34]/td[1]/span').text
        huntsville_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[34]/td[2]/span').text
        if(huntsville_status == 'Available'):
            send_email(huntsville_name, url)

        # sjc_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[35]/td[1]/span').text
        # sjc_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[35]/td[2]/span').text
        # if(sjc_status == 'Available'):
        #     send_email(sjc_name, url)

        katy_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[36]/td[1]/span').text
        katy_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[36]/td[2]/span').text
        if(katy_status == 'Available'):
            send_email(katy_name, url)

        kingsville_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[37]/td[1]/span').text
        kingsville_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[37]/td[2]/span').text
        if(kingsville_status == 'Available'):
            send_email(kingsville_name, url)

        # lamarque_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[38]/td[1]/span').text
        # lamarque_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[38]/td[2]/span').text
        # if(lamarque_status == 'Available'):
        #     send_email(lamarque_name, url)

        # livingston_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[42]/td[1]/span').text
        # livingston_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[42]/td[2]/span').text
        # if(livingston_status == 'Available'):
        #     send_email(livingston_name, url)

        # pasadena_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[56]/td[1]/span').text
        # pasadena_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[56]/td[2]/span').text
        # if(pasadena_status == 'Available'):
        #     send_email(pasadena_name, url)

        # pearland_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[57]/td[1]/span').text
        # pearland_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[57]/td[2]/span').text
        # if(pearland_status == 'Available'):
        #     send_email(pearland_name, url)

        pflugerville_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[58]/td[1]/span').text
        pflugerville_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[58]/td[2]/span').text
        if(pflugerville_status == 'Available'):
            send_email(pflugerville_name, url)

        # richmond_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[64]/td[1]/span').text
        # richmond_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[64]/td[2]/span').text
        # if(richmond_status == 'Available'):
        #     send_email(richmond_name, url)

        # seabrook_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[73]/td[1]/span').text
        # seabrook_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[73]/td[2]/span').text
        # if(seabrook_status == 'Available'):
        #     send_email(seabrook_name, url)

        # woodlands_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[80]/td[1]/span').text
        # woodlands_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[80]/td[2]/span').text
        # if(woodlands_status == 'Available'):
        #     send_email(woodlands_name, url)

        tomball_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[81]/td[1]/span').text
        tomball_status = driver.find_element_by_xpath('/html/body/div[2]/div/div[20]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[81]/td[2]/span').text
        if(tomball_status == 'Available'):
            send_email(tomball_name, url)

        if not appointmentFound:
            print('No appointments found')
        time.sleep(300) #timeout every 5 minutes for maximum effect
        driver.refresh()
        count = count + 1
        print(count)
        print("Hello World!")

