import requests 
import urllib.request
import re 
import os
import constant
from bs4 import BeautifulSoup
import json

def download_videos_from_player_and_team(player_id, team_abbr, events):

    #TODO: loop through multiple seasons

    base_video_urls = _build_list_of_base_video_urls(player_id, events)
    direct_video_urls = _build_list_of_direct_video_urls(base_video_urls, team_abbr)

    #download each individual video into a temp folder and then add appropriate labels
    count = 0
    for direct_video_url in direct_video_urls:
        #download video
        video_name = str(count) + '_' + player_id + constant.MP4_EXT

        download_video_from_savant_url(direct_video_url, player_id + constant.TEMP_FOLDER_PATH, video_name)
        count += 1

def download_video_from_savant_url(url, path, video_name):
    if path is not None:
        if not os.path.exists(path):
            os.makedirs(path)

    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    video_url = soup.select('source[type="video/mp4"]')[0].get('src')
    
    urllib.request.urlretrieve(video_url, path + video_name)

def _build_list_of_base_video_urls(player_id, events):
    #scrape player's base savant page
    full_url = constant.SAVANT_BASE_URL + player_id
    soup = BeautifulSoup(requests.get(full_url).text, 'html.parser')

    #find the javascript script hidden in the html with JSON of player statcast events including vid hrefs
    #load that into a dict
    statcast_script = soup.findAll('script')[constant.CORRECT_GAMELOG_SCRIPT_INDEX].string
    data = re.search(r'statcastGameLogs: (.*])', statcast_script).group(1)
    statcast_gamelogs = json.loads(data)

    #loop through each event and build the video url if it exists for that event
    urls = []
    for event in statcast_gamelogs:
        if event['event'] in [e.value for e in events] and 'video' in event:
            video_url = 'https://baseballsavant.mlb.com' + BeautifulSoup(event['video'], 'html.parser').find('a')['href']
            urls.append(video_url)

    return urls

def _build_list_of_direct_video_urls(urls, team_abbr):
    url_list = []
    for url in urls:
        #find the video information, e.g. batter, pitcher, matchup, date
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        results = soup.select('div[class="mod"]')[0].findAll('li')

        #build a dictionary of the event metadata from the list items scraped into results
        data = dict(result.text.strip().split(':') for result in results)
        
        #determine which broadcasts are available
        broadcast_tags = soup.select('span[class="broadcast"]')
        broadcasts = list(broadcast.get('id') for broadcast in broadcast_tags)
        
        #determine if game is home or away
        home = False
        if '@ ' + team_abbr in data['Matchup']:
            home = True

        #find correct video url
        correct_broadcast_url = url
        if home and constant.BROADCAST_TYPE_HOME_ID in broadcasts:
            correct_broadcast_url += constant.BROADCAST_URL_SUFFIXES[constant.BROADCAST_TYPE_HOME_ID]
        elif not home and constant.BROADCAST_TYPE_AWAY_ID in broadcasts:
            correct_broadcast_url += constant.BROADCAST_URL_SUFFIXES[constant.BROADCAST_TYPE_AWAY_ID]
        elif constant.BROADCAST_TYPE_NETWORK_ID in broadcasts:
            correct_broadcast_url += constant.BROADCAST_URL_SUFFIXES[constant.BROADCAST_TYPE_NETWORK_ID]
        elif broadcasts.count > 0:
            correct_broadcast_url += constant.BROADCAST_URL_SUFFIXES[broadcasts[0]]

        url_list.append(correct_broadcast_url)

    #reverse so it's in chronological order
    return list(reversed(url_list))
            


        