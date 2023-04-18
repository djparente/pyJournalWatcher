import toml


class config:
    def __init__(self, apikey=None, gpt_model="gpt-3.5-turbo", gpt_model_name="GPT-3.5", max_results = 1000, reldate=7, query=None, journals=None, writtenquery=None, basedir="."):
        self.GPT_MODEL = gpt_model
        self.GPT_NAME = gpt_model_name
        self.MAX_RESULTS = max_results
        self.RELDATE = reldate
        self.QUERY = query
        self.API_KEY = apikey
        self.JOURNALS = journals
        self.WRITTENQUERY=writtenquery
        self.BASEDIR = basedir

    @staticmethod
    # Accepts a list of journals
    def build_journal_query(journal_list):
        res = ''
        if len(journal_list) == 0:
            return res
        else:
            res = f'"{journal_list[0]}"[journal]'

        for journal in journal_list[1:]:
            res = config.concat_queries(res, f'"{journal}"[journal]')

        return res

    @staticmethod
    def concat_queries(query1, query2, joiner='or'):
        return f'({query1}) {joiner} ({query2})'

    def __str__(self):
        return f'{self.GPT_NAME} ({self.GPT_MODEL}) with {self.API_KEY} for {self.RELDATE} days and max results {self.MAX_RESULTS} executing query: {self.QUERY}'

    def to_toml(self, path):
        with open(path, 'w') as tomlout:
             toml.dump({
                'GPT_NAME': self.GPT_NAME,
                'GPT_MODEL': self.GPT_MODEL,
                'MAX_RESULTS': self.MAX_RESULTS,
                'RELDATE': self.RELDATE,
                'QUERY': self.QUERY,
                'API_KEY': self.API_KEY,
                'JOURNALS': self.JOURNALS,
                'WRITTENQUERY': self.WRITTENQUERY,
                'BASEDIR': self.BASEDIR
                },
                tomlout
             )
