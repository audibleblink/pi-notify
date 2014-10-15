import time
import httplib2
import simplejson
import RPi.GPIO as GPIO


config = {
  "url": "http://bit.ly/1DaR7WV",
  "pin": 7 
}


def status(args):
  client = httplib2.Http(disable_ssl_certificate_validation = True)
  response, content = client.request(args["url"])
  return simplejson.loads(content)
  
def unread(response):
  return True if response["unread"] else False

def turn_on_for_what(args):
  GPIO.output(args["pin"], True)
  time.sleep(.5)
  GPIO.output(args["pin"] , False)

def main(args):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(args["pin"], GPIO.OUT)

  pull_requests = status(args)

  while True:
    if unread(pull_requests):
      turn_on_for_what(args)
      time.sleep(2)

main(config)

GPIO.cleanup()

