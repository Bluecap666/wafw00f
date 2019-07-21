#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Cloudbric (Penta Security)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<title>Cloudbric \| ERROR!'),
        self.matchContent(r'Your.request.was.blocked.by.Cloudbric'),
        self.matchContent(r'please.contact.Cloudbric.Support'),
        self.matchContent(r'cloudbric.zendesk.com'),
        self.matchContent(r'Cloudbric.Help.Center'),
        self.matchContent(r'Security check by BitNinja'),
        self.matchContent(r'malformed.request.syntax.+?invalid.request.message.framing.+?or.deceptive.request.routing')
    ]
    if any(i for i in schemes):
        return True
    return False