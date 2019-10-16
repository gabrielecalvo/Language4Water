import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return """
    Hello there<br><br>
    <img src="/plot.png" alt="my plot">
    """

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    ax.plot(xs, ys)
    ax.grid(True)
    return fig

if __name__ == '__main__':
    app.run(debug=True)






