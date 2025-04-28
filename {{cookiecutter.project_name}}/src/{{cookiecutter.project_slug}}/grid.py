"""{{ cookiecutter.model_name.upper() }} Rompy grid."""

import logging
from pathlib import Path
from typing import Literal
from pydantic import Field

from rompy.core.grid import BaseGrid, RegularGrid


logger = logging.getLogger(__name__)

HERE = Path(__file__).parent


class Grid(RegularGrid):
    """{{ cookiecutter.model_name.title() }} grid class.

    This is a placeholder for a {{ cookiecutter.model_name.title() }} specific grid class. You do not need to
    implement this class if the existing functionality in one of the existing core
    rompy grid classes (e.g., BaseGrid, RegularGrid) is sufficient.

    """

    model_type: Literal["{{ cookiecutter.model_name.lower() }}"] = Field(
        default="{{ cookiecutter.model_name.lower() }}",
        description="Model type discriminator",
    )
