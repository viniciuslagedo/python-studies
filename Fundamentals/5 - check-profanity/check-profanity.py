import urllib

def read_text():
    quotes = open('D:\Projects\GitHub\python-studies\Fundamentals\/5 - check-profanity\quotes.txt')
    content = quotes.read()
    print(content)
    quotes.close()
    check_profanity(content)

def check_profanity(text_to_check):
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=shot' + text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if 'true' in output:
        print('Curse word founded !')
    elif 'false' in output:
        print('No curse word !')
    else:
        print('Cant Scan !')

read_text()