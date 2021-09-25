import cherrypy
from TwitterAPI import TwitterAPI
import time;
import RobConfig;

@cherrypy.expose
def getDirectMessages():
    # check if cherrypy session is initialized otherwise reload token
    dm_list="";
    if ("consumer_key" not in cherrypy.session.keys() or cherrypy.session['consumer_key'] == ""):
        raise cherrypy.HTTPRedirect("/thirdpartyrats/twitter/tokens");
    else:
        api = TwitterAPI(cherrypy.session['consumer_key'], cherrypy.session['consumer_secret'],
                         cherrypy.session['oauth_token'], cherrypy.session['oauth_secret']);
        r = api.request('direct_messages/events/list');
        dm_list = ""
        i=0;
        for msg in r.json()['events']:
            #timestamp
            timestamp = time.ctime(int(msg['created_timestamp']) / 1000)

            #timestamp = datetime
            # .datetime.fromtimestamp(calendar.timegm(t1), tz=pytz.utc);
            #timestamp =  time.strftime('%Y-%m-%dT%H:%M:%SZ', t1);

            #message type
            message_type = msg['type'];

            #sender id and username
            sender_id = msg['message_create']['sender_id'];
            q = api.request('users/show', {'user_id': sender_id})
            sender_name = q.json()['name'];

            #recipient id and username
            recipient_id = msg['message_create']['target']['recipient_id'];
            q = api.request('users/show', {'user_id': recipient_id});
            recipient_name = q.json()['name'];

            #text
            text = msg['message_create']['message_data']['text'];

            RobConfig.direct_messages.append({"timestamp": str(timestamp),
                                                       "sender_id": str(sender_id),
                                                       "sender_name": sender_name,
                                                       "recipient_id": str(recipient_id),
                                                       "recipient_name": recipient_name,
                                                       "text": text})
            i=i+1;
            record_string = str(timestamp) + " Sender: "+ sender_name + ", Receiver: " + recipient_name;
            dm_list += "<option value=\""+record_string+"\">" + record_string + "</option>";

    return dm_list;