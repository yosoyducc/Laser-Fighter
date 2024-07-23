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


class Hover:
    def __init__(self, mode, button):
        self._mode = mode
        self._button = button

    def __del__(self):
        del self._mode
        del self._button

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        if isinstance(value, str):
            self._mode = value
        else:
            raise ValueError("Mode must be a string")

    def hover(self, event):
        """
            Change the color of the button text to yellow when the mouse is hovering over it.
            It also changes the colors to red/orange for the control buttons based on if there is a keybind conflict or not.

            :param event: Holds the current position of the cursor on the screen
            :type event: tkinter.Event()

            :return: None
        """

        # Extract x and y coordinate of the cursor
        a, b = event.x, event.y
        # Update button text as needed
        if self._mode == "Title_Mode":
            for bu in self._button.buttons_on_screen_list:
                bu.update_highlight(a, b)
        if self._mode == "Machine_Mode" or self._mode == "Alien_Mode" or self._mode == "Stats" or self._mode == "Shop":
            for bu in self._button.buttons_on_screen_list:
                self._button.button_update = bu.update_highlight(a, b)
        if self._mode == "Settings":
            for bu in self._button.buttons_on_screen_list:
                if bu.type == "Regular_Settings_And_Controls":
                    if bu.id == 1:
                        self._button.button_update = bu.update_highlight(a, b)
                    else:
                        bu.update_highlight(a, b)
                else:
                    bu.update_highlight(a, b)
        if self._mode == "Controls":
            for bu in self._button.buttons_on_screen_list:
                if bu.type == "Regular_Settings_And_Controls":
                    if bu.id == 1:
                        self._button.button_update = bu.update_highlight(a, b)
                    else:
                        bu.update_highlight(a, b)
                elif bu.type == "Controls_Toggle":
                    bu.update_highlight(a, b)