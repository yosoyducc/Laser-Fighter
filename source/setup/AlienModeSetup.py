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
    File: AlienModeSetup.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:
    This file contains the setup logic for Alien Mode. This setup logic is run every time the title screen is launched.
    Here, variables for Alien Mode are pre defined before the game starts to avoid in-game lag.
"""

from setup.TextureSetup import PLAYER_GUN_RIGHT_TEXTURE
from setup.TextureSetup import PLAYER_GUN_LEFT_TEXTURE
from setup.TextureSetup import THE_COOKER_RIGHT_TEXTURE
from setup.TextureSetup import THE_COOKER_LEFT_TEXTURE
from setup.TextureSetup import POISON_DART_GUN_RIGHT_TEXTURE
from setup.TextureSetup import POISON_DART_GUN_LEFT_TEXTURE
from setup.TextureSetup import METEOR_GUN_RIGHT_TEXTURE
from setup.TextureSetup import METEOR_GUN_LEFT_TEXTURE
from setup.TextureSetup import SUPERNOVA_RIGHT_TEXTURE
from setup.TextureSetup import SUPERNOVA_LEFT_TEXTURE
from setup.TextureSetup import PLAYER_HEAD_LASER_TEXTURE
from setup.TextureSetup import THE_COOKER_LASER_TEXTURE
from setup.TextureSetup import POISON_DART_LASER_TEXTURE
from setup.TextureSetup import METEOR_GUN_LASER_RIGHT_TEXTURE
from setup.TextureSetup import METEOR_GUN_LASER_LEFT_TEXTURE
from setup.TextureSetup import SUPERNOVA_LASER_RIGHT_TEXTURE
from setup.TextureSetup import SUPERNOVA_LASER_LEFT_TEXTURE


class AlienModeSetup:
    """
        Represents the setup logic for Alien Mode.

        Pointers:
            _shop_config (ShopConfig()): A pointer to the Shop Configuration.
            _power_up_setup (PowerUpSetup()): A pointer to the current power up configuration.
            _scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            _scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode

        Attributes:
            regular_score_multiplier (int): Stores the default score multiplier for Alien Mode (How much does a point
                increase your score)
            blue_power_up_score_multiplier (int): Store the score multiplier when the blue power up is activated

            gun_right_texture (string): stores the current gun facing right texture (depending on shop selection)
            gun_left_texture (string): stores the current gun facing left texture (depending on shop selection)
            gun_offset (int): Stores the current offset of the guns coordinate vs the players (bigger for bigger guns)

            laser_right_texture (string): stores the current laser facing right texture (depending on shop selection)
            laser_left_texture (string): stores the current laser facing left texture (depending on shop selection)
            laser_offset (int): Stores the current offset of the lasers coordinate vs the guns (bigger for bigger lasers)

            laser_speed (float): Stores the player lasers speed
            yellow_power_up_speed (float): Stores the lasers speed when the yellow power up is activated

            damage (int): Stores the current damage infliction of the player
            piercing (int): Stores how many aliens the laser pierces through
            laser_count (int): Stores the number of lasers fired each round

            player_movement (float): Stores the players movement speed
            yellow_player_movement (float): Stores the players movement speed when the yellow power up is active
            jump_frequency (float): Stores the players jump speed
            yellow_jump_frequency (float): Stores the players jump speed when the yellow power up is active

            power_up_spawn_rate (int): Stores the spawn rate of all power ups

            health (int): The maximum health of the player given the current gadgets enabled
    """

    # Set the instance to "None" at the beginning
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
            Ensures only one instance of this class exists at all times.

            :param args: NA
            :param kwargs: NA

            :return: The class instance (Which is created if it does nto already exist)
        """

        if cls._instance is None:
            cls._instance = super(AlienModeSetup, cls).__new__(cls)
        return cls._instance

    def __init__(self, shop_config, power_up_setup, scale_factor_x, scale_factor_y):
        """
            Creates and configures the parameters for Alien Mode.

            :param shop_config: A pointer to the shop configuration
            :type shop_config: ShopConfig()

            :param power_up_setup: A pointer to the current power up setup
            :type power_up_setup: PowerUpSetup()

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        # Everything starts out initialized to 0
        self._shop_config = shop_config
        self._power_up_setup = power_up_setup
        self._scale_factor_x = scale_factor_x
        self._scale_factor_y = scale_factor_y

        self.regular_score_multiplier = 0
        self.blue_power_up_score_multiplier = 0

        self.gun_right_texture = ""
        self.gun_left_texture = ""
        self.gun_offset = 0
        self.laser_right_texture = ""
        self.laser_left_texture = ""
        self.laser_offset = 0

        self.laser_speed = 0
        self.yellow_power_up_speed = 0

        self.damage = 0
        self.piercing = 0
        self.laser_count = 0

        self.player_movement = 4
        self.yellow_player_movement = 4
        self.jump_frequency = 0.006
        self.yellow_jump_frequency = 0.006
        self.power_up_spawn_rate = 1

        self.health = 0

        # Run the setup
        self.setup_alien_mode()

    def __del__(self):
        """
            Clear the variables from memory once the program has terminated

            :return: None
        """

        del self._shop_config
        del self._power_up_setup
        del self._scale_factor_x
        del self._scale_factor_y
        del self.regular_score_multiplier
        del self.blue_power_up_score_multiplier
        del self.gun_right_texture
        del self.gun_left_texture
        del self.gun_offset
        del self.laser_right_texture
        del self.laser_left_texture
        del self.laser_offset
        del self.laser_speed
        del self.yellow_power_up_speed
        del self.damage
        del self.piercing
        del self.laser_count
        del self.player_movement
        del self.yellow_player_movement
        del self.jump_frequency
        del self.yellow_jump_frequency
        del self.power_up_spawn_rate
        del self.health

    def setup_alien_mode(self):
        """
            Sets up the Alien Mode variables.

            :return: None
        """

        # Initializes some variables to their default state (In case they do not need to change)
        self.player_movement = 4
        self.yellow_player_movement = 4
        self.jump_frequency = 0.006
        self.yellow_jump_frequency = 0.006
        self.power_up_spawn_rate = 1

        # Sets the variables based on which items in the shop are selected
        if self._shop_config.alien_slot_selected == 1:
            self.gun_right_texture = PLAYER_GUN_RIGHT_TEXTURE
            self.gun_left_texture = PLAYER_GUN_LEFT_TEXTURE
            self.gun_offset = 20 * self._scale_factor_x

            self.laser_right_texture = PLAYER_HEAD_LASER_TEXTURE
            self.laser_left_texture = PLAYER_HEAD_LASER_TEXTURE
            self.laser_offset = 35 * self._scale_factor_x

            self.laser_speed = 12 * self._scale_factor_x

            self.damage = 1
            self.piercing = 2
            self.laser_count = 1

            self.regular_score_multiplier = 1
        elif self._shop_config.alien_slot_selected == 2:
            self.gun_right_texture = THE_COOKER_RIGHT_TEXTURE
            self.gun_left_texture = THE_COOKER_LEFT_TEXTURE
            self.gun_offset = 20 * self._scale_factor_x

            self.laser_right_texture = THE_COOKER_LASER_TEXTURE
            self.laser_left_texture = THE_COOKER_LASER_TEXTURE
            self.laser_offset = 35 * self._scale_factor_x

            self.laser_speed = 14 * self._scale_factor_x

            self.damage = 1
            self.piercing = 3
            self.laser_count = 1

            self.regular_score_multiplier = 1
        elif self._shop_config.alien_slot_selected == 3:
            self.gun_right_texture = POISON_DART_GUN_RIGHT_TEXTURE
            self.gun_left_texture = POISON_DART_GUN_LEFT_TEXTURE
            self.gun_offset = 20 * self._scale_factor_x

            self.laser_right_texture = POISON_DART_LASER_TEXTURE
            self.laser_left_texture = POISON_DART_LASER_TEXTURE
            self.laser_offset = 35 * self._scale_factor_x

            self.laser_speed = 20 * self._scale_factor_x

            self.damage = 2
            self.piercing = 2
            self.laser_count = 2

            self.regular_score_multiplier = 1
        elif self._shop_config.alien_slot_selected == 4:
            self.gun_right_texture = METEOR_GUN_RIGHT_TEXTURE
            self.gun_left_texture = METEOR_GUN_LEFT_TEXTURE
            self.gun_offset = 28 * self._scale_factor_x

            self.laser_right_texture = METEOR_GUN_LASER_RIGHT_TEXTURE
            self.laser_left_texture = METEOR_GUN_LASER_LEFT_TEXTURE
            self.laser_offset = 65 * self._scale_factor_x

            self.laser_speed = 24 * self._scale_factor_x

            self.damage = 3
            self.piercing = 3
            self.laser_count = 1

            self.regular_score_multiplier = 2
        elif self._shop_config.alien_slot_selected == 5:
            self.gun_right_texture = SUPERNOVA_RIGHT_TEXTURE
            self.gun_left_texture = SUPERNOVA_LEFT_TEXTURE
            self.gun_offset = 28 * self._scale_factor_x

            self.laser_right_texture = SUPERNOVA_LASER_RIGHT_TEXTURE
            self.laser_left_texture = SUPERNOVA_LASER_LEFT_TEXTURE
            self.laser_offset = 65 * self._scale_factor_x

            self.laser_speed = 27 * self._scale_factor_x

            self.damage = 3
            self.piercing = 4
            self.laser_count = 2

            self.regular_score_multiplier = 2

            self.player_movement = self.player_movement * 1.25
            self.jump_frequency = self.jump_frequency / 1.25
            self.power_up_spawn_rate = 2

        # After the gun selection is detected, the variables are modified again based on the current level of the
        #   power ups
        self.yellow_power_up_speed = self.laser_speed * self._power_up_setup.yellow_power_up_speed_increase

        self.blue_power_up_score_multiplier = self.regular_score_multiplier * self._power_up_setup.blue_power_up_multiplier

        self.yellow_player_movement = self.player_movement * self._power_up_setup.yellow_power_up_movement_increase * self._scale_factor_x
        self.player_movement = self.player_movement * self._scale_factor_x

        self.yellow_jump_frequency = self.jump_frequency / self._power_up_setup.yellow_power_up_movement_increase

        # Check if the shield is enabled to determine the maximum health
        if self._shop_config.shield_enabled:
            self.health = 20
        else:
            self.health = 10
