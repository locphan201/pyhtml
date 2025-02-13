from typing import List, Any

class Text:
    def __init__(
        self,
        value: Any = '',
        class_names: List[str] = []
    ):
        self._value = value
        self._class_names = class_names

    @property
    def value(
        self
    ):
        return self._value
    
    @property
    def class_names(
        self
    ):
        return self._class_names
    
    def __repr__(self):
        return f'{self}'
    
    def __str__(self):
        if isinstance(self._value, str):
            inner_html = ''

            
        if len(self._class_names):
            class_names = ' '.join(self._class_names)
            return f'<p class="{class_names}">{self._value}</p>'
        else:
            return f'<p>{self._value}</p>'
    
