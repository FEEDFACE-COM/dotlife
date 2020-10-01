
from dotlife.util import *


from urllib import request, parse




def get(host,path,params):
    url = "http://" + host + "/" + path
    if params != None:
        url += "?" + parse.urlencode(params)
    rsp = None
    try:
        req = request.Request(url,method="GET")
        debug("get {:s}".format(path))
        rsp = request.urlopen(req)
    except Exception as x: 
        error("fail get from {:s}".format(url))
        error("{:s}".format(str(x)))
    if rsp != None:        
        debug("response {:d}".format(rsp.status))
        return rsp
    return None


def put(host,path,params,data):
    url = "http://" + host + "/" + path
    if params != None:
        url += "?" + parse.urlencode(params)
    rsp = None
    try:
        req = request.Request(url, data=data, method="PUT")
        debug("put {:s}".format(path))
        rsp = request.urlopen(req)
    except Exception as x: 
        error("fail put to {:s}".format(url))
        error("{:s}".format(str(x)))
    if rsp != None:        
        debug("response {:d}".format(rsp.status))
        return rsp
    return None


def post(host,path,params,data):
    url = "http://" + host + "/" + path
    if params != None:
        url += "?" + parse.urlencode(params)
    rsp = None
    if data:
        data = data.encode()
    try:
        req = request.Request(url, data=data, method="POST")
        debug("post {:s}".format(path))
        rsp = request.urlopen(req)
    except Exception as x: 
        error("fail post to {:s}".format(url))
        error("{:s}".format(str(x)))

    if rsp != None:        
        debug("response {:d}".format(rsp.status))
        return rsp
    return None

def delete(host,path,params):
    url = "http://" + host + "/" + path
    if params != None:
        url += "?" + parse.urlencode(params)
    rsp = None
    try:
        req = request.Request(url,method="DELETE")
        debug("delete {:s}".format(path))
        rsp = request.urlopen(req)
    except Exception as x: 
        error("fail delete {:s}".format(url))
        error("{:s}".format(str(x)))
    if rsp != None:        
        debug("response {:d}".format(rsp.status))
        return rsp
    return None
