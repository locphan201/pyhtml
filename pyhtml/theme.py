# pyhtml/theme.py

from typing import List

class ColorScheme:
    def __init__(
        self,
        primary: str = '',
        secondary: str = '',
        tertiary: str = '',
    ) -> None:
        self._primary = primary
        self._secondary = secondary
        self._tertiary = tertiary

    @property
    def PRIMARY(self) -> str:
        return self._primary
    
    @property
    def SECONDARY(self) -> str:
        return self._secondary
    
    @property
    def TERTIARY(self) -> str:
        return self._tertiary
    
class Theme:
    def __init__(self) -> None:
        self._color_schemes = {}

    def add(self, key: str, color_scheme: ColorScheme) -> None:
        self._color_schemes[key] = color_scheme

    @property
    def keys(self) -> List[str]:
        return list(self._color_schemes.keys())

    def _to_str_(self) -> str: 
        template ='''
{key} {{
    --color-primary: {primary};
    --color-secondary: {secondary};
    --color-tertiary: {tertiary};
}}
'''
        style = ''
        for key, color_scheme in self._color_schemes.items():
            if style == '':
                style += template.format(
                    key=':root',
                    primary=color_scheme.PRIMARY, 
                    secondary=color_scheme.SECONDARY, 
                    tertiary=color_scheme.TERTIARY,
                )
            else:
                style += template.format(
                    key=f'.{key}',
                    primary=color_scheme.PRIMARY, 
                    secondary=color_scheme.SECONDARY, 
                    tertiary=color_scheme.TERTIARY,
                )
        return style

    def __str__(self) -> str:
        return self._to_str_()
    
    def __repr__(self) -> str:
        return self._to_str_()

theme = Theme()
theme.add('light', ColorScheme(
    primary='#fdfdfd',   # White for light backgrounds
    secondary='#1e90ff', # Dodger Blue for accents
    tertiary='#1f1f1f'   # Black for text
))

theme.add('dark', ColorScheme(
    primary='#1f1f1f',   # Black for dark backgrounds
    secondary='#1e90ff', # Dodger Blue for accents
    tertiary='#fdfdfd'   # White for text
))

theme.add('yellow-gray', ColorScheme(
    primary='#242423',   # A very dark gray-brown, giving a moody background without being pure black
    secondary='#FFB703', # A warm, bright golden accent for contrast
    tertiary='#E0FBFC'   # A light, pale aqua for text to stand out against the dark background
))

theme.add('cream', ColorScheme(
    primary='#FFF7E6',   # A soft off-white / cream color (not pure white)
    secondary='#EE6C4D', # A muted, yet vibrant warm accent (reddish-orange)
    tertiary='#2A2A2A'   # A dark gray for text, ensuring readability without being true black
))
