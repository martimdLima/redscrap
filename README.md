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

    Usage: redscrap [OPTIONS] COMMAND [ARGS]...
    
      Reddit Scraper
    
    Options:
      --help  Show this message and exit.
    
    Commands:
      subreddits  Scrape subreddits threads
      user        Scrape user threads

    
    Usage: redscrap subreddits [OPTIONS] [SUBREDDITS]...
    
    Scrape subreddits threads
    
    Options:
      -n, --number_results INTEGER    Number of threads to scrape
      -s, --sorting_filter [top|hot|new]
                                      Filter threads
      -d, --details                   If enable outputs the detailed list of
                                      threads of each subreddit provided into an
                                      individual file
      -o, --output TEXT               The directory to output the downloads
      -v, --verbose                   Enables verbose mode
      --help                          Show this message and exit.

    Usage: redscrap user [OPTIONS] [REDDIT_USER]...

    Scrape user threads
    
    Options:
      -n, --number_results INTEGER    Number of threads to scrape
      -s, --sorting_filter [top|hot|new]
                                      Filter threads
      -o, --output TEXT               The directory to output the downloads
      -v, --verbose                   Enables verbose mode
      --help                          Show this message and exit.


    in order to correctly run the application, the user must set this environment variables,
    that will be used to generate a token and make requests to the Reddit API
    REDDIT_API_KEY
    REDDIT_API_SECRET
    REDDIT_USERNAME
    REDDIT_PASSWORD

    If the user wants to ommit certain parameters like the sort method, the subreddits or user to
    scrape, this values can be defined by setting environment variables below with the desired values

    SUBREDDIT_SORT_METHOD
    SUBREDDITS_TO_SCRAPE
    REDDIT_USER_TO_SCRAPE

See `redscrap --help` for more command-line switches and the [documentation]
for more usage examples.


Features
--------
* Can scrape either a single subreddit or multiple subreddits or a user threads
* Validates the subreddits or user against the Reddit API to assert their validity
* User can define the amount of threads to scrape
* Downloads all the scraped images to a pre-determined directory ($HOME/Documents/output) or a directory provided by the user
* Sorts all the downloaded images by mimetype and resolution. Example: $HOME/Documents/output/downloads/subreddit/wallpaper/720p/jpeg/h5e3wklys2ua1.jpg
* Uses tqdm to display a dynamic progress bar to display the downloading and sorting processes
* Generates a detailed report of all the subreddits or user threads and their respective comments by chronological order

Development
-----------
Check [contributing.md](contributing.md) for hacking details.
