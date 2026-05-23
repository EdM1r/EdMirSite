import os
import sys


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_ROOT_NAME = os.path.basename(PROJECT_ROOT)


def _find_virtualenv_python():
    home_dir = os.path.expanduser("~")
    venv_root = os.path.join(home_dir, "virtualenv", APP_ROOT_NAME)
    if not os.path.isdir(venv_root):
        return None

    candidates = []
    for root, _, files in os.walk(venv_root):
        if os.path.basename(root) != "bin":
            continue
        for name in files:
            if not name.startswith("python"):
                continue
            candidate = os.path.join(root, name)
            if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
                priority = 0
                if name.endswith("_bin"):
                    priority += 10
                if name.startswith("python3"):
                    priority += 5
                candidates.append((priority, candidate))

    if not candidates:
        return None
    candidates.sort(reverse=True)
    return candidates[0][1]


INTERP = _find_virtualenv_python()
if INTERP and os.path.realpath(sys.executable) != os.path.realpath(INTERP):
    os.execl(INTERP, INTERP, *sys.argv)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from wsgi import application
