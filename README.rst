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

Configuration
_____________

Kobol requires no configuration for development or build. Deploy mode requires your AWS API key and secret. These are stored in a .kobol file in your project directory::

    [S3]
    bucket: myproject
    accesskey: [YOUR ACCESS KEY]
    secretkey: [YOUR SECRET KEY]

Credits
_______

My daughter and I are writing this together. Miranda's Github is https://github.com/mirandahandley. We hope to be presenting Kobol at local meetups within a couple of months.

The name of this project is (of course) inspired by Battlestar Galactica, but the nod to Admiral Grace Hopper is also entirely intentional.
