
# A seperate file which is included in .gitignore so that the credentials are not saved on GitHib
# This is just a best practice move, even through test credentials its good to get in the habit!

import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3dunh)!@eu^-%f$&1!bu#-=r+w$8-xdc(5yel)!v=6z+ykvp^b'

#Stripe Environment Variables:
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_AVtmQrxAW5mVkGxRQsDZpnG0')

#Don't want this email going up on GitHub
PAYPAL_RECEIVER_EMAIL = 'paul_cheeseman@zoho.com'