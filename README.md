<div>
    <p><a href="https://github.com/philiprbrenan/flask"><img src="https://github.com/philiprbrenan/flask/workflows/Test/badge.svg"></a>
</div>

# Test Flask

Invoke a Python script via the [Python
flask](https://flask.palletsprojects.com) web [server](https://en.wikipedia.org/wiki/Server_(computing)) running as a [GitHub](https://github.com/philiprbrenan) action.

You cannot run a production web [server](https://en.wikipedia.org/wiki/Server_(computing)) like this: but this technique does
demonstrate a compelling testing methodology to confirm the functionality of
your web pages.

The associated [GitHub](https://github.com/philiprbrenan) action starts the web [server](https://en.wikipedia.org/wiki/Server_(computing)) app in **app.py** and then
invokes [curl](https://linux.die.net/man/1/curl) to simulate [user](https://en.wikipedia.org/wiki/User_(computing)) actions on the web site. The responses to the [curl](https://linux.die.net/man/1/curl) requests are captured as [HTML](https://en.wikipedia.org/wiki/HTML) in local files. These local files can then
be checked via [automation](https://en.wikipedia.org/wiki/Automation) to confirm that they contain the expected content.
