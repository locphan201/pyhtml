# pyhtml/__init__.py

from typing import List, Dict, Any, Union
from .theme import theme
from .styles import *
import uuid
import os

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
    def __init__(self, title: str = 'Document') -> None:
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
    def __init__(self, **kwargs) -> None:
        super().__init__(tag='style', **kwargs)

class Head(Base):
    def __init__(self, **kwargs) -> None:
        base_value = [
            Meta(charset='UTF-8'),
            Meta(name='viewport', content="width=device-width, initial-scale=1.0"),
            Link(rel='stylesheet', href='https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0'),
            Script(src='https://unpkg.com/@tailwindcss/browser@4'),
            Style(children=str(theme)),
            Title(title=kwargs.get('title', 'Document'))
        ]
        base_value.extend(kwargs.get('children', []))
        super().__init__(tag='head', children=base_value, **kwargs)

class Body(Base):
    def __init__(self, **kwargs) -> None:
        class_names = Styles().w('dvw').h('dvh').flex('col')
        class_names = class_names.justify('center').items('center').overflow('x-hidden').overflow('y_auto').to_list()
        class_names.extend(kwargs.pop('class_names', []))
        super().__init__(
            tag='body',
            style='background-color:var(--color-primary);transition:background-color 0.3s ease,color 0.3s ease;',
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

    def render(self, filename, reload: bool = True) -> str:
        return self._to_str()

    def save(self, filename, reload: bool = True) -> str:
        if reload or not os.path.isfile(os.path.join('templates', filename)):
            os.makedirs('templates', exist_ok=True)
            with open(os.path.join('templates', filename), 'w', encoding='utf-8') as file:
                file.write(str(self._to_str()))
            return filename

class Text(Base):
    def __init__(self, **kwargs) -> None:
        super().__init__(tag='p', style='color:var(--color-tertiary);', **kwargs)

class Label(Base):
    def __init__(self, **kwargs) -> None:
        super().__init__(tag='label', style='color:var(--color-tertiary);', **kwargs)

class Span(Base):
    def __init__(self, **kwargs) -> None:
        super().__init__(tag='span', style='color:var(--color-tertiary);', **kwargs)

class Row(Base):
    def __init__(self, **kwargs) -> None:
        class_names = Styles().flex('row').justify('center').items('center').gap(2).to_list()
        class_names.extend(kwargs.pop('class_names', []))
        super().__init__(
            tag='div',
            class_names=class_names,
            **kwargs
        )

class Column(Base):
    def __init__(self, **kwargs) -> None:
        class_names = Styles().flex('col').justify('center').items('center').gap(2).to_list()
        class_names.extend(kwargs.pop('class_names', []))
        super().__init__(
            tag='div',
            class_names=class_names,
            **kwargs
        )

class Input(Base):
    def __init__(self, **kwargs) -> None:
        class_names = Styles().rounded('lg').p('2.5').border('1').to_list()
        class_names.extend(kwargs.pop('class_names', []))
        super().__init__(
            tag='input', 
            style='background-color: var(--color-primary);color:var(--color-tertiary);',
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
        class_names = Styles().underline().cursor('pointer').to_list()
        class_names.extend(kwargs.pop('class_names', []))
        super().__init__(
            tag='a', 
            style='color:var(--color-tertiary);',
            class_names=class_names,
            **kwargs
        )

class A(Anchor):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

class Button(Base):
    def __init__(self, **kwargs) -> None:
        class_names = Styles().flex('row').justify('center').items('center').gap(2)
        class_names = class_names.rounded('lg').p('2.5').cursor('pointer').hover('opacity-75').to_list()
        class_names.extend(kwargs.pop('class_names', []))
        super().__init__(
            tag='button', 
            style='background-color:var(--color-secondary);color:var(--color-tertiary);',
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
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

class Select(Base):
    def __init__(self, **kwargs) -> None:
        id = kwargs.pop('id', str(uuid.uuid4()).replace('-', '_'))
        class_names = Styles().rounded('lg').p('2.5').border('1').to_list()
        class_names.extend(kwargs.pop('class_names', []))
        items = kwargs.pop('items', [])
        super().__init__(
            id=id,
            tag='select', 
            style='background-color:var(--color-primary);color:var(--color-tertiary);',
            class_names=class_names,
            children=[Option(value=item) for item in items],
            **kwargs
        )

class Option(Base):
    def __init__(self, **kwargs) -> None:
        super().__init__(
            tag='option',
            class_names=kwargs.pop('class_names', []),
            value=kwargs.get('value', ''),
            children=kwargs.pop('value', '').replace('_', ' ').capitalize()
        )

class SelectTheme(Base):
    def __init__(self, **kwargs) -> None:
        id = kwargs.pop('id', str(uuid.uuid4()).replace('-', '_'))
        class_names = Styles().absolute().bottom('5').left('5').rounded('lg').p('2.5').border('1').to_list()
        class_names.extend(kwargs.pop('class_names', []))
        items = [Option(value=item) for item in theme.keys]
        items.append(Script(children=f'''
if (localStorage.getItem('themeMode')) {{
    document.documentElement.className = localStorage.getItem('themeMode');
    document.getElementById('{id}').value = localStorage.getItem('themeMode');
}} else {{
    document.documentElement.className = 'light';
    document.getElementById('{id}').value = 'light';
}}

document.getElementById('{id}').addEventListener('change', function() {{
    document.documentElement.className = document.getElementById('{id}').value;
    localStorage.setItem('themeMode', document.getElementById('{id}').value);
}});
'''))
        super().__init__(
            id=id,
            tag='select', 
            style='background-color:var(--color-primary);color:var(--color-tertiary);',
            class_names=class_names,
            children=items,
            **kwargs
        )

class ToggleButton(Label):
    def __init__(self, value: str = '', class_names: List[str] = []):
        id = str(uuid.uuid4()).replace('-', '_')
        temp = Styles().inline_flex().items('center').cursor('pointer').to_list()
        temp.extend(class_names)
        super().__init__(
            class_names=temp,
            children=[
                Input(
                    type='checkbox',
                    value='',
                    class_names=Styles().sr_only().peer().to_list(),
                    id=id,
                ),
                Base(
                    tag='div',
                    class_names=Styles().relative().w('11').h('6').bg('gray-200').other('peer-focus:outline-none').other('peer-focus:ring-4').other('peer-focus:ring-blue-300').rounded('full').peer().bg('gray-700').other('peer_checked:bg-blue-600').other('peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full').other("peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px]").other('after:start-[2px] after:bg-white after:border-gray-300 after:border').other('after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600').to_list()
                ),
                Span(
                    class_names=Styles().text('sm').font('medium').other('ms-3').to_list(),
                    children=value
                ),
                Script(
                    children=f'''
if (localStorage.getItem('darkMode') === 'enabled') {{
    document.documentElement.classList.add('dark');
    document.getElementById('{id}').checked = true;
}}
document.getElementById('{id}').addEventListener('change', function() {{
    if (document.getElementById('{id}').checked) {{
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