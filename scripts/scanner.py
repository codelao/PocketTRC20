import requests
import json
import sys
import colorama
from termcolor import colored
from progress.bar import IncrementalBar


def hash_scanner(hash):
    colorama.init()
    if not len(hash) == 64:
        print(colored('! Incorrect hash\n', 'red'))
        sys.exit(1)
    else:
        bar = IncrementalBar('Scanning transaction', max=7, suffix='%(percent)d%%')
        link = 'https://apilist.tronscan.org/api/transaction-info?hash=' + hash
        get_link = requests.get(link).text
        bar.next()
        check_hash = json.loads(get_link)
        bar.next()
        if check_hash == {} or check_hash == {"message":"some parameters are missing"}:
            bar.finish()
            print(colored('! Unable to get details of this transaction\n', 'red'))
            sys.exit(1)
        else:
            token_check = check_hash["contractType"]
            bar.next()
            if token_check == 31:
                usdt_status = check_hash["contractRet"]
                bar.next()
                if usdt_status == 'SUCCESS':
                    from_address_usdt = check_hash["tokenTransferInfo"]["from_address"]
                    bar.next()
                    to_address_usdt = check_hash["tokenTransferInfo"]["to_address"]
                    bar.next()
                    amount_usdt = check_hash["tokenTransferInfo"]["amount_str"]
                    bar.next()
                    bar.finish()
                    print('Transaction details:' +
                    '\nStatus: ' + usdt_status +
                    '\nFrom: ' + from_address_usdt +
                    '\nTo: ' + to_address_usdt +
                    '\nAmount: ' + str(amount_usdt)[0:-6] + ' USDT\n'
                    )
                    sys.exit(0)
                else:
                    bar.finish()
                    print('Transaction details:' +
                    '\nStatus: ' + usdt_status +
                    '\nAmount: ' + '0 USDT\n'
                    )
                    sys.exit(0)
            elif token_check == 1:
                trx_status = check_hash["contractRet"]
                bar.next()
                if trx_status == 'SUCCESS':
                    from_address_trx = check_hash["contractData"]["owner_address"]
                    bar.next()
                    to_address_trx = check_hash["contractData"]["to_address"]
                    bar.next()
                    amount_trx = check_hash["contractData"]["amount"]
                    bar.next()
                    bar.finish()
                    print('Transaction details:' +
                    '\nStatus: ' + trx_status +
                    '\nFrom: ' + from_address_trx +
                    '\nTo: ' + to_address_trx +
                    '\nAmount: ' + str(amount_trx)[0:-6] + ' TRX\n'
                    )
                    sys.exit(0)
                else:
                    bar.finish()
                    print('Transaction details:' +
                    '\nStatus: ' + trx_status +
                    '\nAmount: ' + '0 TRX\n'
                    )
                    sys.exit(0)
            else:
                bar.finish()
                print(colored('! Unable to get details of this transaction\n', 'red'))
                sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        hash = sys.argv[2]
        hash_scanner(hash)
    else:
        print(colored('! Hash wasn\'t entered\n'))
