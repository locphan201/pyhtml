from typing import Literal

class Styles:
    def __init__(self) -> None:
        self._styles = []

    def _insert(self, cfg: str) -> 'Styles':
        if cfg not in self._styles:
            self._styles.append(cfg)
        return self

    @property
    def flex(self) -> 'Styles':
        return self._insert('flex')

    @property
    def flex_row(self) -> 'Styles':
        return self._insert('flex-row')
    
    @property
    def flex_col(self) -> 'Styles':
        return self._insert('flex-col')
    
    @property
    def flex_wrap(self) -> 'Styles':
        return self._insert('flex-wrap')
    
    @property
    def flex_nowrap(self) -> 'Styles':
        return self._insert('flex-nowrap')
    
    def p_(self, size: float = 0, ) -> 'Styles':

        return self._insert(f'p-{size}')


    
    def margin(self, size) -> 'Styles':
        return self._insert('m', size)
    
    def border(self, size) -> 'Styles':
        return self._insert('border', size)
    
    def __str__(self):
        return f"Style: {self.style}"