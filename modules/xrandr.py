from subprocess import check_output, call
from collections import defaultdict

def get_screens(preferred_only = False):
    xrandr_out = check_output('xrandr')
    xrandr = str(xrandr_out, encoding='utf8').split('\n')

    screens = defaultdict(dict)
    current_screen_type = None

    for line_num, line in enumerate(xrandr):
        fields = line.split()
        is_screen_type = not line.startswith(' ') and len(line) > 0
        if is_screen_type and 'connected' in fields:
            screen_type = fields[0]
            current_screen_type = screen_type
            screens[current_screen_type] = defaultdict(list)
        elif current_screen_type is not None and 'disconnected' not in fields:
            # we've actually found a screen already, so this is a res line
            if len(fields) > 0:
                res = fields[0]
                ref = fields[1].rstrip('+*')
                if "+" in fields[-1]:
                    # this is the preferred mode so we want it at the start of
                    # the list
                    c_res = screens[current_screen_type]['resolutions']
                    c_ref = screens[current_screen_type]['refresh_rates']
                    screens[current_screen_type]['resolutions'] = c_res + [res]
                    screens[current_screen_type]['refresh_rates'] = (c_ref +
                                                                     [ref])
                elif not preferred_only:
                    screens[current_screen_type]['resolutions'].append(res)
                    screens[current_screen_type]['refresh_rates'].append(ref)
    return screens

def set_modes(screens, off='off'):
    xr_args = get_command_list(screens,off)
    if len(xr_args) > 1:
        call(xr_args)


def get_command_list(screens, off='off'):
    out = ['xrandr']
    for screen, mode in screens.items():
        out.extend(['--output', screen])
        if mode == off:
            out.append('--off')
        else:
            out.extend(['--mode', mode])
    return out

