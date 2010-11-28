#  Copyright (c) 2010 Franz Allan Valencia See
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.__version__ = '0.1'

from connection_manager import ConnectionManager
from query import Query
from assertion import Assertion

class DatabaseLibrary(ConnectionManager, Query, Assertion):
    """
    Contains Database utilities meant for Robot Framework's usage.
    """
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    