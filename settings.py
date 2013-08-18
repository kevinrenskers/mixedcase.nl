# -*- coding: utf-8 -*-
#: settings for liquidluck

from datetime import date


site = {
    "name": "mixedCase.nl",
    "url": "http://mixedcase.nl",
    "prefix": "articles",
    "feed": "/articles/feed.xml",
    "date": date.today(),
}

config = {
    "source": "content",
    "output": "deploy",
    "static": "deploy/static",
    "static_prefix": "/static/",
    "permalink": "{{date.year}}/{{date.month}}/{{date.day}}/{{slug}}/index.html",
    "relative_url": False,
    "perpage": 5,
    "feedcount": 20,
    "timezone": "+00:00",
}

author = {
    "default": "kevin",
    "vars": {
        "kevin": {
            "name": "Kevin Renskers",
            "email": "info@mixedcase.nl",
        }
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
        "liquidluck.writers.core.TagWriter",
    ],
    "vars": {
        "archive_output": "articles/index.html",
        "archive_feed_output": "articles/feed.xml",
        "year_template": "year.html",
        "tag_template": "tag.html",
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
            {'title': 'FAQ', 'link': 'faq'},
            {'title': 'Support / contact', 'link': 'support'},
        ]
    }
}
