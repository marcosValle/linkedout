#!/usr/bin/env python3

import argparse
import getLinks

parser = argparse.ArgumentParser()
parser.add_argument("url", help="URL to parse")
parser.add_argument("-v", "--verbose", help="Displays more information",
        action="store_true")
parser.add_argument("-l", "--links", help="Print every link in the URL",
        action="store_true")
parser.add_argument("-t", "--test", help="Test for broken links",
        action="store_true")
args = parser.parse_args()

print("""
**************************************************
*  _     _       _            _  ___             *
* | |   (_)_ __ | | _____  __| |/ _ \ _   _| |_  *
* | |   | | '_ \| |/ / _ \/ _` | | | | | | | __| *
* | |___| | | | |   <  __/ (_| | |_| | |_| | |_  *
* |_____|_|_| |_|_|\_\___|\__,_|\___/ \__,_|\__| *
*                                                *
* LinkedOut Ver. 0.0.1                           *
* Coded by Marcos Valle (@__mvalle__)            *
* marcosvalle@protonmail.com                     *
**************************************************
""")

print("Check './linkedout.py -h' for help\n")

if args.links:
    baseUrl = getLinks.prepareUrl(args.url)
    print(baseUrl)
    print("[+] Collecting links...")
    links = getLinks.getRawLinks(baseUrl)
    prettyLinks = getLinks.prettifyLinks(links, baseUrl)

    if(args.verbose):
        for l in prettyLinks:
            print("\t"+l)

    if(args.test):
        print("\n[+] Testing links...")
        ok = getLinks.testLinks(prettyLinks)

        print("[+] Links ok:")
        for l in ok:
            print("\t"+l)

        if args.verbose:
            print("[-] Broken links:")
            for l in list(set(links)-set(ok)):
                print("\t"+l)
