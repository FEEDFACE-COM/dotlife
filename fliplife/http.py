
import dotlife
from dotlife.util import *


from urllib import request, parse


#def debug(s): pass
    
    


def get(host,path,params):
    proto = "http"
    url = proto + "://" + host + "/" + path
    if params != None:
        url += "?" + parse.urlencode(params)
    rsp = None
    try:
        req = request.Request(url,method="GET")
        debug("get {:s}".format(url))
        rsp = request.urlopen(req)
    except Exception as x: 
        error("fail get from {:s}".format(url))
        error("{:s}".format(str(x)))
    if rsp == None:
        error("get {:s}/{:s}: no response".format(host,path))
        return None
    if rsp.status != 200:
        error("get {:s}/{:s}: {:d} response".format(host,path,rsp.status))
        return None
    return rsp


def put(host,path,params,data):
    proto = "http"
    url = proto + "://" + host + "/" + path
    if params != None:
        url += "?" + parse.urlencode(params)
    rsp = None
    try:
        req = request.Request(url, data=data, method="PUT")
        debug("put {:s}".format(url))
        rsp = request.urlopen(req)
    except Exception as x: 
        error("fail put to {:s}".format(url))
        error("{:s}".format(str(x)))
    if rsp == None:
        error("put {:s}/{:s}: no response".format(host,path))
        return None
    if rsp.status != 200:
        error("put {:s}/{:s}: {:d} response".format(host,path,rsp.status))
        return None
    return rsp


def post(host,path,params,data):
    proto = "http"
    url = proto + "://" + host + "/" + path
    if params != None:
        url += "?" + parse.urlencode(params)
    rsp = None
    if data:
        data = data.encode()
    try:
        req = request.Request(url, data=data, method="POST")
        debug("post {:s}".format(url))
        rsp = request.urlopen(req)
    except Exception as x: 
        error("fail post to {:s}".format(url))
        error("{:s}".format(str(x)))
    if rsp == None:
        error("post {:s}/{:s}: no response".format(host,path))
        return None
    if rsp.status != 200:
        error("post {:s}/{:s}: {:d} response".format(host,path,rsp.status))
        return None
    return rsp


def delete(host,path,params):
    proto = "http"
    url = proto + "://" + host + "/" + path
    if params != None:
        url += "?" + parse.urlencode(params)
    rsp = None
    try:
        req = request.Request(url,method="DELETE")
        debug("delete {:s}".format(url))
        rsp = request.urlopen(req)
    except Exception as x: 
        error("fail delete {:s}".format(url))
        error("{:s}".format(str(x)))
    if rsp == None:
        error("delete {:s}/{:s}: no response".format(host,path))
        return None
    if rsp.status != 200:
        error("delete {:s}/{:s}: {:d} response".format(host,path,rsp.status))
        return None
    return rsp
