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
    File: TextureSetup.py
    Author: Christian Marinkovich
    Date: 2024-08-01
    Description:
    This file is used to correctly load all of the textures into the game based off whether fullscreen mode is on
        or off.
"""

# Import the current fullscreen configuration
from setup.ConfigurationSetup import settings
fullscreen = settings.fullscreen

# Determine whether to use scaled textures or not based on if fullscreen is on or off
MACHINE_PLAYER_TEXTURE = "textures/player/Player.gif" if fullscreen == 0 else "textures/player/Player_Scaled.gif"
MACHINE_WASHER_TEXTURE = "textures/player/Machine_Washer.gif" if fullscreen == 0 else "textures/player/Machine_Washer_Scaled.gif"
THE_INCINERATOR_TEXTURE = "textures/player/The_Incinerator.gif" if fullscreen == 0 else "textures/player/The_Incinerator_Scaled.gif"
THE_BLACK_HOLE_TEXTURE = "textures/player/The_Black_Hole.gif" if fullscreen == 0 else "textures/player/The_Black_Hole_Scaled.gif"
THE_STAR_KILLER_TEXTURE = "textures/player/The_Star_Killer.gif" if fullscreen == 0 else "textures/player/The_Star_Killer_Scaled.gif"
MACHINE_PLAYER_LASER_TEXTURE = "textures/lasers/Player_Laser.gif" if fullscreen == 0 else "textures/lasers/Player_Laser_Scaled.gif"
MACHINE_WASHER_LASER_TEXTURE = "textures/lasers/Machine_Washer_Laser.gif" if fullscreen == 0 else "textures/lasers/Machine_Washer_Laser_Scaled.gif"
INCINERATOR_LASER_TEXTURE = "textures/lasers/Incinerator_Laser.gif" if fullscreen == 0 else "textures/lasers/Incinerator_Laser_Scaled.gif"
BLACK_HOLE_LASER_TEXTURE = "textures/lasers/The_Black_Hole_Laser.gif" if fullscreen == 0 else "textures/lasers/The_Black_Hole_Laser_Scaled.gif"
STAR_KILLER_LASER_TEXTURE = "textures/lasers/The_Star_Killer_Laser.gif" if fullscreen == 0 else "textures/lasers/The_Star_Killer_Laser_Scaled.gif"
BLUE_MACHINE_TEXTURE = "textures/machines/Enemy(1-5).gif" if fullscreen == 0 else "textures/machines/Enemy(1-5)_Scaled.gif"
BLUE_MACHINE_LASER_TEXTURE = "textures/lasers/Enemy(1-5)_Laser.gif" if fullscreen == 0 else "textures/lasers/Enemy(1-5)_Laser_Scaled.gif"
YELLOW_MACHINE_TEXTURE = "textures/machines/Enemy(6-10).gif" if fullscreen == 0 else "textures/machines/Enemy(6-10)_Scaled.gif"
YELLOW_MACHINE_LASER_TEXTURE = "textures/lasers/Enemy(6-10)_Laser.gif" if fullscreen == 0 else "textures/lasers/Enemy(6-10)_Laser_Scaled.gif"
RED_MACHINE_TEXTURE = "textures/machines/Enemy(11-15).gif" if fullscreen == 0 else "textures/machines/Enemy(11-15)_Scaled.gif"
RED_MACHINE_LASER_TEXTURE = "textures/lasers/Enemy(11-15)_Laser.gif" if fullscreen == 0 else "textures/lasers/Enemy(11-15)_Laser_Scaled.gif"
MACHINE_BOSS_TEXTURE = "textures/machines/Boss.gif" if fullscreen == 0 else "textures/machines/Boss_Scaled.gif"
MACHINE_BOSS_LASER_TEXTURE = "textures/lasers/Boss_Laser.gif" if fullscreen == 0 else "textures/lasers/Boss_Laser_Scaled.gif"
HEALTH_BAR_22_TEXTURE = "textures/healthbars/HealthBar_2.2.gif" if fullscreen == 0 else "textures/healthbars/HealthBar_2.2_Scaled.gif"
HEALTH_BAR_12_TEXTURE = "textures/healthbars/HealthBar_2.1.gif" if fullscreen == 0 else "textures/healthbars/HealthBar_2.1_Scaled.gif"
HEALTH_BAR_1010_TEXTURE = "textures/healthbars/HealthBar_10.10.gif" if fullscreen == 0 else "textures/healthbars/HealthBar_10.10_Scaled.gif"
HEALTH_BAR_910_TEXTURE = "textures/healthbars/HealthBar_10.9.gif" if fullscreen == 0 else "textures/healthbars/HealthBar_10.9_Scaled.gif"
HEALTH_BAR_810_TEXTURE = "textures/healthbars/HealthBar_10.8.gif" if fullscreen == 0 else "textures/healthbars/HealthBar_10.8_Scaled.gif"
HEALTH_BAR_710_TEXTURE = "textures/healthbars/HealthBar_10.7.gif" if fullscreen == 0 else "textures/healthbars/HealthBar_10.7_Scaled.gif"
HEALTH_BAR_610_TEXTURE = "textures/healthbars/HealthBar_10.6.gif" if fullscreen == 0 else "textures/healthbars/HealthBar_10.6_Scaled.gif"
HEALTH_BAR_510_TEXTURE = "textures/healthbars/HealthBar_10.5.gif" if fullscreen == 0 else "textures/healthbars/HealthBar_10.5_Scaled.gif"
HEALTH_BAR_410_TEXTURE = "textures/healthbars/HealthBar_10.4.gif" if fullscreen == 0 else "textures/healthbars/HealthBar_10.4_Scaled.gif"
HEALTH_BAR_310_TEXTURE = "textures/healthbars/HealthBar_10.3.gif" if fullscreen == 0 else "textures/healthbars/HealthBar_10.3_Scaled.gif"
HEALTH_BAR_210_TEXTURE = "textures/healthbars/HealthBar_10.2.gif" if fullscreen == 0 else "textures/healthbars/HealthBar_10.2_Scaled.gif"
HEALTH_BAR_110_TEXTURE = "textures/healthbars/HealthBar_10.1.gif" if fullscreen == 0 else "textures/healthbars/HealthBar_10.1_Scaled.gif"
HEALTH_BAR_33_TEXTURE = "textures/healthbars/HealthBar_3.3.gif" if fullscreen == 0 else "textures/healthbars/HealthBar_3.3_Scaled.gif"
HEALTH_BAR_23_TEXTURE = "textures/healthbars/HealthBar_3.2.gif" if fullscreen == 0 else "textures/healthbars/HealthBar_3.2_Scaled.gif"
HEALTH_BAR_13_TEXTURE = "textures/healthbars/HealthBar_3.1.gif" if fullscreen == 0 else "textures/healthbars/HealthBar_3.1_Scaled.gif"
ARMOR_BAR_10_10_TEXTURE = "textures/armor/ArmorBar_10.10.gif" if fullscreen == 0 else "textures/armor/ArmorBar_10.10_Scaled.gif"
ARMOR_BAR_10_9_TEXTURE = "textures/armor/ArmorBar_10.9.gif" if fullscreen == 0 else "textures/armor/ArmorBar_10.9_Scaled.gif"
ARMOR_BAR_10_8_TEXTURE = "textures/armor/ArmorBar_10.8.gif" if fullscreen == 0 else "textures/armor/ArmorBar_10.8_Scaled.gif"
ARMOR_BAR_10_7_TEXTURE = "textures/armor/ArmorBar_10.7.gif" if fullscreen == 0 else "textures/armor/ArmorBar_10.7_Scaled.gif"
ARMOR_BAR_10_6_TEXTURE = "textures/armor/ArmorBar_10.6.gif" if fullscreen == 0 else "textures/armor/ArmorBar_10.6_Scaled.gif"
ARMOR_BAR_10_5_TEXTURE = "textures/armor/ArmorBar_10.5.gif" if fullscreen == 0 else "textures/armor/ArmorBar_10.5_Scaled.gif"
ARMOR_BAR_10_4_TEXTURE = "textures/armor/ArmorBar_10.4.gif" if fullscreen == 0 else "textures/armor/ArmorBar_10.4_Scaled.gif"
ARMOR_BAR_10_3_TEXTURE = "textures/armor/ArmorBar_10.3.gif" if fullscreen == 0 else "textures/armor/ArmorBar_10.3_Scaled.gif"
ARMOR_BAR_10_2_TEXTURE = "textures/armor/ArmorBar_10.2.gif" if fullscreen == 0 else "textures/armor/ArmorBar_10.2_Scaled.gif"
ARMOR_BAR_10_1_TEXTURE = "textures/armor/ArmorBar_10.1.gif" if fullscreen == 0 else "textures/armor/ArmorBar_10.1_Scaled.gif"
EXPLOSION_1_TEXTURE = "textures/explosions/Explosion1.gif" if fullscreen == 0 else "textures/explosions/Explosion1_Scaled.gif"
EXPLOSION_2_TEXTURE = "textures/explosions/Explosion2.gif" if fullscreen == 0 else "textures/explosions/Explosion2_Scaled.gif"
GROUND_TEXTURE = "textures/ground/Ground.gif" if fullscreen == 0 else "textures/ground/Ground_Scaled.gif"
SUN_TEXTURE = "textures/background/Sun.gif" if fullscreen == 0 else "textures/background/Sun_Scaled.gif"
EARTH_TEXTURE = "textures/background/Earth.gif" if fullscreen == 0 else "textures/background/Earth_Scaled.gif"
SPACE_SHIP_TEXTURE = "textures/background/Space_Ship.gif" if fullscreen == 0 else "textures/background/Space_Ship_Scaled.gif"
HUMAN_STILL_RIGHT_TEXTURE = "textures/player/Player_Head_Still_Right.gif" if fullscreen == 0 else "textures/player/Player_Head_Still_Right_Scaled.gif"
HUMAN_STILL_LEFT_TEXTURE = "textures/player/Player_Head_Still_Left.gif" if fullscreen == 0 else "textures/player/Player_Head_Still_Left_Scaled.gif"
HUMAN_WALKING_RIGHT_TEXTURE = "textures/player/Player_Head_Walking_Right.gif" if fullscreen == 0 else "textures/player/Player_Head_Walking_Right_Scaled.gif"
HUMAN_WALKING_LEFT_TEXTURE = "textures/player/Player_Head_Walking_Left.gif" if fullscreen == 0 else "textures/player/Player_Head_Walking_Left_Scaled.gif"
PLAYER_HEAD_LASER_TEXTURE = "textures/lasers/Player_Head_Laser.gif" if fullscreen == 0 else "textures/lasers/Player_Head_Laser_Scaled.gif"
THE_COOKER_LASER_TEXTURE = "textures/lasers/The_Cooker_Laser.gif" if fullscreen == 0 else "textures/lasers/The_Cooker_Laser_Scaled.gif"
POISON_DART_LASER_TEXTURE = "textures/lasers/Poison_Dart_Laser.gif" if fullscreen == 0 else "textures/lasers/Poison_Dart_Laser_Scaled.gif"
METEOR_GUN_LASER_RIGHT_TEXTURE = "textures/lasers/Meteor_Gun_Laser_Right.gif" if fullscreen == 0 else "textures/lasers/Meteor_Gun_Laser_Right_Scaled.gif"
METEOR_GUN_LASER_LEFT_TEXTURE = "textures/lasers/Meteor_Gun_Laser_Left.gif" if fullscreen == 0 else "textures/lasers/Meteor_Gun_Laser_Left_Scaled.gif"
SUPERNOVA_LASER_RIGHT_TEXTURE = "textures/lasers/The_Supernova_Laser_Right.gif" if fullscreen == 0 else "textures/lasers/The_Supernova_Laser_Right_Scaled.gif"
SUPERNOVA_LASER_LEFT_TEXTURE = "textures/lasers/The_Supernova_Laser_Left.gif" if fullscreen == 0 else "textures/lasers/The_Supernova_Laser_Left_Scaled.gif"
PLAYER_GUN_RIGHT_TEXTURE = "textures/gun/Player_Gun_Right.gif" if fullscreen == 0 else "textures/gun/Player_Gun_Right_Scaled.gif"
PLAYER_GUN_LEFT_TEXTURE = "textures/gun/Player_Gun_Left.gif" if fullscreen == 0 else "textures/gun/Player_Gun_Left_Scaled.gif"
THE_COOKER_RIGHT_TEXTURE = "textures/gun/The_Cooker_Right.gif" if fullscreen == 0 else "textures/gun/The_Cooker_Right_Scaled.gif"
THE_COOKER_LEFT_TEXTURE = "textures/gun/The_Cooker_Left.gif" if fullscreen == 0 else "textures/gun/The_Cooker_Left_Scaled.gif"
POISON_DART_GUN_RIGHT_TEXTURE = "textures/gun/Poison_Dart_Gun_Right.gif" if fullscreen == 0 else "textures/gun/Poison_Dart_Gun_Right_Scaled.gif"
POISON_DART_GUN_LEFT_TEXTURE = "textures/gun/Poison_Dart_Gun_Left.gif" if fullscreen == 0 else "textures/gun/Poison_Dart_Gun_Left_Scaled.gif"
METEOR_GUN_RIGHT_TEXTURE = "textures/gun/Meteor_Gun_Right.gif" if fullscreen == 0 else "textures/gun/Meteor_Gun_Right_Scaled.gif"
METEOR_GUN_LEFT_TEXTURE = "textures/gun/Meteor_Gun_Left.gif" if fullscreen == 0 else "textures/gun/Meteor_Gun_Left_Scaled.gif"
SUPERNOVA_RIGHT_TEXTURE = "textures/gun/Supernova_Right.gif" if fullscreen == 0 else "textures/gun/Supernova_Right_Scaled.gif"
SUPERNOVA_LEFT_TEXTURE = "textures/gun/Supernova_Left.gif" if fullscreen == 0 else "textures/gun/Supernova_Left_Scaled.gif"
OXYGEN_TANK_TEXTURE = "textures/other/Oxygen_Tank.gif" if fullscreen == 0 else "textures/other/Oxygen_Tank_Scaled.gif"
ALIEN_STILL_LEFT_1_5_TEXTURE = "textures/aliens/Alien_Still_Left(1-5).gif" if fullscreen == 0 else "textures/aliens/Alien_Still_Left(1-5)_Scaled.gif"
ALIEN_STILL_RIGHT_1_5_TEXTURE = "textures/aliens/Alien_Still_Right(1-5).gif" if fullscreen == 0 else "textures/aliens/Alien_Still_Right(1-5)_Scaled.gif"
ALIEN_WALKING_LEFT_1_5_TEXTURE = "textures/aliens/Alien_Walking_Left(1-5).gif" if fullscreen == 0 else "textures/aliens/Alien_Walking_Left(1-5)_Scaled.gif"
ALIEN_WALKING_RIGHT_1_5_TEXTURE = "textures/aliens/Alien_Walking_Right(1-5).gif" if fullscreen == 0 else "textures/aliens/Alien_Walking_Right(1-5)_Scaled.gif"
ALIEN_STILL_LEFT_6_10_TEXTURE = "textures/aliens/Alien_Still_Left(6-10).gif" if fullscreen == 0 else "textures/aliens/Alien_Still_Left(6-10)_Scaled.gif"
ALIEN_STILL_RIGHT_6_10_TEXTURE = "textures/aliens/Alien_Still_Right(6-10).gif" if fullscreen == 0 else "textures/aliens/Alien_Still_Right(6-10)_Scaled.gif"
ALIEN_WALKING_LEFT_6_10_TEXTURE = "textures/aliens/Alien_Walking_Left(6-10).gif" if fullscreen == 0 else "textures/aliens/Alien_Walking_Left(6-10)_Scaled.gif"
ALIEN_WALKING_RIGHT_6_10_TEXTURE = "textures/aliens/Alien_Walking_Right(6-10).gif" if fullscreen == 0 else "textures/aliens/Alien_Walking_Right(6-10)_Scaled.gif"
ALIEN_STILL_LEFT_11_15_TEXTURE = "textures/aliens/Alien_Still_Left(11-15).gif" if fullscreen == 0 else "textures/aliens/Alien_Still_Left(11-15)_Scaled.gif"
ALIEN_STILL_RIGHT_11_15_TEXTURE = "textures/aliens/Alien_Still_Right(11-15).gif" if fullscreen == 0 else "textures/aliens/Alien_Still_Right(11-15)_Scaled.gif"
ALIEN_WALKING_LEFT_11_15_TEXTURE = "textures/aliens/Alien_Walking_Left(11-15).gif" if fullscreen == 0 else "textures/aliens/Alien_Walking_Left(11-15)_Scaled.gif"
ALIEN_WALKING_RIGHT_11_15_TEXTURE = "textures/aliens/Alien_Walking_Right(11-15).gif" if fullscreen == 0 else "textures/aliens/Alien_Walking_Right(11-15)_Scaled.gif"
ALIEN_BOSS_TEXTURE = "textures/aliens/Alien_Boss.gif" if fullscreen == 0 else "textures/aliens/Alien_Boss_Scaled.gif"
ALIEN_DEATH_1_TEXTURE = "textures/explosions/Alien_Death_1.gif" if fullscreen == 0 else "textures/explosions/Alien_Death_1_Scaled.gif"
ALIEN_DEATH_2_TEXTURE = "textures/explosions/Alien_Death_2.gif" if fullscreen == 0 else "textures/explosions/Alien_Death_2_Scaled.gif"
PLAYER_DEATH_1_TEXTURE = "textures/explosions/Player_Death_1.gif" if fullscreen == 0 else "textures/explosions/Player_Death_1_Scaled.gif"
PLAYER_DEATH_2_TEXTURE = "textures/explosions/Player_Death_2.gif" if fullscreen == 0 else "textures/explosions/Player_Death_2_Scaled.gif"
SOUND_BUTTON_TEXTURE = "textures/buttons/Sound_Button.gif" if fullscreen == 0 else "textures/buttons/Sound_Button_Scaled.gif"
CONTROL_BUTTON_TEXTURE = "textures/buttons/Control_Button.gif" if fullscreen == 0 else "textures/buttons/Control_Button_Scaled.gif"
SETTINGS_MAIN_MENU_BUTTON_TEXTURE = "textures/buttons/Settings_Main_Menu_Button.gif" if fullscreen == 0 else "textures/buttons/Settings_Main_Menu_Button_Scaled.gif"
MAIN_MENU_BUTTON_MAIN_TEXTURE = "textures/buttons/Main_Menu_Button_Main.gif" if fullscreen == 0 else "textures/buttons/Main_Menu_Button_Main_Scaled.gif"
TITLE_SCREEN_BUTTON_TEXTURE = "textures/buttons/Title_Screen_Button.gif" if fullscreen == 0 else "textures/buttons/Title_Screen_Button_Scaled.gif"
TITLE_SCREEN_BUTTON_SMALL_TEXTURE = "textures/buttons/Title_Screen_Button_Small.gif" if fullscreen == 0 else "textures/buttons/Title_Screen_Button_Small_Scaled.gif"
MAIN_MENU_BUTTON_MAIN_HIGHLIGHTED_TEXTURE = "textures/buttons/Main_Menu_Button_Main_Highlighted.gif" if fullscreen == 0 else "textures/buttons/Main_Menu_Button_Main_Highlighted_Scaled.gif"
TITLE_SCREEN_BUTTON_HIGHLIGHTED_TEXTURE = "textures/buttons/Title_Screen_Button_Highlighted.gif" if fullscreen == 0 else "textures/buttons/Title_Screen_Button_Highlighted_Scaled.gif"
TITLE_SCREEN_BUTTON_SMALL_HIGHLIGHTED_TEXTURE = "textures/buttons/Title_Screen_Button_Small_Highlighted.gif" if fullscreen == 0 else "textures/buttons/Title_Screen_Button_Small_Highlighted_Scaled.gif"
BUY_BUTTON_TEXTURE = "textures/buttons/Buy_Button.gif" if fullscreen == 0 else "textures/buttons/Buy_Button_Scaled.gif"
BUY_BUTTON_HIGHLIGHTED_TEXTURE = "textures/buttons/Buy_Button_Highlighted.gif" if fullscreen == 0 else "textures/buttons/Buy_Button_Highlighted_Scaled.gif"
INVENTORY_SLOT_FRAME_TEXTURE = "textures/buttons/Inventory_Slot_Frame.gif" if fullscreen == 0 else "textures/buttons/Inventory_Slot_Frame_Scaled.gif"
INVENTORY_SLOT_FRAME_HIGHLIGHTED_TEXTURE = "textures/buttons/Inventory_Slot_Frame_Highlighted.gif" if fullscreen == 0 else "textures/buttons/Inventory_Slot_Frame_Highlighted_Scaled.gif"
TAB_TEXTURE = "textures/buttons/Tab.gif" if fullscreen == 0 else "textures/buttons/Tab_Scaled.gif"
TAB_HIGHLIGHTED_TEXTURE = "textures/buttons/Tab_Highlighted.gif" if fullscreen == 0 else "textures/buttons/Tab_Highlighted_Scaled.gif"
SIDE_PANEL_SHOP_TEXTURE = "textures/gui/Side_Panel_Shop.gif" if fullscreen == 0 else "textures/gui/Side_Panel_Shop_Scaled.gif"
POP_UP_MESSAGE_FRAME_TEXTURE = "textures/gui/Pop_Up_Message_Frame.gif" if fullscreen == 0 else "textures/gui/Pop_Up_Message_Frame_Scaled.gif"
LOCKED_TEXTURE = "textures/gui/Locked.gif" if fullscreen == 0 else "textures/gui/Locked_Scaled.gif"
TAB_SELECTOR_TEXTURE = "textures/gui/Tab_Selector.gif" if fullscreen == 0 else "textures/gui/Tab_Selector_Scaled.gif"
SLOT_SELECTOR_TEXTURE = "textures/gui/Slot_Selector.gif" if fullscreen == 0 else "textures/gui/Slot_Selector_Scaled.gif"
SETTINGS_AND_CONTROLS_BUTTON_TEXTURE = "textures/buttons/Settings_And_Controls_Button.gif" if fullscreen == 0 else "textures/buttons/Settings_And_Controls_Button_Scaled.gif"
SETTINGS_AND_CONTROLS_BUTTON_HIGHLIGHTED_TEXTURE = "textures/buttons/Settings_And_Controls_Button_Highlighted.gif" if fullscreen == 0 else "textures/buttons/Settings_And_Controls_Button_Highlighted_Scaled.gif"
MACHINE_DEFAULT_DISPLAY_ICON_TEXTURE = "textures/interface/display/Machine_Default_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/Machine_Default_Display_Icon_Scaled.gif"
MACHINE_WASHER_DISPLAY_ICON_TEXTURE = "textures/interface/display/Machine_Washer_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/Machine_Washer_Display_Icon_Scaled.gif"
THE_INCINERATOR_DISPLAY_ICON_TEXTURE = "textures/interface/display/The_Incinerator_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/The_Incinerator_Display_Icon_Scaled.gif"
THE_BLACK_HOLE_DISPLAY_ICON_TEXTURE = "textures/interface/display/The_Black_Hole_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/The_Black_Hole_Display_Icon_Scaled.gif"
THE_STAR_KILLER_DISPLAY_ICON_TEXTURE = "textures/interface/display/The_Star_Killer_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/The_Star_Killer_Display_Icon_Scaled.gif"
ALIEN_DEFAULT_DISPLAY_ICON_TEXTURE = "textures/interface/display/Alien_Default_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/Alien_Default_Display_Icon_Scaled.gif"
THE_COOKER_DISPLAY_ICON_TEXTURE = "textures/interface/display/The_Cooker_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/The_Cooker_Display_Icon_Scaled.gif"
POISON_DART_DISPLAY_ICON_TEXTURE = "textures/interface/display/Poison_Dart_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/Poison_Dart_Display_Icon_Scaled.gif"
METEOR_GUN_DISPLAY_ICON_TEXTURE = "textures/interface/display/Meteor_Gun_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/Meteor_Gun_Display_Icon_Scaled.gif"
SUPERNOVA_DISPLAY_ICON_TEXTURE = "textures/interface/display/Supernova_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/Supernova_Display_Icon_Scaled.gif"
YELLOW_POWER_UP_DISPLAY_ICON_TEXTURE = "textures/interface/display/Yellow_Power_Up_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/Yellow_Power_Up_Display_Icon_Scaled.gif"
BLUE_POWER_UP_DISPLAY_ICON_TEXTURE = "textures/interface/display/Blue_Power_Up_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/Blue_Power_Up_Display_Icon_Scaled.gif"
GREEN_POWER_UP_DISPLAY_ICON_TEXTURE = "textures/interface/display/Green_Power_Up_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/Green_Power_Up_Display_Icon_Scaled.gif"
RED_POWER_UP_DISPLAY_ICON_TEXTURE = "textures/interface/display/Red_Power_Up_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/Red_Power_Up_Display_Icon_Scaled.gif"
COIN_MAGNET_DISPLAY_ICON_TEXTURE = "textures/interface/display/Coin_Magnet_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/Coin_Magnet_Display_Icon_Scaled.gif"
ARMOR_DISPLAY_ICON_TEXTURE = "textures/interface/display/Armor_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/Armor_Display_Icon_Scaled.gif"
THORNS_DISPLAY_ICON_TEXTURE = "textures/interface/display/Thorns_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/Thorns_Display_Icon_Scaled.gif"
HEART_POWER_UP_DISPLAY_ICON_TEXTURE = "textures/interface/display/Heart_Power_Up_Display_Icon.gif" if fullscreen == 0 else "textures/interface/display/Heart_Power_Up_Display_Icon_Scaled.gif"
MACHINE_MODE_TAB_ICON_TEXTURE = "textures/interface/icons/tab/Machine_Mode_Tab_Icon.gif" if fullscreen == 0 else "textures/interface/icons/tab/Machine_Mode_Tab_Icon_Scaled.gif"
GADGETS_TAB_ICON_TEXTURE = "textures/interface/icons/tab/Gadgets_Tab_Icon.gif" if fullscreen == 0 else "textures/interface/icons/tab/Gadgets_Tab_Icon_Scaled.gif"
MACHINE_DEFAULT_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/Machine_Default_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/Machine_Default_Slot_Icon_Scaled.gif"
MACHINE_WASHER_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/Machine_Washer_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/Machine_Washer_Slot_Icon_Scaled.gif"
THE_INCINERATOR_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/The_Incinerator_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/The_Incinerator_Slot_Icon_Scaled.gif"
THE_BLACK_HOLE_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/The_Black_Hole_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/The_Black_Hole_Slot_Icon_Scaled.gif"
THE_STAR_KILLER_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/The_Star_Killer_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/The_Star_Killer_Slot_Icon_Scaled.gif"
ALIEN_DEFAULT_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/Alien_Default_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/Alien_Default_Slot_Icon_Scaled.gif"
THE_COOKER_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/The_Cooker_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/The_Cooker_Slot_Icon_Scaled.gif"
POISON_DART_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/Poison_Dart_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/Poison_Dart_Slot_Icon_Scaled.gif"
METEOR_GUN_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/Meteor_Gun_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/Meteor_Gun_Slot_Icon_Scaled.gif"
SUPERNOVA_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/Supernova_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/Supernova_Slot_Icon_Scaled.gif"
YELLOW_POWER_UP_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/Yellow_Power_Up_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/Yellow_Power_Up_Slot_Icon_Scaled.gif"
RED_POWER_UP_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/Red_Power_Up_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/Red_Power_Up_Slot_Icon_Scaled.gif"
GREEN_POWER_UP_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/Green_Power_Up_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/Green_Power_Up_Slot_Icon_Scaled.gif"
BLUE_POWER_UP_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/Blue_Power_Up_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/Blue_Power_Up_Slot_Icon_Scaled.gif"
COIN_MAGNET_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/Coin_Magnet_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/Coin_Magnet_Slot_Icon_Scaled.gif"
ARMOR_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/Armor_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/Armor_Slot_Icon_Scaled.gif"
THORNS_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/Thorns_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/Thorns_Slot_Icon_Scaled.gif"
HEART_POWER_UP_SLOT_ICON_TEXTURE = "textures/interface/icons/slot/Heart_Power_Up_Slot_Icon.gif" if fullscreen == 0 else "textures/interface/icons/slot/Heart_Power_Up_Slot_Icon_Scaled.gif"
YELLOW_LIGHTNING_POWER_UP_TEXTURE = "textures/powerups/Yellow_Lightning_Power_Up.gif" if fullscreen == 0 else "textures/powerups/Yellow_Lightning_Power_Up_Scaled.gif"
GREEN_LIGHTNING_POWER_UP_TEXTURE = "textures/powerups/Green_Lightning_Power_Up.gif" if fullscreen == 0 else "textures/powerups/Green_Lightning_Power_Up_Scaled.gif"
RED_LIGHTNING_POWER_UP_TEXTURE = "textures/powerups/Red_Lightning_Power_Up.gif" if fullscreen == 0 else "textures/powerups/Red_Lightning_Power_Up_Scaled.gif"
BLUE_LIGHTNING_POWER_UP_TEXTURE = "textures/powerups/Blue_Lightning_Power_Up.gif" if fullscreen == 0 else "textures/powerups/Blue_Lightning_Power_Up_Scaled.gif"
HEART_POWER_UP_TEXTURE = "textures/powerups/Heart_Power_Up.gif" if fullscreen == 0 else "textures/powerups/Heart_Power_Up_Scaled.gif"
BLUE_POWER_UP_INDICATOR_ON_TEXTURE = "textures/powerups/Blue_Power_Up_Indicator_On.gif" if fullscreen == 0 else "textures/powerups/Blue_Power_Up_Indicator_On_Scaled.gif"
GREEN_POWER_UP_INDICATOR_ON_TEXTURE = "textures/powerups/Green_Power_Up_Indicator_On.gif" if fullscreen == 0 else "textures/powerups/Green_Power_Up_Indicator_On_Scaled.gif"
YELLOW_POWER_UP_INDICATOR_ON_TEXTURE = "textures/powerups/Yellow_Power_Up_Indicator_On.gif" if fullscreen == 0 else "textures/powerups/Yellow_Power_Up_Indicator_On_Scaled.gif"
RED_POWER_UP_INDICATOR_ON_TEXTURE = "textures/powerups/Red_Power_Up_Indicator_On.gif" if fullscreen == 0 else "textures/powerups/Red_Power_Up_Indicator_On_Scaled.gif"
BLUE_POWER_UP_INDICATOR_OFF_TEXTURE = "textures/powerups/Blue_Power_Up_Indicator_Off.gif" if fullscreen == 0 else "textures/powerups/Blue_Power_Up_Indicator_Off_Scaled.gif"
GREEN_POWER_UP_INDICATOR_OFF_TEXTURE = "textures/powerups/Green_Power_Up_Indicator_Off.gif" if fullscreen == 0 else "textures/powerups/Green_Power_Up_Indicator_Off_Scaled.gif"
YELLOW_POWER_UP_INDICATOR_OFF_TEXTURE = "textures/powerups/Yellow_Power_Up_Indicator_Off.gif" if fullscreen == 0 else "textures/powerups/Yellow_Power_Up_Indicator_Off_Scaled.gif"
RED_POWER_UP_INDICATOR_OFF_TEXTURE = "textures/powerups/Red_Power_Up_Indicator_Off.gif" if fullscreen == 0 else "textures/powerups/Red_Power_Up_Indicator_Off_Scaled.gif"
COPPER_COIN_TEXTURE = "textures/coins/Copper_Coin.gif" if fullscreen == 0 else "textures/coins/Copper_Coin_Scaled.gif"
SILVER_COIN_TEXTURE = "textures/coins/Silver_Coin.gif" if fullscreen == 0 else "textures/coins/Silver_Coin_Scaled.gif"
GOLD_COIN_TEXTURE = "textures/coins/Gold_Coin.gif" if fullscreen == 0 else "textures/coins/Gold_Coin_Scaled.gif"
PLATINUM_COIN_TEXTURE = "textures/coins/Platinum_Coin.gif" if fullscreen == 0 else "textures/coins/Platinum_Coin_Scaled.gif"
COIN_INDICATOR_TEXTURE = "textures/coins/Coin_Indicator.gif" if fullscreen == 0 else "textures/coins/Coin_Indicator_Scaled.gif"
