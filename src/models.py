from src import db


class Contact(db.Model):
    __tablename__ = 'contacts'
    cont_id = db.Column(db.Integer, primary_key=True)
    cont_name = db.Column(db.String(60), nullable=False)
    cont_address = db.relationship("Address", back_populates="contact_ad")
    cont_phone = db.relationship('Phone', back_populates='contact')
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
