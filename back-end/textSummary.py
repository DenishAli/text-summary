import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


def summrization(docs):
    stopwords = list(STOP_WORDS)
    # print(stopwords)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(docs)
    # print(doc)

    # Word Count dictionary
    word_count = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_count.keys():
                word_count[word.text] = 1
            else:
                word_count[word.text] += 1

    # print(word_count)

    max_count = max(word_count.values())
    # print(max_count)

    for word in word_count.keys():
        word_count[word] = word_count[word]/max_count
    # print(max_count)

    sent_token = [sent for sent in doc.sents]
    # print(sent_token)

    sent_count = {}
    for sent in sent_token:
        for word in sent:
            if word.text in word_count.keys():
                if sent not in sent_count.keys():
                    sent_count[sent] = word_count[word.text]
                else:
                    sent_count[sent] += word_count[word.text]
    # print(sent_count)

    lentofsumm = int(len(sent_token) * .40)
    # print(lentofsumm)

    summary = nlargest(lentofsumm, sent_count, key = sent_count.get)
    # print(summary)

    final_summ = [word.text for word in summary]
    summary = ' '.join(final_summ)
    
    return summary
