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


import random


def read_ip_proxy(filename="../ip.txt"):
    ip_list = []
    f = open(filename)
    for line in f.readlines():
        line = line.strip()
        ip_list.append(line)
    f.close()
    return ip_list


def read_account(filename="../account.txt"):
    f = open(filename)
    account_list = []
    for line in f.readlines():
        account_list.append(line.strip().split(" "))
    f.close()
    random.shuffle(account_list)
    return account_list


def read_target(filename="../target.txt"):
    f = open(filename)
    target_list = []
    for line in f.readlines():
        line = line.strip()
        target_list.append(line)
    f.close()
    return target_list


def read_all(ip='ip.txt', account='account.txt', target='target.txt'):
    return read_ip_proxy(ip), read_account(account), read_target(target)


def read_without_ip(account, target):
    return read_account(account), read_target(target)


if __name__ == "__main__":
    print(read_ip_proxy())
    print(read_account())
    print(read_target())
