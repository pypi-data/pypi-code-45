#     LOFTER-POP-INDEX, an automatic tool used for increase LOFTER blogs' popular index.
#     Copyright (C) 2019  PengFCB
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.


def write_unuse(account_list, current_index, filename='unuse.txt'):
    i = current_index
    f = open(filename, 'w')
    while i < len(account_list):
        f.writelines(account_list[i][0]+" "+account_list[i][1]+"\n")
        i = i + 1
    f.close()
    print('Ran out of ip proxy resources, the unfinished accounts have been written in'+filename)
    exit(1)


if __name__ == '__main__':
    exit(0)
