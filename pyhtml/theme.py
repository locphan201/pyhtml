class ColorScheme:
    def __init__(
        self,
        primary: str = '',
        secondary: str = '',
        tertiary: str = ''
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

# Dark color scheme:
#   - primary: black (background)
#   - secondary: blue (accent)
#   - tertiary: white (text)
DEFAULT_DARK_COLOR_SCHEME: ColorScheme = ColorScheme(
    primary='#1f1f1f',   # Black for dark backgrounds
    secondary='#1e90ff', # Dodger Blue for accents
    tertiary='#fdfdfd'   # White for text
)

# Light color scheme:
#   - primary: white (background)
#   - secondary: blue (accent)
#   - tertiary: black (text)
DEFAULT_LIGHT_COLOR_SCHEME: ColorScheme = ColorScheme(
    primary='#fdfdfd',   # White for light backgrounds
    secondary='#1e90ff', # Dodger Blue for accents
    tertiary='#1f1f1f'   # Black for text
)