
# Project Structure
```commandline
.
├── docs
│   ├── contributing.md
│   ├── explanation.md
│   ├── how-to-guides.md
│   ├── index.md
│   ├── license.md
│   ├── reference.md
│   └── tutorials.md
├── flake8
├── LICENSE
├── mkdocs.yml
├── README.md
├── requirements.txt
├── setup.py
├── src
│   ├── common
│   │   ├── constants
│   │   │   ├── common_constants.py
│   │   │   ├── __init__.py
│   │   │   └── logging_constants.py
│   │   ├── exceptions
│   │   │   ├── __init__.py
│   │   │   └── main_exceptions.py
│   │   ├── __init__.py
│   │   ├── io_operations
│   │   │   ├── image_downloader.py
│   │   │   ├── __init__.py
│   │   │   ├── io_operations.py
│   │   │   └── request_factory.py
│   │   ├── logging
│   │   │   ├── __init__.py
│   │   │   ├── logging_setup.py
│   │   │   ├── loguru_setup.py
│   │   │   └── utils
│   │   │       ├── color_formatter.py
│   │   │       ├── __init__.py
│   │   │       ├── logging_wrappers.py
│   │   │       ├── log_rotator.py
│   │   │       ├── loguru_wrappers.py
│   │   │       └── padding_formatter.py
│   │   ├── utils
│   │   │   ├── __init__.py
│   │   │   └── string_builder.py
│   │   └── validations
│   │       ├── __init__.py
│   │       ├── parameter_validations.py
│   │       ├── reddit_api_validations.py
│   │       └── url_validations.py
│   ├── core
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   └── reddit_api.py
│   │   ├── helper
│   │   │   ├── __init__.py
│   │   │   └── main_helper.py
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── scraper
│   │       ├── comment_scraper.py
│   │       ├── __init__.py
│   │       ├── scraper_helper.py
│   │       └── thread_scraper.py
│   └── __init__.py
└── tests
          ├── acceptance
          │   └── __init__.py
          ├── __init__.py
          └── unit
              ├── core
              │   ├── __init__.py
              │   └── TestRedditApi.py
              ├── __init__.py
              └── validations
                  ├── __init__.py
                  ├── parameter_validations_test.py
                  ├── reddit_validations_test.py
                  └── url_validations_test.py

```