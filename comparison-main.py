# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public Licence as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public Licence for more details.

# You should have received a copy of the GNU General Public Licence
# along with this program.  If not, see https://www.gnu.org/licenses/.

from random import randint, seed
seed()
a = randint(1, 9)
b = randint(1, 9)
c = randint(1, 9)
if a > b:
    if b > c:
        highest = a
        middle = b
        lowest = c
    else:
        if a > c:
            highest = a
            middle = c
            lowest = b
        else:
            highest = c
            middle = a
            lowest = b
else:
    if a > c:
        highest = b
        middle = a
        lowest = c
    else:
        if b > c:
            highest = b
            middle = c
            lowest = a
        else:
            highest = c
            middle = b
            lowest = a
            
print(highest)

print(middle)

print(lowest)
