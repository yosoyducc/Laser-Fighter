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


class TextRefresh:
    def __init__(self, screen, button, panel, textbox, settings, settings_manager, statistics, refresh):
        self._screen = screen
        self._button = button
        self._panel = panel
        self._textbox = textbox
        self._settings = settings
        self._settings_manager = settings_manager
        self._statistics = statistics
        self._refresh = refresh

    def __del__(self):
        del self._screen
        del self._button
        del self._panel
        del self._textbox
        del self._settings
        del self._settings_manager
        del self._statistics
        del self._refresh
