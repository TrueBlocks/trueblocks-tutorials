#
# This file was generated with makeClass --sdk. Do not edit it.
#
from . import session

stateCmd = "state"
statePos = "addrs"
stateFmt = "json"
stateOpts = {
    "parts": {"hotkey": "-p", "type": "flag"},
    "changes": {"hotkey": "-c", "type": "switch"},
    "noZero": {"hotkey": "-z", "type": "switch"},
    "call": {"hotkey": "-l", "type": "flag"},
    "articulate": {"hotkey": "-a", "type": "switch"},
    "proxyFor": {"hotkey": "-r", "type": "flag"},
    "ether": {"hotkey": "-H", "type": "switch"},
    "cache": {"hotkey": "-o", "type": "switch"},
    "fmt": {"hotkey": "-x", "type": "flag"},
    "verbose:": {"hotkey": "-v", "type": "switch"},
    "help": {"hotkey": "-h", "type": "switch"},
}

def state(self):
    ret = self.toUrl(stateCmd, statePos, stateFmt, stateOpts)
    url = 'http://localhost:8080/' + ret[1]
    if ret[0] == 'json':
        return session.get(url).json()
    return session.get(url).text

