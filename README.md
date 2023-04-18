# pyJournalWatcher

## Descriptionpy
JournalWatcher is a method of systematically monitoring the medical literature indexed by PubMed and producing summaries using OpenAI's GPT-3.5 and GPT-4 API.

## Quickstart
For Windows, an executable (.exe) has been created using pyInstaller that can be copied to the directory of your choosing and run by double-clicking the executable. 

You will need to obtain an OpenAI API key to use the software, available at: https://platform.openai.com. OpenAI charges for the use of their API, but the costs are relatively modest. See more details at their website: https://openai.com/pricing. 

A graphical user interface will appear. You will need to choose journals you want to review and can also specify arbitrary PubMed queries. You can build PubMed queries here: https://pubmed.ncbi.nlm.nih.gov/advanced/


## Installation
### Clone the repository locally

    git clone https://github.com/djparente/pyjournalwatcher.git

### Create a virtual environment

    python -m venv pyjournalwatch-venv

### Activate the virtual environment

Under Windows with the command line:

    .\pyjournalwatch-venv\Scripts\activate.bat

or under Winwodws with the PowerShell:

    .\pyjournalwatch-venv\Scripts\activate.ps1

Under Linux/OSX:

    source pyjournalwatch-venv/bin/activate

### Install dependencies

Once inside the venv:

    pip install -r requirements.txt

### Run the program

Once inside the venv, run the program as follows:

    python src/main.py

## Citation
This project is currently under peer review. If for some reason you need to cite it in the interim, please contact me at dparente@kumc.edu.

## Problems?

Please contact me at dparente@kumc.edu for bug reports (or open a GitHub issue).

## Cautions and Disclaimers

1. I am not affiliated with the National Library of Medicine (NLM), National Center for Biotechnology Information (NCBI), PubMed, or OpenAI.
2. Use of the software requires you to comply with the NLM and NCBI API requirements. The software should automatically try to do this (it is based on PyMed), but the API may change requirements or format over time.
3. Use of the OpenAI API incurs costs. You will need to use an API key. Based on current pricing, I estimate the summarizing a typical abstract with GPT-3.5 costs about $0.002. However, pricing may change. The program is hard-coded to abort if it thinks it is about to spend more than $5. However, you are responsible for all costs incurred with OpenAI through use of the software.
4. GPT-based summaries may sometimes be inaccurate or have biases. This is a ***research tool*** that might help scientists and physicians more quickly find articles they want to read.  Do not rely on these summaries to make medical decisions. Medical decisions should be made on the basis of thoughtful review of the full text of the human-written medical literature, meta-analyses, and professional guidelines. Summaries are not a subsitute for physician judgement.
