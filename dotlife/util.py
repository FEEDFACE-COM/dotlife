
import logging, subprocess, pprint, re
from subprocess import PIPE

from enum import Enum

class Enum(Enum):

    def __str__(self):
        return self.name


class Struct: 
    pass



from dotlife.about import NAME


def _log(msg,level,prefix=""):
    for line in msg.split("\n"): logging.getLogger(NAME).log(level, prefix+line)


def debug(msg): _log(msg,logging.DEBUG)
def info(msg): _log(msg,logging.INFO)
def log(msg): _log(msg,logging.WARNING)
def usage(msg): _log(msg,logging.ERROR)
def error(msg): _log(msg,logging.ERROR,"!!ERROR! ")
def FATAL(msg): _log(msg,logging.DEBUG,"!!FATAL! "); exit(-2)

    

def dump(x,msg=None): logging.getLogger(NAME).debug( ((msg + "\n")  if msg else "") + pprint.pformat(x))


def pausable(): return logging.getLogger(NAME).level < logging.DEBUG



class Error(Exception):
    def __init__(self,s):
        self.str = s
    def __str__(self):
        return self.str




def shell(cmd,inn=None):
    debug("$ " + cmd)
    try:
        child = subprocess.Popen(cmd,stdout=PIPE, stderr=PIPE, stdin=(PIPE if inn else None), shell=True )
        out,err = child.communicate(inn)
    except Exception as x:
        raise OSError("could not execute command {}: {}".format(cmd,x.message))
    if child.returncode >= 127:
        raise OSError("could not execute command {}".format(cmd))
    return out,err,(True if child.returncode == 0 else False)


def popen(cmd, **params):
    debug("| " + " ".join(cmd))
    return subprocess.Popen(cmd,**params)


