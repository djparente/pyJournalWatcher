import os.path
import globalconf
import openai
from datetime import datetime
import time
import logging
from diskcache import Cache
import os

# This just creates a dummy 'summary' for testing purposes, avoiding OpenAI API calls
def create_summary_dummy(abstract_content):
    logging.info('Dummy summary requested')
    print("=======")
    print(abstract_content)
    return abstract_content[0:100]

def summary_from_cache_or_create(pmid, abstract_content, apikey, model="gpt-3.5-turbo", baseDirectory = '', simple_instructions=False):
    # Get the cache

    cache_path = os.path.join(globalconf.CACHEDIR, globalconf.CACHE_OPEN_AI)
    cache = Cache(cache_path)
    k = f'{pmid}_{model}'   # Calculate a key based on PMID and the GPT model (so, for example, if a GPT-3.5-turbo
                            # summary was cached, and a gpt-4 summary was requested; this is a cache miss)

    # If we are using simple instructions, add this to the key
    if simple_instructions:
        k = k + "_simple"

    result = cache.get(k)   # Try to get the result from the cache
    if result is None:
        # If not in cache, query the API to create a new summary
        logging.info(f'Cache miss for {pmid} with {model} and will query OpenAI')
        return create_summary(pmid, abstract_content, apikey, model=model, cache=cache)
    else:
        # Otherwise return the summary
        logging.info(f'Cache hit for {pmid} with {model}; returning from cache')
        return result


# Get a summary of the article using the OpenAI API; note this WILL NOT work with GPT-3 models which use the
# completion endpoints. The below example assumes you are using the ChatCompletions endpoint (e.g., GPT-3.5 or 4)
def create_summary(pmid, abstract_content, apikey, model="gpt-3.5-turbo", cache=None, simple_instructions=False):
    openai.api_key = apikey # Specify the API key

    # The summarization instructions
    expert_instruct = 'The following is the abstract of a medical research article. In a paragraph, summarize the most important points for a practicing physician. If possible, include details of the study design, total number of participants, major results, and important conclusions. For this summary paragraph, use no more than 150 words. Include quantitative information when possible.'
    lay_instruct = 'The following is the abstract of a medical research article. In a paragraph, summarize the most important points for an intelligent layperson who is not a physician. Use simple and clear words. Avoid jargon. Emphasize aspects that are new and important. For this summary paragraph, use no more than 150 words.'

    instruct = expert_instruct
    if simple_instructions:
        instruct = lay_instruct

    # I've noticed occassional random and unexpected failures from the OpenAI endpoint, so wrap this in a try/catch
    # so that one abstract failing summarization doesn't abort the entire program
    try:
        logging.info("Preparing to run OpenAI query (sleeping 2 seconds)...")
        time.sleep(2)   # Include a short delay to prevent submitting too many queries at once and allowing the user
                        # time to cancel the program
        logging.info(f'Running OpenAI query against {model}...')    # Inform the user

        # Execute the request against the ChatCompletions endpoint
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": instruct},
                {"role": "user", "content": abstract_content},
            ]
        )

        # Process the response
        tokens_used = response['usage']['total_tokens'] # Keep track of tokens used
        res = response['choices'][0]['message']         # Get the response message
        content = res['content']                        # Get the summary out of the response

        logging.info(f'Recieved OpenAI Response and used {tokens_used} tokens') # Inform the user

        stime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')    # Keep track of the time and date

        # If we're using a cache
        if cache is not None:
            k = f'{pmid}_{model}'   # Calculate the cache key
            if simple_instructions:
                k = k + "_simple"

            cache.set(k, content)

        # During debugging, we were logging these queries, but not in production
        #with open(f'queries/output-{stime}.txt', 'w', encoding='utf-8') as f:
        #    print(f'== Tokens: {tokens_used} ==', file=f)
        #    print(res, file=f)
        #    print("======", file=f)
        #    print(content, file=f)

        # Return the summary
        return content
    except Exception as e:
        logging.error(f'OpenAI failure: {str(e)}')
        return "OpenAI summarization failure"
