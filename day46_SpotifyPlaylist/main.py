import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# ---------- date input ---------- #
date = input("Which year do you want to travel to?\nType the date in this format YYYY-MM-DD (ex. 2020-01-01): ")
hot100_url = f"https://www.billboard.com/charts/hot-100/{date}/"
hot100 = requests.get(url=hot100_url).text


# ---------- find hot 100 songs ---------- #
soup = BeautifulSoup(hot100, "html.parser")

first_song = soup.find(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
song_list = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
song_list.insert(0, first_song)

first_artist = soup.find(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet")
artist_list = soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")
artist_list.insert(0, first_artist)

song_list = [song.text.strip() for song in song_list]
artist_list = [artist.text.strip() for artist in artist_list]

# for i in range(0, len(artist_list)):
#     print(f"{song_list[i]} -- {artist_list[i]}")


# ---------- find the songs on Spotify ---------- #
client_id = "dd59b122d247412aa234bcd4f37646a7"
client_secret = "1b8a1465b15b45cdabbfbbc0fe7c7980"
user_id = "315asb73a4lr5ztusmwsjhmo6bv4"
uri_list = []
skipped_songs = 0

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private"))
for i in range(0, len(song_list)):
    result = sp.search(q=f"track:{song_list[i]} artist:{artist_list[i]}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except IndexError:
        skipped_songs += 1
        # print(f"{song_list[i]} by {artist_list[i]} doesn't exist in Spotify. Skipped.")

print(f"Total of {skipped_songs} songs were skipped.")


# ---------- create a playlist with the hot 100 songs on Spotify ---------- #
playlist_name = f"{date} Billboard 100"
playlist_description = f"Playlist of Billboard Hot 100 songs on {date}"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_description)

playlist_id = playlist["id"]
playlist_url = playlist["external_urls"]["spotify"]
success = sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=uri_list)

if success:
    print(f"The playlist of {date} has been successfully created.\nFollow this link to view your playlist: {playlist_url}")
