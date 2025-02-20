# examples/form.py

from pyhtml import *

html = HTML(
    title='Document',
    children=[
        Column(children=[
            Form(
                action='/hello',
                method='POST',
                children=[
                    Text(children='Form'),
                    Input(type='text'),
                    Input(type='text'),
                    Input(type='text'),
                    Button(
                        type='submit',
                        class_names=['bg-blue-400', 'text-white'],
                        children=[
                            Icon(children='upload'),
                            Text(children='upload')
                        ]
                    )
                ]
            ),
            SelectTheme()
        ])
    ]
)