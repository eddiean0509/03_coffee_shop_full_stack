from app import db


class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    genres = db.Column(db.JSON)  # compatible to sqlite
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.Text)

    # relationships
    upcoming_shows = db.relationship(
        "Show",
        primaryjoin="and_(Venue.id==Show.venue_id, Show.start_time >= func.now())",
        lazy=False,
    )
    past_shows = db.relationship(
        "Show",
        primaryjoin="and_(Venue.id==Show.venue_id, Show.start_time < func.now())",
        lazy=False,
    )

    @property
    def upcoming_shows_count(self):
        return (self.upcoming_shows and len(self.upcoming_shows)) or 0

    @property
    def past_shows_count(self):
        return (self.past_shows and len(self.past_shows)) or 0

    @property
    def num_upcoming_shows(self):
        return self.upcoming_shows_count


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.JSON)  # compatibe to sqlite
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.Text)

    # relationships
    upcoming_shows = db.relationship(
        "Show",
        primaryjoin="and_(Artist.id==Show.artist_id, Show.start_time >= func.now())",
        lazy=False,
    )
    past_shows = db.relationship(
        "Show",
        primaryjoin="and_(Artist.id==Show.artist_id, Show.start_time < func.now())",
        lazy=False,
    )

    @property
    def upcoming_shows_count(self):
        return (self.upcoming_shows and len(self.upcoming_shows)) or 0

    @property
    def past_shows_count(self):
        return (self.past_shows and len(self.past_shows)) or 0

    @property
    def num_upcoming_shows(self):
        return self.upcoming_shows_count

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.


class Show(db.Model):
    # unique together (artist, venue) ? no!
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'))
    start_time = db.Column(db.DateTime, nullable=False)

    # relationships
    artist = db.relationship("Artist")
    venue = db.relationship("Venue")

    @property
    def artist_name(self):
        return self.artist and self.artist.name

    @property
    def artist_image_link(self):
        return self.artist and self.artist.image_link

    @property
    def venue_name(self):
        return self.venue and self.venue.name

    @property
    def venue_image_link(self):
        return self.venue and self.venue.image_link
