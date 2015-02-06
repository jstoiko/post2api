#!/usr/bin/env python
import json
import requests
import sys, getopt

def load(inputfile, destination):
    json_file = open(inputfile)
    json_data = json.load(json_file)

    def _jdefault(o):
        return o.__dict__

    for i in json_data:
        one = json.dumps(i, default=_jdefault)
        print('Posting: %s' % one)
        r = requests.post(destination, data=one, headers={'Content-type': 'application/json'})
        print r.status_code

    json_file.close()

def main(argv):

    try:
        opts, args = getopt.getopt(argv,'hf:u:',['help', 'file=', 'url='])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ('-f', '--file'):
            inputfile = arg
        elif opt in ('-u', '--url'):
            destination = arg

    try:
        inputfile
        destination
    except NameError:
        usage()
        sys.exit()

    load(inputfile, destination)

def usage():
    print 'Usage: ./post2api.py -f <jsonFile> -u <urlToPost>'

if __name__ == '__main__':
    main(sys.argv[1:])
