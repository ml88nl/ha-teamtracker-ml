# API
URL_HEAD = "http://site.api.espn.com/apis/site/v2/sports/"
URL_TAIL = "/scoreboard"
API_LIMIT = 25
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"

LEAGUE_LIST = [
    ["PGA", "golf", "pga"],
    ["F1", "racing", "f1"],
    ["CL", "soccer", "uefa.champions"], 
    ["EL", "soccer", "uefa.europa"], 
    ["ECL", "soccer", "uefa.europa.conf"], 
    ["EPL", "soccer", "eng.1"],
    ["EREDIV", "soccer", "ned.1"],
    ]

SPORT_LIST = [
    ["golf", "mdi:golf-tee"],
    ["racing", "mdi:flag-checkered"],
    ["soccer", "mdi:soccer"]
]

# Config
CONF_CONFERENCE_ID = "conference_id"
CONF_LEAGUE_ID = "league_id"
CONF_LEAGUE_PATH = "league_path"
CONF_SPORT_PATH = "sport_path"
CONF_TIMEOUT = "timeout"
CONF_TEAM_ID = "team_id"

# Defaults
DEFAULT_CONFERENCE_ID = ""
DEFAULT_ICON = "mdi:scoreboard"
DEFAULT_LEAGUE = "NFL"
DEFAULT_LOGO = "https://cdn0.iconfinder.com/data/icons/shift-interfaces/32/Error-512.png"
DEFAULT_LEAGUE_PATH = "league_not_found"
DEFAULT_NAME = "team_tracker"
DEFAULT_PROB = 0.0
DEFAULT_SPORT_PATH = "sport_not_found"
DEFAULT_TIMEOUT = 120
DEFAULT_LAST_UPDATE = "2022-02-02 02:02:02-05:00"
DEFAULT_KICKOFF_IN = "{test} days"

# Misc
TEAM_ID = ""
VERSION = "v0.1"
ISSUE_URL = "https://github.com/vasqued2/ha-teamtracker"
DOMAIN = "teamtracker"
PLATFORM = "sensor"
ATTRIBUTION = "Data provided by ESPN"
COORDINATOR = "coordinator"
PLATFORMS = ["sensor"]
