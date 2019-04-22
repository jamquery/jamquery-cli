"""
Jamquery CLI - Easily add/manage links

Usage:
    jamquery (-t | -d | -n | -a) <keyword>
    jamquery add <tags> <name> <url>
    jamquery -h | --help
    jamquery --version

Arguments:
    keyword     Searching keyword.
    tags        Comma-separated list of tags. (e.g. python,testing)
    name        Name of new jamquery. Put it in quotes if you want to include some spaces.
    url         URL of new jamquery. No space is allowed.

Options:
    -h --help   Show this screen.
    --version   Show version.
    -t, --tag   Search in tags.
    -d, --date  Search in dates.
    -n, --name  Search in names.
    -a, --all   Search for all fields.
"""
from docopt import docopt, DocoptExit
import requests

VERSION = "0.1.0"
URL = "http://jamquery.turastory.com/api"

def search(keyword):
    r = requests.get(f"{URL}/name/{keyword}")
    if r.status_code == 200:
        jamqueries = r.json()
        for jamquery in jamqueries:
            print(f"{jamquery['name']} - {jamquery['content']}")
    else:
        print(f"Error: {r.text}")

def parse_tags(tags):
    return [n.strip().lower() for n in tags.split(',')]

def add(tag_list, name, url):
    post_data = {'tags': tag_list, 'name': name, 'url': url}
    r = requests.post(f"{URL}", json=post_data)
    if r.status_code == 200:
        print(f"Add jamquery success with id: {r.json()['id']}")
    else:
        print(f"Error: {r.text}")
    pass

if __name__ == "__main__":
    arguments = docopt(__doc__, version=VERSION)

    if arguments['add']:
        tags = arguments['<tags>']
        name = arguments['<name>']
        url = arguments['<url>']
        if tags == None or name == None or url == None:
            print("Arguments are needed")
        else:
            add(parse_tags(tags), name, url)
    else:
        # TODO: various search for various options
        keyword = arguments['<keyword>']
        search(keyword)
