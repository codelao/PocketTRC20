# -*- coding: utf-8 -*-

import time
import requests
import urllib.request
import json
import sys
from .config import VERSION
from progress.bar import IncrementalBar


class Scan():
    def __init__(self):
        self.bar = IncrementalBar('Scanning transaction', max=7, suffix='%(percent)d%%')

    def banner(self):
        art = '''
 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$                                      $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$  ____   ___   ____ _  _______ _____  $
$ |  _ \ / _ \ / ___| |/ / ____|_   _| $
$ | |_) | | | | |   | ' /|  _|   | |   $
$ |  __/| |_| | |___| . \| |___  | |   $
$ |_|    \___/ \____|_|\_\_____| |_|   $
$    _____ ____   ____ ____   ___      $
$   |_   _|  _ \ / ___|___ \ / _ \     $
$     | | | |_) | |     __) | | | |    $
$     | | |  _ <| |___ / __/| |_| |    $
$     |_| |_| \_|\____|_____|\___/     $
$                                      $
 $                                    $
  $               (..)               $
   $$$$$$$$                  $$$$$$$$
           $$$$$$$$$$$$$$$$$$
                 \033[1;34mby Lao\033[0m
        '''
        print(art + '         \033[34mv' + VERSION + '\033[0m')

    def check_intConnection(self):
        try:
            urllib.request.urlopen('https://google.com', timeout=1)
            return True
        except:
            return False

    def hash_scanner(self, hash):
        if self.check_intConnection() == True:
            if not len(hash) == 64:
                print('\033[31m! Incorrect hash entered\033[0m')
                sys.exit(1)
            else:
                link = 'https://apilist.tronscan.org/api/transaction-info?hash=' + hash
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
                get_link = requests.get(link, headers=headers).text
                time.sleep(0.1)
                self.bar.next()
                self.check_hash = json.loads(get_link)
                time.sleep(0.1)
                self.bar.next()
                if self.check_hash == {} or self.check_hash == {"message":"some parameters are missing"} or self.check_hash == {"riskTransaction":False}:
                    time.sleep(0.1)
                    self.bar.finish()
                    print('\033[31m! Unable to get details of this transaction\033[0m')
                    sys.exit(1)
                else:
                    token_check = self.check_hash["contractType"]
                    time.sleep(0.1)
                    self.bar.next()
                    if token_check == 31:
                        status = self.check_hash["contractRet"]
                        time.sleep(0.1)
                        self.bar.next()
                        if status == 'SUCCESS':
                            from_address = self.check_hash["tokenTransferInfo"]["from_address"]
                            time.sleep(0.1)
                            self.bar.next()
                            to_address = self.check_hash["tokenTransferInfo"]["to_address"]
                            time.sleep(0.1)
                            self.bar.next()
                            amount = self.check_hash["tokenTransferInfo"]["amount_str"]
                            time.sleep(0.1)
                            self.bar.next()
                            time.sleep(0.1)
                            self.bar.finish()
                            print(
                                '\033[32mTransaction details:\033[0m' +
                                '\nStatus: ' + status +
                                '\nFrom: ' + from_address +
                                '\nTo: ' + to_address +
                                '\nAmount: ' + str(amount)[0:-6] + ' USDT'
                            )
                            sys.exit(0)
                        else:
                            time.sleep(0.1)
                            self.bar.finish()
                            print(
                                '\033[32mTransaction details:\033[0m' +
                                '\nStatus: ' + status +
                                '\nAmount: 0 USDT'
                            )
                            sys.exit(0)
                    elif token_check == 1:
                        status = self.check_hash["contractRet"]
                        time.sleep(0.1)
                        self.bar.next()
                        if status == 'SUCCESS':
                            from_address = self.check_hash["contractData"]["owner_address"]
                            time.sleep(0.1)
                            self.bar.next()
                            to_address = self.check_hash["contractData"]["to_address"]
                            time.sleep(0.1)
                            self.bar.next()
                            amount = self.check_hash["contractData"]["amount"]
                            time.sleep(0.1)
                            self.bar.next()
                            time.sleep(0.1)
                            self.bar.finish()
                            print(
                                '\033[32mTransaction details:\033[0m' +
                                '\nStatus: ' + status +
                                '\nFrom: ' + from_address +
                                '\nTo: ' + to_address +
                                '\nAmount: ' + str(amount)[0:-6] + ' TRX'
                            )
                            sys.exit(0)
                        else:
                            time.sleep(0.1)
                            self.bar.finish()
                            print(
                                '\033[32mTransaction details:\033[0m' +
                                '\nStatus: ' + status +
                                '\nAmount: 0 TRX'
                            )
                            sys.exit(0)
                    else:
                        time.sleep(0.1)
                        self.bar.finish()
                        print('\033[31m! Unable to get details of this transaction\033[0m')
                        sys.exit(1)
        else:
            print('\033[31m! Check your internet connection\033[0m')
            sys.exit(1)