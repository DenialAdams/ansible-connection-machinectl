#!/usr/bin/env python2

# Dynamic inventory for machinectl virtual machines and containers
# (c) 2016, Matt Schreiber <schreibah@gmail.com>
#
# This machinectl dynamic inventory is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

from connection_plugins.machinectl import MachineCtl
from connection_plugins.machinectl import Connection as MachineCtlConnection

import re
import sys
import json

machinectl = MachineCtl()

result = {}
result['all'] = {}
result['all']['hosts'] = [m for m in machinectl.list()]
result['all']['vars'] = dict(machinectl.show())
result['all']['vars']['ansible_connection'] = MachineCtlConnection.transport


if len(sys.argv) == 2 and sys.argv[1] == '--list':
    print(json.dumps(result))
elif len(sys.argv) == 3 and sys.argv[1] == '--host':
    print(json.dumps({'ansible_connection': MachineCtlConnection.transport}))
else:
    print("Need an argument, either --list or --host <host>")
