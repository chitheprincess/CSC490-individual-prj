from model import InputForm
from flask import Flask, render_template, request
from compute import plot_heatmap

app = Flask(__name__)


@app.route('/pde', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        print(form.initial_condition.data)
        result = plot_heatmap(form.L.data, form.delta_x.data, form.T.data, form.delta_t.data,
                              form.beta.data, form.boundary_1.data, form.boundary_2.data, form.initial_condition.data)

    else:
        result = None

    return render_template('view.html', form=form, result=result)


if __name__ == '__main__':
    app.run(debug=True)
