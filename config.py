#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "f027227f-05e5-4e40-97f9-07d7f1eaabbb")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "4-xs.Rc.Ik2.2Kdh7L~NEyd1mOHdb_19j2")
