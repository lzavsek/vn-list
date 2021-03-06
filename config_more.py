import os
from config import DOMAIN_ID

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True # cross-site request forgery prevention for Flask-WTF

UPLOAD_URL = '/games-dl/'

IMAGE_UPLOAD_URL = '/media/screenshot/'
IMAGE_UPLOAD_URL_SMALL = IMAGE_UPLOAD_URL + 'small/'
IMAGE_UPLOAD_URL_MEDIUM = IMAGE_UPLOAD_URL + 'medium/'
IMAGE_SIZE_NORMAL = 1024, 768
IMAGE_SIZE_SMALL = 240, 180 #160, 120
IMAGE_SIZE_MEDIUM = 320, 240

#ALLOWED_EXTENSIONS = set(['exe', 'zip', 'rar'])
ALLOWED_EXTENSIONS_IMG = set(['png', 'jpg', 'jpeg', 'bmp'])
#MAX_CONTENT_LENGTH = 16 * 1024 * 1024

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

# domain settings    
START_YEARS=[0,2001,2005]
DOMAIN_URLS=['','http://www.renai.us/', 'http://games.renpy.org/']
DOMAIN_NAMES=['','renai.us', 'games.renpy.org']
DOMAIN_TITLES=["","Ren'Ai Archive", "Ren'Py Games List"]

DOMAIN_NAME=DOMAIN_NAMES[DOMAIN_ID]
DOMAIN_TITLE=DOMAIN_TITLES[DOMAIN_ID]
START_YEAR=START_YEARS[DOMAIN_ID]