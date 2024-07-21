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

from setup.ScreenSetup import scale_factor
from setup.ScreenSetup import scale_factor_X
from setup.ScreenSetup import scale_factor_Y
from setup.ScreenSetup import fullscreen
from components.spawn.SpawnButton import SpawnButton
from components.spawn.SpawnTextBox import SpawnTextbox
from components.spawn.SpawnGUI import SpawnPanel
from components.spawn.SpawnGUI import SpawnSelector
from components.spawn.SpawnGUI import SpawnPriceLabel

button = SpawnButton(scale_factor, scale_factor_X, scale_factor_Y)

textbox = SpawnTextbox(scale_factor, scale_factor_X)

panel = SpawnPanel(scale_factor, scale_factor_X, scale_factor_Y)

selector = SpawnSelector(scale_factor_X, scale_factor_Y)

price_label = SpawnPriceLabel()
