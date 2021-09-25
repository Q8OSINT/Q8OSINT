# ROB | روب
## RAT Exploitation Tool for Social Networks

========================================================

@developed by KuwaitHackers LLC. 
https://kuwaithackers.com

========================================================

### Description

This project provides RAT control over Twitter accounts by combining the powers of social engineering with malicious third party apps.

It exploits social-engineering apps that are organized in a private catalogue organized into genres (e.g. news channels, games, ..etc).

Hacker can pick and choose any malicious app they want and send over the authorization links to targeted users so that they can include the apps as add-ons to their profiles.

Once authorized, the following functionalities can be exercised (on behalf of the users):
* Capturing user-agent and IP address information
* Sending long-lived tracking HTTP cookie to user session.
* Viewing tweet history
* Viewing direct messages 
* Viewing followers and following profiles
* Posting a tweet
* Sending a direct message
* Extracting location of geo-tagged tweets 

python 3.7.x

### Running

Go to the project directory and on the cmd, type the command follow:


```
python3 Main.py
```
This will open the HTTP socket listener and start the app.

### Testing

In your browser, type the url follow:

```
http://<server.host_socket>:<server.socket_port>/thirdpartyrats/twitter/tokens/
```
See configuration under `RobConfig.py`