
## Statcast video downloader

The purpose of this is to programmatically download videos of events from a player's statcast ID, and then grab corresponding event "metadata", e.g. date, exit velocity, launch angle, xwOBA, etc. to then use in video editing software.

### Configuration
 Go to config.py and

1. enter the desired player's statcast ID, e.g. `player_id  =  '694192'` 
	- this can be found in the URL of a player's statcast page, or, alternatively, you can grab this using pybaseball's [playerid_lookup](https://github.com/jldbc/pybaseball/blob/master/docs/playerid_lookup.md)
2. enter the desired start season and end season, e.g. `start_season  =  '2024'` (#TODO this doesn't work yet)
3. enter the team abbreviation of the player for that season to grab the correct broadcast, e.g. `team_abbr  =  'MIL'`
	- if this is left blank or filled in incorrectly, videos downloaded may be from incorrect broadcast
4. enter the desired statcast events that you want to download the videos of

Once configured, run main. 

### Outputs
- the videos will be saved to a folder in the working directory titled `[player_id]_videos` and videos will be titled `[chronological_index_of_event]_[player_id].mp4'
- a CSV of statcast data for each event that is downloaded, including a column matching the name of the video so it's easier to process in video editor down the line

### #TODOs 
- ability to download multiple seasons at once
- take desired "metadata" columns as input
- learn what the fuck I'm doing when creating/releasing a python library
- who knows
