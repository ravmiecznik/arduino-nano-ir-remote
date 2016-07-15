__author__ = 'rafal'

import subprocess

key_codes = {
    '40bd8877': 'left_arrow',
    '40bd08f7': 'right_arrow',
    '40bd48b7': 'up_arrow',
    '40bdc837': 'down_arrow',
    '0bda25d': 'power_off'
}

# subprocess_actions = {
#     'desk0': ["xdotool", "set_desktop", "0"],
#     'desk1': ["xdotool", "set_desktop", "1"],
#     'desk2': ["xdotool", "set_desktop", "2"],
#     'desk3': ["xdotool", "set_desktop", "3"],
#     'desk4': ["xdotool", "set_desktop", "4"],
#     'desk5': ["xdotool", "set_desktop", "5"],
#
# }

# def xdotool_change_desktop(key, current_desk=None):
#     #if not current_desk:
#     #    current_desk = subprocess.call(["xdotool", "get_desktop"])
#     print 'cur crd ',current_desk
#     if 'right' in key and current_desk<5:
#         current_desk += 1
#         print 'if crd ',current_desk
#     if 'left' in key and current_desk>0:
#         current_desk -= 1
#     if 'down' in key and current_desk<=2:
#         current_desk += 3
#     if 'up' in key and current_desk>=3:
#         current_desk -= 3
#     print 'crd ',current_desk
#     return ["xdotool", "set_desktop", str(current_desk)]

def remote_key(cmd):
    found_cmd = None
    for k in key_codes:
        if k in cmd:
            found_cmd = key_codes[k]
    return found_cmd



def subprocess_action(key):
    action = None
    if key in subprocess_actions:
        action = subprocess_actions[key]
    return action