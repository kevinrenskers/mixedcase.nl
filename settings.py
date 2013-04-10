# -*- coding: utf-8 -*-
#: settings for liquidluck

from datetime import date


site = {
    "name": "mixedCase.nl",
    "url": "http://mixedcase.nl",
    "prefix": "articles",
    "date": date.today(),
}

config = {
    "source": "content",
    "output": "deploy",
    "static": "deploy/static",
    "static_prefix": "/static/",
    "permalink": "{{date.year}}/{{date.month}}/{{date.day}}/{{slug}}/index.html",
    "relative_url": False,
    "perpage": 300000,
    "feedcount": 20,
    "timezone": "+00:00",
}

author = {
    "default": "kevin",
    "vars": {
        "name": "Kevin Renskers",
        "email": "info@mixedcase.nl",
        "twitter": "mixedCase",
    }
}

reader = {
    "active": [
        "markdown.MarkdownReader",
    ],
}

writer = {
    "active": [
        "liquidluck.writers.core.PostWriter",
        "liquidluck.writers.core.PageWriter",
        "liquidluck.writers.core.ArchiveWriter",
        "liquidluck.writers.core.ArchiveFeedWriter",
        "liquidluck.writers.core.FileWriter",
        "liquidluck.writers.core.StaticWriter",
        "liquidluck.writers.core.YearWriter",
        #"liquidluck.writers.core.CategoryWriter",
        #"liquidluck.writers.core.CategoryFeedWriter",
    ],
    "vars": {
        "archive_output": "articles/index.html",
        "year_template": "year.html",
    }
}

theme = {
    "name": "mixedcase",
    "vars": {
        "analytics": "UA-11162625-2",
        'navigation': [
            {'title': 'Home', 'link': '/'},
            {'title': 'Articles', 'link': '/articles/'},
            {'title': 'Projects', 'link': '/projects/'},
            {'title': 'Apps', 'link': '/apps/'},
            {'title': 'About', 'link': '/about/'},
        ],
        'dmmjobcontrol_pages': [
            {'title': 'Introduction', 'link': 'index'},
            {'title': 'Users manual', 'link': 'users'},
            {'title': 'Administration', 'link': 'admins'},
            {'title': 'Configuration', 'link': 'config'},
            {'title': 'Extending JobControl', 'link': 'extending'},
            {'title': 'Contribute', 'link': 'contribute'},
            {'title': 'FAQ', 'link': 'faq'},
            {'title': 'Support / contact', 'link': 'support'},
        ]
    }
}
