#---------------------------------------
#	Import Libraries
#---------------------------------------
import clr, codecs, json, os, re, sys
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

import sqlite3

#---------------------------------------
#	[Required]	Script Information
#---------------------------------------
ScriptName = "TwitchCharity"
Website = "https://twitch.tv/digitalnyc"
Creator = "digitalnyc"
Version = "1.0.0"
Description = "Script which listens for Twitch #charity donation messages and creates a command to display the latest message in chat"
settingsFile = os.path.join(os.path.dirname(__file__), "settings.json")

#---------------------------------------
#   Version Information
#---------------------------------------

class Settings:
	def __init__(self, settingsFile = None):
		if settingsFile is not None and os.path.isfile(settingsFile):
			with codecs.open(settingsFile, encoding='utf-8-sig',mode='r') as f:
				self.__dict__ = json.load(f, encoding='utf-8-sig') 
		else:
			self.Enabled = True
            
	def ReloadSettings(self, data):
		self.__dict__ = json.loads(data, encoding='utf-8-sig')
		return

	def SaveSettings(self, settingsFile):
		with codecs.open(settingsFile,  encoding='utf-8-sig',mode='w+') as f:
			json.dump(self.__dict__, f, encoding='utf-8-sig')
		with codecs.open(settingsFile.replace("json", "js"), encoding='utf-8-sig',mode='w+') as f:
			f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8-sig')))
		return

#---------------------------------------
# Initialize Data on Load
#---------------------------------------
def Init():
	global MySettings, messageFile
	MySettings = Settings(settingsFile)
	messageFile = os.path.join(os.path.dirname(__file__), "TwitchCharity.txt")
	return

#---------------------------------------
# Reload Settings on Save
#---------------------------------------
def ReloadSettings(jsonData):
	global MySettings
	MySettings.ReloadSettings(jsonData)
	return

def Execute(data):
	match = re.search(r'msg-id=charity;.*(?<=system-msg=)(.*?)(?=;)', data.RawData)
	if match:
		message = re.sub(r"\\s", ' ', match.group(1))
		with codecs.open(messageFile, encoding='utf-8-sig',mode='w+') as f:
			f.write(message)
	if MySettings.Enabled and data.IsChatMessage() and data.GetParam(0).lower() == MySettings.Command:
		if os.path.isfile(messageFile):
			with codecs.open(messageFile, encoding='utf-8-sig',mode='r') as f:
				message = f.read()
				Parent.SendTwitchMessage(MySettings.Format.format(message))
		return
	return
	
def Tick():
	return

def UpdateSettings():
	with open(m_ConfigFile) as ConfigFile:
		MySettings.__dict__ = json.load(ConfigFile)
	return
