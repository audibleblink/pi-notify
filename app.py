import httplib2
import time
import simplejson
import RPi.GPIO as GPIO

settings = {
  "url": "https://raw.githubusercontent.com/audibleblink/mock-data/master/binary/true.json",
  "pin": 7 
}


GPIO.setmode(GPIO.BOARD)
GPIO.setup(settings["pin"], GPIO.OUT)


def status(url):
  response, content = httplib2.Http(disable_ssl_certificate_validation=True).request(url)
  return simplejson.loads(content)
  
def unread(response):
  return True if response["unread"] else False

def turn_on_for_what():
  GPIO.output( settings["pin"], True )
  time.sleep(.5)
  GPIO.output( settings["pin"] , False )
  print "Light ON!"

while True:
  if unread( status(settings["url"]) ):
    turn_on_for_what()
    time.sleep(5)


GPIO.cleanup()

