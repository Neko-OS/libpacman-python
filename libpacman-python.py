import os

def install(package_name, update_all, print_output):
    if update_all == True:
        call = os.popen('pacman -Syu --noconfirm ' + package_name).read()
    elif update_all == False:
        call = os.popen('pacman -Syy --noconfirm ' + package_name).read()
    elif print_output == True:
        print(call)
    else:
        print('Installation canceled')

def remove(package_name, print_output):
    call = os.popen('pacman -R --noconfirm ' + package_name).read()
    if print_output == True:
        print(call)
    else:
        print('Installation canceled')

