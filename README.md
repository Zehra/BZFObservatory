# BZFObservatory
> The observatory for watching the many worlds and those within them.

**In a nutshell:** *BZFObservatory is a CLI app which uses (BZFlag) stats sites API's. It's more efficient in network and memory usage.*

BZFObservatory is a utility which performs a query at intervals for data on which servers have players. It then displays the data in a nice format for easy viewing. The biggest feature is a where it highlights favorite server(s) and friend(s). This displays data in the order of friends and favorites, friends, favorites and finally other active servers/players.

## Background:
Originally this was two simple scripts made as a side project. Known as watcher and observer, one would check servers and the other for players. They were merged and with a friends list and favorites list added as features, this became BZFObservatory. This was then released to the general public and a bit of the code has been cleaned up.

It's a bit more efficient compare to viewing the stats sites normally, but it isn't as lightweight as expected, even though it runs in the shell and doesn't have a fancy GUI.

## TODO:
* Add proxy API utility
* Don't depend on a single service.
* Add ability to get live stats on demand.

## License:
**CC0 1.0 Universal**

## Usage of friends and favorites feature:
BZFObservatory accepts a conf as argument. (Plain text file)
* In the conf file: Add in each friend's callsign on a new line.
Example:
```
[F] Sample Player
[F] Example Player
```
To use the favorites feature:
* In the conf file: Add in each server by server name and server port on a new line.
Example:
```
[S] awesomehosting.example.com:5555
[S] 255.255.255.255:5155
[S] 127.0.0.1:5155
```

Example of results:

* Friends and favorites, friends, favorites and other:
```
===Friends on Favorite Servers:===
   Sample Player ::: On :: awesomehosting.example.com:5555 As Red team
===Friends found on Servers:===
   Example Player ::: On :: Some-other-host.example.org:5555 As Red team
===Favorite Servers:===
   Another Player ::: On :: awesomehosting.example.com:5555 As Red team
   Template Player ::: On :: awesomehosting.example.com:5555 As Green team
===End of favorites/friends===
   A Player ::: On :: other-host.example.net:5555 As Green team
   Some Player ::: On :: 127.0.0.9:5252 As Red team
   Playing Player ::: On :: hosting.example.net:5154 As Red team

```
* Friends and other:
```
===Friends found on Servers:===
   Example Player ::: On :: Some-other-host.example.org:5555 As Red team
   Sample Player ::: On :: Some-other-host.example.org:5555 As Green team
===End of favorites/friends===
   A Player ::: On :: other-host.example.net:5555 As Green team
   Some Player ::: On :: 127.0.0.9:5252 As Red team
   Playing Player ::: On :: hosting.example.net:5154 As Red team

```

## Changelog:
* **0.0.1** - Initial release
* **0.0.2** - Refactored code and updated display of listings.
* **0.0.3** - Minor cleanup/refactor
* **0.0.4** - Refactored rewrite and cleanup
