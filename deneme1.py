from datetime import datetime

now = datetime.now()
print now

#print "bugun %s yili %s ayi %s gunudur." + %(yil, ay, gun)
print 'bugun %s yili %s. ayi %s. gunudur.' % (now.year, now.month, now.day)

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

