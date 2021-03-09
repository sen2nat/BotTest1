#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "f2bf3b20-7b8c-4761-a9c6-7e3703076f43")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "9Okwbvfk-b..SGbvxQc3w2W4jaP80t_.Bx")
