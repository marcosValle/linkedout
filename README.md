# linkedOut
OSINT tool for searching information on a web page with python3.

## Dependencies
To install the dependencies:

    pip install -r requirements.txt
  
## Usage
~~~
usage: linkedOut.py [-h] [-v] [-l] [-t] url

positional arguments:
  url            URL to parse

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Displays more information
  -l, --links    Print every link in the URL
  -t, --test     Test for broken links
~~~

## Example
~~~
$ ./linkedOut.py http://www.iitk.ac.in/cc/personalhomepage.html --links -v

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

Check './linkedout.py -h' for help

http://www.iitk.ac.in/cc/personalhomepage.html
[+] Collecting links...
Total links: 6
	http://www.iitk.ac.in/cc/homepage
	http://www.iitk.ac.in/cc/coolmenus4.js
	http://www.iitk.ac.in/cc/bannerdesign_july.jpg
	http://www.iitk.ac.in/cc/#topmenu
	http://www.iitk.ac.in/cc/menu.js
	http://www.iitk.ac.in/cc/picture/bullut.gif
~~~

## Contributing
No requiremets! Feel free to help :)

## DISCLAIMER
This tool is being developed. No guarantees are provided.
