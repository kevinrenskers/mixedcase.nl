# New site, new Django / Plone blog!
Hooray! A new site! One that actually has content! The bolhoed.net domain was a gift from a friend, about 2 years ago. I really only used it for email, but once you have a domain, you gotta have a site, right? Problem was, what to put on it? So that's why the old one was just some filler text, with one important link: my photoalbum on Flickr. It's a lot easier to tell someone to go to bolhoed.net instead of flickr.com/user/bolhoed. For those of you who've never seen the old site, [here is a screenshot](http://dl.getdropbox.com/u/2310965/bolhoednet_old.png).

But, as I got more and more annoyed with the way Flickr presents my photos, and as I got more and more into Django development, it seemed like a good idea to build my own Flickr UI with their [free API](http://www.flickr.com/services/api/). At the same time it gave me a playground to try out the [960.gs](http://g60.gs) grid css framework and the [Twitter API](http://apiwiki.twitter.com/). So, after a couple of afternoons of a lot of fun and some swearing at one Flickr API bug in particular (paginating doesn't work when using their XMLPRC service), lo and behold: a brand new site WITH content. My photos, shown the way I want and a blog. Something I said I would never do, but I guess Twitter got the ball rolling.

The main reason to start the blog was to share my short adventure hosting this site on Google Apps and Google App Engine and the problems that presented, and the problems I faced while building this site. At the same time, I come across many problems during the day when developing Django and Plone sites, and I will be blogging about them and the solutions I find.

In this post, I'd like to mention the software used to build this site:

## [Django](http://www.djangoproject.com)
An amazing framework for quickly building websites in Python. Despite a few quirks (their template language comes to mind), a joy to work with. This site uses the automatically created Admin site, the build-in comments system and Textile Markup parser.

## [Python](http://python.org)
A no-brainer, since it's a Django site after all. After working with PHP for 9 years, I made the switch to Python in September 2009, and have not regretted it. It has some weird things (all those underscores, and an import system I can't always get to work), but it's very easy to learn and very powerful. I use [Netbeans](http://www.netbeans.org) as my IDE of choice, which offers pretty good autocompletion support for Django projects, with a lot of promised improvements to come (like starting your development server, the syncdb command, and so on).

## [Python Twitter API](http://code.google.com/p/python-twitter/)
I didn't feel like parsing the JSON you get back from the API, so I used this piece of Python software to do it for me. Very easy to use, but for me a bit overkill. I might remove all the functions I don't need, like posting to Twitter using the API.

## [Python Flickr API](http://stuvel.eu/projects/flickrapi)
At first, I just used the XMLRPC interface provided by Flickr, together with ElementTree for parsing the XML response. It worked like a charm and I had absolutely no need for a Python library to do it for me, until I found out that the Flickr API has some bugs in their XMLRPC interface (paginating doesn't work for example), so I has to switch to their REST interface. I didn't feel like doing the work all over again, and came across this Python code to do it for me. And in the end, I love its ease of use and just wished I used it from the start.

## [jQuery](http://jquery.com and the "BBQ plugin":http://benalman.com/projects/jquery-bbq-plugin/)
I mainly used [prototype.js](http://www.prototypejs.org/) for many years, but made the switch to jQuery somewhere in 2008 because of all the amazing plugins. The BBQ plugin is one of those: it offers an onhashchange event, that you can use to make bookmarkable links on AJAX sites. It's used on the Photoalbum pages: every time you choose an album or click on an image, the content in loaded using AJAX. Normally, the url in your browser would stay the same, but with this plugin you can change the #hash part of the url. The beauty is that your browser will not make a new request, but the new link is bookmarkable all the same. 

## [Fluid 960.gs grid css framework](http://www.designinfluences.com/fluid960gs/)
When you want to build a fluid website that scales well, and want to use columns, check this out. It makes it very easy to quickly build your layout.

In the next post I'll talk about Google Apps and Google App Engine: what's good about it and what not, when to use it and when to avoid it.