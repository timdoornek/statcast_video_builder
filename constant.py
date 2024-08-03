from enum import Enum

CORRECT_GAMELOG_SCRIPT_INDEX = 4
SAVANT_BASE_URL = 'https://baseballsavant.mlb.com/savant-player/'
TEMP_FOLDER_PATH = '_videos/'

#file extensions
MP4_EXT = '.mp4'
CSV_EXT = '.csv'

#broadcast type ids
BROADCAST_TYPE_HOME_ID = 'type_HOME'
BROADCAST_TYPE_AWAY_ID = 'type_AWAY'
BROADCAST_TYPE_NETWORK_ID = 'type_NETWORK'
BROADCAST_URL_SUFFIXES = {BROADCAST_TYPE_HOME_ID: '&videoType=HOME', BROADCAST_TYPE_AWAY_ID: '&videoType=AWAY', BROADCAST_TYPE_NETWORK_ID: '&videoType=BROADCAST'}

#day of year helpers
LAST_DAY_OF_YEAR = '-01-01'
FIRST_DAY_OF_YEAR = '-12-31'

#options for statcast pitch events
class Event_Type(Enum):
    STRIKEOUT = 'strikeout' 
    FIELD_OUT = 'field_out' 
    FORCE_OUT = 'force_out' 
    WALK = 'walk' 
    HOME_RUN = 'home_run' 
    TRIPLE = 'triple'
    SINGLE = 'single' 
    HIT_BY_PITCH = 'hit_by_pitch' 
    DOUBLE = 'double' 
    CAUGHT_STEALING_2B = 'caught_stealing_2b'
    FIELD_ERROR = 'field_error'
