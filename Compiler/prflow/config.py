from pathlib import Path
import os
from config import *

SIZE=os.getenv("SIZE") or "8x32"
DESIGN="RAM{}".format(SIZE)

MARGIN=5

DESIGN_WIDTH=1000
DESIGN_HEIGHT=1000

BUILD_FOLDER="./build/{}".format(DESIGN)

FULL_SAFE_AREA=MARGIN

FULL_WIDTH=DESIGN_WIDTH + FULL_SAFE_AREA
FULL_HEIGHT=DESIGN_HEIGHT + FULL_SAFE_AREA

DOCKER_INTERACTIVE="0"
PROJECT_ROOT = Path(__file__).parent.parent.parent
