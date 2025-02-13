from typing import List, Dict, Any

class Base:
    def __init__(
        self,
        tag: str,
        value: Any,
        class_names: List[str]
    ):
        self._tag = tag.lower()
        self._value = value
        self._class_names = class_names

    @property
    def tag(self):
        return self._tag

    @property
    def value(self):
        return self._value
    
    @property
    def class_names(self):
        return self._class_names
    
    def __repr__(self):
        return f'{self}'
    
    def __str__(self):
        return self._to_str(indent_level=0)
    
    def _to_str(self, indent_level: int) -> str:
        indent = '  ' * indent_level
        inner_html = ""

        if self._value is None:
            inner_html = ""
        elif isinstance(self._value, str):
            inner_html = f"{'  ' * (indent_level + 1)}{self._value}\n"
        elif isinstance(self._value, list):
            inner_html = '\n'.join(child._to_str(indent_level + 1) for child in self._value)

        class_attr = f' class="{" ".join(self._class_names)}"' if self._class_names else ""
        
        if inner_html:
            return f"{indent}<{self._tag}{class_attr}>\n{inner_html}{indent}</{self._tag}>\n"
        else:
            return f"{indent}<{self._tag}{class_attr}></{self._tag}>\n"
        
class NonValueBase:
    def __init__(
        self,
        tag: str,
        **kwargs: Dict[str, str]
    ):
        self._tag = tag.lower()
        self._attrs = kwargs

    @property
    def tag(self):
        return self._tag
    
    @property
    def attrs(self):
        return self._attrs

    def __repr__(self):
        return f'{self}'
    
    def __str__(self):
        return self._to_str(indent_level=0)
    
    def _to_str(self, indent_level: int) -> str:
        indent = '  ' * indent_level

        attrs = []
        for key, value in self._attrs.items():
            attrs.append(f'{key}="{value}"')
        attrs = ' '.join(attrs)

        if self._tag == 'script':
            return f'{indent}<{self._tag} {attrs}></{self._tag}>'
        else:
            return f'{indent}<{self._tag} {attrs}>'

class Head(Base):
    def __init__(
        self, 
        title: str,
        value: List[Any] = []
    ):
        base_value = [
            NonValueBase('meta', charset='UTF-8'),
            NonValueBase('meta', name='viewport', content="width=device-width, initial-scale=1.0"),
            NonValueBase('script', src='https://unpkg.com/@tailwindcss/browser@4'),
            Base('title', title, [])
        ]
        base_value.extend(value)
        super().__init__(
            tag='head', 
            class_names=[],
            value=base_value
        )

class Body(Base):
    def __init__(
        self, 
        value: Any
    ):
        super().__init__(
            tag='body', 
            value=value, 
            class_names=['w-dvw', 'h-dvh', 'flex', 'flex-col', 'justify-center', 'items-center', 'overflow-x-hidden', 'overflow-y-auto']
        )

class HTML(Base):
    def __init__(
        self, 
        title: str,
        value: Any
    ):
        super().__init__(
            tag='html',
            class_names=[],
            value=[
                Head(title=title),
                Body(value=value)
            ]
        )
    
    def _to_str(self, indent_level: int) -> str:
        indent = '  ' * indent_level
        inner_html = ""

        if self._value is None:
            inner_html = ""
        elif isinstance(self._value, str):
            inner_html = f"{'  ' * (indent_level + 1)}{self._value}\n"
        elif isinstance(self._value, list):
            inner_html = '\n'.join(child._to_str(indent_level + 1) for child in self._value)

        class_attr = f' class="{" ".join(self._class_names)}"' if self._class_names else ""
        
        if inner_html:
            return f'<!DOCTYPE html>\n{indent}<{self._tag} lang="en"{class_attr}>\n{inner_html}{indent}</{self._tag}>\n'
        else:
            return f'<!DOCTYPE html>\n{indent}<{self._tag} lang="en"{class_attr}></{self._tag}>\n'
        