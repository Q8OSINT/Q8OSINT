from enum import Enum;


class AppsEnum(Enum):
    #news genre
    ALARABIYA = 1
    ALJAZEERA = 2
    CNNARABIC = 3
    DERWAZA = 4
    WATAN = 5

    #entertainment genre
    CINESCAPE = 6

    #services genre
    TALABAT = 7

    #telecom genre
    VIVA = 8
    ZAIN = 9


DestinationUrl = {}
DestinationUrl[AppsEnum.ALARABIYA] = "https://twitter.com/alarabiya"
DestinationUrl[AppsEnum.ALJAZEERA] = "https://twitter.com/ajarabic"
DestinationUrl[AppsEnum.CNNARABIC] = "https://twitter.com/cnnarabic"
DestinationUrl[AppsEnum.DERWAZA] = "https://twitter.com/derwazanews";
DestinationUrl[AppsEnum.WATAN] = "http://watan.tv";
DestinationUrl[AppsEnum.CINESCAPE] = "https://twitter.com/cinescapeq8";
DestinationUrl[AppsEnum.TALABAT] = "https://twitter.com/talabat";
DestinationUrl[AppsEnum.VIVA] = "https://twitter.com/vivatelecom";
DestinationUrl[AppsEnum.ZAIN] = "https://twitter.com/zainkuwait";

LogoFilename = {}
LogoFilename[AppsEnum.ALARABIYA] = "alarabiya.jpg"
LogoFilename[AppsEnum.ALJAZEERA] = ""
LogoFilename[AppsEnum.CNNARABIC] = "cnnarabic.png"
LogoFilename[AppsEnum.DERWAZA] = "derwaza.jpg";
LogoFilename[AppsEnum.WATAN] = "watan.jpg";
LogoFilename[AppsEnum.CINESCAPE] = "cinescape.jpg";
LogoFilename[AppsEnum.TALABAT] = "talabat.png";
LogoFilename[AppsEnum.VIVA] = "viva.jpg";
LogoFilename[AppsEnum.ZAIN] = "zain.jpg";

AppName = {}
AppName[AppsEnum.ALARABIYA] = "ALARABIYA"
AppName[AppsEnum.ALJAZEERA] = "ALJAZEERA"
AppName[AppsEnum.CNNARABIC] = "CNNARABIC"
AppName[AppsEnum.DERWAZA] = "DERWAZA"
AppName[AppsEnum.WATAN] = "WATAN"
AppName[AppsEnum.CINESCAPE] = "CINESCAPE"
AppName[AppsEnum.TALABAT] = "TALABAT"
AppName[AppsEnum.VIVA] = "VIVA"
AppName[AppsEnum.ZAIN] = "ZAIN"

def getAppNameFromEnum(enum):
    return AppName[enum];

def getEnumFromAppName(APPNAME):
    for enum in AppsEnum:
        if APPNAME == AppName[enum]:
            return enum;

ConsumerKeyString = {}
ConsumerSecretString = {}

#news channel apps
ConsumerSecretString[AppsEnum.ALARABIYA] = "Fq9Vs9thDcA4XGnYoog4UzvJflwFKcdEjurM9UOB56zcahvkrc"
ConsumerKeyString[AppsEnum.ALARABIYA] = "46Zhv8TXomlpMkSiIslMzHDbm"

ConsumerSecretString[AppsEnum.CNNARABIC] = "rydxVk8Z6cnuCA8pydz8CXKEOBhJi6trzAh7TGxw5LUTjzCn6N"
ConsumerKeyString[AppsEnum.CNNARABIC] = "AQRBxJJE5ohjdMbNpZa0aj8ZI"

ConsumerSecretString[AppsEnum.DERWAZA] = "1RNUbZhkTJZQw1R7M5iJ8BsbMyyttJE8u7Kfg4QHRDELx13I3Q";
ConsumerKeyString[AppsEnum.DERWAZA] = "hIDBzrjY6JkyOARxgkA2PS11y";

ConsumerSecretString[AppsEnum.WATAN] = "uLCI0sIanZnmoFXTu9G8MEqpPzZhszfiLmpYw1HF8GHJNOLlOu";
ConsumerKeyString[AppsEnum.WATAN] = "y9o4eqEb2gfjtkDiPunegk31H";

ConsumerKeyString[AppsEnum.ALJAZEERA] = ""
ConsumerSecretString[AppsEnum.ALJAZEERA] = ""

#entertainment apps
ConsumerKeyString[AppsEnum.CINESCAPE] = "T8iIxBTgdZcpYNgpT6fUHWvoN";
ConsumerSecretString[AppsEnum.CINESCAPE] = "e9WAXohVXPf9wpHz3XNLOof9rQaKkNLA12IV38KRWgM1NHXCYS";

#food delivery
ConsumerKeyString[AppsEnum.TALABAT] = "kRwGRXlhiBYTXmITQpJOVL8Il";
ConsumerSecretString[AppsEnum.TALABAT] = "AoPHrP7diGC1MBHmCmXSupDaZpy8bxvi5fQKKcXaTj3iZR2duk";

#telecom
ConsumerKeyString[AppsEnum.VIVA] = "";
ConsumerSecretString[AppsEnum.VIVA] = "";

ConsumerKeyString[AppsEnum.ZAIN] = "";
ConsumerSecretString[AppsEnum.ZAIN] = "";
