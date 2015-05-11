# With this code, a CloudBit and a pressure sensor from littleBits you are 
# able to build your own TMI machine. Place the TMI machine with the presure sensor 
# on the toilet seat. This will enable the machine to send a tweet about when and 
# how long the visit at the loo was. See examle at https://twitter.com/tmimachine


from twitter import *   #from twitter.api import Twitter. Doc: https://github.com/sixohsix/twitter/tree/master
import partlycloudy   #import api for littlebits cloudbit. Doc: https://github.com/technoboy10/partly-cloudy 
import time


# Access token and Device ID for the CloudBit (neds to be renewed when the WiFi changes)
bit = partlycloudy.Bit('[AccessToken]', '[Device ID]')

# Create your twitter application here https://apps.twitter.com/app/new
# Auth into twitter account of choice 
twitter = Twitter(auth = OAuth(
  consumer_key='[ConsumerKey]',
  consumer_secret='[ConsumerSecret]',
  token='[Token]',
  token_secret='[TokenSecret]'
))

# Continiusly collects values from the sensor
old_pct = 1
for pct in bit.stream():
  print pct # input, on a scale of 1 to 100
  if pct == 100 and old_pct < 100:
    print "sat down"
    start_time = time.time()
    time_message = time.strftime("%D %H:%M", time.localtime(int(start_time)))

  # If sensor is pressed start timer.
  if old_pct == 100 and pct < 100:
    stop_time = time.time()
    duration = stop_time - start_time
    time_at_loo = duration
    print start_time 
    print duration
    # Post a tweet when the sensor is released 
    time_at_loo = int(duration)
    print time_at_loo
    print "User sat on the loo at " + str(time_message) + " for " + str(time_at_loo) + " seconds"
    twitter.statuses.update(status="User sat on the loo at " + str(time_message) + " for " + str(time_at_loo) + " seconds")

  old_pct = pct

