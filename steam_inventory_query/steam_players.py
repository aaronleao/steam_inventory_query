"""This module contains the class to represent an player."""

import json
import os
import logging
import sys
from datetime import datetime
from steam_inventory_query import constants
from steam_inventory_query import fetch_inventory
from steam_inventory_query import fs_handler
from steam_inventory_query import inventory_item
from steam_inventory_query import steam_api_handler

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__package__)


class Player:
    """
    This class represents an inventory from a player item.
    """

    def __init__(
        self,
        player_summaries: dict,
        app_id: str = constants.APP_NAME,
        steam_user: str = None,
    ):
        """Initialize the player data."""

        if player_summaries is None:
            raise SystemExit("Player summaries is empty.")

        self.inventory = {}
        self.app_id = app_id
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
        self.community_visibility_state = player_summaries.get(
            "communityvisibilitystate"
        )
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
        """Print the player summaries."""

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
        print("_" * 142, "\n")

    def print_inventory(self, display_inventory_full: bool = False):
        """Print the player inventory."""

        print(f"{self.persona_name} inventory")
        for description in self.inventory["descriptions"]:
            item = inventory_item.InventoryItem(description)
            if display_inventory_full:
                item.print(display_inventory_full)
            else:
                if item.item_desc_type not in (
                    constants.ItemType.HERO.name,
                    constants.ItemType.MISC.name,
                ):
                    item.print(display_inventory_full)
        print("_" * 142, "\n")

    def fetch_inventory(self, api_key: str, overwrite: bool = False):
        """
        Fetches the inventory for a player.
        """
        self.inventory = fetch_inventory.fetch(
            self.app_id, constants.CONTEXT_ID, self.steam_id, api_key, overwrite
        )


def fetch_players(
    api_key: str, steam_ids: list, steam_users: list, app_id: str = constants.APP_ID
):
    """Fetches player data from the Steam API."""

    if steam_ids is None and steam_users:
        steam_ids = [
            steam_api_handler.resolve_vanity(api_key, steam_user)
            for steam_user in steam_users
        ]

    steam_ids_to_fetch = []
    players_summaries = []
    players = []

    for steam_id in steam_ids:
        input_file_path = fs_handler.get_player_summaries_path(steam_id)
        if os.path.exists(input_file_path):
            with open(input_file_path, "r", encoding="utf-8") as input_file:
                logger.info("Player found in cache: %s", input_file_path)
                players_summaries.append(json.load(input_file))
        else:
            steam_ids_to_fetch.append(steam_id)

    if steam_ids_to_fetch:
        players_summaries.extend(
            steam_api_handler.fetch_player_summaries(api_key, steam_ids_to_fetch)
        )

    for player_summaries in players_summaries:
        output_file_path = fs_handler.get_player_summaries_path(
            player_summaries.get("steamid")
        )
        if not os.path.exists(output_file_path):
            with open(output_file_path, mode="w", encoding="utf-8") as output_file:
                logger.info("Player saving in cache: %s", output_file_path)
                json.dump(player_summaries, output_file, indent=4)

    for player_summaries in players_summaries:
        player = Player(player_summaries, app_id)
        players.append(player)

    return players
