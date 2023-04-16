#_________                        ___       
#__  ____/___________  _________ /  /______ 
#_  /    __  ___/_  / / /__  __ \  __/  __ \
#/ /___  _  /   _  /_/ /__  /_/ / /_ / /_/ /
#\____/  /_/    _\__, / _  .___/___/ \____/ 
#               /____/  /_/                 
#________                           
#  _____/___________ _______________
#_____ \_  ___/  __ `/_  __ \_  ___/
#____/ // /__ / /_/ /_  / / /(__  ) 
#_____/ \___/ \__,_/ /_/ /_//____/
#
# by Lao


import requests
import json
import time
import sys
import colorama
from urllib.request import urlopen
from pyfiglet import figlet_format
from termcolor import colored, cprint
from progress.bar import IncrementalBar


class App:
    def __init__(self):
        self.check_internet_connection()
        self.main()

    def check_internet_connection(self):
        try:
            urlopen('https://google.com')
            return True
        except:
            return False

    def main(self):
        colorama.init()
        cprint(figlet_format('Crypto Scans', 'speed'), 'green')
        self.hash = input(colored('Enter TRC20 transaction hash\nMore info - /info\n', 'blue'))
        if self.hash == '/info':
            self.info = input(colored('Crypto Scans\n', 'green') + colored('by Lao\n', 'yellow') + colored('GitHub repository: https://github.com/codelao/CryptoScans\n', 'green') + colored('Go back?(yes/no)\n', 'blue'))
            if self.info == 'yes':
                self.main()
            elif self.info == 'no':
                sys.exit()
            else:
                print(colored('Unknown command', 'red'))
                time.sleep(1)
                self.main()
        elif not len(self.hash) == 64:
            self.wrong_hash = input(colored('Incorrect hash\nTry again?(yes/no)\n', 'red'))
            if self.wrong_hash == 'yes':
                self.main()
            elif self.wrong_hash == 'no':
                sys.exit()
            else:
                print(colored('Unknown command', 'red'))
                time.sleep(1)
                self.main()
        else:
            if self.check_internet_connection() == True:
                self.bar = IncrementalBar(colored('Scanning transaction', 'blue'), max=7, suffix='%(percent)d%%')
                self.link = 'https://apilist.tronscan.org/api/transaction-info?hash=' + self.hash
                self.get_link = requests.get(self.link).text
                self.bar.next()
                self.check_hash = json.loads(self.get_link)
                self.bar.next()
                if self.check_hash == {} or self.check_hash == {"message":"some parameters are missing"}:
                    self.bar.finish()
                    self.hash_error = input(colored('Unable to get details of this transaction\nTry again?(yes/no)\n', 'red'))
                    if self.hash_error == 'yes':
                        self.main()
                    elif self.hash_error == 'no':
                        sys.exit()
                    else:
                        print(colored('Unknown command', 'red'))
                        time.sleep(1)
                        self.main()
                else:
                    self.token_check = self.check_hash["contractType"]
                    self.bar.next()
                    if self.token_check == 31:
                        self.usdt_status = self.check_hash["contractRet"]
                        self.bar.next()
                        if self.usdt_status == 'SUCCESS':
                            self.from_address_usdt = self.check_hash["tokenTransferInfo"]["from_address"]
                            self.bar.next()
                            self.to_address_usdt = self.check_hash["tokenTransferInfo"]["to_address"]
                            self.bar.next()
                            self.amount_usdt = self.check_hash["tokenTransferInfo"]["amount_str"]
                            self.bar.next()
                            self.bar.finish()
                            self.result_usdt = input(colored('Transaction details:', 'blue') +
                            colored('\nStatus: ', 'yellow') + colored(self.usdt_status, 'green') +
                            colored('\nFrom: ', 'yellow') + colored(self.from_address_usdt, 'green') +
                            colored('\nTo: ', 'yellow') + colored(self.to_address_usdt, 'green') +
                            colored('\nAmount: ', 'yellow') + colored(str(self.amount_usdt)[0:-6] + ' USDT', 'green') +
                            colored('\nGo back?(yes/no)\n', 'blue')
                            )
                            if self.result_usdt == 'yes':
                                self.main()
                            elif self.result_usdt == 'no':
                                sys.exit()
                            else:
                                print(colored('Unknown command', 'red'))
                                time.sleep(1)
                                self.main()
                        else:
                            self.bar.finish()
                            self.failed_usdt = input(colored('Transaction details:', 'blue') +
                            colored('\nStatus: ', 'yellow') + colored(self.usdt_status, 'red') +
                            colored('\nAmount: ', 'yellow') + colored('0 USDT', 'red') +
                            colored('\nGo back?(yes/no)\n', 'blue')
                            )
                            if self.failed_usdt == 'yes':
                                self.main()
                            elif self.failed_usdt == 'no':
                                sys.exit()
                            else:
                                print(colored('Unknown command', 'red'))
                                time.sleep(1)
                                self.main()
                    elif self.token_check == 1:
                        self.trx_status = self.check_hash["contractRet"]
                        self.bar.next()
                        if self.trx_status == 'SUCCESS':
                            self.from_address_trx = self.check_hash["contractData"]["owner_address"]
                            self.bar.next()
                            self.to_address_trx = self.check_hash["contractData"]["to_address"]
                            self.bar.next()
                            self.amount_trx = self.check_hash["contractData"]["amount"]
                            self.bar.next()
                            self.bar.finish()
                            self.result_trx = input(colored('Transaction details:', 'blue') +
                            colored('\nStatus: ', 'yellow') + colored(self.trx_status, 'green') +
                            colored('\nFrom: ', 'yellow') + colored(self.from_address_trx, 'green') +
                            colored('\nTo: ', 'yellow') + colored(self.to_address_trx, 'green') +
                            colored('\nAmount: ', 'yellow') + colored(str(self.amount_trx)[0:-6] + ' TRX', 'green') +
                            colored('\nGo back?(yes/no)\n', 'blue')
                            )
                            if self.result_trx == 'yes':
                                self.main()
                            elif self.result_trx == 'no':
                                sys.exit()
                            else:
                                print(colored('Unknown command', 'red'))
                                time.sleep(1)
                                self.main()
                        else:
                            self.bar.finish()
                            self.failed_trx = input(colored('Transaction details:', 'blue') +
                            colored('\nStatus: ', 'yellow') + colored(self.trx_status, 'red') +
                            colored('\nAmount: ', 'yellow') + colored('0 TRX', 'red') +
                            colored('\nGo back?(yes/no)\n', 'blue')
                            )
                            if self.failed_trx == 'yes':
                                self.main()
                            elif self.failed_trx == 'no':
                                sys.exit()
                            else:
                                print(colored('Unknown command', 'red'))
                                time.sleep(1)
                                self.main()
                    else:
                        self.bar.finish()
                        self.token_error = input(colored('Unable to get details of this transaction\nTry again?(yes/no)\n', 'red'))
                        if self.token_error == 'yes':
                            self.main()
                        elif self.token_error == 'no':
                            sys.exit()
                        else:
                            print(colored('Unknown command', 'red'))
                            time.sleep(1)
                            self.main()
            else:
                print(colored('Check your internet connection', 'red'))
                time.sleep(1)
                sys.exit()


if __name__ == '__main__':
    App()