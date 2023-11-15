import os
import sys
import time
import requests

# Originally two scripts known as watcher and observer.

# Currently has a friends list, a favorites server and a blocklist.
# If you don't specify, it tries defaults and if that fails, it just notifies of new player sessions.

if __name__ == '__main__':
    url = "http://bzstats.strayer.de/stuff/LePoulpe303.php"
    favoritesinc = True
    friendsinc = True

    try:
        friendsfile = open("friends.txt", "r")
    except:
        friendsinc = False
        print("Friends file not found.")
    
    try:
        favoritesfile = open("favorites.txt", "r")
    except:
        favoritesinc = False
        print("Favorite servers file not found.")
    
    if friendsinc == True:
        friends = []
        friendslist = friendsfile.read()
        friendsc = -1
        
        for friend in friendslist.splitlines():
            friendsc += 1
            friends.append(friend)
        
        friendsc = len(friends)
        friendsfile.close()

    if favoritesinc == True:
        favorites = []
        favoriteslist = favoritesfile.read()
        favoritesc = -1
        
        for favorite in favoriteslist.splitlines():
            favoritesc += 1
            favorites.append(favorite)

        favoritesc = len(favorites)
        favoritesfile.close()

    if favoritesinc == True and friendsinc == True:
        phaseset = 1
    elif favoritesinc == False and friendsinc == True:
        phaseset = 2
    elif favoritesinc == True and friendsinc == False:
        phaseset = 3
    else:
        phaseset = 5
    phase = phaseset
    lines = []
    while True:
        req = requests.get(url)
        
        if req.status_code != 200:
            print("ERROR in getting request.")
            time.sleep(60)
        else:
            if friendsinc == False and favoritesinc == False:
                for line in resp.splitlines():
                    data = line.split("\t")
                    print("{} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
            else:
                resp = req.text
                lines = resp.splitlines()
                lenlines = len(lines)
                count = 0
                phase = phaseset
                standard = True
                ruset = 0
                naset = 0
                t1 = False
                t2 = False
                while phase != 5:
                    data = lines[count].split("\t")
                    if favoritesinc == True:
                        while ruset < favoritesc:
                            t1 = data[2] == favorites[ruset]
                            if t1 == True:
                                break
                            ruset += 1
                    if friendsinc == True:  
                        while naset < friendsc:
                            t2 = data[0] == friends[naset]
                            if t2 == True:
                                break
                            naset += 1
                    if phase == 1:
                        if t1 == True and t2 == True:
                            if standard == True:
                                print("===Friends on Favorite Servers:===")
                                standard = False
                            print("   {} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
                    elif phase == 2:
                        if t1 == False and t2 == True:
                            if standard == True:
                                print("===Friends found on Servers:===")
                                standard = False
                            print("   {} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
                    elif phase == 3:
                        if t1 == True and t2 == False:
                            if standard == True:
                                print("===Favorite Servers:===")
                                standard = False
                            print("   {} ::: On :: {} As {} team".format(data[0], data[2], data[1]))                 
                    else:
                        if friendsinc == True or favoritesinc == True:
                            if t1 == False and t2 == False:
                                if standard == True:
                                    print("===End of favorites/friends===")
                                    standard = False
                                print("   {} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
                    count += 1
                    if count == lenlines:
                        count = 0
                        phase += 1
                        standard = True
                        
                    ruset = 0
                    naset = 0
                    t1 = False
                    t2 = False
        time.sleep(60 * 5)
        os.system("clear")
        # You can use it to run a ping too.
