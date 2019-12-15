
from luigi import build, LuigiStatusCode

from task import Validation, VennGraph

build([VennGraph(),Validation()], local_scheduler=True, detailed_summary=True)
