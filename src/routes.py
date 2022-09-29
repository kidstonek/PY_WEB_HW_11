from . import app
from flask import render_template, request, redirect, url_for
from src.repository import workscripts


@app.route('/healthcheck', strict_slashes=False)
def healthcheck():
    return 'All good'


@app.route('/', strict_slashes=False)
def index():
    contacts = workscripts.get_all_contacts()
    return render_template('pages/index.html', title='Notebook', contacts=contacts)


@app.route('/contact', methods=['GET', 'POST'], strict_slashes=False)
def create_contact():
    if request.method == 'POST':
        cname = request.form.get('name')
        c_add = request.form.get('address')
        c_phone = request.form.get('phone')
        c_email = request.form.get('email')
        contact_nn = workscripts.contact_input(cname)
        workscripts.contact_details(c_add, c_phone, c_email, contact_nn.cont_id)
        return redirect(url_for('index'))
    return render_template('pages/contact.html', title='Add Contact')


@app.route('/test', methods=['GET', 'POST'], strict_slashes=False)
def test_input():
    if request.method == 'POST':
        text = request.form.get('text')
        in_text = workscripts.test_input(text)
        print(in_text.test_id)
        text_r = request.form.get('mri')
        text_rel = workscripts.test_input_rel(text_r, in_text.test_id)
        return redirect(url_for('index'))
    return render_template('pages/test.html', title='test input')


@app.route('/detail/<_id>', strict_slashes=False)
def detail(_id):
    contact = workscripts.get_detail(_id)
    return render_template('pages/detail.html', contact=contact.cont_id)
