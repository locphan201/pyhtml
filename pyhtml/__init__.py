from typing import List, Dict, Any
from .theme import *
import uuid

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
    
    def set(self, key: str, value: str) -> None:
        self._attrs[key] = value

    def add_child(self, child: Any) -> bool:
        if isinstance(self._children, str):
            if isinstance(child, str):
                self._children += child
            else:
                print(f'Error - Tag {self._tag}: Cannot add Object into this parent since the content is a string!')
                return False

        if isinstance(child, str):
            print(f'Error - Tag {self._tag}: Cannot add a string into this parent since the content is a list of Object!')
            return False
        else:
            self._children.append(child)
            return True

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
            --color-light-primary: {DEFAULT_LIGHT_COLOR_SCHEME.PRIMARY};
            --color-light-secondary: {DEFAULT_LIGHT_COLOR_SCHEME.SECONDARY};
            --color-light-tertiary: {DEFAULT_LIGHT_COLOR_SCHEME.TERTIARY};
            --color-dark-primary: {DEFAULT_DARK_COLOR_SCHEME.PRIMARY};
            --color-dark-secondary: {DEFAULT_DARK_COLOR_SCHEME.SECONDARY};
            --color-dark-tertiary: {DEFAULT_DARK_COLOR_SCHEME.TERTIARY};
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
        class_names = [
            'w-dvw', 'h-dvh', 'flex', 'flex-col', 
            'justify-center', 'items-center', 'overflow-x-hidden', 'overflow-y-auto',
            'bg-light-primary', 'dark:bg-dark-primary'
        ]
        class_names.extend(kwargs.pop('class_names', []))
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
                Head(title=kwargs.pop('title', 'Document')),
                Body(children=kwargs.pop('children', []))
            ],
            **kwargs
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
        class_names = ['text-light-tertiary', 'dark:text-dark-tertiary']
        class_names.extend(kwargs.pop('class_names', []))
        super().__init__(tag='p', class_names=class_names,**kwargs)

class Label(Base):
    def __init__(self, **kwargs) -> None:
        class_names = ['text-light-tertiary', 'dark:text-dark-tertiary']
        class_names.extend(kwargs.pop('class_names', []))
        super().__init__(tag='label', class_names=class_names,**kwargs)

class Span(Base):
    def __init__(self, **kwargs) -> None:
        super().__init__(tag='span', **kwargs)

class Row(Base):
    def __init__(self, **kwargs) -> None:
        class_names = ['flex', 'justify-center', 'items-center', 'gap-2']
        class_names.extend(kwargs.pop('class_names', []))
        super().__init__(
            tag='div',
            class_names=class_names,
            **kwargs
        )

class Column(Row):
    def __init__(self, **kwargs) -> None:
        class_names = ['flex-col']
        class_names.extend(kwargs.pop('class_names', []))
        super().__init__(
            class_names=class_names,
            **kwargs
        )

class Input(Base):
    def __init__(self, **kwargs) -> None:
        class_names = [
            'rounded-lg', 'p-2.5', 'border',
            'bg-light-primary', 'dark:bg-dark-primary',
            'text-light-tertiary', 'dark:text-dark-tertiary'
        ]
        class_names.extend(kwargs.pop('class_names', []))
        super().__init__(
            tag='input', 
            class_names=class_names,
            **kwargs
        )

class Form(Base):
    def __init__(self, **kwargs) -> None:
        class_names = ['flex', 'flex-col', 'justify-center', 'items-center', 'gap-2', 'border', 'rounded-lg', 'p-5']
        class_names.extend(kwargs.pop('class_names', []))
        super().__init__(
            tag='form', 
            class_names=class_names,
            **kwargs
        )

class Anchor(Base):
    def __init__(self, **kwargs) -> None:
        class_names = ['cursor-pointer', 'text-light-tertiary', 'dark:text-dark-tertiary']
        class_names.extend(kwargs.pop('class_names', []))
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
        class_names = [
            'flex', 'justify-center', 'items-center', 'gap-2', 
            'rounded-lg', 'p-2.5', 'cursor-pointer', 'hover:opacity-75',
            'bg-light-secondary', 'dark:bg-dark-secondary',
            'text-light-tertiary', 'dark:text-dark-tertiary'
        ]
        class_names.extend(kwargs.pop('class_names', []))
        super().__init__(
            tag='button', 
            class_names=class_names,
            **kwargs
        )

class Icon(Span):
    def __init__(self, **kwargs) -> None:
        class_names = ['material-symbols-outlined']
        class_names.extend(kwargs.pop('class_names', []))
        super().__init__(
            class_names=class_names,
            **kwargs
        )

class Image(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class ToggleButton(Label):
    def __init__(self, value: str = '', class_names: List[str] = []):
        id = str(uuid.uuid4()).replace('-', '_')
        temp = ['inline-flex', 'items-center', 'cursor-pointer']
        temp.extend(class_names)
        super().__init__(
            class_names=temp,
            children=[
                Input(
                    type='checkbox',
                    value='',
                    class_names=['sr-only', 'peer'],
                    id=id,
                ),
                Base(
                    tag='div',
                    class_names=[
                        'relative', 'w-11', 'h-6', 'bg-gray-200', 'peer-focus:outline-none', 'peer-focus:ring-4', 
                        'peer-focus:ring-blue-300', 'dark:peer-focus:ring-blue-800', 'rounded-full', 'peer', 
                        'dark:bg-gray-700', 'peer-checked:after:translate-x-full', 'rtl:peer-checked:after:-translate-x-full', 
                        "peer-checked:after:border-white after:content-['']", 'after:absolute after:top-[2px]', 'after:start-[2px]', 
                        'after:bg-white', 'after:border-gray-300', 'after:border', 'after:rounded-full', 'after:h-5', 'after:w-5', 
                        'after:transition-all', 'dark:border-gray-600', 'peer-checked:bg-blue-600', 'dark:peer-checked:bg-blue-600'
                    ],
                ),
                Span(
                    class_names=['ms-3', 'text-sm', 'font-medium', 'text-light-tertiary', 'dark:text-dark-tertiary'],
                    children=value
                ),
                Script(
                    children=f'''
if (localStorage.getItem('darkMode') === 'enabled') {{
    document.documentElement.classList.add('dark');
    document.getElementById("{id}").checked = true;
}}

// Add an event listener for the checkbox toggle
document.getElementById("{id}").addEventListener("change", function() {{
    if (document.getElementById("{id}").checked) {{
        document.documentElement.classList.add('dark');
        localStorage.setItem('darkMode', 'enabled');
    }} else {{
        document.documentElement.classList.remove('dark');
        localStorage.setItem('darkMode', 'disabled');
    }}
}});
'''
                )
            ]
        )