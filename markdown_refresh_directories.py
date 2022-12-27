import os
CWD = os.getcwd()

SITE_DIR = 'nadc'
# YAML
PAYORS_YAML_DIR = 'receipts/payors/'
PAYEES_YAML_DIR = 'expenditures/payees/'
RCP_YAML_DIR = 'receipts/filers/'
EXP_YAML_DIR = 'expenditures/filers/'

# PAYORS_YAML_DIR = 'campaign_finance/receipts/payors/'
# PAYEES_YAML_DIR = 'campaign_finance/expenditures/payees/'
# RCP_YAML_DIR = 'campaign_finance/receipts/filers/'
# EXP_YAML_DIR = 'campaign_finance/expenditures/filers/'


# filers
BUILDER_OUTPUT_RCP = f'{SITE_DIR}\\docs\\receipts\\filers'
BUILDER_OUTPUT_EXP = f'{SITE_DIR}\\docs\\expenditures\\filers'

# BUILDER_OUTPUT_RCP = f'{SITE_DIR}\\docs\\campaign_finance\\receipts\\filers'
# BUILDER_OUTPUT_EXP = f'{SITE_DIR}\\docs\\campaign_finance\\expenditures\\filers'

# payees
BUILDER_OUTPUT_PAYEES = f'{SITE_DIR}\\docs\\expenditures\\payees'
# BUILDER_OUTPUT_PAYEES = f'{SITE_DIR}\\docs\\campaign_finance\\expenditures\\payees'
OUTPUT_PATH_PAYEES = CWD + '\\' + BUILDER_OUTPUT_PAYEES
PAYEES_PREFIX = 'payees_'
PAYEES_OUTPUT_PATH = OUTPUT_PATH_PAYEES + '\\'

# payees single file
BUILDER_OUTPUT_SINGLE_FILE_PAYEES = f'{SITE_DIR}\\docs\\expenditures'
# BUILDER_OUTPUT_SINGLE_FILE_PAYEES = f'{SITE_DIR}\\docs\\campaign_finance\\expenditures'
OUTPUT_PATH_SINGLE_FILE_PAYEES = CWD + '\\' + BUILDER_OUTPUT_SINGLE_FILE_PAYEES
PAYEES_SINGLE_FILE_PREFIX = 'payees_'
PAYEES_SINGLE_FILE_OUTPUT_PATH = OUTPUT_PATH_SINGLE_FILE_PAYEES + '\\'


# payors single file
# BUILDER_OUTPUT_SINGLE_FILE_PAYORS = f'{SITE_DIR}\\docs\\campaign_finance\\receipts'
BUILDER_OUTPUT_SINGLE_FILE_PAYORS = f'{SITE_DIR}\\docs\\receipts'
OUTPUT_PATH_SINGLE_FILE_PAYORS = CWD + '\\' + BUILDER_OUTPUT_SINGLE_FILE_PAYORS
PAYORS_SINGLE_FILE_PREFIX = 'payees_'
PAYORS_SINGLE_FILE_OUTPUT_PATH = OUTPUT_PATH_SINGLE_FILE_PAYORS + '\\'

# BUILDER_OUTPUT_PAYORS = f'{SITE_DIR}\\docs\\campaign_finance\\receipts\\payors'
BUILDER_OUTPUT_PAYORS = f'{SITE_DIR}\\docs\\receipts\\payors'
OUTPUT_PATH_PAYORS = CWD + '\\' + BUILDER_OUTPUT_PAYORS
PAYORS_PREFIX = 'payors_'
PAYORS_OUTPUT_PATH = OUTPUT_PATH_PAYORS + '\\'
