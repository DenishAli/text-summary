import spacy
from collections import Counter
import en_core_web_sm

def text_summarization(text, num_sentences=3):
    # Load the spaCy English model
    nlp = spacy.load('en_core_web_sm')

    # Process the input text with spaCy
    doc = nlp(text)

    # Tokenize the sentences and get the lemma for each word
    sentences = [sent.text for sent in doc.sents]
    words = [token.text for token in doc if not token.is_stop and not token.is_punct]
    lemma_words = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]

    # Calculate word frequency using lemmatized words
    word_freq = Counter(lemma_words)

    # Calculate the importance score for each sentence using TextRank algorithm
    sentence_scores = {}
    for sentence in sentences:
        for word in sentence.split():
            if word in word_freq:
                if len(sentence.split()) < 30:
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = word_freq[word]
                    else:
                        sentence_scores[sentence] += word_freq[word]

    # Get the top 'num_sentences' sentences with highest scores
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]

    # Join the top sentences to form the summary
    summary = " ".join(top_sentences)

    return summary
