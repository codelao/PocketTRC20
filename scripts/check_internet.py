from urllib.request import urlopen


def check_internet_connection(self):
        try:
            urlopen('https://google.com')
            return True
        except:
            return False
