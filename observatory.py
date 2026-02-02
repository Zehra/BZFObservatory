import os
import sys
import time
import requests

if __name__ == '__main__':
  if len(sys.argv) != 2:
    sys.exit('Usage: {0} <conf.txt>'.format(sys.argv[0]))
  try:    
    conf = open(sys.argv[1], "r")
  except:
    sys.exit('Unable to open: {}'.format(sys.argv[1]))
  # Standard values:
  url = "http://bzstats.strayer.de/stuff/LePoulpe303.php"
  favorites=[]
  friends=[]
  Display=[]
  count = 1
  launch = 0
  Friend=0
  Server=0
  AddToList=-1
  # Reading and setting configs.
  confval = conf.read()
  for line in confval.splitlines():
    if len(line) >= 7: # [S] Space Username or Server
      if line[:5] == "[F] ":
        friends.append(line[5:].lower())
      if line[:5] == "[S] ":
        favorites.append(line[5:].lower())
  conf.close()
  # Setting standard type
  if len(favorites) >= 1:
    count += 1
  if len(friends) >= 1:
    count += 1
  if count == 3:
    count = 4
  # Main loop.
  while True: 
    req = requests.get(url)
    if req.status_code != 200:
      print("ERROR in getting request.")
    else:
      resp = req.text
      lines = resp.splitlines()
      if len(resp) < 3:
        print("===NO PLAYERS FOUND===")
      elif count == 1:
        for line in lines:
          data = line.split("\t")
          print("{} :: {} :: On :: {}".format(data[0], data[1], data[2]))
      else:
        for con in range(count):
          launch = con
          for line in lines:
            AddToList=-1
            data = line.split("\t")
            Friend=0
            Server=0
            if len(friends) >= 1:
              for fri in friends:
                if fri == data[0].lower():
                  Friend=1
            if len(favorites) >= 1:
              for fav in favorites:
                if fav == data[2].lower():
                  Server=1

            # Probably the values should be stored in an array or something to lookup.
            if Friend == 0 and Server == 0:
              if con == 1 and count == 2 or con == 3 and count == 4:
                AddToList=3
            else:
              if Friend == 1:
                if Server == 1:# Friend & Server
                  AddToList = 0
                else:
                  if con == 0 and count == 2 or con == 1 and count == 4:# Friend
                    AddToList=1
              else: # Server
                if con == 0 and count == 2 or con == 2 and count == 4:
                  AddToList=2

            if AddToList != -1:
              if launch == con:
                if AddToList == 0:
                  Display.append("===Friends on Favorite Servers:===")
                if AddToList == 1:
                  Display.append("===Friends found on Servers:===")
                if AddToList == 2:
                  Display.append("===Favorite Servers:===")
                if AddToList == 3:
                  if len(Display) >= 1:
                    Display.append("===End of favorites/friends===")
                launch += 1
              Display.append("   {} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
        for display in Display:
          print(display)
        Display.clear()
    time.sleep(150) 
    os.system("clear")
