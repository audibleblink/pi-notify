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
  client = httplib2.Http(disable_ssl_certificate_validation=True)
  response, content = client.request(url)
  return simplejson.loads(content)
  
def unread(response):
  return True if response["unread"] else False

def turn_on_for_what(pin):
  GPIO.output(pin, True)
  time.sleep(.5)
  GPIO.output(pin , False)


pull_requests = status(settings["url"])
while True:
  if unread(pull_requests):
    turn_on_for_what(settings["pin"])
    time.sleep(5)


GPIO.cleanup()

