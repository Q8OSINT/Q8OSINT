
import os, time
import urllib.request
from datetime import datetime

class GlobalFunctions:
    def file_get_contents(filename, offset = -1, maxlen = -1):
        if (filename.find('://') > 0):
            ret = urllib.request.urlopen(filename).read()
            if (offset > 0):
                ret = ret[offset:]
            if (maxlen > 0):
                ret = ret[:maxlen]
            return ret
        else:
            fp = open(filename,'rb')
            try:
                if (offset > 0):
                    fp.seek(offset)
                ret = fp.read(maxlen)
                return ret
            finally:
                fp.close()


    def file_put_contents(filename, data, flag):
        f = open(filename, flag)
        f.write(data)
        f.close()

    def date_default_timezone_set(timezone_str):
        os.environ['TZ'] = timezone_str
        time.tzset()


    def microtime(get_as_float = False) :
        d = datetime.now()
        t = time.mktime(d.timetuple())
        if get_as_float:
            return t
        else:
            ms = d.microsecond / 1000000.
        return '%f %d' % (ms, t)