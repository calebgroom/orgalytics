# Copyright (c) 2014 Caleb Groom
# All Rights Reserved.
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Things that should happen first (on app entry) go here."""

import argparse
import logging
import os
import sys

import keyring

from orgalytics import github


LOG = logging.getLogger(__name__)


def start():
    """Entry point for orgalytics command."""
    parser = argparse.ArgumentParser(
        description='Github organization statistics')
    parser.add_argument('--user', '-u',
                        default=os.environ.get('GITHUB_USERNAME'),
                        help='Github username')
    parser.add_argument('--password', '-p',
                        default=os.environ.get('GITHUB_PASSWORD'),
                        help='Github password')
    parser.add_argument('--oauth-token', '-t',
                        default=os.environ.get(
                            'GITHUB_OATH_TOKEN',
                            keyring.get_password('github', 'oauth_token')),
                        help="Github OAuth Token")
    parser.add_argument('--ignore-inactive-users',
                        dest='ignore_inactive_users',
                        default=False,
                        action='store_true',
                        help='Ignore users without contributions')
    parser.add_argument('--start-date',
                        help='Ignore contributions before this date, in '
                             'CCYY-MM-DD format')
    parser.add_argument('orgs', nargs='+', help='organization name(s)')
    args = parser.parse_args()

    if not args.oauth_token or all([args.user, args.password]):
        print("Github OAuth token or username and password required.")
        sys.exit(1)

    github.weekly_organization_stats(
        args.orgs,
        user=args.user,
        password=args.password,
        oauth_token=args.oauth_token,
        ignore_inactive_users=args.ignore_inactive_users,
        start_date=args.start_date
    )
