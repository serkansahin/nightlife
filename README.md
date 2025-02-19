[![Build Status](https://travis-ci.org/LeMayhem/nightlife.svg?branch=deploy)](https://travis-ci.org/LeMayhem/nightlife)

# Nightlife

## Welcome to Nightlife

Nightlife is a schedule of the week's outings, for people who love electronic music, build by an electronic music lover.
You can find all the popular events and artists, follow them to stay tuned and make friends before going out.

This project aims to use Django framework and Spotify API. This is a WIP, you can follow the building of new features on this repo.

## Features

### Homepage

![alt text](https://i.ibb.co/fz5ky8Td/localhost-8000.png)

You have access to:
- The 4 most populars events from current week (based on "ongoing" button)
- 4 most popular artists (based on "following" button)
- Latest events created
- The top 4 promoters

### Events

![alt text](https://i.ibb.co/Ng6QZ6f3/localhost-8000-events-the-magician-album-tour.png)

Here you can discover and follow events. Promoters can sign up to create their own events to reach new people.
Promoters can ask to feature their events.
Members can discuss on every events to find friends to hangout with.

### Artists

![alt text](https://i.ibb.co/xqbVw0KG/localhost-8000-artists.png)
![alt text](https://i.ibb.co/pmLfggr/localhost-8000-artists-amelie-lens.png)

You can check all the events your favorites artists are playing. You can follow them in order to keep you in touch.
With Spotify API, you can do some actions:
- You can massively follow all the artists from your spotify to Nightlife.
- You can massively import all the artists from your Spotify to Nightlife (Admin)
Members can discuss on every artists fan pages to meet other fans.

### Blog

![alt text](https://i.ibb.co/JbVp1yY/localhost-8000-blog.png)
![alt text](https://i.ibb.co/ycghbM0Z/localhost-8000-blog-the-magician-sera-au-badaboum-le-14-fevrier-pour-son-album-tour.png)

Members can inform themselves with the blog part. Admin can create posts to feature events or artists, to be desplayed on home page.
Members can also discuss on every blog posts.

### Search

![alt text](https://i.ibb.co/zhVfTtGf/localhost-8000-search.png)

- You can search globally from the header's searchbar, which will search on Artists, events and blogposts
- You can filter by using searchbars on Artists, events and blogposts list pages

## WIP:
- Build more interactions between Spotify API and Nightlife (Playlists, etc)
- Add Facebook login
- Add Soundcloud API
- More filters on list pages
- Footer

# Installation
- Download this repository
- Create your postgreSQL database  fill the credentials into credentials.py
- Create your Spotify API. Add your own credentials into credentials.py
- Enjoy :)
