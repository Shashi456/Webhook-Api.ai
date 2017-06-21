#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os
from time import strftime 

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    #print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
   # if req.get("result").get("action") == "DealsDestination":
    result = req.get("result")
    parameters = result.get("parameters")

    city = parameters.get("location")
    print(city)
    main = "https://www.teletextholidays.co.uk/serp-es#/overseas/"
    search = city + "/"
    t = time.strftime("%Y-%m-%d") + "/"
    end = "Any_London/boardtype=allinclusive/nights=7/adults=2/children=0/minstars=3"
    print(main + t + end)
    speech = main + search + t + end
    #else :
    #    return {}
    print("Response:")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }



if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
