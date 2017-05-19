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
import json
import logging

import six.moves
import testtools

import daiquiri


class TestDaiquiri(testtools.TestCase):
    def test_setup(self):
        daiquiri.setup()
        daiquiri.setup(level=logging.DEBUG)
        daiquiri.setup(binary="foobar")

    def test_setup_json_formatter(self):
        stream = six.moves.StringIO()
        daiquiri.setup(outputs=(
            daiquiri.output.Stream(
                stream, formatter=daiquiri.output.JSON_FORMATTER),
        ))
        daiquiri.getLogger(__name__).info("foobar")
        self.assertEqual({"message": "foobar", "color": "", "color_stop": ""},
                         json.loads(stream.getvalue()))
