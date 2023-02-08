import requests
import json
import time
import sys
import colorama
from pyfiglet import figlet_format
from termcolor import colored, cprint


def start():
    colorama.init()
    cprint(figlet_format('CryptoScans', 'speed'), 'green')
    hash = input(colored('Enter USDT or TRX transaction hash (TRC20)\nMore info - /info\n', 'green'))
    if hash == '/info':
        info = input(colored('CryptoScans\n', 'green') + colored('Made by CodeLao\n', 'yellow') + colored('GitHub repository: https://github.com/codelao/CryptoScans\n', 'green') + colored('Go back?(yes/no)\n', 'blue'))
        if info == 'yes':
            start()
        elif info == 'no':
            sys.exit()
        else:
            print(colored('Unknown command', 'red'))
            time.sleep(1)
            sys.exit()
    else:
        link = 'https://apilist.tronscan.org/api/transaction-info?hash=' + hash
        get_link = requests.get(link).text
        check_hash = json.loads(get_link)
        if check_hash == {} or check_hash == {"message":"some parameters are missing"}:
            invalid_msg1 = input(colored('Unable to get information about this hash\nTry again?(yes/no)\n', 'red'))
            if invalid_msg1 == 'yes':
                start()
            elif invalid_msg1 == 'no':
                sys.exit()
            else:
                print(colored('Unknown command', 'red'))
                time.sleep(1)
                sys.exit()
        else:
            token_check = check_hash["contractType"]
            if token_check == 31:
                usdt_status = check_hash["contractRet"]
                if usdt_status == 'SUCCESS':
                    from_address_usdt = check_hash["tokenTransferInfo"]["from_address"]
                    to_address_usdt = check_hash["tokenTransferInfo"]["to_address"]
                    amount_usdt = check_hash["tokenTransferInfo"]["amount_str"]
                    token_usdt = 'USDT'
                    type_usdt = 'TRC20'
                    print(colored('Transaction details:', 'blue') +
                    colored('\nFrom: ', 'yellow') + colored(from_address_usdt, 'green') +
                    colored('\nTo: ', 'yellow') + colored(to_address_usdt, 'green') +
                    colored('\nAmount: ', 'yellow') + colored(str(amount_usdt), 'green') +
                    colored('\nToken: ', 'yellow') + colored(token_usdt, 'green') +
                    colored('\nType: ', 'yellow') + colored(type_usdt, 'green') +
                    colored('\nStatus: ', 'yellow') + colored(usdt_status, 'green') +
                    colored('\nClosing in 30 sec...', 'blue')
                    )
                    time.sleep(30)
                    sys.exit()
                else:
                    failed_usdt = input(colored('Failed transaction', 'red') +
                    colored('\nStatus: ', 'yellow') + colored(usdt_status, 'green') +
                    colored('\nTry again?(yes/no)\n', 'red')
                    )
                    if failed_usdt == 'yes':
                        start()
                    elif failed_usdt == 'no':
                        sys.exit()
                    else:
                        print(colored('Unknown command', 'red'))
                        time.sleep(1)
                        sys.exit()
            elif token_check == 1:
                trx_status = check_hash["contractRet"]
                if trx_status == 'SUCCESS':
                    from_address_trx = check_hash["contractData"]["owner_address"]
                    to_address_trx = check_hash["contractData"]["to_address"]
                    amount_trx = check_hash["contractData"]["amount"]
                    token_trx = 'TRX'
                    type_trx = 'TRC20'
                    print(colored('Transaction details:', 'blue') +
                    colored('\nFrom: ', 'yellow') + colored(from_address_trx, 'green') +
                    colored('\nTo: ', 'yellow') + colored(to_address_trx, 'green') +
                    colored('\nAmount: ', 'yellow') + colored(str(amount_trx), 'green') +
                    colored('\nToken: ', 'yellow') + colored(token_trx, 'green') +
                    colored('\nType: ', 'yellow') + colored(type_trx, 'green') +
                    colored('\nStatus: ', 'yellow') + colored(trx_status, 'green') +
                    colored('\nClosing in 30 sec...', 'blue')
                    )
                    time.sleep(30)
                    sys.exit()
                else:
                    failed_trx = input(colored('Failed transaction', 'red') +
                    colored('\nStatus: ', 'yellow') + colored(trx_status, 'green') +
                    colored('\nTry again?(yes/no)\n', 'red')
                    )
                    if failed_trx == 'yes':
                        start()
                    elif failed_trx == 'no':
                        sys.exit()
                    else:
                        print(colored('Unknown command', 'red'))
                        time.sleep(1)
                        sys.exit()
            else:
                invalid_msg2 = input(colored('Unable to get information about this transaction\nTry again?(yes/no)\n', 'red'))
                if invalid_msg2 == 'yes':
                    start()
                elif invalid_msg2 == 'no':
                    sys.exit()
                else:
                    print(colored('Unknown command', 'red'))
                    time.sleep(1)
                    sys.exit()


start()
