import os
from typing import Union
from . import Base

def save(filename, html: Union[str, Base]) -> str:
    os.makedirs('templates', exist_ok=True)
    with open(os.path.join('templates', filename), 'w', encoding='utf-8') as file:
        file.write(str(html))
    return filename