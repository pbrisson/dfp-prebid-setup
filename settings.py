import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
GOOGLEADS_YAML_FILE = os.path.join(ROOT_DIR, 'googleads.yaml')


#########################################################################
# DFP SETTINGS
#########################################################################

# A string describing the order
DFP_ORDER_NAME = None

# The email of the DFP user who will be the trafficker for
# the created order
DFP_USER_EMAIL_ADDRESS = None

# The exact name of the DFP advertiser for the created order
DFP_ADVERTISER_NAME = None

# Names of placements the line items should target. Has priority over ad units.
DFP_TARGETED_PLACEMENT_NAMES = []

# Sizes of placements. These are used to set line item and creative sizes.
DFP_PLACEMENT_SIZES = [
  {
    'width': '300',
    'height': '250'
  },
  {
    'width': '728',
    'height': '90'
  },
]

# If no placement should be used, for example for a run of network. If True, 
# DFP_TARGETED_PLACEMENT_NAMES still need to be set to an empty array.
DFP_ALLOW_NO_INVENTORY_TARGETING = False

# Whether we should create the advertiser in DFP if it does not exist.
# If False, the program will exit rather than create an advertiser.
DFP_CREATE_ADVERTISER_IF_DOES_NOT_EXIST = False

# If settings.DFP_ORDER_NAME is the same as an existing order, add the created 
# line items to that order. If False, the program will exit rather than
# modify an existing order.
DFP_USE_EXISTING_ORDER_IF_EXISTS = False

# Optional
# Each line item should have at least as many creatives as the number of 
# ad units you serve on a single page because DFP specifies:
#   "Each of a line item's assigned creatives can only serve once per page,
#    so if you want the same creative to appear more than once per page,
#    copy the creative to associate multiple instances of the same creative."
# https://support.google.com/dfp_sb/answer/82245?hl=en
#
# This will default to the number of placements specified in
# `DFP_TARGETED_PLACEMENT_NAMES`.
# DFP_NUM_CREATIVES_PER_LINE_ITEM = 2

# Optional
# The currency to use in DFP when setting line item CPMs. Defaults to 'USD'.
# DFP_CURRENCY_CODE = 'USD'

# Optional
# Determine if line items and creative should be associated in batch.
# Useful to avoid timeouts if many of them have to be created.
# DFP_ASSOCIATIONS_BATCH = 50

#########################################################################
# PREBID SETTINGS
#########################################################################

PREBID_BIDDER_CODE = None

# Whether DFP targeting keys should be created following Bidders' Params structure.
# This is used when it's required to send all bids to the ad server.
# See: http://prebid.org/dev-docs/bidders.html
# And: http://prebid.org/adops/send-all-bids-adops.html
PREBID_BIDDER_PARAMS = False

# Price buckets. This should match your Prebid settings for the partner. See:
# http://prebid.org/dev-docs/publisher-api-reference.html#module_pbjs.setPriceGranularity
# FIXME: this should be an array of buckets. See:
# https://github.com/prebid/Prebid.js/blob/8fed3d7aaa814e67ca3efc103d7d306cab8c692c/src/cpmBucketManager.js
PREBID_PRICE_BUCKETS = {
  'precision': 2,
  'min' : 0,
  'max' : 20,
  'increment': 0.10,
}

#########################################################################

# Try importing local settings, which will take precedence.
try:
    from local_settings import *
except ImportError:
    pass