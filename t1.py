#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S',
	filename='mylog.log',
	filemode='a'
)

logging.info("testtest")