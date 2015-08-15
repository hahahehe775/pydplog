#!/usr/bin/env python
# encoding: utf-8
from pydplog import pydplog
from flup.server.fcgi import WSGIServer
WSGIServer(pydplog,bindAddress='./flask_pydplog.sock').run()
