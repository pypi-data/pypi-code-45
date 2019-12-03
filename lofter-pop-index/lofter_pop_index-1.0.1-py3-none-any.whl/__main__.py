#     LOFTER-POP-INDEX, an automatic tool used for increase LOFTER blogs' popular index.
#     Copyright (C) 2019 PengFCB
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


import readfile
import exception_func
import chrome_func
import sys
import os


def show_license():
    print('\033[34m')
    t = open("lofter-pop-index/LICENSE/LICENSE.txt")
    for line in t:
        print(line.strip('\n'))
    t.close()
    print()


def judge_args():
    global account, target, ip, flag
    if len(sys.argv) == 4:
        account = sys.argv[1]
        target = sys.argv[2]
        ip = sys.argv[3]
        flag = 1
        if os.path.isfile(account) is False or os.path.isfile(target) is False or os.path.isfile(ip) is False:
            print("\033[31mSOME FILES DON'T EXIST!")
            exit(0)

    elif len(sys.argv) == 3:
        account = sys.argv[1]
        target = sys.argv[2]
        flag = 0
        if os.path.isfile(account) is False or os.path.isfile(target) is False:
            print("\033[31mSOME FILES DON'T EXIST!")
            exit(0)

    else:
        print('\033[33m')
        print("\tUse the program as:")
        print("\tpython3 lofter_pop_index ACCOUNT_ADDR TARGET_ADDR IP_ADDR")
        print("\tEXAMPLE: python3 lofter_pop_index account.txt target.txt ip.txt")
        print()
        print("\tIf you don't want to use proxy, please use the following command:")
        print("\tpython3 lofter_pop_index ACCOUNT_ADDR TARGET_ADDR")
        print("\tEXAMPLE: python3 lofter_pop_index account.txt target.txt")
        print()
        print("\tBefore using the program,  chrome and chromedriver should have been installed in your system!")
        exit(0)


if __name__ == '__main__':
    show_license()
    judge_args()

    max_failure = 10

    if flag:
        ip_list, account_list, target_list = readfile.read_all(ip=ip, account=account, target=target)
    else:
        ip_list = ['']
        account_list, target_list = readfile.read_without_ip(account=account, target=target)
    ip_index = 0
    i = 0
    failure_count = 0

    while i < len(account_list):
        if chrome_func.one_loop(account_list[i], target_list, flag, ip_list[ip_index], 100, 0):
            failure_count = failure_count + 1
            if failure_count == max_failure:
                exception_func.write_unuse(account_list, i, filename='unuse.txt')
            if flag:
                ip_index = (ip_index + 1) % len(ip_list)
            else:
                continue
        else:
            failure_count = 0
            i = i + 1
    print("Done!")

