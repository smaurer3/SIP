#!/usr/bin/python
# encoding: utf-8

# standard library imports
import gettext
import json
import locale
import os
import sys

__author__ = "Dan"

try:
    with open("./data/sd.json", "r") as sdf:
        sd_temp = json.load(sdf)
except:
    pass

try:
    sd_lang = sd_temp["lang"]
except:
    sd_lang = "default"

languages = {
    "en_US": "English",
    "af_AF": "Afrikaans",
    "ar_SA": "Arabic",
    "cs_CZ": "Czech",
    "fr_FR": "French",
    "de_DE": "German",
    "gr_GR": "Greek",
    "it_IT": "Italian",
    "pl_PL": "Polish",
    "pt_PT": "Portuguese",
    "sl_SL": "Slovenian",
    "es_ES": "Spanish",
    "ta_TA": "Tamil",
}


def get_system_lang():
    """Return default system locale language"""
    lc, encoding = locale.getdefaultlocale()
    if lc:
        return lc
    else:
        return None


# File location directory.
curdir = os.path.abspath(os.path.dirname(__file__))

# i18n directory.
localedir = curdir + "/i18n"

gettext.install("sip_messages", localedir)

sys_lang = get_system_lang()

if sd_lang == "default":
    if sys_lang in languages:
        ui_lang = sys_lang
    else:
        ui_lang = "en_US"
else:
    ui_lang = sd_lang

try:
    install_kwargs = {}
    if sys.version_info.major == 2:
        install_kwargs['unicode'] = True
    gettext.translation("sip_messages", localedir, languages=[ui_lang]).install(**install_kwargs)
except IOError:
    pass
