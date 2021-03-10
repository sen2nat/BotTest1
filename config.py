#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "6b683274-224a-4016-9871-8c22dd981eb8")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "yKBs_s5iIK4xouc3cG8yGq-B_w-08lN1-~")
