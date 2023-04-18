import appdirs
import os

# These are 'hard-coded' global configuration options that are not specifiable the command line
CACHE_OPEN_AI = '.CACHE_OPENAI'
NLM_TOOL_NAME = "pyJournalWatcher Program being run by unknown user"
NLM_EMAIL = "not-specified@example.com"
PMID_FILE = 'processed_pmids.txt'
BACKUP_PREFIX = 'processed_pmids-'
OUTSUFFIX = ''
OUTPUT_DIRECTORY = 'ToReview'
OAI_LOWER_THRESHOLD = 800
MAX_COST = 5

DATADIR = appdirs.user_data_dir('pyjournalwatch', 'kumcfm')
LOGDIRECTORY = appdirs.user_log_dir('pyjournalwatch', 'kumcfm')
CACHEDIR = appdirs.user_cache_dir('pyjournalwatch', 'kumcfm')
BACKUP_DIRECTORY = os.path.join(DATADIR, 'bak')

# Create any missing directories
for d in [DATADIR, LOGDIRECTORY, CACHEDIR, BACKUP_DIRECTORY]:
    if not os.path.exists(d):
        os.makedirs(d)



