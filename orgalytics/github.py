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

import datetime

import github3


def weekly_organization_stats(organization_names, user, password):
    """Print weekly summary data for all repos in organizations."""
    github_client = github3.login(user, password=password)
    weeks = {}
    for organization_name in organization_names:
        organization = github_client.organization(organization_name)

        for repo in organization.iter_repos():
            print("Looking at %s/%s" % (organization_name, repo.name))
            for contrib in repo.iter_contributor_statistics():
                user = contrib.author.login
                for week_data in contrib.weeks:
                    week = week_data['w']
                    if not week in weeks:
                        weeks[week] = {}
                    if user not in weeks[week]:
                        weeks[week][user] = {'a': week_data['a'],
                                             'c': week_data['c'],
                                             'd': week_data['d']}
                    else:
                        weeks[week][user]['a'] += week_data['a']
                        weeks[week][user]['c'] += week_data['c']
                        weeks[week][user]['d'] += week_data['d']

    for week in sorted(weeks.keys()):
        week_timestamp = datetime.datetime.fromtimestamp(week)
        print("\nWeek beginning %s" % week_timestamp)
        for user in sorted(weeks[week].keys()):
            row_format = "    {:<20}      {} commits (+{}, -{})"
            user_data = weeks[week][user]
            print row_format.format(
                user, user_data['c'], user_data['a'], user_data['d'])
