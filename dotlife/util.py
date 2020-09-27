
import logging, subprocess, pprint, re
import enum




from dotlife.about import NAME

def debugable(): 
    return logging.getLogger(NAME).level <= logging.DEBUG

def debug(s): 
    for l in s.split("\n"): logging.getLogger(NAME).debug(l)
def info(s):  
    for l in s.split("\n"): logging.getLogger(NAME).info(l)
def log(s):   
    for l in s.split("\n"): logging.getLogger(NAME).log(logging.WARNING,l)
def warn(s):  
    for l in s.split("\n"): logging.getLogger(NAME).warning("!! " + l)
def error(s): 
    for l in s.split("\n"): logging.getLogger(NAME).error("!!ERROR! " + l)
def fatal(s): 
    for l in s.split("\n"): 
        logging.getLogger(NAME).critical("!!FATAL! " + l); 
    exit(-2)
def dump(x,s=None): logging.getLogger(NAME).debug( ((s + "\n")  if s else "") + pprint.pformat(x))



class Error(Exception):
    def __init__(self,s):
        self.str = s
    def __str__(self):
        return self.str


class Enum(enum.Enum):
#    def _generate_next_value_(name,s_,c_,l_):
#        return name
    pass

#def auto(): 
#    return enum.auto()


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

