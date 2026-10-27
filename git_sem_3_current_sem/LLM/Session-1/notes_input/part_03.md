# Part 03  [00:33:43 - 00:50:35]

## Segment 021  [00:33:43 - 00:36:23]
Slide: slides/slide_021.jpg

**Monali Mavani** [00:33:46]: See, I want to perform sentiment classification. Yes, you can use the any BERT-based or encoder-based classifiers, but you can also do this using Llms, or I can say that by the means of conditional generation of text. See, this is you want to say? And I assume you know transformer is a decoder based architecture. There is no encoder part over here. We'll again review
the decoder architecture in the third module. This is my transformer decoder, and I'll put the classification head on top of it, so that given the input, the sentiment of the sentence, I like Jackie Chan is, you can see the column here, that is my input. I will call it context. And then, what is the probability that my language model will output a positive, or what is the probability that my
language model will output negative? So, you can see probability of a positive sentiment, the word positive, the token positive, is conditioned on the text. And here the text is, the sentiment of the sentence is like that. Similarly, probability of this. Like a negative or a positive sentiment, so that's called conditional generation of text. I can convert my sentiment classification using this.
Similarly, I have the question answering. Hmm. We have a question, probability of a word. See, question answering that means you want to answer. Then what will go as a context? Say, question, column, who wrote the book, then the name of the book, the origin of the species, then question mark, then some indicator that you have to start the answer. And then dot. So this becomes the context and my
language model can output the actual answer. So those kind of application we can always model using language modelling objective. by simply designing a prompt. So, that's the very high level idea that many NLP tasks can be solved using Llms. But obviously, the question that you have to answer, as an application designer, that you really need an Llms, or you can you need large models, or you need a
small models, or you can go ahead with the BERT-based model. All these answers you have to answer. So, yeah. And then we will talk about Generative AI. Now, understand this diagram.

## Segment 022  [00:36:23 - 00:37:51]
Slide: slides/slide_022.jpg

**Monali Mavani** [00:36:27]: I hope this diagram is visible. Yeah, see this is an input to the transformer. You know the working of the transformer. So long N thanks for. Now the next token has to be predicted. So the next token is all. How does this get predicted? Yes. any input. You know the transformer and the output of the transformer. You have so many layers of transformer and then there is
an output. And the next token, like you are testing the transformer, not the training. Training you do teacher forcing, but we are doing using it for some task. OK, so that means you're testing our inference, so... After so many, you know, input, you are generating, predicting the next word in the decoder only transformer. And here my prediction is all. How does it get predicted out of the final
layer and the final output of your transformer? What is that in the final layer? Of the transformer. Or, what could be there in the final layer of the transformer? Software, correct? So again, we'll talk about it in detail. One minute. Yeah. So, you can see this.

## Segment 023  [00:37:51 - 00:38:43]
Slide: slides/slide_023.jpg

**Monali Mavani** [00:37:53]: I have the probability. Softmax gives me the probabilities. I have 10 classes in my data set. Let's understand Softmax from the, or I can say let's recap the Softmax from the machine learning perspective. You have 10 classes in your data set and Softmax will give probabilities for each of the class. And then you can pick up the maximum. Highest probability class that
you must have learned by now. Now, here, what are my classes? In case of my text in data, which is divided into tokens, and for the time being, consider your words are your tokens. So, yes, what are my classes? Corpus are my classes, I'm talking about classes. Yes, RAJEEV. M.V., you are correct. Tokens are my classes. Correct. So, if I have a text data, each of the tokens or each of the words

## Segment 024  [00:38:43 - 00:42:39]
Slide: slides/slide_024.jpg

**Monali Mavani** [00:38:47]: in my vocabulary are my classes, and Software will give me probability of the next word over my context. That's my language modelling, and what is the context here? my entire vocabulary. Out of my vocabulary, which is the token I should choose next. So what do you see over here? This is my vocabulary. I mean, all tokens in my vocabulary. This is like your English,
your dictionary. You can think about your vocabulary as your dictionary. All the unique words. are given in your dictionary. So that becomes my vocabulary. I'll talk about vocabulary in a while, but for now, we can understand in that way. And for each words in my vocabulary, I have the probability. And softmax will do what? It will give us this probability distribution for each class. And then we
are picking up the highest probability that becomes the next token prediction or predict the text. That means assigning a distribution over the. All the words, sorry, not the following words, vocabulary words. This is what is my standard language modelling objective. Now, this objective I can tweak a little bit. Now, question is, why should I pick up always the highest probability word? Why can't
I pick up the next highest probability word? Just imagine. You have 50,000 words in vocabulary, like our English language. If I want to develop a language model for the English language, we have so many unique words. So I have 50,000 unique words. Many of the words are synonymous of each other. Why should I restrict myself only to choose the highest probability word? Why not the second highest?
Why not the third highest? In other words, I can sample. And I can sample any of the words over from this probability distribution. So that makes this language model as a generative model. And when you sample randomly any of those words, like rather than all, I can sample your also. I can sample any other words. So that means I can generate different kind of text. And that's called Generative AI.
They are the language modelling objective. Our transformer is a standard transformer, which performs next token prediction. which is my language modelling objective, but I will add something else at the end of the transformer. We call it decoding or the sampling logic, which can sample. Not just the highest probability word, but any of the words, and that is based on the different techniques. We
have sampling algorithms, and that is part of your inference, and we will talk about in that 4th module. So, process of generating natural language text with the Llms is called a decoding. Remember, it uses transformer. Transformers still are trained on the next token prediction task, but how do we use that in Llms is different, and that process is a decoding, and due to this, we call it as a
generative model, and if your transformer can generate, your LLM can generate. text, why not code, why not images, speech, audio, and so on. So the idea which originated with the text input, now you can see it is transformed to all kind of inputs, multi-modal inputs. So that's the idea of what is Generative AI. Okay, let me see if you've got any questions here.

## Segment 025  [00:42:39 - 00:43:17]
Slide: slides/slide_025.jpg

**Monali Mavani** [00:42:42]: Yes, Tushar, you are correct. Context is a words in the prompt. Why all vocabulary? We'll talk about it. Yes, Aditya, you are correct. Harmanpreet, all of that we will discuss when we'll discuss the inference, why it is required. Yes, you are correct. Temperature sampling, somebody said, then yes. Vocabulary is corpus; vocabulary is not a corpus. I'll talk about it,
okay? Yeah, let me go ahead. All of these questions will be answered subsequently. So let's understand what are the building blocks of Llms.

## Segment 026  [00:43:17 - 00:43:57]
Slide: slides/slide_026.jpg

**Monali Mavani** [00:43:21]: See, you have the transformer on the core of your Llms is a transformer. which uses the attention mechanism. Those are architecture details. But like any other neural network or any other machine learning model, what do you need as an input? It should be numbers or it should be like our text words. What should be there? Should be numbers, correct numbers. Yeah,
vectors, it's a good way of telling, but basically we need numbers. So that's a classical machine learning.

## Segment 027  [00:43:57 - 00:46:55]
Slide: slides/slide_027.jpg

**Monali Mavani** [00:43:58]: But now here I have a text as an input. And this text, I have so many documents with me. All PDF documents or text documents or e-mail documents or my web documents and so many documents are there. Collection of those documents. Collection of such documents. Pre-processed. Becomes corpus. because there are so many, so many pre-processing required. See, this is not.
Still, it is the text. Still, it is the collection of different sentences. I cannot give it to the Llms. I cannot give it to the transformer. But I have collection of documents. There are so many handwritten documents. There are so many chat logs, which doesn't make sense, right? So I have to be very sure and create a corpus. And that's called the corpus. And it is a general lingo which is used in
NLP. And you can use any model, not only just the LLM that you need to use it. So that's collection of document is a corpus. Now, this corpus has got sentences or documents. So I need to convert them into tokens. In a simplest word you can think about, token is nothing but words. I'll convert my sentences into words. In a simple words, but in this technical words, I'll have to convert this into
the tokens. How do we convert them into tokens? Can I take each word as one token? Like this building is 1 token, blocks is another token, office is another token, Llms is another token. The original idea of tokenization started with this concept. Treat each word as the tokens, and then we have the NLP libraries like NLTK and all. They can do this tokenization over a time. There are many
tokenization algorithms have been evolved due to various pros and cons, and today what is popular that we will discuss is byte pair encoding and the byte level. BP. That's about tokenization. Remember, still, we have only converted my series of sentences into tokens. They are still the characters. They are not converted into numbers. So I'll have to convert them into token embeddings. I cannot
just simply convert into numbers, right? So tokenization is a process. Here, OK. This, so these two steps are input steps, the input pre-processing happens, and I'll talk about each of each of the steps. We'll talk in detail, then this is your actual transformer architecture, and then on top of it, we are adding the language modelling head. So, this first two and three, I'll talk, I'll discuss
today.

## Segment 028  [00:46:55 - 00:47:53]
Slide: slides/slide_028.jpg

**Monali Mavani** [00:46:56]: This is what I just shown. You give input, like you all are using ChatGPT or Cloud or Gemini. You give input to that LLM, and then we get an output one by one. You can actually see the output is generated one word at a time. Although today's LLM has become so fast, But if you just pay attention, they are generated 1 by one. That's very important for you to remember
that output is generated 1 token at a time. And that is where you will understand the inference, how does inference happens? But yeah, right now understand this LLM. We have input is a tokenizer, then we have standard stack of transformer blocks, and then we have a language modelling header. And this is the transformer architecture. I'm just keeping it for a third module. We'll discuss this
architecture in. Detail. What is tokenization? Yeah, now how the vocabulary is built?

## Segment 029  [00:47:53 - 00:50:35]
Slide: slides/slide_029.jpg

**Monali Mavani** [00:47:58]: We have a complete training data set, which is nothing but corpus. And so this is just example of 1 sentence. The quick brown fox jumps over the lazy dog. Likewise, you have so many corpus, okay? From the collection of documents, there are people who create the corpus and make it publicly available. So which you can use it to train your models. So, that's a corpus,
which a collection of pre-processed documents. From that, you will tokenize. Depending on the tokenization algorithm, for a simplicity, we see that every word is a token. The quick is 1 token, quick is another token, brown is another token. From your training data set, which is a training corpus, you will build the vocabulary. Of unique words. So you can say this is a vocabulary that we have built
up of the unique words, and each of these unique words will be given a token IDs. This is a job of tokenizer when you say you are training a tokenizer. This is what you will do. You will first create a corpus, then you will tokenize the corpus using any of the tokenization algorithm. Then you will build the vocabulary of unique words, and each of the words you will give a token ID. So if I have,
say, 50, 000 tokens, In my vocabulary, my token IDs. Will be say from zero to. 49,999 and 9. That's the technique of vocabulary building. So this is an English example. You can build a vocabulary in Thai language, in Maruti language, in English language, or a medical language, or finance language, any language, any jargon. You can build your vocabulary. Either you are changing the language or you
are changing your domain. Your vocabulary depends only on your domain corpus. It doesn't depend on anything else, and you are going to train your model on your vocabulary only. Any words which are out of vocabulary, we will see how different organisation handles it. But there is always possibility that there are words could be out of your vocabulary. Now, so why tokenization? Why can't we just
have words as tokens?
