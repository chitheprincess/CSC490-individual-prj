from model import HeatForm, WaveForm
from flask import Flask, render_template, request
from compute_heat import plot_3D, plot_heatmap
from compute_wave import plot_3D_wave, plot_gif

app = Flask(__name__)


@app.route('/')
def firstpage():
    """Entry point; the view for the main page"""
    return render_template('firstpage.html')


@app.route('/heat', methods=['GET', 'POST'])
def heat():
    form = HeatForm(request.form)
    if request.method == 'POST' and form.validate() and request.form['btn'] == "Show heat map":
        result = plot_heatmap(form.L.data, form.delta_x.data, form.T.data, form.delta_t.data,
                              form.beta.data, form.boundary_1.data, form.boundary_2.data, form.f_x.data)

    elif request.method == 'POST' and form.validate() and request.form['btn'] == "Show 3D graph":
        result = plot_3D(form.L.data, form.delta_x.data, form.T.data, form.delta_t.data,
                         form.beta.data, form.boundary_1.data, form.boundary_2.data, form.f_x.data)

    else:
        result = None

    return render_template('view_heat.html', form=form, result=result)


@app.route('/wave', methods=['GET', 'POST'])
def wave():
    form = WaveForm(request.form)
    if request.method == 'POST' and form.validate() and request.form['btn'] == "Show gif":
        result = plot_gif(form.L.data, form.delta_x.data, form.T.data, form.delta_t.data,
                          form.c.data, form.f_x.data, form.g_x.data, form.boundary_1.data, form.boundary_2.data)
    elif request.method == 'POST' and form.validate() and request.form['btn'] == "Show 3D graph":
        result = plot_3D_wave(form.L.data, form.delta_x.data, form.T.data, form.delta_t.data,
                              form.c.data, form.f_x.data, form.g_x.data, form.boundary_1.data, form.boundary_2.data)
    else:
        result = None

    return render_template('view_wave.html', form=form, result=result)


if __name__ == '__main__':
    app.run(debug=True)
