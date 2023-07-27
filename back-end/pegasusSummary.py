from transformers import BartForConditionalGeneration, BartTokenizer

def summaryGen(text):
    model_name = "facebook/bart-large-cnn"  # You can choose a different BART model here
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)


    inputs = tokenizer(input_text, max_length=1024, return_tensors="pt", truncation=True)

    # Step 4: Generate Summarization
    summary_ids = model.generate(inputs.input_ids, num_beams=4, min_length=30, max_length=200, early_stopping=True)

    # Step 5: Postprocess the Summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary
