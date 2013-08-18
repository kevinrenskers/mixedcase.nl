# A new website! What, again?
- tags: mixedCase

---

It's been 13 months since the first version of [Bolhoed.net](http://www.bolhoed.net) went online, complete with a blog. Only 9 months since the [brand new design](http://www.mixedcase.nl/articles/2010/02/19/brand-new-design-comments-reenabled/). And now not only got the site yet another design, it even got a new domain name.

## The problem

While I like the iPad layout of Bolhoed.net, it wasn't particularly great for reading articles on. The domain name is also not very international.

## Solution

I've started working on the new design on October 16. I didn't start with a Photoshop template, instead just started writing HTML and CSS code. My biggest goal was to use CSS media selectors to provide a nice layout for all screen sizes (Bolhoed.net uses Javascript to insert the right stylesheet). I also wanted text to resize properly in the browser. Lastly, I wanted the source to be semantically correct: use as few `<div>`'s as possible, instead using HTML 5 tags like `<header>`, `<footer>`, `<nav>`, `<section>` and `<article>`.

If I had to make an estimate, I think about 80 hours went into creating the template for the new website. On thursday November 4, I was happy with the design and started on the implementation. Of course I went with Django, but had to start from scratch, as the Bolhoed.net code was not usable, since it did not have any kind of CMS (almost all pages are hardcoded templates). I first looked at [Mezzanine](http://mezzanine.jupo.org/) because it has a very promising list of features. However, I didn't like some of their core design decisions. For example, the homepage is not part of the CMS pages, and as such cannot be edited.

On friday I removed all code, and again started from scratch, but now with [Django-CMS](https://github.com/divio/django-cms) and [Zinnia](https://github.com/Fantomas42/django-blog-zinnia) running the show. It was surprisingly easy to implement my templates exactly as I wanted, and the system works beautifully. I write all articles in [Markdown](http://daringfireball.net/projects/markdown/) syntax, while the other pages are written with a WYSIWYG editor.

As a bonus, this blog now offers RSS feeds, a pingback server, better date-based archives, syntax highlighting of code in articles, and remote editing of posts which I still have to try out but sounds very cool.

## Future

The site is not completely done yet. Search doesn't work, the design is not yet tested in Internet Explorer and there are no comments yet. Some templates like 404 pages are not customized yet. This should all be easy to finish up in the next couple of days.

And after that, I plan to write a lot more articles about stuff that I find interesting, like Python and iPhone development, design and usability. Having a new site where the articles are finally easy to read already made me more enthusiastic about it!

Once the site is completely done, I will put the source up on [Bitbucket](http://bitbucket.org/). Who knows, maybe someone else would like to use the same system, and see how it's all integrated.

_**Update**
Searching now works, and I think all templates are now properly done. Hooray!_

## The packages behind mixedCase.nl

* Django
* Django-CMS
* Django-blog-zinnia
* Mysql-python
* Memcached
* Gunicorn
* South
* Django-markup, Markdown and Pygments
* Django-xmlrpc
* Django-tagging
* BeautifulSoup
* PIL

Everything is installed inside virtualenv, and most packages come from PyPi. This site runs on the Nginx webserver, which proxies to Gunicorn that does the actual work of serving Django. Soon the entire website will be cached to Memcached, which can be read from Nginx thus making the hit to Gunicorn unnecessary.
