from pyhtml import *
from pyhtml.utils import save
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    html = HTML(
        title='Document',
        class_names=['dark'],
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
                )
            ])
        ]
    )
    return render_template(save('index.html', html))

if __name__ == '__main__':
    app.run(
        host='localhost',
        port=5000,
        debug=True
    )

