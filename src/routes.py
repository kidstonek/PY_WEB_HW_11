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


@app.route('/detail/<_id>', strict_slashes=False)
def detail(_id):
    contact = workscripts.get_detail(_id)
    return render_template('pages/detail.html', contact=contact)


@app.route("/delete/<_id>", strict_slashes=False)
def delete(_id):
    workscripts.delete_contact(_id)
    return redirect("/")


@app.route('/edit/<_id>', methods=['GET', 'POST'], strict_slashes=False)
def detail_for_edit(_id):
    contact = workscripts.get_detail(_id)
    if request.method == 'POST':
        c_add = request.form.get('address')
        c_phone = request.form.get('phone')
        c_email = request.form.get('email')
        workscripts.contact_details(c_add, c_phone, c_email, _id)
        return redirect(url_for('index'))
    return render_template('pages/edit.html', contact=contact)
