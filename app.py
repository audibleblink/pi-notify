#so we can call sleep
import time

#allows us to make get/curl requests
import httplib2 

#json parsing, made simple
import simplejson

#the library that allows interfacing with the 
#pins on our RPi
import RPi.GPIO as GPIO


#config hash, takes url to ping and pin number
config = {
    "url": "http://bit.ly/1DaR7WV",
    "pin": 7 
}

# returns a json object we can use in Python
def status(args):
    client = httplib2.Http(disable_ssl_certificate_validation = True)
    response, content = client.request(args["url"])
    return simplejson.loads(content)
    # => {"unread": True}

  
# returns a Boolean. Do we have unread code review requests?
def unread(response):
    return True if response["unread"] else False


# Turns on the LED, then off
def turn_on_for_what(args):
    GPIO.output(args["pin"], True)
    time.sleep(.5)
    GPIO.output(args["pin"] , False)


# Controller method. Kicks everything off. Takes our settings dictionary
def main(args):
    #configures how the pins are referenced (chip vs board)
    GPIO.setmode(GPIO.BOARD)

    #tells our library that pin 7 is to be used for output (3.3v)
    GPIO.setup(args["pin"], GPIO.OUT)

    # set a var that is our JSON from the URL in settings
    pull_requests = status(args)

    # this loop will run indefinitely
    while True:

        # if we have unclaimed pull requests, TURN ON FOR WHAT!
        if unread(pull_requests):
            turn_on_for_what(args)
            time.sleep(2)

# run that shit.
main(config)

# GPIO.cleanup()

