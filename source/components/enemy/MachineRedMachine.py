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
    File: MachineRedMachine.py
    Author: Christian Marinkovich
    Date: 2024-07-05
    Description:
    This file contains the logic related to the red machine, which is the third enemy you will
    encounter in Machine Mode.
    The red machine fires large red lasers at the player. It dies in two hits and has a 1.5 second long
    death animation.
    When killed, the red machine grants the player 5 points.
    When hit, the red machine grants the player 1 point.
    The red machine also moves up and down to simulate floating in outer space. It also moves left to right after
    it has been killed enough times.
"""

import turtle
import random
import pygame
import time
from components.ItemCoin import Coin
from setup.ModeSetupMaster import machine_mode_setup
from setup.TextureSetup import RED_MACHINE_TEXTURE
from setup.TextureSetup import RED_MACHINE_LASER_TEXTURE
from setup.TextureSetup import HEALTH_BAR_12_TEXTURE
from setup.TextureSetup import HEALTH_BAR_22_TEXTURE
from setup.TextureSetup import EXPLOSION_1_TEXTURE
from setup.TextureSetup import EXPLOSION_2_TEXTURE


class RedMachine:
    """
        Represents a red machine in Laser Fighter. The third enemy in Machine Mode that is red
            and fires red lasers.

        Attributes:
            red_machine (turtle.Turtle()): The red machine enemy sprite.
            red_machine_laser (turtle.Turtle()): The laser sprite for each red machine enemy.
            red_machine_health_bar (turtle.Turtle()): The health bar sprite for each red machine enemy.

            death_count (int): Stores the death count for the enemy since the player has last died.
            health_bar (int): Stores the current health of the enemy
            hit_delay (int): Delays how often the enemy can be hit
            update (float): Value that is incremented during the death animation of the enemy.

            movement (int): Stores the direction that the enemy is supposed to move on
                the x-axis (1 = right and -1 = left)
            float (int): Stores the direction that the enemy is supposed to move on the y-axis (1 = up and -1 == down)
            start_y_float (float): Stores the y-coordinate of the enemy when the float effect is starting or when
                it is changing direction
            float_activated (int): Determines if the float effect is currently active or not (For timing purposes)

            start_time (float): Used as a timestamp for the death animation of the enemy (To make the animation run in
                a consistent amount of time)
            hit_start_time (float): Used as a timestamp for the hit delay of the enemy (To make the delay tun in
                a consistent amount of time)
            laser_start_time (float): Used as a timestamp for the laser movement of the enemy (To make the movement
                happen in a consistent amount of time)
            move_start_time (float): Used as a timestamp for the enemies movement (To make the enemies movement
                happen in a consistent amount of time and not based on code execution speed)
            float_start_time (float): Used as a timestamp for the enemies floating effect movement (To make the
                movement happen in a consistent amount of time)

            laser_has_attacked (int): Determines if the enemy has been hit by the players laser since it was last fired
                (So that it does not get hit two times in a row)
            movement_activated (int): Check if the enemies side to side movement is currently happening or not. (So
                that it can create a start time for it)

            id (int): The id of the current red machine (Used for counting how many are on the screen)

            enemy_center (float): The y-axis center of the sine wave created by the machines float effect
                (when t=0, where is it?)
            float_time_offset (float): The timestamp when the float effect for the machine begins

            x_range_list (tuple): The x-axis of the hitboxes for the machine. (The range of x-coordinates the laser
                has to be in in order to hit the enemy)
            collision_y_coordinate_list: The y-axis point that the players lasers have to pass in order to
                hit the machine.
            thorns_initiated_damage (int): Checks if the enemy has damaged the player while the player has thorns on

            scale_factor_x (float): The scale factor for the x-axis used in fullscreen mode
            scale_factor_y (float): The scale factor for the y-axis used in fullscreen mode
    """

    def __init__(self, id, scale_factor_x, scale_factor_y):
        """
            Creates a red machine object and spawns it on the screen

            :param id: Ths id of the red machine (Determines where it spawns and it keeps track of how many are on
                the screen)
            :type id: int

            :param scale_factor_x: The scale factor for the x-axis used in fullscreen mode
            :type scale_factor_x: float

            :param scale_factor_y: The scale factor for the y-axis used in fullscreen mode
            :type scale_factor_y: float
        """

        self.red_machine = turtle.Turtle()
        self.red_machine.shape(RED_MACHINE_TEXTURE)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.red_machine.penup()
        self.red_machine.shapesize(2 * scale_factor_y, 2 * scale_factor_x)
        # Correct location based on id
        if id == 1:
            self.red_machine.goto(375 * scale_factor_x, 220 * scale_factor_y)
        elif id == 2:
            self.red_machine.goto(-375 * scale_factor_x, 220 * scale_factor_y)
        elif id == 3:
            self.red_machine.goto(325 * scale_factor_x, 220 * scale_factor_y)
        elif id == 4:
            self.red_machine.goto(-325 * scale_factor_x, 220 * scale_factor_y)
        elif id == 5:
            self.red_machine.goto(275 * scale_factor_x, 220 * scale_factor_y)
        self.red_machine.direction = "down"

        self.red_machine_laser = turtle.Turtle()
        self.red_machine_laser.shape(RED_MACHINE_LASER_TEXTURE)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.red_machine_laser.penup()
        self.red_machine_laser.shapesize(2.25 * scale_factor_y, 0.5 * scale_factor_x)
        self.red_machine_laser.direction = "down"
        # Correct location based on id
        if id == 1:
            self.red_machine_laser.goto(375 * scale_factor_x, 150 * scale_factor_y)
        elif id == 2:
            self.red_machine_laser.goto(-375 * scale_factor_x, 150 * scale_factor_y)
        elif id == 3:
            self.red_machine_laser.goto(325 * scale_factor_x, 150 * scale_factor_y)
        elif id == 4:
            self.red_machine_laser.goto(-325 * scale_factor_x, 150 * scale_factor_y)
        elif id == 5:
            self.red_machine_laser.goto(275 * scale_factor_x, 150 * scale_factor_y)

        self.red_machine_health_bar = turtle.Turtle()
        self.red_machine_health_bar.shape(HEALTH_BAR_22_TEXTURE)
        # Ensure that the turtle does not draw lines on the screen while moving
        self.red_machine_health_bar.penup()
        self.red_machine_health_bar.shapesize(1 * scale_factor_y, 1 * scale_factor_x)
        # Correct location based on id
        if id == 1:
            self.red_machine_health_bar.goto(375 * scale_factor_x, 295 * scale_factor_y)
        elif id == 2:
            self.red_machine_health_bar.goto(-375 * scale_factor_x, 295 * scale_factor_y)
        elif id == 3:
            self.red_machine_health_bar.goto(325 * scale_factor_x, 295 * scale_factor_y)
        elif id == 4:
            self.red_machine_health_bar.goto(-325 * scale_factor_x, 295 * scale_factor_y)
        elif id == 5:
            self.red_machine_health_bar.goto(275 * scale_factor_x, 295 * scale_factor_y)

        self.death_count = 0
        self.health_bar = 2
        self.hit_delay = 0
        self.update = 0
        self.movement = 1
        self.float = 1
        self.start_y_float = 0
        self.float_activated = 0
        self.start_time = 0
        self.hit_start_time = 0
        self.laser_start_time = 0
        self.move_start_time = time.time()
        self.float_start_time = time.time()
        self.laser_has_attacked = 0
        self.movement_activated = 0
        self.id = id

        # For collision
        self.enemy_center = self.red_machine.ycor()
        self.float_time_offset = time.time()
        self.x_range_list = [(0, 0)] * machine_mode_setup.laser_count
        self.collision_y_coordinate_list = [0] * machine_mode_setup.laser_count
        self.thorns_initiated_damage = 0

        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def __del__(self):
        """
            Cleans up the sprite from memory once the program has terminated

            :return: None
        """

        self.red_machine.hideturtle()
        self.red_machine_laser.hideturtle()
        self.red_machine_health_bar.hideturtle()
        self.red_machine.clear()
        self.red_machine_laser.clear()
        self.red_machine_health_bar.clear()
        del self.red_machine
        del self.red_machine_laser
        del self.red_machine_health_bar

    def reinstate(self, id):
        """
            Reuses the existing sprite to spawn a red machine on the screen with the correct id

            :param id: Ths id of the new red machine (Determines where it spawns and its keeps track of how many are
                on the screen)
            :type id: int

            :return: None
        """

        self.red_machine.shape(RED_MACHINE_TEXTURE)
        self.red_machine_health_bar.shape(HEALTH_BAR_22_TEXTURE)
        # Correct location based on id
        if id == 1:
            self.red_machine.goto(375 * self.scale_factor_x, 220 * self.scale_factor_y)
            self.red_machine_laser.goto(375 * self.scale_factor_x, 150 * self.scale_factor_y)
            self.red_machine_health_bar.goto(375 * self.scale_factor_x, 295 * self.scale_factor_y)
        elif id == 2:
            self.red_machine.goto(-375 * self.scale_factor_x, 220 * self.scale_factor_y)
            self.red_machine_laser.goto(-375 * self.scale_factor_x, 150 * self.scale_factor_y)
            self.red_machine_health_bar.goto(-375 * self.scale_factor_x, 295 * self.scale_factor_y)
        elif id == 3:
            self.red_machine.goto(325 * self.scale_factor_x, 220 * self.scale_factor_y)
            self.red_machine_laser.goto(325 * self.scale_factor_x, 150 * self.scale_factor_y)
            self.red_machine_health_bar.goto(325 * self.scale_factor_x, 295 * self.scale_factor_y)
        elif id == 4:
            self.red_machine.goto(-325 * self.scale_factor_x, 220 * self.scale_factor_y)
            self.red_machine_laser.goto(-325 * self.scale_factor_x, 150 * self.scale_factor_y)
            self.red_machine_health_bar.goto(-325 * self.scale_factor_x, 295 * self.scale_factor_y)
        elif id == 5:
            self.red_machine.goto(275 * self.scale_factor_x, 220 * self.scale_factor_y)
            self.red_machine_laser.goto(275 * self.scale_factor_x, 150 * self.scale_factor_y)
            self.red_machine_health_bar.goto(275 * self.scale_factor_x, 295 * self.scale_factor_y)

        self.enemy_center = self.red_machine.ycor()
        self.float_time_offset = time.time()

        self.x_range_list = [(0, 0)] * machine_mode_setup.laser_count
        self.collision_y_coordinate_list = [0] * machine_mode_setup.laser_count

        self.red_machine.direction = "down"
        self.red_machine_laser.direction = "down"

        # Set the id to the new id
        self.id = id
        self.red_machine.showturtle()
        self.red_machine_laser.showturtle()
        self.red_machine_health_bar.showturtle()

        self.move_start_time = time.time()
        self.float_start_time = time.time()

    def get_red_machine(self):
        """
            Returns the red_machine sprite so its class attributes can be accessed

            :return: red_machine: the red machine sprite
            :type: turtle.Turtle()
        """

        return self.red_machine

    def get_red_machine_laser(self):
        """
            Returns the red_machine_laser sprite so its class attributes can be accessed

            :return: red_machine_laser: the red machine laser sprite
            :type: turtle.Turtle()
        """

        return self.red_machine_laser

    def get_red_machine_health_bar(self):
        """
            Returns the red_machine_health_bar sprite so its class attributes can be accessed

            :return: red_machine_health_bar: the red machine health bar sprite
            :type: turtle.Turtle()
        """

        return self.red_machine_health_bar

    def get_update_value(self):
        """
            Returns the death animation update value of the red machine

            :return: update: the death animation update value of the red machine
            :type: float
        """

        return self.update

    def get_hit_value(self):
        """
            Returns the hit delay value of the red machine

            :return: hit_delay: the hit delay value of the red machine
            :type: int
        """

        return self.hit_delay

    def set_laser_has_attacked(self, new_value):
        """
            Sets the laser_has_attacked of the red machine (Used for when the player fires a new laser and this value
                has to be reset to 0)

            :param new_value: The new laser_has_attacked of the red machine.
            :type new_value: int

            :return: None
        """

        self.laser_has_attacked = new_value

    def remove(self):
        """
            Removes the red machine sprite form the screen and resets its attributes.

            :return: None
        """

        self.red_machine.hideturtle()
        self.red_machine_laser.hideturtle()
        self.red_machine_health_bar.hideturtle()
        self.death_count = 0
        self.hit_delay = 0
        self.health_bar = 2
        self.update = 0
        self.movement = 1
        self.float = 1
        self.start_y_float = 0
        self.float_activated = 0
        self.start_time = 0
        self.hit_start_time = 0
        self.laser_start_time = 0
        self.move_start_time = 0
        self.float_start_time = 0
        self.laser_has_attacked = 0
        self.movement_activated = 0
        self.x_range_list.clear()
        self.collision_y_coordinate_list.clear()
        self.thorns_initiated_damage = 0

    def remove_collisions(self):
        """
            Clears and resets the machines hitboxes so they can be recreated.

            :return: None
        """

        # Clear the lists
        self.x_range_list.clear()
        self.collision_y_coordinate_list.clear()

        # Initialize lists with the required number of elements
        self.x_range_list = [(0, 0)] * machine_mode_setup.laser_count
        self.collision_y_coordinate_list = [0] * machine_mode_setup.laser_count

    def shoot_laser(self, green_power_up, shooting_sound):
        """
            Shoots the red machine laser (Spawning it right below the sprite) and move it down across the screen

            :param green_power_up: Variable used to determine if the green power up is active or not. If it is active,
                the enemy laser will not fire.
            :type green_power_up: int

            :param shooting_sound: Determines whether the toggle for the enemy lasers shooting sound is on. If it is,
                the shooting sound will play when the enemy laser is fired.
            :type shooting_sound: int

            :return: None
        """

        if green_power_up == 0:
            # Remove the laser from the screen once it has hit the player
            if self.laser_has_attacked == 1:
                self.red_machine_laser.hideturtle()
            else:
                self.red_machine_laser.showturtle()
            # If the laser is still visible in the frame of the screen
            if self.red_machine_laser.ycor() > -360 * self.scale_factor_y:
                # Keep moving the laser down the screen 11 units every 0.015 seconds
                current_time = time.time()
                elapsed_time = current_time - self.laser_start_time
                if elapsed_time >= 0.015:
                    # Calculate the delta movement
                    # This the extra movement required to make up for the amount of time passed beyond 0.015 seconds
                    # Done to ensure the game speed stays the same regardless of frame rate
                    delta_movement = 11 * self.scale_factor_y * ((elapsed_time - 0.015) / 0.015)
                    self.red_machine_laser.sety(self.red_machine_laser.ycor() - 11 * self.scale_factor_y - delta_movement)
                    self.laser_start_time = time.time()
            else:
                # Otherwise, set the laser to its original state and shoot it again
                self.red_machine_laser.setx(self.red_machine.xcor())
                self.red_machine_laser.sety(self.red_machine.ycor() - 70 * self.scale_factor_y)
                self.laser_has_attacked = 0
                if shooting_sound == 1:
                    sound = pygame.mixer.Sound("sound/Laser_Gun_Enemy.wav")
                    sound.play()
                self.laser_start_time = time.time()
        # If the green power up is active, hide the laser and do not fire
        else:
            self.red_machine_laser.hideturtle()
            self.red_machine_laser.setx(self.red_machine.xcor())
            self.red_machine_laser.sety(self.red_machine.ycor() - 70 * self.scale_factor_y)
            self.laser_has_attacked = 0
            self.laser_start_time = time.time()

    def kill_enemy(self, death_sound, coins_on_screen, all_coins):
        """
            Kills the enemy and plays the enemies death animation. After that, it spawns the enemy in a new location.

            :param death_sound: Determines if the death sound for the enemy is toggled on or off
            :type death_sound: int

            :param coins_on_screen: Array that lists all of the coins currently on the screen
            :type coins_on_screen: list

            :param all_coins: Array that lists all of the coin sprites generated since the
                programs execution (for reusing purposes)
            :type all_coins: list

            :return: None
        """

        # When the death animation and respawning is finished, the red machine appears on the screen again
        if self.update == 6:
            self.red_machine.showturtle()
            self.red_machine_health_bar.showturtle()
            self.movement_activated = 0
            self.update = 0
            return

        # Wait 0.05 seconds
        if 4 <= self.update < 6:
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            if elapsed_time >= 0.05:
                self.update = 6
                self.start_time = 0
            return

        if self.update == 3.5:
            # Reset the health bar and the enemies health
            self.red_machine_health_bar.goto(self.red_machine.xcor(), self.red_machine.ycor() + 75 * self.scale_factor_y)
            self.red_machine_health_bar.shape(HEALTH_BAR_22_TEXTURE)
            self.health_bar = 2
            self.update = 4
            self.start_time = time.time()
            return

        if self.update == 3:
            # Hide the red machine and spawn a gold coin where the red machine died
            self.red_machine.hideturtle()
            if len(all_coins) <= len(coins_on_screen):
                gold_coin = Coin(type="gold", pos_x=self.red_machine.xcor(), pos_y=self.red_machine.ycor())
                # Set the hitbox for the coin
                gold_coin.range = (gold_coin.coin.xcor() - gold_coin.COIN_DISTANCE, gold_coin.coin.xcor() + gold_coin.COIN_DISTANCE)
                gold_coin.collision_coordinate = gold_coin.coin.ycor() - gold_coin.COIN_DISTANCE
                coins_on_screen.append(gold_coin)
                all_coins.append(gold_coin)
            else:
                for coin in all_coins:
                    if coin.get_coin().isvisible():
                        continue
                    else:
                        coin.reinstate_to_gold(pos_x=self.red_machine.xcor(), pos_y=self.red_machine.ycor())
                        # Set the hitbox for the coin
                        coin.range = (coin.coin.xcor() - coin.COIN_DISTANCE, coin.coin.xcor() + coin.COIN_DISTANCE)
                        coin.collision_coordinate = coin.coin.ycor() - coin.COIN_DISTANCE
                        coins_on_screen.append(coin)
                        break
            # Respawn the red machine in a different random location
            self.red_machine.shape(RED_MACHINE_TEXTURE)
            # Want to cast these ranges to integers to avoid a crash at certain resolutions
            self.red_machine.goto(random.randint(int(-640 * self.scale_factor_x), int(640 * self.scale_factor_x)), random.randint(int(120 * self.scale_factor_y), int(220 * self.scale_factor_y)))
            # Restart the float effect
            self.float_activated = 0
            self.float = 1
            self.float_time_offset = time.time()
            self.enemy_center = self.red_machine.ycor()
            # Reset the hitboxes
            self.x_range_list.clear()
            self.collision_y_coordinate_list.clear()
            self.x_range_list = [(0, 0)] * machine_mode_setup.laser_count
            self.collision_y_coordinate_list = [0] * machine_mode_setup.laser_count
            self.update = 3.5
            return

        # Wait 0.15 seconds
        if 1.5 <= self.update < 3:
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            if elapsed_time >= 0.15:
                self.update = 3
                self.start_time = 0
            return

        # Change the texture of the red machine to the second frame of the explosion
        if 1.0 <= self.update <= 1.1:
            self.red_machine.shape(EXPLOSION_2_TEXTURE)
            self.update = 1.5
            self.start_time = time.time()
            self.kill_enemy(death_sound, coins_on_screen, all_coins)
            return

        # Wait 0.1 seconds
        if 0.5 <= self.update < 1:
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            if elapsed_time >= 0.1:
                self.update = 1
                self.start_time = 0
            return

        if self.update == 0:
            # Increase the death count
            self.death_count = self.death_count + 1
            # Set health to 0 and hide the health bar
            self.health_bar = 0
            self.red_machine_health_bar.hideturtle()
            # Play the death sound
            if death_sound == 1:
                sound = pygame.mixer.Sound("sound/Explosion.wav")
                sound.play()
            # Change the texture of the red machine to the first frame of the death explosion
            self.red_machine.shape(EXPLOSION_1_TEXTURE)
            self.update = 0.5
            # Set the thorns initiated damage back to 0 if needed
            self.thorns_initiated_damage = 0
            self.start_time = time.time()
            return

    def hit_enemy(self, hit_sound):
        """
            Makes the enemy take "one hit" of damage and creates a hit delay before the enemy can be hit again

            :param hit_sound: Determines if the enemy hit sound is toggled on or off
            :type hit_sound: int

            :return: None
        """

        # Reset the hit delay back to 0
        if self.hit_delay == 9:
            self.hit_delay = 0

        # Wait 0.1 seconds
        if 1 <= self.hit_delay < 9:
            current_time = time.time()
            elapsed_time = current_time - self.hit_start_time
            if elapsed_time >= 0.1:
                self.hit_delay = 9
                self.hit_start_time = 0

        if self.update == 0 and self.health_bar == 2:
            # Decrease the enemies health by 1
            self.red_machine_health_bar.shape(HEALTH_BAR_12_TEXTURE)
            if hit_sound == 1:
                sound = pygame.mixer.Sound("sound/Explosion2.wav")
                sound.play()
            self.health_bar = 1
            self.hit_delay = 1
            # Set the thorns initiated damage back to 0 if needed
            self.thorns_initiated_damage = 0
            self.hit_start_time = time.time()

    def float_effect(self):
        """
            Moves the red machine up and down to create a float effect and make it seem as if the enemy is moving
                fast through outer space.

            :return: None
        """

        # Activate the float effect
        if self.float_activated == 0:
            self.float_activated = 1
            self.start_y_float = self.red_machine.ycor()

        if self.start_y_float + 50 * self.scale_factor_y < self.red_machine.ycor():
            # Move down
            self.float = -1
        elif self.start_y_float - 50 * self.scale_factor_y > self.red_machine.ycor():
            # Move up
            self.float = 1
        current_time = time.time()
        elapsed_time = current_time - self.float_start_time
        # Make a movement every 0.0075 seconds to reduce the effects of lag
        if elapsed_time >= 0.0075:
            if self.float == 1:
                # Calculate the delta movement and add it as additional movement required
                delta_movement = machine_mode_setup.MACHINE_FLOAT * ((elapsed_time - 0.0075) / 0.0075)
                self.red_machine.goto(self.red_machine.xcor(), self.red_machine.ycor() + machine_mode_setup.MACHINE_FLOAT + delta_movement)
                self.red_machine_health_bar.goto(self.red_machine.xcor(), self.red_machine.ycor() + 75 * self.scale_factor_y)
            elif self.float == -1:
                # Calculate the delta movement and add it as additional movement required
                delta_movement = machine_mode_setup.MACHINE_FLOAT * ((elapsed_time - 0.0075) / 0.0075)
                self.red_machine.goto(self.red_machine.xcor(), self.red_machine.ycor() - machine_mode_setup.MACHINE_FLOAT - delta_movement)
                self.red_machine_health_bar.goto(self.red_machine.xcor(), self.red_machine.ycor() + 75 * self.scale_factor_y)
            self.float_start_time = time.time()

    def move_enemy(self, death):
        """
            When the red machine has died enough times, this function will cause it to start moving left and
                right, which will speed up the more times that the red machine dies.

            :param death: Determines whether the death animation for the player is active or not.
            :type death: int

            :return: None
        """

        if self.death_count >= 4 and death == 0 and self.update == 0:
            # If the movement has just started, a start time is created for it
            if self.movement_activated == 0:
                self.move_start_time = time.time()
                self.movement_activated = 1
            # Move the red machine every 0.02 seconds
            current_time = time.time()
            elapsed_time = current_time - self.move_start_time
            if elapsed_time >= 0.02:
                # Red machine reaches the right end of the screen
                if 640 * self.scale_factor_x < self.red_machine.xcor():
                    # Move left
                    self.movement = -1
                # Red machine reaches the left end of the screen
                if -640 * self.scale_factor_x > self.red_machine.xcor():
                    # Move right
                    self.movement = 1
                if self.movement == 1:
                    # Speeds up based on the death_count variable
                    if 4 <= self.death_count < 7:
                        # Calculate the delta movement as extra movement needed
                        delta_movement = machine_mode_setup.MACHINE_MOVE_2 * ((elapsed_time - 0.02) / 0.02)
                        self.red_machine.setx(self.red_machine.xcor() + machine_mode_setup.MACHINE_MOVE_2 + delta_movement)
                        self.red_machine_health_bar.goto(self.red_machine.xcor(), self.red_machine.ycor() + 75 * self.scale_factor_y)
                    elif 7 <= self.death_count < 10:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_4 * ((elapsed_time - 0.02) / 0.02)
                        self.red_machine.setx(self.red_machine.xcor() + machine_mode_setup.MACHINE_MOVE_4 + delta_movement)
                        self.red_machine_health_bar.goto(self.red_machine.xcor(), self.red_machine.ycor() + 75 * self.scale_factor_y)
                    elif 10 <= self.death_count < 13:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_6 * ((elapsed_time - 0.02) / 0.02)
                        self.red_machine.setx(self.red_machine.xcor() + machine_mode_setup.MACHINE_MOVE_6 + delta_movement)
                        self.red_machine_health_bar.goto(self.red_machine.xcor(), self.red_machine.ycor() + 75 * self.scale_factor_y)
                    elif 13 <= self.death_count < 16:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_8 * ((elapsed_time - 0.02) / 0.02)
                        self.red_machine.setx(self.red_machine.xcor() + machine_mode_setup.MACHINE_MOVE_8 + delta_movement)
                        self.red_machine_health_bar.goto(self.red_machine.xcor(), self.red_machine.ycor() + 75 * self.scale_factor_y)
                    elif 16 <= self.death_count:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_10 * ((elapsed_time - 0.02) / 0.02)
                        self.red_machine.setx(self.red_machine.xcor() + machine_mode_setup.MACHINE_MOVE_10 + delta_movement)
                        self.red_machine_health_bar.goto(self.red_machine.xcor(), self.red_machine.ycor() + 75 * self.scale_factor_y)
                elif self.movement == -1:
                    if 4 <= self.death_count < 7:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_2 * ((elapsed_time - 0.02) / 0.02)
                        self.red_machine.setx(self.red_machine.xcor() - machine_mode_setup.MACHINE_MOVE_2 - delta_movement)
                        self.red_machine_health_bar.goto(self.red_machine.xcor(), self.red_machine.ycor() + 75 * self.scale_factor_y)
                    elif 7 <= self.death_count < 10:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_4 * ((elapsed_time - 0.02) / 0.02)
                        self.red_machine.setx(self.red_machine.xcor() - machine_mode_setup.MACHINE_MOVE_4 - delta_movement)
                        self.red_machine_health_bar.goto(self.red_machine.xcor(), self.red_machine.ycor() + 75 * self.scale_factor_y)
                    elif 10 <= self.death_count < 13:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_6 * ((elapsed_time - 0.02) / 0.02)
                        self.red_machine.setx(self.red_machine.xcor() - machine_mode_setup.MACHINE_MOVE_6 - delta_movement)
                        self.red_machine_health_bar.goto(self.red_machine.xcor(), self.red_machine.ycor() + 75 * self.scale_factor_y)
                    elif 13 <= self.death_count < 16:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_8 * ((elapsed_time - 0.02) / 0.02)
                        self.red_machine.setx(self.red_machine.xcor() - machine_mode_setup.MACHINE_MOVE_8 - delta_movement)
                        self.red_machine_health_bar.goto(self.red_machine.xcor(), self.red_machine.ycor() + 75 * self.scale_factor_y)
                    elif 16 <= self.death_count:
                        delta_movement = machine_mode_setup.MACHINE_MOVE_10 * ((elapsed_time - 0.02) / 0.02)
                        self.red_machine.setx(self.red_machine.xcor() - machine_mode_setup.MACHINE_MOVE_10 - delta_movement)
                        self.red_machine_health_bar.goto(self.red_machine.xcor(), self.red_machine.ycor() + 75 * self.scale_factor_y)
                self.move_start_time = time.time()
        else:
            self.move_start_time = 0
