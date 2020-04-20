# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2/3 compatibility imports
from __future__ import print_function

# standard library imports
import json  # for working with data file
from threading import Thread
from time import sleep

# local module imports
from blinker import signal
import gv  # Get access to SIP's settings
from sip import template_render  #  Needed for working with web.py templates
from urls import urls  # Get access to SIP's URLs
import web  # web.py framework
from webpages import ProtectedPage  # Needed for security
from webpages import showInFooter # Enable plugin to display readings in UI footer
from webpages import showOnTimeline # Enable plugin to display station data on timeline

# Add new URLs to access classes in this plugin.
# fmt: off
urls.extend([
    u"/proto-sp", u"plugins.proto.settings",
    u"/proto-save", u"plugins.proto.save_settings"

    ])
# fmt: on

# Add this plugin to the PLUGINS menu ["Menu Name", "URL"], (Optional)
gv.plugin_menu.append([_(u"Proto Plugin"), u"/proto-sp"])


def empty_function():  # Only a place holder
    """
    Functions defined here can be called by classes
    or run when the plugin is loaded. See comment at end.
    """
    pass

#############################
### Data display examples ###
 
def footer_test():
    """
    Example of plugin data display in UI footer.
    Run in background thread.
    """
    example = showInFooter() #  instantiate class to enable data in footer
    example.label = u"Proto example data"
    example.val = 0
    example.unit = u" sec"
    
    while True: #  Simulate plugin data
        example.val += 2 #  update plugin data
        sleep(2)
  
# Run footer_test() in baskground thread
ft = Thread(target = footer_test)
ft.daemon = True
ft.start()

#  Example plugin data on timeline
flow1 = showOnTimeline()  #  instantiate class to enable data display
flow1.unit = u"lph"
flow1.val = 10

#  Example plugin data on timeline
flow2 = showOnTimeline()  #  instantiate class to enable data display
flow2.unit = u"Used(L)"
flow2.val = 30

# flow1.clear
# flow2.clear

#  Example new column in log
def update_log_data(name, **kw):
    log_value = 60 #  variable to hold value to be logged
    gv.logAppend[u"From proto"] = log_value

program_started = signal(u"stations_scheduled") #  blinker signal from helpers.py
program_started.connect(update_log_data) #  run update_log_data() when program starts

### Station Completed ###
def notify_station_completed(station, **kw):
    print(u"Station {} run completed".format(station))


complete = signal(u"station_completed")
complete.connect(notify_station_completed)

#########################
### class definitions ###

class settings(ProtectedPage):
    """
    Load an html page for entering plugin settings.
    """
    def GET(self):
        try:
            with open(  # Read settings from json file if it exists
                u"./data/proto.json", u"r"
            ) as f:
                settings = json.load(f)
        except IOError:  # If file does not exist return empty value
            settings = {}  # Default settings. can be list, dictionary, etc.
        return template_render.proto(settings)  # open settings page


class save_settings(ProtectedPage):
    """
    Save user input to json file.
    Will create or update file when SUBMIT button is clicked
    CheckBoxes only appear in qdict if they are checked.
    """

    def GET(self):
        qdict = (  # Dictionary of values returned as query string from settings page.
            web.input()
        )
#         print(qdict)  # - test
        with open(u"./data/proto.json", u"w") as f:  # Edit: change name of json file
            json.dump(qdict, f)  # save to file
        raise web.seeother(u"/")  # Return user to home page.


#  Run when plugin is loaded
empty_function()


