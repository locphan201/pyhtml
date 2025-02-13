from typing import List, Any
from .base import Base

class Flex(Base):
    def __init__(
        self,
        value: Any = '',
        class_names: List[str] = []
    ):
        class_names.extend(['flex', 'justify-center', 'items-center'])
        super().__init__(
            tag='div',
            value=value,
            class_names=class_names
        )

class FlexRow(Flex):
    def __init__(
        self,
        value: Any = '',
        class_names: List[str] = []
    ):
        class_names.append('flex-row')
        super().__init__(
            value=value,
            class_names=class_names
        )

class FlexCol(Flex):
    def __init__(
        self,
        value: Any = '',
        class_names: List[str] = []
    ):
        class_names.append('flex-col')
        super().__init__(
            value=value,
            class_names=class_names
        )

