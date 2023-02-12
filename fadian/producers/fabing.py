import os
import random
from typing import List, Optional

import yaml

from fadian.constants import TEMPLATE_PATH
from fadian.producer import producer

_sentences: Optional[List[str]] = None


@producer("fabing")
def fabing(name: str) -> str:
    global _sentences
    if not _sentences:
        _sentences = yaml.safe_load(
            open(os.path.join(TEMPLATE_PATH, "fabing.yml"), encoding="utf-8")
        )
    assert _sentences
    return random.choice(_sentences).format(name=name)
