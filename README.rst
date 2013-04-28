kobol
=====

A static site generator in Python

This project is under active development, but is in no way ready for use. Feel free to look around, give it a star if you're interested in it, and check back later to see if it's ready for use. It's not a large project, so we should be ready soon.

Installation
____________

Kobol will be hosted at PyPi, so installation will be::

    pip install kobol

Usage
_____

Kobol has three modes, development, build, and deploy.

Development
-----------

Kobol has a built-in webserver and will run in development mode, serving your pages dynamically without requiring a build::

    cd myproject
    kobol

Build
-----

Kobol will build all of your pages and deposit them neatly in a build directory::

    cd myproject
    kobol build

Deploy
------

Kobol is designed in the first iteration to deploy to an S3 bucket, which combined with Route53 can be used to host a site without a server::

    cd myproject
    kobol deploy s3

Future features will likely include other deployment options.

First run
---------

When kobol is run in development mode, it will check for the existence of a '.kobol' configuration file. If it finds one, it will use the configuration given - or the default configuration if the .kobol file is empty. If no .kobol file is present, it will scaffold the project by creating the directories and files typically used by a kobol web project::

    .kobol
    pages/
    articles/
    assets/
    themes/
      kobol/
        site.css
        site.js
    templates/
      kobol/
        base.html
        index.html
        page.html
        article.html
        articles.html
        feed.xml

If a .kobol file is not present, Kobol *will* overwrite existing files, but only the only files kobol provides are its own theme files. If a .kobol file is present, it won't create any files or directories.

Information Architecture
________________________

Kobol makes some assumptions about the locations of your content, and expects it to be organized on the file system the same way it will be organized on the website.

Pages are static content that are not organized by time. Kobol will look for them by default in a 'pages' subdirectory, and they can be nested. Pages will be presented on the site nested just as they are in the file system and kobol will always render the pages menu as a nested unordered list. Pages will also be linked at addresses matching their location under the pages subdirectory. For example, 'myproject/pages/about/careers' will be linked at 'about/careers'.

Articles are content that is organized and presented by time. Kobol will look for them by default in an 'articles' subdirectory, but they are not nested. Articles will be presented on a article navigation page within an <article> element, with each pagetitle in a <header> element and linking to the article page. Articles are always organized by the published date in reverse chronological order (most recent articles first). Articles will be linked under the articles section. For example, an article saved on the file system as 'why_i_love_kobol' will be linked at 'articles/why_i_love_kobol'.

The semantic HTML is created using Jinja2 (http://jinja.pocoo.org/docs/) templates that can be modified to suit your individual needs. They are stored under the 'templates' directory organized by theme. Styling for each theme is stored under the 'themes' directory, also organized by theme. Kobol comes with one theme called 'kobol', which is defined by the templates under 'templates/kobol' and styles under 'themes/kobol'.

Content
_______

Content is defined in text files, one file per page or article.

The name of the file on the filesystem will also be the name of the file in the URL. For example, 'pages/about' on the filesystem will be available at 'http://mydomain.tld/about', and 'articles/why_i_hate_kobol' will be at 'http://mydomain.tld/articles/why_i_hate_kobol'.

Individual files are organized in a "YAML over Markdown" structure that's very easy to use.

    * A header block is written in YAML and defines some metadata about the document. Any metadata placed here will be available to the template, so put anything you may wish to use in this block. Some values are expected, and they're described below.
    * A blank line separates the metadata from the content.
    * The rest of the file is content, and it's written in Markdown. Kobol supports standard markdown plus footnotes and code highlighting.

The expected metadata in the YAML section are:

    * pagetitle: The <h1> title for the page. Used by both pages and articles.
    * longtitle: A description of the page. Used by both pages and articles.
    * menuindex: The position of this page in the menu. Used by pages.
    * published: The published date of the article. Used by articles.
    * excerpt: An excerpt, summary, introduction, or abstract for the article. Used by articles.
    * tags: A list of tag words or categories that describe the article. Used by articles.

Metadata are used by templates to create web pages and navigation elements, and because you can create your own templates, you can use any metadata you'd like to add. For example, if your site has more than one author, you might wish to include a byline on each article specifying the author's name and email address. To include this information, simply add more variables in the metadata section of the file, and add a byline to your article template.

Configuration
_____________

Kobol requires no custom configuration for development or build. Kobol's default configuration is::

    { 'kobol': {
      'theme': 'kobol',
      'pages': [ 'pages' ],
      'articles': [ 'articles' ],
      'assets': [ 'assets' ],
      'templates': [ 'templates' ],
      'deploy': [ 'build': { 'build'} ]
    }}

These defaults will be used regardless of whether the settings are present in the configuration file. You can specify alternatives in the .kobol configuration file. Alternatives are used only if the settings are present and specify different values.

Many default settings can be overridden::

    { 'kobol': {
      ...
      'theme': 'mytheme',
      'pages': [ 'mypages' ],
      'articles': [ 'myposts' ],
      'assets': [ 'myassets' ],
      'templates': [ 'mytemplates' ],
      ...
    }}

Deployment will, by default, only build the site locally. Deploying to AWS S3 requires your AWS API key and secret. These are also stored in .kobol configuration file::

    { 'kobol': {
      ...
      'deploy': [
        's3': {
          'bucket': 'myproject',
          'accesskey': 'YOUR ACCESS KEY',
          'secretkey': 'YOUR SECRET KEY'
        },
      ...
    }}

The current version of kobol supports deployment to AWS S3 buckets. Future versions will likely provide other deployment options.

Credits
_______

My daughter and I are writing this together. Miranda's Github is https://github.com/mirandahandley. We hope to be presenting Kobol within a couple of months.

The name of this project is (of course) inspired by Battlestar Galactica, but the nod to Admiral Grace Hopper is also entirely intentional.
