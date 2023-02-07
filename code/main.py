import requests
import json
import time
import sys
import pyfiglet


def start():
    print(pyfiglet.figlet_format(text='CryptoScans', font='speed'))
    hash = input('Enter usdt trc20 transaction hash\nMore info - /info\n')
    if hash == '/info':
        info = input('CryptoScans\nMade by CodeLao\nGitHub repository: https://github.com/codelao/CryptoScans\nGo back?(yes/no)\n')
        if info == 'yes':
            start()
        elif info == 'no':
            sys.exit()
        else:
            print('Unknown command')
            time.sleep(3)
            sys.exit()
    else:
        link = 'https://apilist.tronscan.org/api/transaction-info?hash=' + hash
        get_link = requests.get(link).text
        check_hash = json.loads(get_link)
        if check_hash == {} or check_hash == {"message":"some parameters are missing"}:
            invalid_msg1 = input('Invalid hash or network\nTry again?(yes/no)\n')
            if invalid_msg1 == 'yes':
                start()
            elif invalid_msg1 == 'no':
                sys.exit()
            else:
                print('Unknown command')
                time.sleep(3)
                sys.exit()
        else:
            usdt_check = check_hash["contractType"]
            if usdt_check == 31:
                status = check_hash["contractRet"]
                if status == 'SUCCESS':
                    from_address = check_hash["tokenTransferInfo"]["from_address"]
                    to_address = check_hash["tokenTransferInfo"]["to_address"]
                    amount = check_hash["tokenTransferInfo"]["amount_str"]
                    token = check_hash["tokenTransferInfo"]["symbol"]
                    to_address = check_hash["tokenTransferInfo"]["to_address"]
                    from_address = check_hash["tokenTransferInfo"]["from_address"]
                    print('Transaction details:'
                    '\nFrom: ' + from_address + 
                    '\nTo: ' + to_address + 
                    '\nAmount: ' + amount +
                    '\nToken: ' + token +
                    '\nNetwork: ' + 'TRC20'
                    '\nStatus: ' + status
                    )
                    time.sleep(30)
                    sys.exit()
                else:
                    print('Transaction details:'
                    '\nStatus: ' + status
                    )
                    time.sleep(30)
                    sys.exit()
            else:
                invalid_msg2 = input('Invalid token\nTry again?(yes/no)\n')
                if invalid_msg2 == 'yes':
                    start()
                elif invalid_msg2 == 'no':
                    sys.exit()
                else:
                    print('Unknown command')
                    time.sleep(3)
                    sys.exit()


start()