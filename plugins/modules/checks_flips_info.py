#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Mark Mercado <mamercad@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: checks_flips_info
short_description: Get a list of check flips
description:
  - Get a list of check's status changes.
  - Returns a list of "flips" this check has experienced.
  - A flip is a change of status (from "down" to "up," or from "up" to "down").
author: "Mark Mercado (@mamercad)"
version_added: 0.1.0
options:
  state:
    description:
      - C(present) will return the check pings.
    type: str
    choices: ["present"]
    default: present
  baseurl:
    description: The url of the healthchecks.io API to use
    type: str
    default: "https://healthchecks.io/api/v1"
  uuid:
    description:
      - If specified, returns this specific check.
    type: str
    required: false
extends_documentation_fragment:
  - community.healthchecksio.healthchecksio.documentation
"""

EXAMPLES = r"""
- name: Get a list of checks flips
  community.healthchecksio.checks_flips_info:
    state: present
    uuid: cae50618-c97f-483e-9814-0277dc523d1
"""

RETURN = r"""
data:
  description: List of check flips
  returned: always
  type: dict
  sample:
    flips: []
"""


from ansible_collections.community.healthchecksio.plugins.module_utils.healthchecksio import (
    HealthchecksioHelper,
    ChecksFlipsInfo,
)
from ansible.module_utils.basic import AnsibleModule, env_fallback


def run(module):
    state = module.params.pop("state")
    flips = ChecksFlipsInfo(module)
    if state == "present":
        flips.get()


def main():
    argument_spec = HealthchecksioHelper.healthchecksio_argument_spec()
    argument_spec.update(
        state=dict(type="str", choices=["present"], default="present"),
        baseurl=dict(type="str", required=False, default="https://healthchecks.io/api/v1"),
        uuid=dict(type="str", required=False),
    )
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    run(module)


if __name__ == "__main__":
    main()
