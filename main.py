import video_downloader
import video_data
import config

if __name__ == '__main__':
    video_downloader.download_videos_from_player_and_team(config.player_id, config.team_abbr, config.events)
    video_data.build_data_for_videos(config.player_id, config.start_season, config.events)