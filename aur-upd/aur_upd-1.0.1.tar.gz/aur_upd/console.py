
from aur_upd import aur_updater
import os


sudoPassword = ''

if __name__ == '__main__':
    sudoPassword = str(input("Enter sudo password:"))

    home = os.path.expanduser("~") + '/.cache/aurupd'
    if not os.path.isdir(home):
        os.mkdir(home)

    os.chdir(home)

    aur = aur_updater.aur_updater()

    list = aur.get_aur_packages()

    for l in list:
        if l == '':
            continue
        name = l.split(' ')[0]
        ver = l.split(' ')[1]

        v = aur.get_package_current_version(name)

        if v != ver and not (v is None):
            if (aur.clone_package(name)) == 0:
                if aur.build_package(name) == 0:
                    aur.install_package(name, sudoPassword)
                    print('[+] ' + name + ' is updated')
                else:
                    print('[X] ' + name + ' building error')
                    continue
        else:
            if v is None:
                print('[-] ' + name + ' missed in AUR')
            else:
                print('[ ] ' + name + ' is current')





