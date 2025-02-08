""" This module contains the class to represent an player. """

from datetime import datetime
from steam_inventory_query import constants
from steam_inventory_query import fetch_inventory
from steam_inventory_query import steam_api_handler

class Player:
    """
    This class represents an inventory from a player item.
    """
    def __init__(self, player_summaries: dict, steam_user: str=None):
        """ Initialize the player data. """

        self.steam_id = player_summaries.get("steamid")
        self.steam_user = steam_user
        self.persona_name = player_summaries.get("personaname")
        self.profile_url = player_summaries.get("profileurl")
        self.avatar = player_summaries.get("avatar")
        self.avatar_medium = player_summaries.get("avatarmedium")
        self.avatar_full = player_summaries.get("avatarfull")
        self.avatar_hash = player_summaries.get("avatarhash")
        self.persona_state = player_summaries.get("personastate")
        self.persona_state_flags = player_summaries.get("personastateflags")
        self.community_visibility_state = player_summaries.get("communityvisibilitystate")
        self.profile_state = player_summaries.get("profilestate")
        self.last_logoff = player_summaries.get("lastlogoff")
        self.comment_permission = player_summaries.get("commentpermission")
        self.real_name = player_summaries.get("realname")
        self.primary_clan_id = player_summaries.get("primaryclanid")
        self.time_created = player_summaries.get("timecreated")
        self.game_id = player_summaries.get("gameid")
        self.game_extrainfo = player_summaries.get("gameextrainfo")
        self.city_id = player_summaries.get("cityid")
        self.state_code = player_summaries.get("statecode")
        self.country_code = player_summaries.get("countrycode")
        self.loc_country_code = player_summaries.get("loccountrycode")
        self.loc_state_code = player_summaries.get("locstatecode")

    def print(self):
        """ Print the player summaries. """


        print(f"Steam ID: {self.steam_id}")
        print(f"Steam user: {self.steam_user}")
        print(f"Persona name: {self.persona_name}")
        print(f"Profile URL: {self.profile_url}")
        print(f"Avatar: {self.avatar}")
        print(f"Avatar medium: {self.avatar_medium}")
        print(f"Avatar full: {self.avatar_full}")
        print(f"Avatar hash: {self.avatar_hash}")
        print(f"Persona state: {self.persona_state}")
        print(f"Persona state flags: {self.persona_state_flags}")
        print(f"Community visibility state: {self.community_visibility_state}")
        print(f"Profile state: {self.profile_state}")
        print(f"Last logoff: { datetime.fromtimestamp(self.last_logoff)}")
        print(f"Comment permission: {self.comment_permission}")
        print(f"Real name: {self.real_name}")
        print(f"Primary clan ID: {self.primary_clan_id}")
        print(f"Time created: {datetime.fromtimestamp(self.time_created)}")
        print(f"Game ID: {self.game_id}")
        print(f"Game extra info: {self.game_extrainfo}")
        print(f"City ID: {self.city_id}")
        print(f"State code: {self.state_code}")
        print(f"Country code: {self.country_code}")
        print(f"Location country code: {self.loc_country_code}")
        print(f"Location state code: {self.loc_state_code}")
        print("\n")

def fetch_players(api_key: str, steam_ids: list, steam_users: list):
    """
    Fetches player data from the Steam API.
    """

    if steam_ids is None and steam_users:
        steam_ids = [steam_api_handler.resolve_vanity(api_key, steam_user) for steam_user in steam_users]

    players_summaries =  steam_api_handler.fetch_players_summaries(api_key, steam_ids)

    players = [Player(player_summaries) for player_summaries in players_summaries]

    return players

def set_players_inventory(api_key: str, players: list, app_id: str, overwrite: bool=False):
    """
    Fetches the inventory for a player.
    """

    for player in players:
        player.inventory = fetch_inventory.fetch(app_id, constants.CONTEXT_ID, player, api_key, overwrite)
