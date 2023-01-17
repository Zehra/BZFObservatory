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
        sys.exit("Error reading file.")
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
        print("ERR")
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
        serverset = []
        i = 0
        req = requests.get(url)
        if req.status_code != 200:
            print("ERROR in getting request.")
            time.sleep(60)
        else:
            resp = req.text
            for line in resp.splitlines():
                if friendsinc == False and favoritesinc == False:
                    data = line.split("\t")
                    print(data[0], data[1], data[2])
                else:
                    serverset.append(line)
                
            #serverlen = len(serverset) 
            # Was for something, but meh, didn't work.

            #friends and server related stuff            
            if friendsinc == True and favoritesinc == True:
                friendsAndServer = False
                ruset = 0
                naset = 0
                t1 = False
                t2 = False
                
                for dataset in serverset:
                    data = dataset.split("\t")
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
                            print("{} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
                        else:
                            print("Friends on Favorite Servers:")
                            print("{} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
                            friendsAndServer = True
                            # You could run a system command as an audio notification.
                        #print(dataset)
                        serverset.remove(dataset)
                    ruset = 0
                    naset = 0
                    t1 = False
                    t2 = False

            # Friends related stuff
            if friendsinc == True:
                friendsOnly = False
                for dataset in serverset:
                    data = dataset.split("\t")
                    naset = 0
                    t2 = False                
                    while naset < friendsc:
                        t2 = data[0] == friends[naset]
                        if t2 == True:
                            break
                        naset += 1
                    
                    if t2 == True:
                        if friendsOnly == True:
                            print("{} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
                        else:
                            print("Friends found on Servers:")
                            print("{} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
                            friendsOnly = True
                            # You could run a system command for an audio notification.
                        #print(dataset)
                        serverset.remove(dataset)
                    naset = 0
                    t2 = False
                
            # server related stuff            
            if favoritesinc == True:
                serverOnly = False
                ruset = 0
                t1 = False
                for dataset in serverset:
                    data = dataset.split("\t")
                    while ruset < favoritesc:
                        t1 = data[2] == favorites[ruset]
                        if t1 == True:
                            break
                        ruset += 1

                    if t1 == True:
                        if serverOnly == True:
                            print("With ::: {} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
                        else:
                            print("Favorite Servers:")
                            print("With ::: {} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
                            serverOnly = True
                        #print(dataset)
                        serverset.remove(dataset)
                    ruset = 0
                    t1 = False

            print("End of favorites/friends")
            
            for dataset in serverset:
                data = dataset.split("\t")
                print("With ::: {} ::: On :: {} As {} team".format(data[0], data[2], data[1]))
                serverset.remove(dataset)
            print("End of normal data")
            time.sleep(60 * 5)
            os.system("clear")
            # You can use it to run a ping too.

