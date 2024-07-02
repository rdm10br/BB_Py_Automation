# import asyncio
# from playwright.async_api import Page, expect

# from ..Metodos import getPlanilha, getFromAPI
# from Decorators.Main_StartUp import playwright_StartUp


# @playwright_StartUp
# async def run(page: Page, index) -> None:
    
#         id_externo = getPlanilha.getCell(index=index)
#         id_interno = await getFromAPI.API_Req(page=page, index=index)
        
#         baseURL = 'https://sereduc.blackboard.com/'
#         classURL = f'{baseURL}ultra/courses/'
#         classUrlUltra = f'{classURL}{id_interno}/outline'
        
#         print(id_externo)
        
#         await page.goto(classUrlUltra)

# async def main():
#     await run()

# asyncio.run(main())

# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.tag import pos_tag

# # Download NLTK data
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# # Sample text
# text = "NLTK is a leading platform for building Python programs to work with"\
#     " human language data."

# # Tokenize the text
# tokens = word_tokenize(text)

# # Perform part-of-speech tagging
# pos_tags = pos_tag(tokens)

# # Print tokenized text and POS tags
# # print("Tokenized Text:", tokens)
# print("POS Tags:", pos_tags)
# # print('{:5}|{:5}'.format(f'Token Text | {tokens}', f'POS Tags | {pos_tags}'))

from textblob import TextBlob
import sys
# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')

# Sample text
text = '''TextBlob is amazingly simple to use.
What great fun!
TextBlob is amazingly simple to use.
a) teste.'''

# Create a TextBlob object
blob = TextBlob(text)

# Perform sentiment analysis
# sentiment = blob.sentiment
sentence: str = blob.sentences
# Print sentiment polarity and subjectivity
# print("Sentiment Polarity:", sentiment.polarity)
# print("Sentiment Subjectivity:", sentiment.subjectivity)

# print(blob.sentences[0])

index = 3
print(f'\n{sentence[index]}\n')

if sentence[index].startswith('a) ') is True:
    index-=1
    print(f'{index}\n')
    print(f'{sentence[index]}')