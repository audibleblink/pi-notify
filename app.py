import httplib2
import simplejson
# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BOARD)

settings = {
  "url": "https://raw.githubusercontent.com/audibleblink/mock-data/3a2fcca57d691501f2a108a26e795722de58c579/binary/true.json"
}

def status(url):
  response, content = httplib2.Http().request(url)
  return simplejson.loads(content)
  
def unread(response):
  return True if response["unread"] else False

def turn_on_for_what():
  print "Light ON!"

if unread( status(settings["url"]) ):
  turn_on_for_what()

