#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Copyright (C) 2019 Christoph Fink, University of Helsinki
#
#   This program is free software; you can redistribute it and/or
#   modify it under the terms of the GNU General Public License
#   as published by the Free Software Foundation; either version 3
#   of the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, see <http://www.gnu.org/licenses/>.

""" Check the probability of rain in Helsinki and send me an
    e-mail to remind me to take the rain gear with me """


import argparse
import statistics
import xml.etree.ElementTree

import requests


r = requests.get(
    "https://api.met.no/weatherapi/locationforecast/1.9/",
    params={
        "lat": 60.17,
        "lon": 24.94
    }
)

x = xml.etree.ElementTree.fromstring(r.text)

if (
        statistics.fmean(
                [
                    float(p.get("value")) 
                    for p in x.findall(
                        "./product/time/location/precipitation"
                    )[:14]
                ]
        ) > 0.1
):
    print("Chance of rain")


