import configparser
from pathlib import Path

cfgFile = 'qa.ini'
cfgFileDirectory = 'config'

# Here, we initialise the configparser module, and will use the config variable to read the config file.
config = configparser.ConfigParser()


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(cfgFile)

config.read(CONFIG_FILE)

def getGmailUrl():
    return config['gmail']['url']

def getGmailUsr():
    return config['gmail']['user']

def getGmailPass():
    return config['gmail']['pass']

def getOutlookUrl():
    return config['outlook']['url']

def getOutlookUsr():
    return config['outlook']['user']

def getOutlookPass():
    return config['outlook']['pass']


