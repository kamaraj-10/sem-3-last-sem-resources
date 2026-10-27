# Part 08  [01:53:01 - 02:08:25]

## Segment 070  [01:53:01 - 01:53:31]
Slide: slides/slide_070.jpg

**POWAR SAGAR GANPATI** [01:53:02]: And this plus the positional embedding will be given as input, right?

**Monali Mavani** [01:53:07]: Yes, yes, yes, you're correct to the transformer for

**POWAR SAGAR GANPATI** [01:53:10]: Okay, now, now in the B.

**Monali Mavani** [01:53:11]: processing. Mm.

**POWAR SAGAR GANPATI** [01:53:13]: Right now in the bdb.

**Monali Mavani** [01:53:14]: Yeah. Mhm.

**POWAR SAGAR GANPATI** [01:53:16]: This token Embedding is is that the output we are generating in the BP encoding or what what is OK, so it is a token.

**Monali Mavani** [01:53:24]: No, no, no, no. BP just gives you tokens. See, BP will give you... one minute. So again, BP trainer and BP segmenter. BP trainer,

## Segment 071  [01:53:31 - 01:54:45]
Slide: slides/slide_071.jpg

**Monali Mavani** [01:53:33]: it will give you the vocabulary and for each vocabulary token IDs are there, right? It's a number, it's indexing. Say index one, we have one word.

**POWAR SAGAR GANPATI** [01:53:39]: Right.

**Monali Mavani** [01:53:43]: index two, we have another word. So BP's job is only to do this because BP is a tokenizer. It will build a vocabulary during,

**POWAR SAGAR GANPATI** [01:53:50]: OK, bdb.

**Monali Mavani** [01:53:51]: it's a tokenizer. So during training, it will generate your vocabulary and it

**POWAR SAGAR GANPATI** [01:53:54]: Okay.

**Monali Mavani** [01:53:56]: will also give you the token ID because they are fixed, right? So say for example, word fox. It could be in that list of token IDs, it could be 50th word. That will be same. During inferencing, it will help us to pick up.

**POWAR SAGAR GANPATI** [01:54:14]: Yeah.

**Monali Mavani** [01:54:15]: OK, now I have showed you over here during inferencing. I have my input prompt, I'm generating tokens,

**POWAR SAGAR GANPATI** [01:54:19]: Mm.

**Monali Mavani** [01:54:21]: and then I have to get this token IDs from where it is coming. It is coming from the token IDs which are generated.

**POWAR SAGAR GANPATI** [01:54:29]: Hmm.

**Monali Mavani** [01:54:29]: And then embeddings are created by the embedding layer. So BP will give us only this part. It will tokenize.

**POWAR SAGAR GANPATI** [01:54:38]: Right, and and so same token and.

**Monali Mavani** [01:54:39]: Mm. One minute, that again, that again varies, okay? So when you use the open model and use Hugging Face,

## Segment 072  [01:54:45 - 01:55:13]
Slide: slides/slide_072.jpg

**Monali Mavani** [01:54:47]: it will give you tokenization. When you use open ID, then there is no tokenization, you directly get the embedding. So when you look at the implementation, it varies, okay, how your library is using BP and then wrapping around some code around BP and

**POWAR SAGAR GANPATI** [01:54:57]: Okay.

**Monali Mavani** [01:55:01]: what it is giving you as an output. OK, those two are different things.

**POWAR SAGAR GANPATI** [01:55:07]: Okay, okay. So if we are using DP as a tokenizer,

**Monali Mavani** [01:55:08]: Yeah.

**POWAR SAGAR GANPATI** [01:55:10]: then while retrieving the token embedding, right?

**Monali Mavani** [01:55:12]: Mm.

## Segment 073  [01:55:13 - 01:55:57]
Slide: slides/slide_073.jpg

**POWAR SAGAR GANPATI** [01:55:14]: So the same token should have been there, right? Used as during the training also to create the token embeddings for those words.

**Monali Mavani** [01:55:26]: Yeah, yeah, that's why otherwise it will be it will have unknown.

**POWAR SAGAR GANPATI** [01:55:29]: Yeah, it will.

**Monali Mavani** [01:55:31]: It will generate unknown token.

**POWAR SAGAR GANPATI** [01:55:33]: Yes.

**Monali Mavani** [01:55:34]: If some rare token which is not part of the vocabulary, there are always such this kind of token, unknown token, or out of vocabulary token that will be generated. That will still be generated.

**POWAR SAGAR GANPATI** [01:55:47]: Okay.

**Monali Mavani** [01:55:47]: Yeah. Yeah.

**POWAR SAGAR GANPATI** [01:55:48]: OK, thank you.

**Monali Mavani** [01:55:57]: Yes, anything else you want to ask?

## Segment 074  [01:55:57 - 01:59:03]
Slide: slides/slide_074.jpg

**RAJ KUMAR SHARMA** [01:56:00]: Yeah, ma'am, related to word to subwords, how we decide, like,

**VIKASH GAURAV** [01:56:01]: Ohh.

**RAJ KUMAR SHARMA** [01:56:04]: whether words should be split into two subwords or three subwords, for example,

**Monali Mavani** [01:56:09]: That is what is a BP algorithm. That is a BP algorithm.

**RAJ KUMAR SHARMA** [01:56:09]: and have.

**Monali Mavani** [01:56:12]: What I just explained, no? That BP algorithm does the same job. You don't decide.

**RAJ KUMAR SHARMA** [01:56:18]: Okay, no, thank you.

**Monali Mavani** [01:56:19]: Different algorithm does in a different way. BP does it in this way. I mean, there are many algorithms, we can't cover all the algorithms. So BP, which is a popular, that's what I've explained.

**RAJ KUMAR SHARMA** [01:56:29]: Okay, thank you.

**Monali Mavani** [01:56:29]: Mhm. Yes.

**AJAY KUMAR PRASAD** [01:56:37]: Ma'am, every LLM use the same corpus for the training. Yeah, it will be different.

**Monali Mavani** [01:56:41]: No, no, different, different, different. Every Llms has got different.

**AJAY KUMAR PRASAD** [01:56:45]: So, how the output for the suppose we are searching something, then how the output will be almost same for this every LLM?

**Monali Mavani** [01:56:53]: Because you are asking the same input, right? English text. A lot of things are same, but you try asking a model which is not trained on Hindi language, will you give the same output? No, because you are asking very common things and now all Llms are trained on almost

**AJAY KUMAR PRASAD** [01:57:06]: Okay.

**Monali Mavani** [01:57:09]: same things. A lot of corpus are same, but that doesn't mean everything is same. We'll talk about more later. Yeah.

**AJAY KUMAR PRASAD** [01:57:19]: And one thing also, suppose all this LLM are trained on the

**Monali Mavani** [01:57:20]: Go! Hmm.

**AJAY KUMAR PRASAD** [01:57:23]: different, different corpus. If corpus is already embedding vector

**Monali Mavani** [01:57:26]: Mm.

**AJAY KUMAR PRASAD** [01:57:27]: code, so they are using the same MAB they are generating for their own.

**Monali Mavani** [01:57:33]: No, they have the trainings are different, right? Embedding are generated after the training.

**AJAY KUMAR PRASAD** [01:57:38]: Okay, if corpus is already trained, corpus, sorry, trained, yeah.

**Monali Mavani** [01:57:39]: Yeah. Model is trained. Corpus is never trained. Model is trained.

**AJAY KUMAR PRASAD** [01:57:48]: Okay.

**Monali Mavani** [01:57:48]: Yeah. So you see, if you are, I don't know if you're using some application, we have OpenAI Embedding, so they give it free. It is already trained on their model. You can use those embeddings even for your application. So that depends. Embeddings are created while training the model, not training the tokenizer. Tokenizer will only give the tokenized

**AJAY KUMAR PRASAD** [01:58:06]: Thank you.

**Monali Mavani** [01:58:09]: vocabulary with token IDs.

**AJAY KUMAR PRASAD** [01:58:13]: OK, OK. Thank you, ma'am.

**Monali Mavani** [01:58:15]: Mm.

**SHELAR SACHIN KRISHNA** [01:58:18]: Yeah, ma'am, I will, I will go next. So, ma'am, we just on our earlier discussion,

**Monali Mavani** [01:58:20]: Yeah.

**SHELAR SACHIN KRISHNA** [01:58:23]: right, where you were writing that diagram, the tokenization, right? So, BPs, can we say that BP will extend tokens tokens further? So, maybe it is just to add more tokens to get a more fine-grained output, rather than like earlier, if you just token, then it will get like it will not. consider those combinations. Now BP is kind of adding more tokens on the
same words or whatever character, right? It will just add those combinations just to get more results, more accurate result. Is that the right understanding? Like the number of...

**Monali Mavani** [01:58:53]: Re. Yeah, yeah, so you can say that in a common layman's language, yes, but how do you say BP is a subword based tokenization and why we are doing subword? That means we are not considering word

## Segment 075  [01:59:03 - 01:59:49]
Slide: slides/slide_075.jpg

**Monali Mavani** [01:59:07]: together, but some frequently occurring combination of characters which are called subwords and. Why I explained, right? Those rare combination of words also,

**NEHA DEB** [01:59:16]: Okay.

**Monali Mavani** [01:59:18]: we don't need to create their own tokens. Like even apologetic, apologise, apology, all of this have the same semantic meaning. So that is the reason to suffer based then. But yeah, what you said in a common layman's language is correct. But try to understand from the technical point of view. So that you will be able to answer like whenever required, no, in a
technical way.

**SHELAR SACHIN KRISHNA** [01:59:41]: Right.

**Monali Mavani** [01:59:46]: Yes, next, please.

**DEVASHISH VERMA** [01:59:49]: I have a question. So this embedding layer that you're

## Segment 076  [01:59:49 - 02:06:57]
Slide: slides/slide_076.jpg

**Monali Mavani** [01:59:51]: Mm.

**DEVASHISH VERMA** [01:59:52]: saying, it gets trained while training the large language model itself, rather than using a static pre-existing

**Monali Mavani** [01:59:58]: Yes.

**DEVASHISH VERMA** [01:59:59]: embedding like word to work or anything, right?

**Monali Mavani** [02:00:01]: No, no, no, nobody uses what to back now.

**DEVASHISH VERMA** [02:00:04]: OK, so.

**Monali Mavani** [02:00:05]: Yeah.

**DEVASHISH VERMA** [02:00:07]: So the open AI embeddings that you're talking about, those embeddings basically are trained on the entire internet corpus on which other

**Monali Mavani** [02:00:10]: Hmm.

**DEVASHISH VERMA** [02:00:14]: like open AI models are trained on. Is that correct?

**Monali Mavani** [02:00:15]: Yeah, yeah, I think, I think yes, yes. So what is their corpus that we have to cheque on their open embeddings? So maybe have they considered English language only? Have they considered Thai, Malaysia or Hindi, Maruti that we have to cheque. Okay, but generally we deal with the text,

**DEVASHISH VERMA** [02:00:31]: Ohh.

**Monali Mavani** [02:00:34]: right? English text, so. like that. So any, like where we have Germany embeddings,

**DEVASHISH VERMA** [02:00:36]: Okay, cool.

**Monali Mavani** [02:00:39]: we have different embeddings available. And open source model will have their own embedding. That time, like when we do tokenization automatically, our libraries create those embeddings. Okay, so when you will see in webinar one, will be more clear that flow. But I use the example of open AI embedding because It is made publicly available. Those open AI models are not
available, but you can use open AI embeddings.

**DEVASHISH VERMA** [02:01:02]: Got it. So the learning.

**Monali Mavani** [02:01:03]: Because they have used, sorry, one minute, one minute. They have trained their model and then while training the model, they created those embedding and then published it. I can say like that.

**DEVASHISH VERMA** [02:01:13]: I mean, it is not using skip gramme or continuous

**Monali Mavani** [02:01:14]: Hmm.

**DEVASHISH VERMA** [02:01:16]: bag of words for training, right? In this case,

**Monali Mavani** [02:01:16]: Hmm.

**DEVASHISH VERMA** [02:01:18]: it's something else altogether.

**Monali Mavani** [02:01:19]: I don't see, I've not, they have not, I think they have not published the way they just trained, but it is a contextual embedding, you can think about it. See, skip ground and those are static algorithms. Okay, and bot based algorithm, encoder based algorithms are contextual

**DEVASHISH VERMA** [02:01:33]: Mm.

**Monali Mavani** [02:01:37]: embeddings. They create, but while we create, while we train the decoding, we also can capture that context by training the decoder. Now, this OpenAI embeddings could be encoder only embedding, or like you don't want to use OpenAI embeddings, but you can use only decoder model directly. They have already trained, they are already trained models, so that Embedding
layer is also up to date. You can think about that.

**DEVASHISH VERMA** [02:02:05]: So there are two types of embeddings here. There's the embedding layer itself, and then there's the output embeddings that I get after the transformer layers.

**Monali Mavani** [02:02:10]: No.

**DEVASHISH VERMA** [02:02:14]: So what we get after that?

**Monali Mavani** [02:02:14]: I have to talk about it. I have to talk about it. That's what the remaining slide it is consist of. Yeah.

**DEVASHISH VERMA** [02:02:21]: OK, so when you're seeing open AI gives you

**Monali Mavani** [02:02:21]: So we'll talk about that.

**DEVASHISH VERMA** [02:02:23]: the embeddings, it's the final output right after all the transform layers, not the embedding layer.

**Monali Mavani** [02:02:27]: I mean, no, no, open AI, what, no, no, no, what, what open I will give you, because when you develop an application, OK, using any models you can use, you can convert into embeddings. Like, you are using open AI only, right? You are using open AI model, but then your input has to be converted into embedding, so you can use open AI embeddings. That's why, that's why
they have no publisher. You train the model is there, but when you use the model, you have to follow the same input pre-processing, what you do during the training. That means you have to convert your text into tokens, and then tokens into token embeddings. So with OpenAI, directly you get, you give a text, and then intermediate steps are cut down. That's what I meant by, you know,

**DEVASHISH VERMA** [02:03:08]: Okay.

**Monali Mavani** [02:03:09]: those open AI embeddings.

**HARMANPREET SINGH** [02:03:11]: Yeah, anyways, Madam, just to sorry guys, just to come in between. The thing is,

**Monali Mavani** [02:03:12]: Yeah. Oh.

**HARMANPREET SINGH** [02:03:16]: if we are using an API format of the Embedding model, right?

**Monali Mavani** [02:03:19]: Huh.

**HARMANPREET SINGH** [02:03:21]: Or we are using API for open AI, right? Say GPT 5, right?

**Monali Mavani** [02:03:22]: Mm. Mhm.

**HARMANPREET SINGH** [02:03:25]: So we have built an application using GPT 5, right? And.

**Monali Mavani** [02:03:25]: Mm.

**HARMANPREET SINGH** [02:03:29]: When actually we are sending the text, though, the API will do all this to organisation for the input text which is given. It will convert it into embedding, right? So that's why we don't see the clear

**Monali Mavani** [02:03:37]: Yeah, yeah. Yes, yes, yes, yes, yes, yes. But here in this course,

**HARMANPREET SINGH** [02:03:40]: picture. Correct, right? Exactly. Okay.

**Monali Mavani** [02:03:43]: we'll not be using open AI models. We are going to use the open source

**HARMANPREET SINGH** [02:03:45]: Mm.

**Monali Mavani** [02:03:47]: models where you'll be doing everything from scratch.

**HARMANPREET SINGH** [02:03:50]: Yes, that makes sense.

**Monali Mavani** [02:03:50]: We will not do training from the scratch, which we can't do. So,

**HARMANPREET SINGH** [02:03:54]: MMM.

**Monali Mavani** [02:03:54]: but you can see all of this, you know, in steps. And we will be your assignment, one assignment will be on continuous pre-training, which you can do. Take the open weights available, like from Lama model, and then you can from continue, you can continue the training based on that. We can't do it from a pre-train.

**HARMANPREET SINGH** [02:04:12]: Sure.

**Monali Mavani** [02:04:14]: Yes, that's what you will see this close.

**HARMANPREET SINGH** [02:04:14]: Yeah, sure. Thank you so much. Yeah.

**Monali Mavani** [02:04:16]: Discourse.

**HARMANPREET SINGH** [02:04:18]: Yeah, thanks, guys. Please, thanks.

**Monali Mavani** [02:04:21]: Okay.

**GHANSHYAM DESAI** [02:04:25]: Hello.

**Monali Mavani** [02:04:25]: I think, yeah, tell me. Hi.

**VIKASH GAURAV** [02:04:25]: Yeah, fine.

**GHANSHYAM DESAI** [02:04:28]: Yeah, ma'am, so for building the walkability of the organiser using that, we have this token ID to token embeddings, right, ma'am? So for that word bank, can I say that the token embedding will

**Monali Mavani** [02:04:37]: Mm.

**GHANSHYAM DESAI** [02:04:42]: always remain the same, but only the contextual embedding will differ?

**Monali Mavani** [02:04:49]: No, no, you are mixing so many concepts together here. Okay. What is Word Bank?

**GHANSHYAM DESAI** [02:04:53]: Okay.

**Monali Mavani** [02:04:55]: First, I don't know why you use the word word

**GHANSHYAM DESAI** [02:04:57]: The Entire.

**Monali Mavani** [02:04:58]: bank.

**GHANSHYAM DESAI** [02:04:59]: No, word bank, we like the word actual, like the word means bank is a bank,

**Monali Mavani** [02:05:01]: Vocabulary.

**GHANSHYAM DESAI** [02:05:04]: a river, a bank, financial, so in that case, yeah, man.

**Monali Mavani** [02:05:05]: Ah, okay, okay, that, that.

**GHANSHYAM DESAI** [02:05:10]: So.

**Monali Mavani** [02:05:10]: So this embeddings have already captured those meanings. We can say that. Now every models, how they have trained, we don't know. Okay, even the open models, they are not always released their details. But you assume when we use it,

**GHANSHYAM DESAI** [02:05:24]: Thank you.

**Monali Mavani** [02:05:26]: we are getting good results. That's where you have to assume. But theoretically, you will get contextual embedding when you use encoder based models. Decoder models can capture the context while training itself. But there are some limitations that probably will talk. I mean, if you know the decoder architecture and masking or the causal masking, you will understand
the decoder only model while training cannot look in future, but the encoder only models can look into

**GHANSHYAM DESAI** [02:05:53]: Yes, Steve.

**Monali Mavani** [02:05:55]: the future. Hence, encoder only models gives very rich

**GHANSHYAM DESAI** [02:05:56]: Yes.

**Monali Mavani** [02:05:59]: contextual embeddings. Decoder only models can give, but they are, so all these models, how do they create their embedding? I assume it is based on their decoder-based embedding only. They give us the embedding. But I also have not gone through that detail of every models. First of all,

**GHANSHYAM DESAI** [02:06:12]: OK.

**Monali Mavani** [02:06:16]: they should have published, you know, those details. For us,

**GHANSHYAM DESAI** [02:06:16]: Mhm. Yeah.

**Monali Mavani** [02:06:20]: you can assume that they are embedding and we libraries give us the embeddings. But I just explained theoretically, this is what happens. If you want to create anything from scratch, you don't know how to use Lama,

**GHANSHYAM DESAI** [02:06:28]: Okay.

**Monali Mavani** [02:06:32]: Quen or anybody, any open model.

**GHANSHYAM DESAI** [02:06:34]: Okay. Yeah, yeah, got it, ma'am. So just one more question on the

**Monali Mavani** [02:06:34]: Okay, yeah. Of.

**GHANSHYAM DESAI** [02:06:38]: misspelling we saw about that learn example over there where we are like

**Monali Mavani** [02:06:39]: Ohh.

**GHANSHYAM DESAI** [02:06:43]: dividing into tokens means we are like doing supportwilpbits and then this will

**Monali Mavani** [02:06:45]: Yeah.

**GHANSHYAM DESAI** [02:06:47]: be again a part of the vocabulary. If this goes, that wrong word goes to the part of the vocabulary, how actually it will actually correct it and then understand the real world.

**Monali Mavani** [02:06:54]: Huh. Hey, no, no, nothing is wrong, nothing vocabulary is vocabulary, right?

## Segment 077  [02:06:57 - 02:08:25]
Slide: slides/slide_077.jpg

**Monali Mavani** [02:07:02]: It's a static vocabulary created. If that tasty become part of a vocabulary

**GHANSHYAM DESAI** [02:07:04]: Okay.

**Monali Mavani** [02:07:08]: and if your input anytime in the future that is coming, then it will understand,

**GHANSHYAM DESAI** [02:07:08]: Okay. Hmm.

**Monali Mavani** [02:07:14]: right? You don't have to think about that. Vocabulary is like, you know, created in advance.

**GHANSHYAM DESAI** [02:07:22]: Mhm. OK, so if vocabulary had contained some wrong word, then how it is interpreting the correct?

**Monali Mavani** [02:07:29]: I will not say, I will not say wrong word, OK? It is a subword structure is being followed. Simple. Tasty,

**GHANSHYAM DESAI** [02:07:33]: Miss, yeah.

**Monali Mavani** [02:07:37]: if there are four times A, will that get an individual token or not?

**GHANSHYAM DESAI** [02:07:40]: Hmm.

**Monali Mavani** [02:07:42]: Depends upon this four times occurrence of A has come in corpus or not.

**GHANSHYAM DESAI** [02:07:43]: Okay.

**Monali Mavani** [02:07:47]: That's all.

**GHANSHYAM DESAI** [02:07:50]: Okay.

**Monali Mavani** [02:07:50]: There is nothing right and wrong here. Right and wrong is for us when we look at altogether a text.

**GHANSHYAM DESAI** [02:07:56]: Okay, okay.

**Monali Mavani** [02:07:56]: But not the other way, OK?

**GHANSHYAM DESAI** [02:07:59]: Yeah, yeah, got it. Thanks, man.

**Monali Mavani** [02:08:00]: Yeah, see, I all upload all these contact session slides on Takshila. It is there here. Yeah, right. I've already uploaded this yesterday. That's what I told in the beginning. So next Friday also I'll upload session 2 slides, maybe earlier whenever I'll be ready with that. And what I do a lot of annotation, right, that I'll upload here. This is my annotated slides,
but in exam you won't get my annotated
