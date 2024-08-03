import pybaseball
import constant

def build_data_for_videos(player_id, season, events):
    start_dt = season + constant.FIRST_DAY_OF_YEAR
    end_dt = season + constant.LAST_DAY_OF_YEAR

    #get all pitch data for given season and player
    player_pitch_data = pybaseball.statcast_batter(start_dt = start_dt, end_dt = end_dt, player_id=player_id)
    
    #filter pitches by those resulting in a home run
    #TODO: add other hits as well
    player_pitch_data = player_pitch_data[player_pitch_data['events'].isin([e.value for e in events])]

    #reverse order to match order of videos
    player_pitch_data.iloc[::-1]
    #add index col to match hit # on year
    player_pitch_data['hit_index'] = range(0, len(player_pitch_data))
    #add column to match video name
    player_pitch_data['video_name'] = player_pitch_data['hit_index'].astype(str) + '_' + player_id + constant.MP4_EXT

    #trim to columns we care about
    player_pitch_data = player_pitch_data[['hit_index', 'video_name', 'game_date', 'events', 'hit_distance_sc', 
                                                         'launch_speed', 'launch_angle', 'delta_home_win_exp',
                                                         'bat_speed']]

    #output to csv
    player_pitch_data.to_csv(player_id + constant.CSV_EXT)