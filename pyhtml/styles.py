from typing import List, Literal

class Styles:
    def __init__(self) -> None:
        '''
        This class is used to generate tailwindcss classes.
        '''
        self._styles = []

    def _insert(self, cfg: str) -> 'Styles':
        '''
        Insert a new tailwindcss class to the list of styles.
        '''
        if cfg not in self._styles:
            self._styles.append(cfg)
        return self

    # Display utilities
    def block(self) -> 'Styles':
        '''
        Block utility classes.
        '''
        return self._insert('block')
    
    def flex(self, cfg: str) -> 'Styles':
        '''
        Flexbox utility classes.
        '''
        return self._insert(f'flex flex-{cfg}')
    
    def inline_flex(self) -> 'Styles':
        '''
        Inline-flex utility classes.
        '''
        return self._insert('inline-flex')
    
    def grid(self, cfg: str) -> 'Styles':
        '''
        Grid utility classes.
        '''
        return self._insert(f'grid grid-{cfg}')

    def hidden(self) -> 'Styles':
        '''
        Hidden utility classes.
        '''
        return self._insert('hidden')

    def opacity(self, cfg: str) -> 'Styles':
        '''
        Opacity utility classes.
        '''
        return self._insert(f'opacity-{cfg}')

    # Position utilities
    def top(self, size: str) -> 'Styles':
        '''
        Top utility classes.
        '''
        if size[0] == '-':
            return self._insert(f'-top-{size[1:]}')
        return self._insert(f'top-{size}')

    def right(self, size: str) -> 'Styles':
        '''
        Right utility classes.
        '''
        if size[0] == '-':
            return self._insert(f'-right-{size[1:]}')
        return self._insert(f'right-{size}')
    
    def bottom(self, size: str) -> 'Styles':
        '''
        Bottom utility classes.
        '''
        if size[0] == '-':
            return self._insert(f'-bottom-{size[1:]}')
        return self._insert(f'bottom-{size}')
    
    def left(self, size: str) -> 'Styles':
        '''
        Left utility classes.
        '''
        if size[0] == '-':
            return self._insert(f'-left-{size[1:]}')
        return self._insert(f'left-{size}')
    
    def inset(self, size: str) -> 'Styles':
        '''
        Inset utility classes.
        '''
        if size[0] == '-':
            return self._insert(f'-inset-{size[1:]}')
        return self._insert(f'inset-{size}')

    def translate(self, size: str) -> 'Styles':
        '''
        Translate utility classes.
        '''
        if size[0] == '-':
            return self._insert(f'-translate-{size[1:]}')
        return self._insert(f'translate-{size}')

    def static(self) -> 'Styles':
        '''
        Static utility classes.
        '''
        return self._insert('static')

    def fixed(self) -> 'Styles':
        '''
        Fixed utility classes.
        '''
        return self._insert('fixed')

    def absolute(self) -> 'Styles':
        '''
        Absolute utility classes.
        '''
        return self._insert('absolute')
    
    def relative(self) -> 'Styles':
        '''
        Relative utility classes.
        '''
        return self._insert('relative')

    def sticky(self) -> 'Styles':
        '''
        Sticky utility classes.
        '''
        return self._insert('sticky')
    
    # Overflow utilities
    def overflow(self, cfg: str) -> 'Styles':
        '''
        Overflow utility classes.
        '''
        return self._insert(f'overflow-{cfg}')
    
    # Visibility utilities
    def visible(self) -> 'Styles':
        '''
        Visible utility classes.
        '''
        return self._insert('visible')
    
    def invisible(self) -> 'Styles':
        '''
        Invisible utility classes.
        '''
        return self._insert('invisible')

    # Z-index utilities
    def z(self, size: int) -> 'Styles':
        '''
        Z-index utility classes.
        '''
        if size[0] == '-':
            return self._insert(f'-z-{size[1:]}')
        return self._insert(f'z-{size}')
    
    # Padding and margin utilities
    def p(self, size: str = '0', **kwargs) -> 'Styles':
        '''
        Padding utility classes.
        '''
        pl = kwargs.get('l', size)
        pr = kwargs.get('r', size)
        pt = kwargs.get('t', size)
        pb = kwargs.get('b', size)
        px = kwargs.get('x', size)
        py = kwargs.get('y', size)
        added = False

        if pl == pr == pt == pb != '0':
            return self._insert(f'p-{pl}')
        if px == py != '0':
            return self._insert(f'p-{px}')
        if px != '0': 
            added = True
            self._insert(f'pl-{px}')._insert(f'pr-{px}')
        if py != '0': 
            added = True
            self._insert(f'pt-{py}')._insert(f'pb-{py}')
        if pl != '0': 
            added = True
            self._insert(f'pl-{pl}')
        if pr != '0': 
            added = True
            self._insert(f'pr-{pr}')
        if pt != '0': 
            added = True
            self._insert(f'pt-{pt}')
        if pb != '0': 
            added = True
            self._insert(f'pb-{pb}')
        else:
            if not added and size != '0':        
                return self._insert(f'p-{size}') 
            else:
                return self
            
    def m(self, size: str = '0', **kwargs) -> 'Styles':
        '''
        Margin utility classes.
        '''
        ml = kwargs.get('l', size)
        mr = kwargs.get('r', size)
        mt = kwargs.get('t', size)
        mb = kwargs.get('b', size)
        mx = kwargs.get('x', size)
        my = kwargs.get('y', size)
        added = False

        if ml == mr == mt == mb != '0':
            return self._insert(f'm-{ml}')
        if mx == my != '0':
            return self._insert(f'm-{mx}')
        if mx != '0': 
            added = True
            self._insert(f'ml-{mx}')._insert(f'mr-{mx}')
        if my != '0': 
            added = True
            self._insert(f'mt-{my}')._insert(f'mb-{my}')
        if ml != '0': 
            added = True
            self._insert(f'ml-{ml}')
        if mr != '0': 
            added = True
            self._insert(f'mr-{mr}')
        if mt != '0': 
            added = True
            self._insert(f'mt-{mt}')
        if mb != '0': 
            added = True
            self._insert(f'mb-{mb}')
        else:
            if not added and size != 0:        
                return self._insert(f'm-{size}') 
            else:
                return self
    
    def gap(self, size: float) -> 'Styles':
        '''
        Gap utility classes.
        '''
        return self._insert(f'gap-{size}')

    # Width and height utilities
    def w(self, size: str) -> 'Styles':
        '''
        Width utility classes.
        '''
        return self._insert(f'w-{size}')
    
    def h(self, size: str) -> 'Styles':
        '''
        Height utility classes.
        '''
        return self._insert(f'h-{size}')
    
    def min_w(self, size: str) -> 'Styles':
        '''
        Min width utility classes.
        '''
        return self._insert(f'min-w-{size}')
    
    def min_h(self, size: str) -> 'Styles':
        '''
        Min height utility classes.
        '''
        return self._insert(f'min-h-{size}')
    
    def max_w(self, size: str) -> 'Styles':
        '''
        Max width utility classes.
        '''
        return self._insert(f'max-w-{size}')
    
    def max_h(self, size: str) -> 'Styles':
        '''
        Max height utility classes.
        '''
        return self._insert(f'max-h-{size}')
    
    # Alignment utilities
    def place(self, cfg: str) -> 'Styles':
        '''
        Place utility classes.
        '''
        return self._insert(f'place-{cfg}')
    
    def justify(self, cfg: str) -> 'Styles':
        '''
        Horizontal alignment utility classes.
        '''
        return self._insert(f'justify-{cfg}')
    
    def items(self, cfg: str) -> 'Styles':
        '''
        Vertical alignment utility classes.
        '''
        return self._insert(f'items-{cfg}')
    
    def content(self, cfg: str) -> 'Styles':
        '''
        Content utility classes.
        '''
        return self._insert(f'content-{cfg}')

    # Border utilities
    def rounded(self, size: Literal['sm', 'md', 'lg', 'full']) -> 'Styles':
        '''
        Border radius utility classes.
        '''
        return self._insert(f'rounded-{size}')

    def border(self, cfg: str) -> 'Styles':
        '''
        Border utility classes.
        '''
        return self._insert(f'border-{cfg}')

    # Background and shadow utilities
    def shadow(self, cfg: str) -> 'Styles':
        '''
        Shadow utility classes.
        '''
        return self._insert(f'shadow-{cfg}')
    
    def bg(self, cfg: str) -> 'Styles':
        '''
        Background utility classes.
        '''
        return self._insert(f'bg-{cfg}')

    # Text utilities
    def text(self, cfg: str) -> 'Styles':
        '''
        Text utility classes.
        '''
        return self._insert(f'text-{cfg}')
    
    def font(self, cfg: str) -> 'Styles':
        '''
        Font utility classes.
        '''
        return self._insert(f'font-{cfg}')

    def underline(self) -> 'Styles':
        '''
        Underline utility classes.
        '''
        return self._insert('underline')

    # Other utilities
    def sr_only(self) -> 'Styles':
        '''
        Screen reader only utility classes.
        '''
        return self._insert('sr-only')
    
    def peer(self) -> 'Styles':
        '''
        Peer utility classes.
        '''
        return self._insert('peer')

    def cursor(self, cfg: str) -> 'Styles':
        '''
        Cursor utility classes.
        '''
        return self._insert(f'cursor-{cfg}')
    
    def hover(self, cfg: str) -> 'Styles':
        '''
        Hover utility classes.
        '''
        return self._insert(f'hover:{cfg}')

    def focus(self, cfg: str) -> 'Styles':
        '''
        Focus utility classes.
        '''
        return self._insert(f'focus:{cfg}')

    def other(self, cfg: str) -> 'Styles':
        '''
        Other utility classes.
        '''
        return self._insert(cfg)

    def __str__(self) -> str:
        '''
        Return the list of tailwindcss classes as a string.
        '''
        return ' '.join(self._styles)

    def to_list(self) -> List[str]:
        '''
        Return the list of tailwindcss classes.
        '''
        return self._styles

class ResponsiveStyles:
    def __init__(self, **kwargs) -> None:
        '''
        This class is used to generate responsive tailwindcss classes.
        '''
        self._styles = {
            'base': kwargs.get('base', Styles()),
            'sm':   kwargs.get('sm',   None),
            'md':   kwargs.get('md',   None),
            'lg':   kwargs.get('lg',   None),
            'xl':   kwargs.get('xl',   None),
            '2xl':  kwargs.get('2xl',  None),
        }

    def _to_str_(self) -> str:
        '''
        Return the list of tailwindcss classes as a string.
        '''
        class_names = str(self._styles['base']) if self._styles['base'] else ''
        for device in ['sm', 'md', 'lg', 'xl', '2xl']:
            if self._styles[device]:
                class_names += f' {device}:' + str(self._styles[device]).replace(' ', f' {device}:')
        return class_names

    def to_list(self) -> List[str]:
        '''
        Return the list of tailwindcss classes.
        '''
        class_names = self._styles['base'].to_list() if self._styles['base'] else []
        for device in ['sm', 'md', 'lg', 'xl', '2xl']:
            if self._styles[device]:
                class_names += [f'{device}:{x}' for x in self._styles[device].to_list()]
        return class_names

    def __repr__(self) -> str:
        '''
        Return the list of tailwindcss classes as a string.
        '''
        return self._to_str_()

    def __str__(self) -> str:
        '''
        Return the list of tailwindcss classes as a string.
        '''
        return self._to_str_()
    
if __name__ == '__main__':
    styles = Styles().flex('col').p_(l=10).hover('bg-blue-400')

    print(styles)
