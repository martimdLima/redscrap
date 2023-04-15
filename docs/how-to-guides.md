
# Project Structure
```commandline
.  
│   
├── docs/
│   ├── explanation.md
│   ├── how-to-guides.md
│   ├── index.md
│   ├── reference.md
│   └── tutorials.md
├── flake8
├── mkdocs.yml
├── requirements.txt
├── resolv.conf
├── setup.py
├── src/
│   ├── common/
│   │   ├── common_constants.py
│   │   ├── exceptions.py
│   │   ├── image_downloader.py
│   │   ├── __init__.py
│   │   ├── io_operations.py
│   │   ├── logging/
│   │   │   ├── __init__.py
│   │   │   ├── logging_constants.py
│   │   │   ├── logging_setup.py
│   │   │   ├── loguru_setup.py
│   │   │   └── utils/
│   │   │       ├── color_formatter.py
│   │   │       ├── __init__.py
│   │   │       ├── logging_wrappers.py
│   │   │       ├── log_rotator.py
│   │   │       ├── loguru_wrappers.py
│   │   │       ├── padding_formatter.py
│   │   ├── request_manager.py
│   │   ├── string_builder.py
│   │   └── validations/
│   │       ├── __init__.py
│   │       ├── parameter_validations.py
│   │       ├── reddit_api_validations.py
│   │       └── url_validations.py
│   └── core/
│       ├── api/
│       │   ├── __init__.py
│       │   └── reddit_api.py
│       ├── helper/
│       │   ├── __init__.py
│       │   ├── main_helper.py
│       ├── __init__.py
│       ├── main.py
│       └── scraper/
│           ├── comment_scraper.py
│           ├── __init__.py
│           ├── scraper_helper.py
│           └── thread_scraper.py
│       
└── tests/
    ├── acceptance/
    │   ├── __init__.py
    ├── __init__.py
    │   
    └── unit/
        ├── core/
        │   ├── __init__.py
        │   └── TestRedditApi.py
        ├── __init__.py
        │   
        └── validations/
            ├── __init__.py
            ├── parameter_validations_test.py
            ├── reddit_validations_test.py
            └── url_validations_test.py

```