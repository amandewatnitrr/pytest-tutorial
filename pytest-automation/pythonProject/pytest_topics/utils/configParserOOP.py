import configparser
from pathlib import Path

from setuptools.command.setopt import config_file


class ConfigParser():

    cfgFile = 'qa.ini' # default config file
    cfgFileDirectory = 'config' # config directory

    config = configparser.ConfigParser()

    # Next, we will start by creating a constructor for the clas
    def __init__(self, cfg=cfgFile):
        self.cfgFile = cfg
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.CONFIG_FILE = self.BASE_DIR.joinpath(self.cfgFileDirectory).joinpath(self.cfgFile)
        self.config.read(self.CONFIG_FILE)

    def getGmailUrl(self):
        return self.config['gmail']['url']


    def getGmailUsr(self):
        return self.config['gmail']['user']


    def getGmailPass(self):
        return self.config['gmail']['pass']


    def getOutlookUrl(self):
        return self.config['outlook']['url']


    def getOutlookUsr(self):
        return self.config['outlook']['user']


    def getOutlookPass():
        return config['outlook']['pass']