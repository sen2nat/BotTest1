#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "9a13b51f-efab-4b3b-8ea2-4c0a0d5aebcf")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "ciiXeJAgJ5SX5r5B-8PeZe5CO6~-L-2248")
