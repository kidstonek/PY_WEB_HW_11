from src import db


class Contact(db.Model):
    __tablename__ = 'contacts'
    cont_id = db.Column(db.Integer, primary_key=True)
    cont_name = db.Column(db.String(60), nullable=False)
    cont_address = db.relationship("Address", back_populates="contact_ad")
    cont_phone = db.relationship('Phone', back_populates='contact_ad')
    cont_email = db.relationship('Email', back_populates='contact_email')


class Phone(db.Model):
    __tablename__ = 'phones'
    phone_id = db.Column(db.Integer, primary_key=True)
    phone_num = db.Column(db.String(60), nullable=False)
    # contact = relationship('Contact', secondary='contacts_to_phone', back_populates='phones')
    contact_id = db.Column('contact_id', db.ForeignKey('contacts.cont_id', ondelete='CASCADE'), nullable=False)
    contact_ad = db.relationship("Contact", back_populates="cont_phone")


class Address(db.Model):
    __tablename__ = 'addresses'
    address_id = db.Column(db.Integer, primary_key=True)
    address_ad = db.Column(db.String(60), nullable=None)
    contact_id = db.Column('contact_id', db.ForeignKey('contacts.cont_id', ondelete='CASCADE'), nullable=False)
    contact_ad = db.relationship("Contact", back_populates="cont_address")


class Email(db.Model):
    __tablename__ = 'emails'
    email_id = db.Column(db.Integer, primary_key=True)
    email_mail = db.Column(db.String(60), nullable=False)
    contact_id = db.Column('contact_id', db.ForeignKey('contacts.cont_id', ondelete='CASCADE'), nullable=False)
    contact_email = db.relationship("Contact", back_populates="cont_email")


class Test(db.Model):
    __tablename__ = 'test'
    test_id = db.Column(db.Integer, primary_key=True)
    test_text = db.Column(db.String(120), nullable=False)
    test_tri = db.relationship('Tri', back_populates='test_trir')


class Tri(db.Model):
    __tablename__ = 'tri'
    tri_id = db.Column(db.Integer, primary_key=True)
    tri_text = db.Column(db.String(120), nullable=False)
    test_id = db.Column('test_id', db.ForeignKey('test.test_id', ondelete='CASCADE'), nullable=False)
    test_trir = db.relationship("Test", back_populates="test_tri")
