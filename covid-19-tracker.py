#Eugene Lee
#2020-06-15
#COVID-19 Information Provider and Tracker
#This program will provide numbers of current infections, deaths, e.t.c, a small quiz to determine if you may have COVID-19 and a list of latest news articles from CTV about COVID-19

#POST PROJECT NOTES - Although I did try to add a future projections section, I could not, at this time, figure out the equation or find out how to create my own model on the future of COVID-19. I looked at the SEIR epidemic model but unfortunately I could not make sense of the model nor have success attempting to create my own model. Also I found that scraping from Google itself was quite difficult and I was unsuccessful as the names of the div classes were different from what I inspected as Google has customized the news based on my location and thus, provided a different result from what my link actually showed. Overall I'd say that the project met/exceeded my expectations and was what I had envisioned it to be but I was unfortunately not able to add the extra features I may have liked, though the project has inspired me to further explore data science with computer science. To conclude, although I did have a few moments of going insane, I had an overall enjoyable and fulfilled experience with the project


import sys
import replit
import colorama
import time
from colorama import Fore, Back, Style
import requests, webbrowser
from bs4 import BeautifulSoup

def quitProgram():  #the code for when he user quits the program
  replit.clear()
  print("Bye Have A Good Time!")
  time.sleep(3)
  print(Fore.GREEN + "( ͡° ͜ʖ ͡°)")
  time.sleep(3)
  replit.clear()
  sys.exit("you didn't see anything...")

def userWrongAnswer():  #when the user enters an incorrect answer
  replit.clear()
  colorama.init()
  print(Fore.RED + "PLEASE ENTER A VALID RESPONSE\nYOU MAY RETRY IN:")
  for i in range (3, 0, -1):  #this is a 3 second cooldown for an incorrect answer
    if i == 1:
      print("\t--- {}".format(i)+ Style.RESET_ALL)
      time.sleep(1)
    else:
      print("\t--- {}".format(i))
      time.sleep(1)
  replit.clear()  #clears the text from the warning and the 3 second cooldown

def FAQModule(txt): #a module for each section of the FAQ
  replit.clear()
  print(txt)  #prints the text needed to answer a FAQ
  time.sleep(5)
  returnToMenu = input("\nPlease hit enter to return to the FAQ list\n\t--> ")  #this portion allows for the user to return to the orginal FAQ list 
  FAQList = True
  showMenu = True
  replit.clear()

def webScrapperNum(link, tagOne, tagTwo, tagThree, group):  #webscrapper module
  url = link  
  page = requests.get(url)  #takes url of website and gets the html from it
  soup = BeautifulSoup(page.content, 'html.parser') #for parsing the html on our page
  results = soup.find_all(tagOne,{tagTwo:tagThree}) #finding the needed data
  finalOutput=[]  #list to hold parsed data
  for i in results:
    tempNum=''
    for j in i.text:  #goes through the data
      try:
        float(j)  #since this is for numbers, i filter out only the numbers required
        tempNum+=j
      except:
        {} 
    finalOutput.append(tempNum) #add the numbers to the list
  return(finalOutput[group])  #return the needed data based on the 5 requirements the user put into the function

def latestNews(): #webscrapping links for latest news from a website
  replit.clear()
  print("Here are a list of recent CTV articles about COVID-19:\n")
  time.sleep(1)
  url = 'https://www.ctvnews.ca/health/coronavirus/'
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')   #same logic here to the webScrapperNum()
  results = soup.find_all('a')  #this time i look for a tags
  #'div',{'class':'columnsplitter container threeColumns none'}
  listOfLinks={}  #make an empty dictionary for the links
  linkCount=0 #link counter
  for links in results: #goes through the results
    href=links.get('href')  #finds ths links
    if 'coronavirus' in href or 'covid-19' in href:   #if the links contain keywords coronavirus or covid-19 i filter it into the dictionary
      if href not in listOfLinks.values():
        linkCount+=1
        listOfLinks[linkCount]=href
  for i in range(1,len(listOfLinks)+1): #for outputting the links to the console
    print("Link {}: ".format(i)+Fore.BLUE+"{}".format(listOfLinks.get(i)+Style.RESET_ALL))
  progressToMenu=input("\n\tPlease hit enter to return to the menu:\n\t\t-->")  
  replit.clear()

def trackerSectionModule(message,data): #for printing the data and message for the numbers for the tracker
  print(Fore.YELLOW+message.format(data)+Style.RESET_ALL)
  progressToMenu=input("\n\tPlease hit enter to return to the menu:\n\t\t-->")
  replit.clear()

def covidSymptomChecker():  #for unofficially checking the symptoms the user has
  replit.clear()
  symptomScore=0  #initial symptom score
  messagesForSymptoms={'noSymptoms':"You seem to have no symptoms, but remember to continue to be careful!",'noSymptomsButMaybe':"You don't have any symptoms but you may have been in contact with the virus. It may be best to self quarentine and take precautions.",'someSymptoms':"You do have some symptoms but it may not be COVID-19. Your case is unclear so it may be best talking to a medical proffesional.",'exposedToVirus':"You have some symptoms of the virus and may have been to exposed to the virus. You should want to get tested and/or talk to a medical proffesional but be careful for yourelf and others!",'seekMedicalAttention':"You seem to have an emergency warning sign for COVID-19. Seek medical attention immeadiately."} #dictionary with messages based on certain scores
  userAnswer=True
  validAnswers=['yes no','abcdefghijklmnop'] #valid answers

  while userAnswer: #in case the user enters an invalid answer so the code doesnt break
    answerValidChecker=True
    userExposureQuestion=input("DISCLAIMER: THIS IS NOT AN OFFICIAL DIAGNOSIS!\nHave you been in contact with or possibly exposed to someone with COVID-19? Please enter yes or no:\n\n\t--> ")
    replit.clear()
    userSymptoms=input("Please select all symptoms you have by entering the letters corresponding with the symptom without any seperation, if none please hit enter without any input:\n\nA) Fever or chills\nB) Cough\nC) Shortness of breath or difficulty breathing\nD) Fatigue\nE) Muscle or body aches\nF) Headache\nG) New loss of taste or smell\nH) Sore throat\nI) Congestion or runny nose\nJ) Nausea or vomiting\nK) Diarrhea\nL) Trouble breathing\nM) Persistent pain or pressure in the chest\nN) New confusion\nO) Inability to wake or stay awake\nP) Bluish lips or face\n\n\t--> ")
    replit.clear()
    for i in userSymptoms.strip().lower():  #checks for an invalid input from the user
      if i not in validAnswers[1]:
        answerValidChecker=False
        userWrongAnswer()
        break
      if userExposureQuestion not in validAnswers[0]:
        answerValidChecker=False
        userWrongAnswer()
        break
    if answerValidChecker:
      userAnswer=False
  emergencySymptomsList="lmnop" #list of choices that are emergency symptoms
  commonSymptomsList='abcdefghijk'  #list of common symptoms choices
  print("Here is your unofficial diagnosis for COVID-19...\n\t")
  for symptoms in userSymptoms.lower().strip():
    if symptoms in emergencySymptomsList: #if the user has an emergency symptom the loop breaks 
      symptomScore=2020 
      break
    if symptoms in commonSymptomsList:
      symptomScore += 5   #adds 5 points per common symptom

  #based on the number of points and the exposure question, the program gives a different responce from the dictiionary
  if symptomScore < 5 and userExposureQuestion.lower() == 'no':
    print(Fore.YELLOW+messagesForSymptoms.get('noSymptoms')+Style.RESET_ALL)
  elif symptomScore < 5 and userExposureQuestion.lower() == 'yes':
    print(Fore.YELLOW+messagesForSymptoms.get('noSymptomsButMaybe')+Style.RESET_ALL)
  elif 15 >= symptomScore >= 5 :
    print(Fore.YELLOW+messagesForSymptoms.get('someSymptoms')+Style.RESET_ALL)
  elif 2020> symptomScore > 15:
    print(Fore.YELLOW+messagesForSymptoms.get('exposedToVirus')+Style.RESET_ALL)
  elif symptomScore == 2020:
    print(Fore.YELLOW+messagesForSymptoms.get('seekMedicalAttention')+Style.RESET_ALL)
  else:
    print(Fore.YELLOW+"You have not provided enough information. Please try again."+Style.RESET_ALL)
  returnToMenu=input("\nPlease hit enter to return to the menu\n\n\t-->")
  replit.clear()

def main():
  quitChoice = True
  showMenu = True
  #The main menu
  while quitChoice: 
    print("""   _____  ____ __      __ _____  _____          __   ___    _____                                           _    _               
  / ____|/ __ \\ \    / /|_   _||  __ \        /_ | / _ \  |_   _|        / _|                              | |  (_)              
 | |    | |  | |\ \  / /   | |  | |  | | ______ | || (_) |   | |   _ __  | |_  ___   _ __  _ __ ___    __ _ | |_  _   ___   _ __  
 | |    | |  | | \ \/ /    | |  | |  | ||______|| | \__, |   | |  | '_ \ |  _|/ _ \ | '__|| '_ ` _ \  / _` || __|| | / _ \ | '_ \ 
 | |____| |__| |  \  /    _| |_ | |__| |        | |   / /   _| |_ | | | || | | (_) || |   | | | | | || (_| || |_ | || (_) || | | |
  \_____|\____/    \/    |_____||_____/         |_|  /_/   |_____||_| |_||_|  \___/ |_|   |_| |_| |_| \__,_| \__||_| \___/ |_| |_|
                                                                                                                                 """)
    while showMenu: #while the user has not closed the menu
      userChoice = input("\nSelect An Option\n\tA) Start\n\tB) Help\n\tC) Quit\n\n\t\t--> ")
      replit.clear()

  #Option A
      if userChoice.lower() == 'a':
        covidMenu = True
    #covid-19 menu
        while covidMenu:
          userChoiceA = input("Please Select An Option\n\tA) Tracker\n\tB) Latest Information\n\tC) COVID-19 Self Diagnosis\n\tD) Return To Menu\n\n\t\t--> ")

          if userChoiceA.lower() == 'a':
            replit.clear()
            trackerMenu = True
            while trackerMenu:
              userChoiceTracker = input("Please Select An Option\n\tA) World Total Infected\n\tB) World Total Deaths\n\tC) World Total Recovered\n\tD) World Current Infected\n\tE) Return To Menu\n\n\t\t--> ")#menu for the covid-19 tracker

              #all of the numbers for the coronavirus and the functions
              if userChoiceTracker.lower() == 'a':
                replit.clear()
                print("Please wait a moment...")
                trackerSectionModule("There have been {} total cases of COVID-19.",webScrapperNum("https://www.worldometers.info/coronavirus/", "div", "class", "maincounter-number", 0)) #require the message, and data which is from the webScrapperNum function
              
              elif userChoiceTracker.lower() == 'b':
                replit.clear()
                print("Please wait a moment...")
                trackerSectionModule("There have been {} total deaths due to COVID-19.",webScrapperNum("https://www.worldometers.info/coronavirus/", "div", "class", "maincounter-number", 1))
              
              elif userChoiceTracker.lower() == 'c':
                replit.clear()
                print("Please wait a moment...")
                trackerSectionModule("{} people have recovered from COVID-19.",webScrapperNum("https://www.worldometers.info/coronavirus/", "div", "class", "maincounter-number", 2))
              
              elif userChoiceTracker.lower() == 'd':
                replit.clear()
                print("Please wait a moment...")
                recoveredNum=int(webScrapperNum("https://www.worldometers.info/coronavirus/", "div", "class", "maincounter-number", 0))-int(webScrapperNum("https://www.worldometers.info/coronavirus/", "div", "class", "maincounter-number", 2))-int(webScrapperNum("https://www.worldometers.info/coronavirus/", "div", "class", "maincounter-number", 1))
                trackerSectionModule("There are {} people currently infected with COVID-19.",recoveredNum)

              elif userChoiceTracker.lower() == 'e':  #exits the tracker menu
                replit.clear()
                trackerMenu=False
              
              else: #in case the user enters a wrong answer
                userWrongAnswer()
          
          elif userChoiceA.lower() == 'b':  #for the latest news section
            latestNews()

          elif userChoiceA.lower() == 'c':  #for the symptoms checker 
            covidSymptomChecker()
        
          elif userChoiceA.lower() == 'd':  #to return to the original menu
            covidMenu = False
            showMenu = True
            replit.clear()

          else: #in case of an invalid answer
            userWrongAnswer()

  #Option B
      elif userChoice.lower() == 'b':
        partB = True
        while partB: 
          showMenu = False
          FAQList = True
          userChoiceB = input("Please Select An Option\n\tA) FAQ\n\tB) Return To Menu\n\n\t\t--> ")

    #FAQ
          if userChoiceB.lower() == 'a':
            while FAQList:
              replit.clear()
              FAQchoice = input("Frequently Asked Questions\n\tA) How do you get this information?\n\tB) How does the self diagnosis work?\n\tC) How does one use the app?\n\tD) Are there any hidden costs?\n\tE) How to contact us\n\tF) Return to the menu\n\n\t\t--> ")

              
              if FAQchoice.lower() == 'a':  #each FAQ module includes the message needed to output
                FAQModule("We get this information from the worldmeters website, CTV news and the Centres For Disease Control And Prevention.")

              elif FAQchoice.lower() == 'b':
                FAQModule("The self diagnosis uses data from Centres For Disease And Prevention for symptoms and assigns a value to each symptom to determine if the user is likely to have COVID-19.")
              
              elif FAQchoice.lower() == 'c':
                FAQModule("The user experience should be quite simple as you just enter the letter incorporated with your desired option and if you enter an incorrect answer the program will tell you and allow you to retry.")
              
              elif FAQchoice.lower() == 'd':
                FAQModule("No, there are ZERO additional or hidden fees! The program is free to use for anybody.")
              
              elif FAQchoice.lower() == 'e':
                FAQModule("To contacts us please use the email: eugene.lee3@student.tdsb.on.ca")

              elif FAQchoice.lower() == 'f':  #to return to the menu
                showMenu = True
                partB = False
                FAQList = False
                replit.clear()
              
              else: #in case of an invalid answer
                userWrongAnswer()
    #Return to menu
          elif userChoiceB.lower() == 'b':
            showMenu = True
            replit.clear()
    #Wrong Input Module    
          else:
            userWrongAnswer()

  #Option C
      elif userChoice.lower() == 'c':
        quitProgram()

  #For incorrect input in intial menu
      else:
        userWrongAnswer()

main()#runs the main function
