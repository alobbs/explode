# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
test_explode
----------------------------------

Tests for `explode` module.
"""

import explode
from explode.tests import base

import os
import tempfile


class TestExplode(base.TestCase):
    def test_build_explode(self):
        MAGIC1 = "First file content"

        # Create temporary dirs
        orig = tempfile.mkdtemp()
        target = tempfile.mkdtemp()

        # Populate source directory
        os.makedirs(os.path.join(orig, "a/ccc/bb/dddd"))
        with open(os.path.join(orig, "a/ccc/file1"), "w+") as f:
            f.write(MAGIC1)

        # Build data and Expand tree
        data = explode.build_data(orig)
        explode.explode_data(data, target)

        for i in range(200):
            print(os.listdir(target))

        # Test everything is in place
        with open(os.path.join(target, "a/ccc/file1"), "r") as f:
            self.assertTrue(MAGIC1 in f.read())

        path = target
        for d in "a/ccc/bb/dddd".split("/"):
            path = os.path.join(path, d)
            self.assertTrue(path)

    def test_something(self):
        pass
