from sqlalchemy.orm import joinedload

from src import db, models
from src.models import Contact, Phone, Address, Email


def contact_input(contact_name):
    contact_n = models.Contact(cont_name=contact_name)
    db.session.add(contact_n)
    db.session.commit()
    return contact_n


def contact_details(contact_address, contact_phone, contact_email, _id):
    add_address = models.Address(address_ad=contact_address, contact_id=_id)
    add_phone = models.Phone(phone_num=contact_phone, contact_id=_id)
    add_email = models.Email(email_mail=contact_email, contact_id=_id)
    db.session.add(add_address)
    db.session.add(add_phone)
    db.session.add(add_email)
    db.session.commit()
    return


def get_detail(_id):
    detail = db.session.query(Contact).filter(Contact.cont_id == _id).first()
    address = db.session.query(Address).filter(Address.contact_id == detail.cont_id).first()
    phone = db.session.query(Phone).filter(Phone.contact_id == detail.cont_id).first()
    email = db.session.query(Email).filter(Email.contact_id == detail.cont_id).first()
    # print(detail.cont_name, address.address_ad,  phone.phone_num, email.email_mail)
    return detail.cont_name, address.address_ad,  phone.phone_num, email.email_mail
    # note = db_session.query(Note).filter(Note.id == id).first()


def get_all_contacts():
    contacts = db.session.query(Contact).all()
    # contacts = db.session.query(Contact, Phone, Address, Email).filter()
    # query(table1, table2).filter(table1.thing == table2.other_thing)
    return contacts


def delete_contact(_id):
    db.session.query(Contact).filter(Contact.cont_id == _id).delete()
    db.session.query(Address).filter(Address.contact_id == _id).delete()
    db.session.query(Phone).filter(Phone.contact_id == _id).delete()
    db.session.query(Email).filter(Email.contact_id == _id).delete()
    db.session.commit()