# Copyright (C) [2024] [Christian Marinkovich]
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
    File: UpdateStatsData.py
    Author: Christian Marinkovich
    Date: 2024-08-03
    Description:
    This file contains the logic for saving the game statistics to the player data file and for loading the
        game statistics from the player data file.
"""

from utils.PlayerDataManager import PlayerDataManager


class Stats:
    """
        Represents the parser for the current game statistics.

        Attributes:
            player_data_manager (PlayerDataManager()): The parser for the playerData.ini file

            score (int): The current in game score

            high_score_machine_war (int): The current high score in Machine Mode.
            bosses_killed (int): The number of machine bosses killed.
            red_bots_killed (int): The number of red machines killed.
            yellow_bots_killed (int): The number of yellow machines killed.
            blue_bots_killed (int): The number of blue machines killed.
            classic_deaths (int): The number of deaths in machine mode.
            machine_damage_taken (int): The amount of damage taken in machine mode.
            classic_lasers_fired (int): The number of lasers fired in machine mode.
            classic_power_ups_picked_up (int): The number of power-ups picked up in machine mode.
            machine_coins_collected (int): The number of coins collected in machine mode.

            high_score_alien_mode (int): The current high score in the Alien Mode.
            ufos_killed (int): The number of alien UFOs killed.
            big_aliens_killed (int): The number of big aliens killed.
            medium_aliens_killed (int): The number of medium aliens killed.
            small_aliens_killed (int): The number of small aliens killed.
            alien_deaths (int): The number of deaths in alien mode.
            damage_taken (int): The amount of damage taken.
            alien_lasers_fired (int): The number of lasers fired in alien mode.
            jumps (int): The number of jumps performed in alien mode.
            alien_power_ups_picked_up (int): The number of power-ups picked up in alien mode.
            alien_coins_collected (int): The number of coins collected in alien mode.

            god_mode (int): Determines if god mode is currently toggled on or off
    """

    def __init__(self, god_mode):
        """
            Initializes and loads the current game statistics.

            :param god_mode: Determines if god mode is currently toggled on or off
            :type god_mode: int
        """

        # Initialize the player data parser
        self.player_data_manager = PlayerDataManager()

        # Set the score to 0
        self.score = 0

        # Initialize the Machine Mode statistics variables
        self.high_score_machine_war = 0
        self.bosses_killed = 0
        self.red_bots_killed = 0
        self.yellow_bots_killed = 0
        self.blue_bots_killed = 0
        self.classic_deaths = 0
        self.machine_damage_taken = 0
        self.classic_lasers_fired = 0
        self.classic_power_ups_picked_up = 0
        self.machine_coins_collected = 0

        # Initialize the Alien Mode statistics variables
        self.high_score_alien_mode = 0
        self.ufos_killed = 0
        self.big_aliens_killed = 0
        self.medium_aliens_killed = 0
        self.small_aliens_killed = 0
        self.alien_deaths = 0
        self.damage_taken = 0
        self.alien_lasers_fired = 0
        self.jumps = 0
        self.alien_power_ups_picked_up = 0
        self.alien_coins_collected = 0

        # Initialize the god mode pointer
        self.god_mode = god_mode

        # Load the current game statistics
        self.load()

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self.player_data_manager

    def load(self):
        """
            Loads the current game statistics from the player data file.

            :return: None
        """

        # Machine Mode Statistics
        if self.god_mode == 1:
            self.high_score_machine_war = "NA"
        else:
            self.high_score_machine_war = self.player_data_manager.getint('High_Score', 'High_Score_Machine_War')
        self.bosses_killed = self.player_data_manager.getint('Statistics_Machine_Mode', 'Bosses_Killed')
        self.red_bots_killed = self.player_data_manager.getint('Statistics_Machine_Mode', 'Red_Bots_Killed')
        self.yellow_bots_killed = self.player_data_manager.getint('Statistics_Machine_Mode', 'Yellow_Bots_Killed')
        self.blue_bots_killed = self.player_data_manager.getint('Statistics_Machine_Mode', 'Blue_Bots_Killed')
        self.classic_deaths = self.player_data_manager.getint('Statistics_Machine_Mode', 'Deaths')
        self.machine_damage_taken = self.player_data_manager.getint('Statistics_Machine_Mode', 'Damage_Taken')
        self.classic_lasers_fired = self.player_data_manager.getint('Statistics_Machine_Mode', 'Lasers_Fired')
        self.classic_power_ups_picked_up = self.player_data_manager.getint('Statistics_Machine_Mode', 'Power_Ups_Picked_Up')
        self.machine_coins_collected = self.player_data_manager.getint('Statistics_Machine_Mode', 'Coins_Collected')

        # Alien Mode Statistics
        if self.god_mode == 1:
            self.high_score_alien_mode = "NA"
        else:
            self.high_score_alien_mode = self.player_data_manager.getint('High_Score', 'High_Score_Alien_Mode')
        self.ufos_killed = self.player_data_manager.getint('Statistics_Alien_Mode', 'Ufos_Killed')
        self.big_aliens_killed = self.player_data_manager.getint('Statistics_Alien_Mode', 'Big_Aliens_Killed')
        self.medium_aliens_killed = self.player_data_manager.getint('Statistics_Alien_Mode', 'Medium_Aliens_Killed')
        self.small_aliens_killed = self.player_data_manager.getint('Statistics_Alien_Mode', 'Small_Aliens_Killed')
        self.alien_deaths = self.player_data_manager.getint('Statistics_Alien_Mode', 'Deaths')
        self.damage_taken = self.player_data_manager.getint('Statistics_Alien_Mode', 'Damage_Taken')
        self.alien_lasers_fired = self.player_data_manager.getint('Statistics_Alien_Mode', 'Lasers_Fired')
        self.jumps = self.player_data_manager.getint('Statistics_Alien_Mode', 'Jumps')
        self.alien_power_ups_picked_up = self.player_data_manager.getint('Statistics_Alien_Mode', 'Power_Ups_Picked_Up')
        self.alien_coins_collected = self.player_data_manager.getint('Statistics_Alien_Mode', 'Coins_Collected')

    def save(self):
        """
            Saves the current game statistics to the player data file.

            :return: None
        """

        # High Scores
        if self.god_mode != 1:
            self.player_data_manager.set('High_Score', 'High_Score_Machine_War', str(self.high_score_machine_war))
            self.player_data_manager.set('High_Score', 'High_Score_Alien_Mode', str(self.high_score_alien_mode))

        # Machine Mode Statistics
        self.player_data_manager.set('Statistics_Machine_Mode', 'Bosses_Killed', str(self.bosses_killed))
        self.player_data_manager.set('Statistics_Machine_Mode', 'Red_Bots_Killed', str(self.red_bots_killed))
        self.player_data_manager.set('Statistics_Machine_Mode', 'Yellow_Bots_Killed', str(self.yellow_bots_killed))
        self.player_data_manager.set('Statistics_Machine_Mode', 'Blue_Bots_Killed', str(self.blue_bots_killed))
        self.player_data_manager.set('Statistics_Machine_Mode', 'Deaths', str(self.classic_deaths))
        self.player_data_manager.set('Statistics_Machine_Mode', 'Damage_Taken', str(self.machine_damage_taken))
        self.player_data_manager.set('Statistics_Machine_Mode', 'Lasers_Fired', str(self.classic_lasers_fired))
        self.player_data_manager.set('Statistics_Machine_Mode', 'Power_Ups_Picked_Up', str(self.classic_power_ups_picked_up))
        self.player_data_manager.set('Statistics_Machine_Mode', 'Coins_Collected', str(self.machine_coins_collected))

        # Alien Mode Statistics
        self.player_data_manager.set('Statistics_Alien_Mode', 'Ufos_Killed', str(self.ufos_killed))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Big_Aliens_Killed', str(self.big_aliens_killed))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Medium_Aliens_Killed', str(self.medium_aliens_killed))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Small_Aliens_Killed', str(self.small_aliens_killed))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Deaths', str(self.alien_deaths))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Damage_Taken', str(self.damage_taken))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Lasers_Fired', str(self.alien_lasers_fired))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Jumps', str(self.jumps))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Power_Ups_Picked_Up', str(self.alien_power_ups_picked_up))
        self.player_data_manager.set('Statistics_Alien_Mode', 'Coins_Collected', str(self.alien_coins_collected))

    def __repr__(self):
        """
            Creates a print statement for the game statistics where they are all listed out in order.

            :return: Prints all of the game statistics in a list.
            :type: string
        """

        return (f"Statistics("
                f"high_score_machine_war={self.high_score_machine_war}, "
                f"bosses_killed={self.bosses_killed}, "
                f"red_bots_killed={self.red_bots_killed}, "
                f"yellow_bots_killed={self.yellow_bots_killed}, "
                f"blue_bots_killed={self.blue_bots_killed}, "
                f"classic_deaths={self.classic_deaths}, "
                f"machine_damage_taken={self.machine_damage_taken}, "
                f"classic_lasers_fired={self.classic_lasers_fired}, "
                f"classic_power_ups_picked_up={self.classic_power_ups_picked_up}, "
                f"machine_coins_collected={self.machine_coins_collected}, "
                f"high_score_alien_mode={self.high_score_alien_mode}, "
                f"ufos_killed={self.ufos_killed}, "
                f"big_aliens_killed={self.big_aliens_killed}, "
                f"medium_aliens_killed={self.medium_aliens_killed}, "
                f"small_aliens_killed={self.small_aliens_killed}, "
                f"alien_deaths={self.alien_deaths}, "
                f"damage_taken={self.damage_taken}, "
                f"alien_lasers_fired={self.alien_lasers_fired}, "
                f"jumps={self.jumps}, "
                f"alien_power_ups_picked_up={self.alien_power_ups_picked_up}, "
                f"alien_coins_collected={self.alien_coins_collected})")
