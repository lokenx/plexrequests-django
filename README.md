#Plex Requests

**This project is no longer maintained. Please checkout [plexrequests-meteor](https://github.com/lokenx/plexrequests-meteor) for an updated project!**

---

__Update 2:__ The meteor version of plex requests has switched to my main focus for now. It's got the same features as this version including CP integration. I'm putting a hold on this version for the time being. Check the meteor repo out [here](https://github.com/lokenx/plexrequests-meteor)!

__Update:__ I've also started working on a meteor application that does most of what the Django version does. Why the change? I was playing around with the JS version and wondered if I could make the whole application that way...enter Meteor! I'm bringing it up to the same features the Django one has, and it includes the extra ability to view requested movies as well! Check the repo out [here](https://github.com/lokenx/plexrequests-meteor)!

---

This is a simple Django application that relies on IMDB, CouchPotato and PushBullet to allow Plex users to request movies to be queued for downloading. For those of us with family and friends using our Plex Servers it allows a friendly way for them to requests new Movies with out having to bug you directly!

This is my first django app/app just in general so it'll be rough around the edges and wrong in many places with unpleasant breakages I haven't found yet. I've warned you!

![plex_requests_search](/screenshots/1plexrequests_search.png)

## Requirements

There is a pip requirements file included. I'm assuming you've a Django project already that you can add this app too, but if not you can create a simple one and import this application. Also I haven't tested this with the Django app and CouchPotato not being on the same LAN

##Quick Start

1. Clone the repository into your Django project
2. Add "plexrequests" to your INSTALLED_APPS setting at the bottom of the list of your settings.py file and a reference to the templates if you don't already have one
    `TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]`
3. Include the plexrequests URLconf into your projects urls.py as seen below (adjust as per your project needs):
    `url(r'^', include('plexrequests.urls', namespace="plexrequests")),`
4. Open the views.py file within the plexrequests directory as two smal changes need to be made
    - For CouchPotato to work you need to get your servers IP and API from within settings and copy it in on line 57 for variable cp_url. It should look like example below
        `http://192.168.0.100:5050/api/abcdefghijk0123456/`
    - For PushBullet enter your API key on line 67 such as below
        `Pushbullet("abcdefghijk0123456")`
5. Run `./manage.py migrate` to get the non-exist models created (they're coming!)
6. Start up the development server or reset your existing server and you should be able to see the app on `http://127.0.0.1:8000/` or whatever base URL you used in step 2.
