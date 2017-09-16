# TwitchCharity
A small AnkhBot R2 Python script which monitors Twitch channel chat for #charity system messages.  The message is stored in TwitchChat.txt in the script's folder.  The script adds a command called !twitchcharity (by default) which will displays the contents of the TwitchChat.txt file, if it exists.

Sample system message in Twitch IRC:
@badges=;color=#8A2BE2;display-name=Twitch;emotes=;id=d694a485-eaea-4e96-ad53-0cbd38fb8494;login=twitch;mod=0;msg-id=charity;room-id=138909053;subscriber=0;system-msg=$83,687\stotal\sraised\sso\sfar\sfor\sExtra\sLife!\s3\smore\sdays\sto\sshow\ssupport.\sCheer\sand\sinclude\s#charity.\sLearn\sMore\sat\slink.twitch.tv/cheer4kids;tmi-sent-ts=1505525623789;turbo=0;user-id=12826;user-type= :tmi.twitch.tv USERNOTICE #twitch
