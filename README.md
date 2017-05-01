# <img src="https://github.com/johncoleman83/mini-tweet-bot/blob/master/static/images/anonymousface.png" width="160" height="160" /> mini tweet bot

:a python application, for twitter automation with Cloud Foundry on IBM Bluemix

### python

  * __language:__ Python 2.7.10
  * __libraries:__ tweepy, time, multiprocessing
  * __web framework:__ web.py

### cloud:

  * __infrastructure:__ IBM Bluemix, https://www.ibm.com/cloud-computing/bluemix/
  * __platform:__ Cloud Foundry, https://www.cloudfoundry.org/
  * __Cloud Foundry command line interface (CLI):__ https://github.com/cloudfoundry/cli
  * __CF python template app:__ https://github.com/IBM-Bluemix/get-started-python

### examples:

  * __code on github:__ https://github.com/johncoleman83/mini-tweet-bot
  * __working app:__ https://mtb.mybluemix.net/
  * __blog:__ http://www.davidjohncoleman.com/2017/mini-tweet-bot/

### twitter:

  * __twitter dev tools:__ https://dev.twitter.com/
  * __tweet deck:__ https://tweetdeck.twitter.com/
  * __twitter (bot) account:__ https://twitter.com/are_no_one
  * __api limits:__ https://support.twitter.com/articles/160385
  * __best practices:__ https://dev.twitter.com/basics

## Description

This has my integrations of the tweepy python library to auto generate tweets,
retweets, and to follow users.  There is a custom integration with twitter to
allow multiple users or anyone from the public to post tweets to one specified
twitter account.  The current specified twitter account is specified above;
however, any account can be substituted such as a tourist destination twitter
account or company account.  The app is designed to run on cloudfoundry
applications with IBM Bluemix.

## Documentation

For integration with IBM Bluemix, cloudfoundry apps, see the 
[README.md](https://github.com/IBM-bluemix/get-started-python) 
from the below referenced repository.  Or read the blog post referenced above.

## Usage

`$ python app.py`

## References

* **forked from:** https://github.com/IBM-bluemix/get-started-python

## Author

David John Coleman II.	Check out my website [davidjohncoleman.com](http://www.davidjohncoleman.com/)

## License

Public Domain, no copyright protection
