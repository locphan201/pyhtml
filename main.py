from pyhtml import *

html = HTML(
    title='Document',
    value=[
        FlexCol([
            Heading1('hello')
        ])
    ]
)

print(html)

