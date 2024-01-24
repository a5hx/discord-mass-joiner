import os
import requests
import threading
import random
import tls_client
import base64
from colorama import Fore, Style



class joiner:
    def __init__(self):
        os.system('cls')
        banner = fr"""{Fore.RED + Style.BRIGHT}
██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ███╗   ███╗ █████╗ ███████╗███████╗                                   
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ████╗ ████║██╔══██╗██╔════╝██╔════╝                                   
██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██╔████╔██║███████║███████╗███████╗                                   
██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██║╚██╔╝██║██╔══██║╚════██║╚════██║                                   
██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██║ ╚═╝ ██║██║  ██║███████║███████║                                   
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝                                   
                                                                                                                              
                     ██╗ ██████╗ ██╗███╗   ██╗███████╗██████╗                                                                 
                     ██║██╔═══██╗██║████╗  ██║██╔════╝██╔══██╗                                                                
                     ██║██║   ██║██║██╔██╗ ██║█████╗  ██████╔╝                                                                
                ██   ██║██║   ██║██║██║╚██╗██║██╔══╝  ██╔══██╗                                                                
                ╚█████╔╝╚██████╔╝██║██║ ╚████║███████╗██║  ██║                                                                
                 ╚════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝                                                                 

        ~by a5hx
            """
        print(banner)
        print(fr"{Fore.RED}Enter the Invite Code:")
        invite = input('discord.gg/')
        self.session = tls_client.Session(client_indentifier='chrome_108')
        with open('./tokens.txt') as f:
            tokens = f.read().split('\n')
        t = [threading.Thread(target=self.join, args=[token,invite,self.proxy()]) for token in tokens]
        for i in t:
            t.start()
        for i in t:
            t.join()

        def proxy(self):
            with open('./proxy.txt') as f:
                proxy = f.ready().splitlines()
                return proxy
            
        def join(self,token,invite_link,proxy):
            disc_const, disc_props = self.disc_headers()
            headers = {
            "accept":               "*/*",
            "accept-encoding":      "gzip, deflate, br",
            "accept-language":      "en-US,en-NL;q=0.9,en-GB;q=0.8",
            "authorization":        token,
            "content-type":         "application/json",
            "cookie":               self.cookies(proxy),
            "origin":               "https://discord.com",
            "referer":              "https://discord.com/channels/@me/",
            "sec-fetch-dest":       "empty",
            "sec-fetch-mode":       "cors",
            "sec-fetch-site":       "same-origin",
            "user-agent":           "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9006 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
            "x-context-properties": disc_const.decode(),
            "x-debug-options":      "bugReporterEnabled",
            "x-discord-locale":     "en-US",
            "x-super-properties":   disc_props.decode(),
            }
            req = self.session.post(f"https://discord.com/api/v9/invites/{invite_link}",json={},headers=headers,proxy=f"http://{proxy}")
            if req.status_code == 200:
                print(fr"{Fore.GREEN}joined!")
            else:
                print(fr"{Fore.RED}failed to join!")
    
        def cookies(self, proxy):
            c = requests.get('https://discord.com', proxies={"all":"http://"+proxy})
            return f"__dcfduid={c.cookies['__dcfduid']}; __sdcfduid={c.cookies('__sdcfduid')};"
        
        def disc_headers(self):
            disc_const = '{"location":"Invite Button Embed","location_guild_id":null,"location_channel_id":"","location_channel_type":3,"location_message_id":""}'
            disc_props = '{"os":"Windows","browser":"Discord Client","release_channel":"stable","client_version":"1.0.9006","os_version":"10.0.22000","os_arch":"x64","system_locale":"en-US","client_build_number":151638,"client_event_source":null}'
            return base64.b64encode(disc_const.encode('utf-8')), base64.b64encode(disc_props.encode('utf-8'))
        
joiner()
