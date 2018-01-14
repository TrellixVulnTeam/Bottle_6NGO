#! /usr/bin/env python
# coding: utf-8
"""
--------------------------------------------------
    File Name   : app.py
    Description :
    Author      : zrh
    Date        : 2018/1/13
--------------------------------------------------
"""
__author__ = 'zrh'

import sys
from bottle import abort, run, route, request, HTTPResponse, error


@route('/abort', method='POST')
def do_abort():
    data = request.body
    data = data.read().decode('utf-8')
    print(data)
    if data != 'abort':
        abort(400,'your request is not abort')
    return 'abort test'


@route('/httpresponse',method='POST')
def do_httpresponse():
    data = request.body
    data = data.read().decode('utf-8')
    print(data)
    if data!='httpresponse':
        return HTTPResponse(body='your request is not httpresponse',status=400)
    return 'httpresponse test'


@route('/code',method='POST')
def do_code():
    data = request.body
    data = data.read()
    if data != 'code':
        abort(499,'your request is not code')
    return 'code test'


@error(499)
def error499(error):
    return error.body


def main():
    run(server='paste',host='0.0.0.0',port=9001)


if __name__ == "__main__":
    sys.exit(main())