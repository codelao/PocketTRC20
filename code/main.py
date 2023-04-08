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
from pyfiglet import figlet_format
from termcolor import colored, cprint
from progress.bar import IncrementalBar


class App:
    def __init__(self):
        self.main()

    def main(self):
        colorama.init()
        cprint(figlet_format('Crypto Scans', 'speed'), 'green')
        self.hash = input(colored('Enter USDT or TRX transaction hash (TRC20)\nMore info - /info\n', 'green'))
        if self.hash == '/info':
            self.info = input(colored('Crypto Scans\n', 'green') + colored('by Lao\n', 'yellow') + colored('GitHub repository: https://github.com/codelao/CryptoScans\n', 'green') + colored('Go back?(yes/no)\n', 'blue'))
            if self.info == 'yes':
                self.main()
            elif self.info == 'no':
                sys.exit()
            else:
                print(colored('Unknown command', 'red'))
                time.sleep(1)
                sys.exit()
        elif not len(self.hash) == 64:
            self.wrong_hash = input(colored('Incorrect hash\nTry again?(yes/no)\n', 'red'))
            if self.wrong_hash == 'yes':
                self.main()
            elif self.wrong_hash == 'no':
                sys.exit()
            else:
                print(colored('Unknown command', 'red'))
                time.sleep(1)
                sys.exit()
        else:
            self.bar = IncrementalBar(colored('Scanning transaction', 'blue'), max=8, suffix='%(percent)d%%')
            self.link = 'https://apilist.tronscan.org/api/transaction-info?hash=' + self.hash
            self.get_link = requests.get(self.link).text
            self.bar.next()
            self.check_hash = json.loads(self.get_link)
            self.bar.next()
            if self.check_hash == {} or self.check_hash == {"message":"some parameters are missing"}:
                self.bar.finish()
                self.invalid_msg = input(colored('Unable to get information about this hash\nTry again?(yes/no)\n', 'red'))
                if self.invalid_msg == 'yes':
                    self.main()
                elif self.invalid_msg == 'no':
                    sys.exit()
                else:
                    print(colored('Unknown command', 'red'))
                    time.sleep(1)
                    sys.exit()
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
                        self.token_usdt = 'USDT'
                        self.type_usdt = 'TRC20'
                        self.bar.next()
                        self.bar.finish()
                        print(colored('Transaction details:', 'blue') +
                        colored('\nStatus: ', 'yellow') + colored(self.usdt_status, 'green') +
                        colored('\nFrom: ', 'yellow') + colored(self.from_address_usdt, 'green') +
                        colored('\nTo: ', 'yellow') + colored(self.to_address_usdt, 'green') +
                        colored('\nAmount: ', 'yellow') + colored(str(self.amount_usdt)[0:-6], 'green') +
                        colored('\nToken: ', 'yellow') + colored(self.token_usdt, 'green') +
                        colored('\nType: ', 'yellow') + colored(self.type_usdt, 'green') +
                        colored('\nReturning in 30 seconds...', 'red')
                        )
                        time.sleep(30)
                        self.main()
                    else:
                        self.bar.finish()
                        self.failed_usdt = input(colored('Failed transaction', 'red') +
                        colored('\nStatus: ', 'yellow') + colored(self.usdt_status, 'green') +
                        colored('\nTry again?(yes/no)\n', 'red')
                        )
                        if self.failed_usdt == 'yes':
                            self.main()
                        elif self.failed_usdt == 'no':
                            sys.exit()
                        else:
                            print(colored('Unknown command', 'red'))
                            time.sleep(1)
                            sys.exit()
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
                        self.token_trx = 'TRX'
                        self.type_trx = 'TRC20'
                        self.bar.next()
                        self.bar.finish()
                        print(colored('Transaction details:', 'blue') +
                        colored('\nStatus: ', 'yellow') + colored(self.trx_status, 'green') +
                        colored('\nFrom: ', 'yellow') + colored(self.from_address_trx, 'green') +
                        colored('\nTo: ', 'yellow') + colored(self.to_address_trx, 'green') +
                        colored('\nAmount: ', 'yellow') + colored(str(self.amount_trx)[0:-6], 'green') +
                        colored('\nToken: ', 'yellow') + colored(self.token_trx, 'green') +
                        colored('\nType: ', 'yellow') + colored(self.type_trx, 'green') +
                        colored('\nReturning in 30 seconds...', 'red')
                        )
                        time.sleep(30)
                        self.main()
                    else:
                        self.bar.finish()
                        self.failed_trx = input(colored('Failed transaction', 'red') +
                        colored('\nStatus: ', 'yellow') + colored(self.trx_status, 'green') +
                        colored('\nTry again?(yes/no)\n', 'red')
                        )
                        if self.failed_trx == 'yes':
                            self.main()
                        elif self.failed_trx == 'no':
                            sys.exit()
                        else:
                            print(colored('Unknown command', 'red'))
                            time.sleep(1)
                            sys.exit()
                else:
                    self.bar.finish()
                    self.invalid_msg = input(colored('Unable to get information about this transaction\nTry again?(yes/no)\n', 'red'))
                    if self.invalid_msg == 'yes':
                        self.main()
                    elif self.invalid_msg == 'no':
                        sys.exit()
                    else:
                        print(colored('Unknown command', 'red'))
                        time.sleep(1)
                        sys.exit()

if __name__ == '__main__':
    App()