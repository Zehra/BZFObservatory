import os
import sys
import time
import requests

# Utility functions
def FriendAndServer(FRIEND, SERVER):
  if FRIEND == 0 and SERVER == 0: # NOT IN FRIENDS OR IN SERVERS
    return 3# NOT IN FRIENDS OR IN SERVERS
  else: # A friend or a favorite server
    if FRIEND == 1:
      if SERVER == 1:# Friend & Server
        return 0 # Friend & Server
      else: # Friend on regular server
        return 1  # Friend on regular server
    else: # Favorite Server
      return 2 # Favorite Server
  return -1 # Something went very wrong.

def AddToListType(friend, server, stage, stagecount):
  status = FriendAndServer(friend, server)
  if status == 0:
    if stage == 0:
      return 0
  elif status == 1:
    if stage == 0 and stagecount == 2 or stage == 1 and stagecount == 4:
      return 1
  elif status == 2:
    if stage == 0 and stagecount == 2 or stage == 2 and stagecount == 4:
      return 2
  else:
    if stage == 1 and stagecount == 2 or stage == 3 and stagecount == 4:
      return 3
  return -1

def PrefixByAddType(AddType):
  if AddType == 0:
    return "===Friends on Favorite Servers:==="
  elif AddType == 1:
    return "===Friends found on Servers:==="
  elif AddType == 2:
    return "===Favorite Servers:==="
  else: #if AddToList == 3:     
    return "===End of favorites/friends==="

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
      if line[:4] == "[F] ":
        friends.append(line[4:].lower())
      if line[:4] == "[S] ":
        favorites.append(line[4:].lower())
  conf.close()
  # Setting standard type
  if len(favorites) >= 1:
    count += 1
  if len(friends) >= 1:
    count += 1
  if count == 3:
    count = 4

  # Main loop.
  os.system("clear")
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

            AddToList = AddToListType(Friend, Server, con, count)

            if AddToList != -1:
              if launch == con:
                if AddToList >= 0 and AddToList <= 2:
                  Display.append(PrefixByAddType(AddToList))
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

