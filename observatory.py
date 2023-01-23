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
    if friendsinc == True:
        friends = []
        friendslist = friendsfile.read()
        friendsc = -1
        
        for friend in friendslist.splitlines():
            friendsc += 1
            friends.append(friend)
        
        friendsc = len(friends)
        friendsfile.close()
        
        #i = 0
        #while i < friendsc: 
        #    print(friends[i])
        #    i += 1

    try:
        favoritesfile = open("favorites.txt", "r")
    except:
        favoritesinc = False
        print("Favorite servers file not found.")
        #sys.exit("Error reading file.")
    if favoritesinc == True:
        favorites = []
        favoriteslist = favoritesfile.read()
        favoritesc = -1
        
        for favorite in favoriteslist.splitlines():
            favoritesc += 1
            favorites.append(favorite)

        favoritesc = len(favorites)
        favoritesfile.close()

        #i = 0
        #while i < favoritesc: 
        #    print(favorites[i])
        #    i += 1

    while True:
        req = requests.get(url)
        
        if req.status_code != 200:
            print("ERROR in getting request.")
            time.sleep(60)
        else:

            resp = req.text
            if friendsinc == True and favoritesinc == True:
                friendsAndServer = False
                ruset = 0
                naset = 0
                t1 = False
                t2 = False
                for line in resp.splitlines():
                    data = line.split("\t")
                    while ruset < favoritesc:
                        t1 = data[2] == favorites[ruset]
                        if t1 == True:
                            break
                        ruset += 1
                        
                    while naset < friendsc:
                        t2 = data[0] == friends[naset]
                        if t2 == True:
                            break
                        naset += 1
                    
                    if t1 == True and t2 == True:
                        if friendsAndServer == True:
                            print("With ::: {} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
                        else:
                            print("Friends on Favorite Servers:")
                            print("With ::: {} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
                            friendsAndServer = True
                            # You could run a system command as an audio notification.
                    ruset = 0
                    naset = 0
                    t1 = False
                    t2 = False

            if friendsinc == True:
                friendsOnly = False
                ruset = 0
                naset = 0
                t1 = False
                t2 = False
                for line in resp.splitlines():
                    data = line.split("\t")
                    if favoritesinc == True:
                        while ruset < favoritesc:
                            t1 = data[2] == favorites[ruset]
                            if t1 == True:
                                break
                            ruset += 1
                        
                    while naset < friendsc:
                        t2 = data[0] == friends[naset]
                        if t2 == True:
                            break
                        naset += 1
                    
                    if t1 == False and t2 == True:
                        if friendsOnly == True:
                            print("With ::: {} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
                        else:
                            print("Friends found on Servers:")
                            print("With ::: {} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
                            friendsOnly = True
                            # You could run a system command as an audio notification.
                        #print(dataset)
                    ruset = 0
                    naset = 0
                    t1 = False
                    t2 = False

            if favoritesinc == True:
                serverOnly = False
                ruset = 0
                naset = 0
                t1 = False
                t2 = False
                for line in resp.splitlines():
                    data = line.split("\t")
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
                    
                    if t1 == True and t2 == False:
                        if serverOnly == True:
                            print("{} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
                        else:
                            print("Favorite Servers:")
                            print("{} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
                            serverOnly = True
                            # You could run a system command as an audio notification.
                    ruset = 0
                    naset = 0
                    t1 = False
                    t2 = False
            if friendsinc == True or favoritesinc == True:
                print("End of favorites/friends")
                ruset = 0
                naset = 0
                t1 = False
                t2 = False
                for line in resp.splitlines():
                    data = line.split("\t")
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
                    
                    if t1 == False and t2 == False:
                        print("{} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
                    ruset = 0
                    naset = 0
                    t1 = False
                    t2 = False
                
                print("End of normal data")
            else:
                for line in resp.splitlines():
                    data = line.split("\t")
                    print("{} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
            time.sleep(60 * 5)
            os.system("clear")
            # You can use it to run a ping too.
