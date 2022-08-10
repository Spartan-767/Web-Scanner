#!/usr/bin/python
import sys, os
import urllib.request
from urllib.request import urlopen, Request
import time

# Restart ####################
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
##############################

os.system("clear")
print (" ")
print ("  ___  ___                         ")
print (" / __|/ __|__ _ _ _  _ _  ___ _ _  ")
print (" \__ \ (__/ _` | ' \| ' \/ -_) '_| ")
print (" |___/\___\__,_|_||_|_||_\___|_|   ")
print ("--------------------------------------- ")
print ("     Coded By Allistar by Star Sec      ")
print ("--------------------------------------- ")
print ("  ===|[ Web Scanner ]|===")
print ("  [01] Scan Web       ")
print ("  [02] Open Scans     ")
print ("  [03] Update         ")
print ("  [00] Exit           ")
print (" ")
MenuOp1 = input(" Choose:  ")

if (MenuOp1 == '01' or MenuOp1 == '1'):
       os.system("clear")
       print ("                                          ")
       print (" ===|[ Scan Configuration ]|===           ")
       print ("  [01] Scan By Keyword                    ")
       print ("  [02] Scan From List                     ")
       print ("  [03] Scan From Text File                ")
       print ("  [04] Undetected Scan                    ")
       MenuOp2 = input("Option:  ")
       if (MenuOp2 == '01' or MenuOp2 == '1'):
              os.system("clear")
              print (" ")
              keyword = input(" Keyword:  ")
              keywordbyte = keyword.encode()
              link = input(" Link:  ")
              linkbyte = link.encode()
              site = urllib.request.urlopen(linkbyte.decode('ASCII')).read() 
              if keywordbyte in site:
                  print("Word Detected:")
                  print(" ")
                  print(keyword)
                  time.sleep(20)
              else:
                  print(keyword, "not found")
                  time.sleep(20)
                  
       if (MenuOp2 == '02' or MenuOp2 == '2'):
              os.system("clear")
              print (" ")
              print ("Broken atm")
              sys.exit()
              keywords = ["word", "python", "cheese"]
              keywordsbyte = keywords.encode()
              link = input(" Link:  ")
              linkbyte = link.encode()
              site = urllib.request.urlopen(linkbyte.decode('ASCII')).read()
              for keyword in site:
                  if keywordbyte in linkbyte:
                      print(keyword)
                  
                  else:
                      print(keyword, "not found")
                      os.system("clear")
                      
       if (MenuOp2 == '03' or MenuOp2 == '3'):
              os.system("clear")
              print (" Coming Soon ")
                          
       if (MenuOp2 == '04' or MenuOp2 == '4'):  
              keyword2 = input(" Keyword:  ")
              url = input(" Link: ")
              req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
              web_byte = urlopen(req).read()
              webpage = web_byte.decode('utf-8')
              if keyword2 in webpage:
                  print("Word Detected:")
                  print(" ")
                  print(keyword2)
                  time.sleep(20)
              else:
                  print(keyword2, "not found")
                  time.sleep(20)
                                
elif (MenuOp1 == '02' or MenuOp1 == '2'):
       os.system("clear")
       print ("Coming Soon")

elif (MenuOp1 == '03' or MenuOp1 == '3'):
       os.system("clear")
       print ("Not enabled yet")
       os.system("git clone")

elif (MenuOp1 == '00' or MenuOp1 == '0'):
       os.system("clear")
       print ("\n[!] Exit the Program...")
       sys.exit()

else:
       os.system("clear")
       print ("\n[!] ERROR : Wrong Input")
       time.sleep(1)
       restart_program() 
