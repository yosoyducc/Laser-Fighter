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
    File: AlienSmallAlien.py
    Author: Christian Marinkovich
    Date: 2024-07-08
    Description:
    This file contains the logic related to the Small Aliens in Alien Mode.
    The small alien is the first enemy the player encounters in Alien Mode.
    The small aliens will always move towards the player and move faster the more times they are killed.
    When they come into contact with the player, they reduce the players health.
    The small aliens die in one hit from the players laser and grant the player one point.
"""

import turtle
import pygame
import random
import time
from components.ItemCoin import Coin
from setup.TextureSetup import ALIEN_STILL_RIGHT_1_5_TEXTURE
from setup.TextureSetup import ALIEN_STILL_LEFT_1_5_TEXTURE
from setup.TextureSetup import ALIEN_WALKING_RIGHT_1_5_TEXTURE
from setup.TextureSetup import ALIEN_WALKING_LEFT_1_5_TEXTURE
from setup.TextureSetup import ALIEN_DEATH_1_TEXTURE
from setup.TextureSetup import ALIEN_DEATH_2_TEXTURE


class SmallAlien:
    """
        Represents a small alien in Alien Mode. The small alien is the same height as the player and moves towards the
            player.

        Attributes:
            small_alien (turtle.Turtle()): The small alien sprite

            death_animation (float): Iterated during the small aliens death animation
            death_count (int): Stores the amount of times the small alien has died since the player has last died

            direction (int): Stores the direction that the small alien is facing (1 = right and 2 = left)

            kill_start_time (float): Used as a timestamp for the death animation of the small alien (To make the animation
                run in a consistent amount of time)
            walk_start_time (float): Used as a timestamp for the small aliens walking texture update (To make sure the
                walking animation happens in a consistent amount of time)
            move_start_time (float): Used as a timestamp for the small aliens movement (To make the small aliens
                movement happen in a consistent amount of time and not based on code execution speed)

            movement_activated (int): Check if the aliens movement is currently happening or not. (So that
                it can create a start time for it)

            got_hit (int): Determines if the alien has already gotten hit or not
            collision_point (int): Determines the x-axis collision line for the alien
            already_ahead (int): Determines if the player is already ahead of the alien (larger x-cor) (This is used
                for detecting what point the laser need to pass in order to kill the alien)
            already_behind (int): Determines of the player is already behind the alien (smaller x-cor) (This is used
                for detecting what point the laser need to pass in order to kill the alien)
            thorns_initiated_damage (int): Checks if the enemy has damaged the player while the player has thorns on

            id (int): The id of the alien

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, id, scale_factor_x, scale_factor_y):
        """
            Creates a small alien object with the given id and spawns it in the game.

            :param id: A unique identifier for the small alien
            :type id: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.small_alien = turtle.Turtle()
        self.small_alien.shape(ALIEN_STILL_RIGHT_1_5_TEXTURE)
        self.small_alien.shapesize(4, 2)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.small_alien.penup()
        # Set the small aliens initial location based on its id
        if id == 1:
            self.small_alien.goto(-800 * scale_factor_x, -141 * scale_factor_y)
        elif id == 2:
            self.small_alien.goto(-700 * scale_factor_x, -141 * scale_factor_y)
        elif id == 3:
            self.small_alien.goto(800 * scale_factor_x, -141 * scale_factor_y)
        elif id == 4:
            self.small_alien.goto(700 * scale_factor_x, -141 * scale_factor_y)
        elif id == 5:
            self.small_alien.goto(750 * scale_factor_x, -141 * scale_factor_y)
        self.small_alien.direction = "stop"

        self.death_animation = 0
        self.death_count = 0
        self.direction = 0
        self.kill_start_time = 0
        self.walk_start_time = 0
        self.move_start_time = time.time()
        self.movement_activated = 0

        # For collision
        self.got_hit = 1
        self.collision_point = 0
        self.already_ahead = 1
        self.already_behind = 1
        self.thorns_initiated_damage = 0

        self.id = id

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.small_alien.clear()
        del self.small_alien

    def reinstate(self, id):
        """
            Reuses the existing sprite to spawn a small alien on the screen

            :param id: A new unique identifier for the small alien
            :type id: int
        """

        self.small_alien.shape(ALIEN_STILL_RIGHT_1_5_TEXTURE)
        # Initial location based on the small aliens new id
        if id == 1:
            self.small_alien.goto(-800 * self.scale_factor_x, -141 * self.scale_factor_y)
        elif id == 2:
            self.small_alien.goto(-700 * self.scale_factor_x, -141 * self.scale_factor_y)
        elif id == 3:
            self.small_alien.goto(800 * self.scale_factor_x, -141 * self.scale_factor_y)
        elif id == 4:
            self.small_alien.goto(700 * self.scale_factor_x, -141 * self.scale_factor_y)
        elif id == 5:
            self.small_alien.goto(750 * self.scale_factor_x, -141 * self.scale_factor_y)
        self.small_alien.direction = "stop"
        self.small_alien.showturtle()
        self.move_start_time = time.time()
        self.id = id

    def get_small_alien(self):
        """
            Returns the small alien sprite so that its class attributes can be accessed.

            :return: small_alien: The small alien sprite
            :type: Turtle.turtle()
        """

        return self.small_alien

    def get_death_animation(self):
        """
            Returns the current state of the small aliens death animation (0 if it is not happening)

            :return: death_animation: The current state of the small aliens death animation
            :type: float
        """

        return self.death_animation

    def remove(self):
        """
            Removes the small alien sprite form the screen and resets its attributes.

            :return: None
        """

        self.small_alien.hideturtle()
        self.death_animation = 0
        self.death_count = 0
        self.direction = 0
        self.kill_start_time = 0
        self.walk_start_time = 0
        self.move_start_time = 0
        self.movement_activated = 0
        self.got_hit = 1
        self.collision_point = 0
        self.already_ahead = 1
        self.already_behind = 1
        self.thorns_initiated_damage = 0

    def set_alien_direction(self, player_x):
        """
            Sets the direction of the small alien so that it is facing the player

            :param player_x: The x-coordinate of the player
            :type player_x: float

            :return: None
        """

        if self.small_alien.isvisible():
            # If the players x-coordinate is smaller than the small aliens, then make the small alien face left
            if self.small_alien.xcor() > player_x:
                self.small_alien.direction = "left"
                self.direction = 2
            # If the players x-coordinate is larger than the small aliens, then make the small alien face right
            else:
                self.small_alien.direction = "right"
                self.direction = 1

    def set_alien_texture(self, right_update, left_update):
        """
            Sets the small aliens texture based on the small aliens direction and creates a walking animation when the
                small alien is walking.

            :param right_update: Used to update the walking right animation correctly
            :type right_update: float

            :param left_update: Used to update the walking left animation correctly
            :type left_update: float

            :return: None
        """

        # Updates the walking animation every 0.005 seconds
        current_time = time.time()
        elapsed_time = current_time - self.walk_start_time
        if elapsed_time >= 0.005:
            # If the small aliens direction is right
            if self.direction == 1 and self.death_animation == 0:
                # Make the small alien face and walk right
                if right_update % 0.5 != 0:
                    self.small_alien.shape(ALIEN_WALKING_RIGHT_1_5_TEXTURE)
                else:
                    self.small_alien.shape(ALIEN_STILL_RIGHT_1_5_TEXTURE)
            # If the small aliens direction is left
            elif self.direction == 2 and self.death_animation == 0:
                # Make the small alien face and walk left
                if left_update % 0.5 != 0:
                    self.small_alien.shape(ALIEN_WALKING_LEFT_1_5_TEXTURE)
                else:
                    self.small_alien.shape(ALIEN_STILL_LEFT_1_5_TEXTURE)
            self.walk_start_time = time.time()

    def kill_alien(self, death_sound, coins_on_screen, all_coins):
        """
            Kills the alien and plays the aliens death animation. After that, it respawns the alien on a random
                side of the screen.

            :param death_sound: Determines if the death sound for the enemy is toggled on or off
            :type death_sound: int

            :param coins_on_screen: Array that lists all of the coins currently on the screen
            :type coins_on_screen: list

            :param all_coins: Array that lists all of the coin sprites generated since the
                programs execution (for reusing purposes)
            :type all_coins: list

            :return: None
        """

        if 4 <= self.death_animation < 5:
            # Spawn a coin where the alien has died
            self.small_alien.hideturtle()
            if len(all_coins) <= len(coins_on_screen):
                copper_coin = Coin(type="copper", pos_x=self.small_alien.xcor(), pos_y=self.small_alien.ycor())
                # Set the hitbox for the coin
                copper_coin.range = (copper_coin.coin.ycor() - copper_coin.COIN_DISTANCE, copper_coin.coin.ycor() + copper_coin.COIN_DISTANCE)
                copper_coin.collision_coordinate = copper_coin.coin.xcor()
                copper_coin.just_fired = 0
                coins_on_screen.append(copper_coin)
                all_coins.append(copper_coin)
            else:
                for coin in all_coins:
                    if coin.get_coin().isvisible():
                        continue
                    else:
                        coin.reinstate_to_copper(pos_x=self.small_alien.xcor(), pos_y=self.small_alien.ycor())
                        # Set the hitbox for the coin
                        coin.range = (coin.coin.ycor() - coin.COIN_DISTANCE, coin.coin.ycor() + coin.COIN_DISTANCE)
                        coin.collision_coordinate = coin.coin.xcor()
                        coin.just_fired = 0
                        coins_on_screen.append(coin)
                        break
            # Respawn the small alien in a random location (side of the screen)
            alien_random = random.randint(1, 2)
            if alien_random == 1:
                self.small_alien.goto(random.randint(-900 * self.scale_factor_x, -690 * self.scale_factor_x), -141 * self.scale_factor_y)
            if alien_random == 2:
                self.small_alien.goto(random.randint(690 * self.scale_factor_x, 900 * self.scale_factor_x), -141 * self.scale_factor_y)
            self.small_alien.showturtle()
            self.movement_activated = 0
            self.death_animation = 0
            return

        # Wait 0.15 seconds
        if 3 <= self.death_animation < 4.5:
            current_time = time.time()
            elapsed_time = current_time - self.kill_start_time
            if elapsed_time >= 0.15:
                self.death_animation = 4.5
                self.kill_start_time = 0
            return

        if 2 <= self.death_animation < 3:
            # Change the small aliens texture to the second frame in the death scene
            self.small_alien.shape(ALIEN_DEATH_2_TEXTURE)
            self.death_animation = 3
            self.kill_start_time = time.time()
            return

        # Wait 0.1 seconds
        if 1 <= self.death_animation < 2:
            if self.death_animation == 1:
                self.death_animation = 1.5
            current_time = time.time()
            elapsed_time = current_time - self.kill_start_time
            if elapsed_time >= 0.1:
                self.death_animation = 2
                self.kill_start_time = 0
            return

        if self.death_animation == 0:
            # Increase the death count
            self.death_count = self.death_count + 1
            # Play the death sound
            if death_sound == 1:
                sound = pygame.mixer.Sound("sound/Alien_Death_Sound.wav")
                sound.play()
            # Set the texture of the small alien to the first frame in the death scene
            self.small_alien.shape(ALIEN_DEATH_1_TEXTURE)
            # Reset collision variables
            self.got_hit = 1
            self.already_ahead = 0
            self.already_behind = 0
            # Set the thorns initiated damage back to 0 if needed
            self.thorns_initiated_damage = 0
            self.death_animation = 1
            self.kill_start_time = time.time()
            return

    def set_movement_speed(self):
        """
            Function for the small aliens movement.
            When the small alien has died enough times, this function will cause it to start moving faster and faster.

            :return: None
        """

        if self.small_alien.isvisible() and self.death_animation == 0:
            # If the movement has just started, a start time is created for it
            if self.movement_activated == 0:
                self.move_start_time = time.time()
                self.movement_activated = 1
            # Move the small alien every 0.012 seconds
            current_time = time.time()
            elapsed_time = current_time - self.move_start_time
            if elapsed_time >= 0.012:
                # If the aliens direction is right
                if self.direction == 1:
                    # Move the alien right
                    if 0 <= self.death_count < 6:
                        # Calculate the delta movement as extra movement needed
                        delta_movement = 0.3 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.small_alien.setx(self.small_alien.xcor() + 0.3 * self.scale_factor_x + delta_movement)
                    if 6 <= self.death_count < 12:
                        delta_movement = 0.6 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.small_alien.setx(self.small_alien.xcor() + 0.6 * self.scale_factor_x + delta_movement)
                    if 12 <= self.death_count < 18:
                        delta_movement = 0.9 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.small_alien.setx(self.small_alien.xcor() + 0.9 * self.scale_factor_x + delta_movement)
                    if 18 <= self.death_count < 24:
                        delta_movement = 1.2 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.small_alien.setx(self.small_alien.xcor() + 1.2 * self.scale_factor_x + delta_movement)
                    if 24 <= self.death_count < 30:
                        delta_movement = 1.5 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.small_alien.setx(self.small_alien.xcor() + 1.5 * self.scale_factor_x + delta_movement)
                    if 30 <= self.death_count:
                        delta_movement = 1.8 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.small_alien.setx(self.small_alien.xcor() + 1.8 * self.scale_factor_x + delta_movement)
                # If the aliens direction is left
                else:
                    # Move the alien left
                    if 0 <= self.death_count < 6:
                        delta_movement = 0.3 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.small_alien.setx(self.small_alien.xcor() - 0.3 * self.scale_factor_x - delta_movement)
                    if 6 <= self.death_count < 12:
                        delta_movement = 0.6 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.small_alien.setx(self.small_alien.xcor() - 0.6 * self.scale_factor_x - delta_movement)
                    if 12 <= self.death_count < 18:
                        delta_movement = 0.9 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.small_alien.setx(self.small_alien.xcor() - 0.9 * self.scale_factor_x - delta_movement)
                    if 18 <= self.death_count < 24:
                        delta_movement = 1.2 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.small_alien.setx(self.small_alien.xcor() - 1.2 * self.scale_factor_x - delta_movement)
                    if 24 <= self.death_count < 30:
                        delta_movement = 1.5 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.small_alien.setx(self.small_alien.xcor() - 1.5 * self.scale_factor_x - delta_movement)
                    if 30 <= self.death_count:
                        delta_movement = 1.8 * self.scale_factor_x * ((elapsed_time - 0.012) / 0.012)
                        self.small_alien.setx(self.small_alien.xcor() - 1.8 * self.scale_factor_x - delta_movement)
                self.move_start_time = time.time()
        else:
            self.move_start_time = 0
