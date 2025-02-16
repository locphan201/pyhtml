class ColorScheme:
    def __init__(
        self,
        dark_mode: bool = False,
        primary: str = '',
        secondary: str = '',
        tertiary: str = ''
    ) -> None:
        self._dark_mode = dark_mode
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
    dark_mode=True,
    primary='#1f1f1f',   # Black for dark backgrounds
    secondary='#1e90ff', # Dodger Blue for accents
    tertiary='#fdfdfd'   # White for text
)

# Light color scheme:
#   - primary: white (background)
#   - secondary: blue (accent)
#   - tertiary: black (text)
DEFAULT_LIGHT_COLOR_SCHEME: ColorScheme = ColorScheme(
    dark_mode=False,
    primary='#fdfdfd',   # White for light backgrounds
    secondary='#1e90ff', # Dodger Blue for accents
    tertiary='#1f1f1f'   # Black for text
)

# DEFAULT_DARK_COLOR_SCHEME: ColorScheme = ColorScheme(
#     dark_mode=True,
#     primary='#242423',   # A very dark gray-brown, giving a moody background without being pure black
#     secondary='#FFB703', # A warm, bright golden accent for contrast
#     tertiary='#E0FBFC'   # A light, pale aqua for text to stand out against the dark background
# )

# DEFAULT_LIGHT_COLOR_SCHEME: ColorScheme = ColorScheme(
#     dark_mode=False,
#     primary='#FFF7E6',   # A soft off-white / cream color (not pure white)
#     secondary='#EE6C4D', # A muted, yet vibrant warm accent (reddish-orange)
#     tertiary='#2A2A2A'   # A dark gray for text, ensuring readability without being true black
# )

# Explanation of color choices:
# - primary: the main background color.
#   - In the dark scheme, #242423 is close to black but has a hint of brown/grey.
#   - In the light scheme, #FFF7E6 is a gentle cream tone, softer than pure white.
#
# - secondary: the accent color, used for interactive elements, highlights, or small details.
#   - In the dark scheme, #FFB703 (golden) pops nicely against the dark background.
#   - In the light scheme, #EE6C4D (warm reddish-orange) provides a pleasant contrast.
#
# - tertiary: often text color, but you might also use it for smaller accent elements.
#   - In the dark scheme, #E0FBFC is a pale aqua that is readable on a dark background.
#   - In the light scheme, #2A2A2A is a dark neutral tone (slightly softer than pure black).