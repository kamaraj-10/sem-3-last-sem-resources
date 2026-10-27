# Part 06  [01:21:17 - 01:37:37]

## Segment 051  [01:21:17 - 01:22:29]
Slide: slides/slide_051.jpg

**Monali Mavani** [01:21:20]: all of this we will be using PyTorch and Hugging Face implementation in PyTorch. So you see this is from tokenizer import tokenizer. Tokenizers is a Hugging Face library. Then you will have tokenizers.models. BPE. You can see over here BPE. So this BPE is algorithm which is already available. You have to use it. So you will, we have created an object tokenizers as a
class. We have created object tokenizer where we will pass our BPE. We will use a BPE trainer and then, so how to use this, you will be able to see in. First webinar. Okay, that's Hugging Phase is where you would like to learn more about it over a time. We will extensively be using Hugging Face Library. All open source models, they are published, I mean many of them, most of them publish in this
Hugging Face platform. OK, now going back here. You are building an open source model pipeline.

## Segment 052  [01:22:29 - 01:24:05]
Slide: slides/slide_052.jpg

**Monali Mavani** [01:22:30]: You are not training a tokenizer. You are developing an application using open source models. There also you will use the Hugging Face tokenizers from the Transformers library. So, Hugging Face Transformer Library, you will use those tokenizers, but if you are using with the proprietary models like Open AI Models, then you will be using the TikToken is a library.
Okay, yeah. Open AI has published this TikToken library. Because Open AI uses the open models, you can use the tokenizer to tokenize your own corpus. The purposes of this TikToken library is perform the token count. counting because you're going to use their API. You're not going to download any model, but you're going to use those models. And your OpenAI is a hosted library, but this big token is
the open source library with which you can use the OpenAI tokenization features. Similarly, Cloud and Gemini models, if you are using Google's model you are using, they don't have, they have their own APIs. with which you can count the tokens. But as such, these are the proprietary models, so you cannot use them to build your own pipeline. You cannot download them, or you cannot extend their
tokenizers. So this is just a landscape of the tokenizer framework. OK, now we will end this tokenization

## Segment 053  [01:24:05 - 01:25:29]
Slide: slides/slide_053.jpg

**Monali Mavani** [01:24:06]: algorithm. We have done tokenization, we have used the tokenization, and we have created tokens. We have built a vocabulary, which is a part of my tokenizer training, and now I'm using it. I'm using my LLM. So whatever input I give to my LLM, again, I have to perform the tokenization. So say this is my sample text. First, it is tokenized, and I have my existing
vocabulary. which I've already built during the training, tokenizer training. The brown dog. This is during inference. This is my text. You can see the has got a token ID 7, brown has got a token ID 0, dog has got a token ID 1. So this is what is my token IDs. Remember, each word in my vocabulary will get the token IDs, and they are fixed. From the token IDs, when I actually use it, I want to pass
those token IDs to my transformer. I have to generate the token embeddings. We are not passing token IDs as it is. How do we? OK, before I explain how do we generate this token IDs, understand what are the embeddings first, and before that...

## Segment 054  [01:25:29 - 01:26:43]
Slide: slides/slide_054.jpg

**Monali Mavani** [01:25:31]: I have built my vocabulary based on my domain corpus. I will also add certain context tokens. Like a known token is one of the example, then end of the text token. These are the tokens that I will add in my vocabulary and some token ID will be generated for those tokens. And for every model, those are different. Like maybe this is a Lama style, Mistral uses a
different. So it's very important that you use your.. . The model with its own vocabulary. And own tokenizer, because they have added their own some helper tokens, so I can say, or context tokens. So, this is a complete flow. We have an input text. We are tokenizing it depending upon the same tokenizer that my model has been trained on. It generates the token IDs. And then finally, we will
generate the token embeddings. What are these embeddings? Now, those who don't know, I'll recap about these embeddings.

## Segment 055  [01:26:43 - 01:30:07]
Slide: slides/slide_055.jpg

**Monali Mavani** [01:26:46]: See, I have a word. I want to generate into some vector of numbers, but in a meaningful way. Say, these are my dimensions. With which I want to rate every word, say, animal, newborn, human, pural - all these are the features, and I want to see, I want to give a number on which all of these words. Will have the some number, say, for example, cat. Cat is an animal, so
for the animal dimension. It will have some higher number. But the word "house" is not an animal, so for the animal dimension, it will have a lower number. This is a meaning of embedding. Every word gets converted into, like here, token. Every token gets converted into embeddings. Embedding will have dimensions, and every dimensions have a particular, or I should say, every dimension captures the
particular characteristics of that token. How does it look like in an Embedding space? Say, for example, this is 2 dimensional. Embedding space, simple X&amp;Y. I have just two dimension. I'm defining every word into two dimension, animal, not animal, and things like that. You can see the words which are similar to each other. They have a similar meaning. They are cluttered or they are clustered
together. in the embedding space. Cat, dog, puppy, they are similar, like they belong to animal category. Similarly, apple and banana, they belong to fruit category. There are some similarity between them, so they are clustered together. This is where, this is the end goal of embedding creation or the embedding algorithms. that every word when we create embeddings. So what is the embedding? I'll
write down here. Vector of numbers, but these numbers are not just arbitrary random any numbers. It captures the meaning of those words, so that's the end of Embedding algorithm. This word gets created, and we call this.. . Is A contextual Embedding. That's what everywhere it is used, because if the context changes, the this vector numbers will also change. So, if a bank is a financial bank. Our
bank is a river bank. Depending upon your corpus, it will have a different contextual embedding generated, but that's the general idea of embedding. We have static embedding in that case. Irrespective of its meaning, bank will have the same Embedding gets generated. Now, how does it relate to our input to the transformer? Remember, after tokenization, I have to give input to the transformer. So it
has to be converted into embeddings. We don't have a separate encoder model which generates the contextual embeddings.

## Segment 056  [01:30:07 - 01:31:07]
Slide: slides/slide_056.jpg

**Monali Mavani** [01:30:11]: But we have something called Embedding layer. So, I have a tokenizer. Which will give me token IDs? Then I have my Embedding layer. Which input the token IDs? Embedding layer, and which will generate the embeddings. This is what is used in practise, and I have given you this example, very small example. You have a text converted into token IDs. That's the job of your
tokenizer. Now, we have something called Embedding matrix. The size of embedding matrix is vocabulary size multiplied by embedding dimensions. And every model has got its own embedding dimensions, like here.

## Segment 057  [01:31:07 - 01:31:37]
Slide: slides/slide_057.jpg

**Monali Mavani** [01:31:09]: GPT-2 has got five and two. Dimension embeddings. And Bert, original Bert has got I guess 7, 768 if I'm not wrong, 768 dimension Embedding. So every model will publish what is its Embedding dimension. So that is what is D, very important number. And V, this is a vocabulary size.

## Segment 058  [01:31:37 - 01:35:13]
Slide: slides/slide_058.jpg

**Monali Mavani** [01:31:42]: Now, this Embedding matrix. Will be randomly initialised initially. That means it will have any random numbers. So this is my token IDs. For each token, there is one row. You can see these are my unique tokens. Again, this is my toy example. So say my vocability size is just six tokens. Now, Fox, your Fox is having a token ID too, so the 2nd row will be picked up. And
they are the three dimension. In this example, I have D is only three, three dimension, and that is the embedding for the word fox. Similarly, jumps. Jumps is having token ID 3. So we'll pick up the third row from this embedding matrix. And the embedding for the word jump will be picked up. As you can see, they are the same number. So in the today's LLM, Embedding layer is nothing but a lookup in
an embedding matrix. And this embedding matrix, while training, it is randomly initialised. When we train the transformer, this E, this embedding matrix is a trainable parameter, and eventually at the end of the training, we will get the correct meaningful embedding vector for. Every word, so that during the inference we will get correct numbers here. So that's the Embedding layer in transformer
input, which converts token ID into the embeddings. And by simple, we have to multiply. You multiply input. Will get multiplied by your Embedding matrix. And we will get the Embedding for each input, so you can say my input is now N into D. East size of East is vocabulary into D, input is North into D, understand this from the matrix multiplication perspective. AN. So, I'm a... Multiplying the
token ID, just it is just the sorry, this is I'm not multiplying X into E, I am generating X. I have 3 inputs, oh sorry, 4 inputs here in my this example, 4 tokens. Each of the token is having three dimension, so my input will become 4 by 3 metrics. Which goes to the Transformer? For each word, there is a three dimension matrix. In reality, my input length is very large, sequence length is very
large, and D, my dimension are also very large. Okay, so any any doubts here? Oh.

## Segment 059  [01:35:13 - 01:37:37]
Slide: slides/slide_059.jpg

**Monali Mavani** [01:35:29]: I'm just reading your questions. I hope you are answering each other's questions, but let me read this. This token IDs for any given word, yes, yes, token ID, token ID, token IDs are part of the tokenizer itself. Uh... Yes, this Embedding will have a context information. Yes, after the training, it will have a context information. OK, can we say vector plus meaning
the vector represents is equal to Embedding? See, embeddings are the vectors, okay? And the numbers which you see in those vectors are the, they are somehow, they have captured the meaning. Okay, this is how I will say. This is, I'm answering the question one minute for Avnish. Embedding RBD vectors, nothing else. So, this is the next question. One minute. BHAWANI PALIWAL. Yeah. Bank in a river,
because this happens during the training, decoder training. Do you now recall your transformer training? During the training, every parameter gets updated. The same thing happens here: I will consider my embedding matrix E as the parameter, and that gets updated during the training, and that's how we are getting a bit of context is added, or I can say bit of the bit of I can say not as good as the
encoder only architectures, but decoder can. Also, create this way contextual embeddings. A general dimension of this Embedding varies from model to model. You have to cheque their model. As I explained, Bert is 76, 768 dimension, but every model will have different dimensions. Okay. There are different types of embeddings. We can have document embeddings,
