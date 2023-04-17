<!--- [![](https://i.imgur.com/kQOtbBk.png)]() -->

redscrap
====
[![redscrap on PyPI](https://img.shields.io/pypi/v/redscrap.svg?color=blue&style=for-the-badge)](https://pypi.org/project/redscrap)

A simple image scraper for Reddit. It can scrape and download images from a subreddit, subreddits or user threads and construct a detailed report of the threads and comments scraped

<!--- [**Project website**]()-->

<!---[Documentation]

[Documentation]: -->


Installation
------------

    $ pip install redscrap


Usage
-----
redscrap will accept a Python module file, package directory or an import path.

    $ redscrap [OPTIONS]

    Options:
        -n, --number_results INTEGER    Number of threads to scrape
        -x, --scrape [user|subreddits]  Scrape user or subreddit
        -s, --sorting_filter [top|hot|new]
                                        Filter threads
        -u, --reddit_user TEXT          The reddit user to search
        -r, --subreddits TEXT           The subreddit/s to search
        -d, --details                   If enable outputs the detailed list of
                                        threads of each subreddit provided into an
                                        individual file
        -o, --output TEXT               The directory to output the downloads
        -v, --verbose                   Enables verbose mode
        --help                          Show this message and exit.


See `redscrap --help` for more command-line switches and the [documentation]
for more usage examples.


Features
--------
* Can scrape either a single subreddit or multiple subreddits or a user threads
* Validates the subreddits or user agains the Reddit API to assert their validity
* User can defined the amount of threads to scrape
* Downloads all the scraped images to a pre determined directory ($HOME/Documents/output) or a directory provided by the user
* Sorts all the downloaded images by mimetype and resolution. Example: $HOME/Documents/output/downloads/subreddit/wallpaper/720p/jpeg/h5e3wklys2ua1.jpg
* Uses tqdm to display a dynamic progress bar to display the downloading and sorting processes
* Generates a detailed report of all the subreddits or user threads and their respective comments by chronological order

Development
-----------
Check [CONTRIBUTING.md](CONTRIBUTING.md) for hacking details.