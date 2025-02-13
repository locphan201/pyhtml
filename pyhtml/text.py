from typing import List, Any
from .base import Base

class Text(Base):
    def __init__(
        self,
        value: Any = '',
        class_names: List[str] = []
    ):
        super().__init__(
            tag='p',
            value=value,
            class_names=class_names
        )

class TextXS(Base):
    def __init__(
        self,
        value: Any = '',
        class_names: List[str] = []
    ):
        class_names.append('text-xs')
        super().__init__(
            tag='p',
            value=value,
            class_names=class_names
        )

class TextSM(Base):
    def __init__(
        self,
        value: Any = '',
        class_names: List[str] = []
    ):
        class_names.append('text-sm')
        super().__init__(
            tag='p',
            value=value,
            class_names=class_names
        )

class TextBase(Base):
    def __init__(
        self,
        value: Any = '',
        class_names: List[str] = []
    ):
        class_names.append('text-base')
        super().__init__(
            tag='p',
            value=value,
            class_names=class_names
        )

class TextLG(Base):
    def __init__(
        self,
        value: Any = '',
        class_names: List[str] = []
    ):
        class_names.append('text-lg')
        super().__init__(
            tag='p',
            value=value,
            class_names=class_names
        )

class TextXL(Base):
    def __init__(
        self,
        value: Any = '',
        class_names: List[str] = []
    ):
        class_names.append('text-xl')
        super().__init__(
            tag='p',
            value=value,
            class_names=class_names
        )

class Text2XL(Base):
    def __init__(
        self,
        value: Any = '',
        class_names: List[str] = []
    ):
        class_names.append('text-2xl')
        super().__init__(
            tag='p',
            value=value,
            class_names=class_names
        )

class Text(Base):
    def __init__(
        self,
        value: Any = '',
        class_names: List[str] = []
    ):
        super().__init__(
            tag='p',
            value=value,
            class_names=class_names
        )

class Heading3(Base):
    def __init__(
        self,
        value: Any = '',
        class_names: List[str] = []
    ):
        class_names.extend(['text-lg', 'font-medium'])
        super().__init__(
            tag='h3',
            value=value,
            class_names=class_names
        )

class Heading2(Base):
    def __init__(
        self,
        value: Any = '',
        class_names: List[str] = []
    ):
        class_names.extend(['text-xl', 'font-semibold'])
        super().__init__(
            tag='h2',
            value=value,
            class_names=class_names
        )

class Heading1(Base):
    def __init__(
        self,
        value: Any = '',
        class_names: List[str] = []
    ):
        class_names.extend(['text-2xl', 'font-bold'])
        super().__init__(
            tag='h1',
            value=value,
            class_names=class_names
        )