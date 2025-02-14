from typing import List, Dict, Any
from .theme import *

class Base:
    def __init__(self, **kwargs) -> None:
        self._tag = kwargs.get('tag', 'div').lower()
        self._children = kwargs.get('children', [])
        self._class_names = kwargs.get('class_names', [])
        self._attrs = {}
        for key, value in kwargs.items():
            if key in ['tag', 'children', 'class_names']:
                continue
            self._attrs[key] = value

    @property
    def tag(self) -> str:
        return self._tag

    @property
    def children(self) -> Any:
        return self._children
    
    @property
    def class_names(self) -> List[str]:
        return self._class_names

    @property
    def attrs(self) -> Dict[str, str]:
        return self._attrs
    
    def __repr__(self) -> str:
        return f'{self}'
    
    def __str__(self) -> str:
        return self._to_str(indent_level=0)
    
    def _to_str(self, indent_level: int) -> str:
        indent = '  ' * indent_level
        inner_html = ''

        if self._children is None:
            inner_html = ''
        elif isinstance(self._children, str):
            inner_html = f"{'  ' * (indent_level + 1)}{self._children}\n"
        elif isinstance(self._children, list):
            inner_html = ''.join(child._to_str(indent_level + 1) for child in self._children)

        classes = f' class="{" ".join(self._class_names)}"' if self._class_names else ''

        attrs = '' 
        if len(self._attrs.keys()):
            attrs = ' ' + ' '.join([f'{key}="{value}"' for key, value in self._attrs.items()])
        
        if inner_html:
            return f"{indent}<{self._tag}{classes}{attrs}>\n{inner_html}{indent}</{self._tag}>\n"
        else:
            return f"{indent}<{self._tag}{classes}{attrs}></{self._tag}>\n"

class Title(Base):
    def __init__(self, title: str = 'Document'):
        super().__init__(tag='title', children=title)

class Meta(Base):
    def __init__(self, **kwargs) -> None:
        super().__init__(tag='meta', **kwargs)

class Link(Base):
    def __init__(self, **kwargs) -> None:
        super().__init__(tag='link', **kwargs)

class Script(Base):
    def __init__(self, **kwargs) -> None:
        super().__init__(tag='script', **kwargs)

class Style(Base):
    def __init__(self, **kwargs):
        super().__init__(tag='style', **kwargs)

class Head(Base):
    def __init__(self, **kwargs) -> None:
        theme_color = f'''
            --light-primary: {DEFAULT_LIGHT_COLOR_SCHEME.PRIMARY};
            --light-secondary: {DEFAULT_LIGHT_COLOR_SCHEME.SECONDARY};
            --light-tertiary: {DEFAULT_LIGHT_COLOR_SCHEME.TERTIARY};
            --dark-primary: {DEFAULT_DARK_COLOR_SCHEME.PRIMARY};
            --dark-secondary: {DEFAULT_DARK_COLOR_SCHEME.SECONDARY};
            --dark-tertiary: {DEFAULT_DARK_COLOR_SCHEME.TERTIARY};
        '''

        base_value = [
            Meta(charset='UTF-8'),
            Meta(name='viewport', content="width=device-width, initial-scale=1.0"),
            Link(rel='stylesheet', href='https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0'),
            Script(src='https://unpkg.com/@tailwindcss/browser@4'),
            Style(type='text/tailwindcss', children=f'@theme{{{theme_color}}}'),
            Title(title=kwargs.get('title', 'Document'))
        ]

        try:
            base_value.extend(children=kwargs.get('children', []))
        except:
            pass

        super().__init__(tag='head', children=base_value, **kwargs)

class Body(Base):
    def __init__(self, **kwargs) -> None:
        class_names = kwargs.pop('class_names', [])
        class_names.extend(['w-dvw', 'h-dvh', 'flex', 'flex-col', 'justify-center', 'items-center', 'overflow-x-hidden', 'overflow-y-auto'])
        super().__init__(
            tag='body', 
            class_names=class_names,
            **kwargs
        )

class HTML(Base):
    def __init__(self, **kwargs) -> None:
        super().__init__(
            tag='html',
            lang='en',
            children=[
                Head(title=kwargs.get('title', 'Document')),
                Body(children=kwargs.get('children', []))
            ],
        )

    def _to_str(self, indent_level: int) -> str:
        indent = '  ' * indent_level
        inner_html = ''

        if self._children is None:
            inner_html = ""
        elif isinstance(self._children, str):
            inner_html = f"{'  ' * (indent_level + 1)}{self._children}\n"
        elif isinstance(self._children, list):
            inner_html = '\n'.join(child._to_str(indent_level + 1) for child in self._children)

        classes = f' class="{" ".join(self._class_names)}"' if self._class_names else ""
        
        attrs = '' 
        if len(self._attrs.keys()):
            attrs = ' ' + ' '.join([f'{key}="{value}"' for key, value in self._attrs.items()])

        return f'<!DOCTYPE html>\n{indent}<{self._tag}{classes}{attrs}>\n{inner_html}{indent}</{self._tag}>\n'

class Text(Base):
    def __init__(self, **kwargs) -> None:
        super().__init__(tag='p', **kwargs)

class Label(Base):
    def __init__(self, **kwargs) -> None:
        super().__init__(tag='label', **kwargs)

class Span(Base):
    def __init__(self, **kwargs) -> None:
        super().__init__(tag='span', **kwargs)

class Row(Base):
    def __init__(self, **kwargs) -> None:
        class_names = kwargs.pop('class_names', [])
        class_names.extend(['flex', 'justify-center', 'items-center', 'gap-2'])
        super().__init__(
            tag='div',
            class_names=class_names,
            **kwargs
        )

class Column(Row):
    def __init__(self, **kwargs) -> None:
        class_names = kwargs.pop('class_names', [])
        class_names.append('flex-col')
        super().__init__(
            class_names=class_names,
            **kwargs
        )

class Input(Base):
    def __init__(self, **kwargs) -> None:
        class_names = kwargs.pop('class_names', [])
        class_names.extend(['rounded-lg', 'p-2.5', 'border'])
        super().__init__(
            tag='input', 
            class_names=class_names,
            **kwargs
        )

class Form(Base):
    def __init__(self, **kwargs) -> None:
        class_names = kwargs.pop('class_names', [])
        class_names.extend(['flex', 'flex-col', 'justify-center', 'items-center', 'gap-2', 'border', 'rounded-lg', 'p-5'])
        super().__init__(
            tag='form', 
            class_names=class_names,
            **kwargs
        )

class Anchor(Base):
    def __init__(self, **kwargs) -> None:
        class_names = kwargs.pop('class_names', [])
        class_names.extend(['cursor-pointer'])
        super().__init__(
            tag='a', 
            class_names=class_names,
            **kwargs
        )

class A(Anchor):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

class Button(Base):
    def __init__(self, **kwargs) -> None:
        class_names = kwargs.pop('class_names', [])
        class_names.extend(['flex', 'justify-center', 'items-center', 'gap-2', 'rounded-lg', 'p-2.5', 'cursor-pointer', 'hover:opacity-75'])
        super().__init__(
            tag='button', 
            class_names=class_names,
            **kwargs
        )

class Icon(Span):
    def __init__(self, **kwargs) -> None:
        class_names = kwargs.pop('class_names', [])
        class_names.extend(['material-symbols-outlined'])
        super().__init__(
            class_names=class_names,
            **kwargs
        )