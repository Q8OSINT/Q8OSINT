Copyright &copy; 2021. The Regents of KuwaitHackers LLC. (Regents). All Rights Reserved. Permission to use, copy, modify, and distribute this software and its documentation for educational, research, and not-for-profit purposes, without fee and without a signed licensing agreement, is hereby granted, provided that the above copyright notice, this paragraph and the following two paragraphs appear in all copies, modifications, and distributions. Contact `KuwaitHackers LLC.,
Alawadhi Tower2 M1, Ahmad Al Jaber Street, Sharq, Kuwait City, State of Kuwait, +965 99 88 71 80, info@hackers.com.kw, http://kuwaithackers.com` for commercial licensing opportunities.

IN NO EVENT SHALL REGENTS BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST PROFITS, ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF REGENTS HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

REGENTS SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE SOFTWARE AND ACCOMPANYING DOCUMENTATION, IF ANY, PROVIDED HEREUNDER IS PROVIDED "AS IS". REGENTS HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.

ETHICAL CONSIDERATION

Tools developed by KuwaitHackers are only for educational and research purposes. Be aware that hacking social network accounts is considered illegal. You shall not misuse the tool to gain unauthorized access. KuwaitHackers shall not be responsible for any direct or indirect damage caused due to the usage of the tool.   

```
                                                 (,,                            
                           &@@@@@@@@@@@&/,,*/////((((#(((/(//(/(/#&@@@&&&@@%    
                  *@@@@@%((/(((((((///(/(***//(//((((#(#((((//(((//((((((((##*@.
             @@%#((((####(#(((#((##((/(((//(//(//*//(((((////((/(//(#(###(#(###@
      /@@(#%%%%%%##((#(#####((###((((((((/*//*/*///***,*/*,,****(*/###(####/#,@ 
  /##%%%%%%%%#%%%%%%%%%%%%##((((##((((/(((//**//*,*,,,,,,,...*/(((##((*@%    @  
*&%%%%%&&&&%%%%%%%%%%%%%%%%######((##(((((#(((#//////**,,. .,**//(/@@       %@  
 .@@@@@&&&&%%((##############%&@@@@@@%/*////////(((////*/,.,,***(&@         @@  
                                              #@@@.////**,,,,*//@/        @@@   
     @                                             @@&**/****/@/          @,    
     @                                                @@@@@@#            *@     
      .@/                             .                                  @@     
        /                                                                @&     
         @                           @@@@@@@@@@@     @@@@@@@@@@@@%      @@      
         @             /@@@@@     (@@@%       @@@@   @@@@       @@@@    @@      
         .@     (@@@@@@@  @@@@&   @@@.         @@@   @@@@@@@@@@@@@@     @@      
          @,    @@@@       @@@    @@@@         @@@   @@@@    #@@@@      @@      
          /@     @@@@@@@@@@#       @@@@      #@@@.   @@@*      *@@@    &@       
           @@     @@@@    &@@@@@     @@@@@@@@@@      @@@@@@@@@@@@@     @@       
            @@     @@@@      ,@@@@                                     @@       
             @.     @@@@                                               @@       
              @            &         #&      &&&/       &&            ,@        
              ,@           &          &#    #&&&&        &            &@        
               &@          &&&&&&&&&&&&&       &&      &&&            @@        
                @@               %&     %&#(&&&&   &&&&&              @         
                 @%               &                                  @@         
                  (                                               &@            
                    @@                                            @*            
                     @@#                                  /@@@@@/               
                       *@@@@@@@@@@@( ,  %@@@@@@@@@@@@@@@@%.

```



# ROB | روب   
("Yogurt” in Kuwaiti-Arabic slang)

## RAT Exploitation Tool for Social Networks

========================================================

@developed by [KuwaitHackers LLC.](https://kuwaithackers.com)

Presented at [BlackHat Europe 2021 Arsenal](
https://www.blackhat.com/eu-21/arsenal/schedule/index.html#rat-exploitation-tool-for-social-networks-25150
)

========================================================

### Summary

This project provides RAT control over Twitter accounts by combining the powers of social engineering with malicious third party apps.

It exploits social-engineering apps that are organized in a private catalogue organized into genres (e.g. news channels, games, ..etc).

Hacker can pick and choose any malicious app they want and send over the authorization links to targeted users so that they can include the apps as add-ons to their profiles.

Once authorized, the following functionalities can be exercised (on behalf of the users):
* Capturing user-agent and IP address information
* Sending long-lived tracking HTTP cookie to user session.
* View token details
* Viewing tweet history
* Viewing direct messages 
* Viewing followers and following profiles
* Posting a tweet
* Sending a direct message
* Extracting location of geo-tagged tweets 
* Generate shortened Urls

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


## Tool Concept

Rob Tool consists of four components
+ Phishing 3rd Party Apps: Creating third-party apps that users would include as add-ons to their profile. These apps are designed to be over-permissive for malicious intents.
+ Malicious App Store: Private third-party app store, grouped by genres to classify and catalogue phishing & trojanized apps that a bad actor can choose from to gain RAT control over victim accounts.
+ Oauth Management Console: oauth management console to handle tokens for compromised social network accounts.
+ RAT Control: Exercise operations on behalf of the user. This includes reading private messages, viewing inbox, sending direct messages, posting on social media, and tracing geolocation. 


## Lessons Learned

* Lesson 1: Humans are the weakest link. Therefore, we should not delegate access control decisions to users.
* Lesson 2: Rethink the design of social network platforms to build in security. 
* Lesson 3: Open platforms enable exploitation of trust boundaries, such as authorizations of third-party apps, through mastery of social-engineering.

## Misc
App-specific credentials including `oauth_consumer_key` and `oauth_consumer_secret` may be valid for demonstration purposes and are intentionally available in our github (We get warning messages from Github Guardian and other scanners about them so relax we know how to review our source code!!). Oauth tokens may be valid for our test accounts. If we see mischief they will be revoked.

