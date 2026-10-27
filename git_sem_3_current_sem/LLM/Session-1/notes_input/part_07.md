# Part 07  [01:37:37 - 01:53:01]

## Segment 060  [01:37:37 - 01:38:35]
Slide: slides/slide_060.jpg

**Monali Mavani** [01:37:39]: we can have sentence embeddings, we can have word embeddings, and we can have token embeddings. Token embeddings, they are used as in... As in the input. Do Llms. And there are different algorithms and different ways to create document embedding. For example, we have doc2vec algorithm. Then we have a sentence embedding. There's something called a sentence transformer.
Which he used to create all of this. Now, somebody asks this question: this token IDs are not positional embedding in a very naive format of position embedding that you have learnt. We can give a simple position embedding. Token Embedding, we add a position embedding, and then input embedding gets created. Over a time, there is a evaluation on this algorithm.

## Segment 061  [01:38:35 - 01:41:35]
Slide: slides/slide_061.jpg

**Monali Mavani** [01:38:37]: Like original transformer, use the sinusoidal encoding, not just like index. If you use an index, then definitely we can use token IDs as the position embedding. Oh, no, no, we cannot still use token IDs as a position embedding. See. Token ID. And this is a vocabulary, zero, some word one in my vocabulary, one, one word in another character in vocabulary, and so on.
This is fixed. Now, order of this tokens coming and my input is different, and position represents that order. So, in any case, we cannot use token ID as my positional Embedding. Anyways, we just cannot use my index, for example. This is my input. Sentence. Going to Llms. For inference. Okay, I'm using an Llms for some task. So, this is a position one, this is a position two, three, 4, 5, and so
on. In a very naive, classical, theoretical format, you can use this position as embedding. It has got its own disadvantage. So, original transformer used sinusoidal encoding. You must have learned in Dnn, which used fixed sine cosine functions, then came GPT-2 and BERT; they changed, they learned this, they use positional embedding also as a learned vector, so create embedding vector. Sorry,
position Embedding Vector. Size is equal to, sorry, size of position Embedding Vector equal to. Size of. Token Embedding Vector. That's what GPT-2 and BERT did. So they created this position embedding vector randomly. And during the training, along with the token embedding, the position embedding were also learned. But now that is also not in use. What is used currently today is a rotary position
embedding rope And that's what we will learn in third module in detail. They will not learn all these things because they are not in use currently. And you might have learned sinusoidal encoding in the original transformer. So no need for any repetition. ROPE is a very mathematics intensive algorithm. I have tried to simplify it as much as possible. But we will learn in third module about rope. So
that's all about position embedding. The next important is language modelling head. You want me to continue or you want me to stop and enable the mic?

## Segment 062  [01:41:35 - 01:43:11]
Slide: slides/slide_062.jpg

**Monali Mavani** [01:41:37]: No, no, no, no, no. These are token embedding plus word embedding. It is token embedding plus positional embedding. What is word embedding? There is nothing called word embedding. Enough for today, all of you agree you want me to stop? Then I can enable the mic and you want to ask me anything we can ask. Oh, yes for what? Yes for what? Stop. I mean, you have to tell
me yes for what? You want me to stop, right? Huh? Okay, let me enable the mic now. Controls. Yeah, unmute themselves. I did that. Are you able to unmute? Hi, yes, you should be able to.

**VIKASH GAURAV** [01:42:37]: Okay. Yeah, good morning, ma'am. I have one question related to the vocab

**Monali Mavani** [01:42:40]: Yes. Oh.

**VIKASH GAURAV** [01:42:43]: building. So we have a lot of data in the corpus. So to create the vocab, it will process all the corpus before they start the training.

**Monali Mavani** [01:42:54]: Vocab training, right?

**VIKASH GAURAV** [01:42:54]: To build a water, yes.

**Monali Mavani** [01:42:57]: Yes, yes, it will.

**VIKASH GAURAV** [01:43:00]: Okay, then it will start training the purpose.

**Monali Mavani** [01:43:03]: Yes, yes, yes, correct.

**VIVEK RANJAN UPADHYAY** [01:43:04]: Model training itself means means I'm just wanted to means model training also

**VIKASH GAURAV** [01:43:04]: Okay.

**Monali Mavani** [01:43:07]: God! Ha.

## Segment 063  [01:43:11 - 01:43:45]
Slide: slides/slide_063.jpg

**VIVEK RANJAN UPADHYAY** [01:43:12]: will start after the corpus work app creation. OK.

**Monali Mavani** [01:43:15]: Yes, yes, yes, it has to like that. It has to be like that.

**VIVEK RANJAN UPADHYAY** [01:43:18]: Yeah.

**Monali Mavani** [01:43:19]: So every model builder first trains their tokenizer and then based on tokenizer,

**VIVEK RANJAN UPADHYAY** [01:43:19]: Thur.

**Monali Mavani** [01:43:24]: they train their model.

**HARMANPREET SINGH** [01:43:28]: Madam, just, just to...

**Monali Mavani** [01:43:28]: That's all part of pre-processing. Yeah.

**HARMANPREET SINGH** [01:43:30]: Sorry, Sagar, I'll take a minute. Thanks. Ma'am, just to continue the question which my, you know, friend has asked. The thing is, when we look at the BPE encoding, right, if we can go to that slide, please, because these questions are related. So, yeah, the other one where you took, yes,

## Segment 064  [01:43:45 - 01:44:27]
Slide: slides/slide_064.jpg

**HARMANPREET SINGH** [01:43:47]: exactly. So, here, when we look at... The current vocab, right? There is B, G, H, N, P, S, U, G, U, N. These 7 to 8 or 9 characters or words doesn't make any sense in the vocabulary. So after the current vocabulary is created or generalised, would there be any step like limitization? to philtre out.

**Monali Mavani** [01:44:11]: Non. No, no. Okay, it makes a sense. When will it make a sense? I tell you. Let's take this tasty example where I've given a starting in the beginning.

**HARMANPREET SINGH** [01:44:22]: Yeah.

**Monali Mavani** [01:44:24]: One minute, it will make a sense, right?

## Segment 065  [01:44:27 - 01:46:01]
Slide: slides/slide_065.jpg

**Monali Mavani** [01:44:28]: Here. Maybe in your corpus, this many times A has not come. Only A has appeared maybe at most two times. So what will you get? You know, T as one token, A is another token, A is another token. Then probably AS is part of your vocabulary or T is TY is part of vocabulary. So this rare word. Will get this many. You can combine right? You can understand tasty. It will get
one, two, three, 4, 5 tokens. The rare word will be represented as five tokens, but rare word will not be part of your vocabulary. Because, in vocabulary, this has been built like this. And that time it will have all your characters will have a meaning. Suppose you don't have any multiple times A appearing, then when you will tokenize this word, it will be tokenized like T, then A,

**HARMANPREET SINGH** [01:45:28]: Mhm.

**Monali Mavani** [01:45:32]: then A, then A, how many times? We have got five times, right? A and A,

**HARMANPREET SINGH** [01:45:37]: Yes.

**Monali Mavani** [01:45:37]: and then probably STY is, you know, character combination might have come in your Corpus, so during inference, when you will tokenize this tasty, it will be tokenized like this. This is where you are, when you are telling, no, all of these characters will not have a meaning. It will have the meaning.

**HARMANPREET SINGH** [01:45:56]: Yeah.

**Monali Mavani** [01:45:57]: It will have the meaning. It will have its use.

**HARMANPREET SINGH** [01:45:59]: So in that case, you know, okay, in rarest of words, probably, you know,

## Segment 066  [01:46:01 - 01:46:43]
Slide: slides/slide_066.jpg

**HARMANPREET SINGH** [01:46:04]: this context or this makes sense when we are actually using, when we are actually studying or doing social media parsing, right, input parsing, you know, there's a lot of content similar to that.

**Monali Mavani** [01:46:14]: Yes, yes, yes, yes, you are correct. Yes, you are very correct. That's the reason, you know,

**HARMANPREET SINGH** [01:46:19]: Okay, okay, okay.

**Monali Mavani** [01:46:22]: nowadays you write anything, you just see, we write, we write so fast in cloud or charge, we misspell, we, but still it understands,

**HARMANPREET SINGH** [01:46:29]: Yeah. Yes, yes.

**Monali Mavani** [01:46:32]: right? Because one of the criteria is this tokenization process.

**HARMANPREET SINGH** [01:46:38]: And. Okay, thank you. Yeah.

**Monali Mavani** [01:46:39]: Obviously, there are other things also, not only just tokenization, yeah.

**HARMANPREET SINGH** [01:46:42]: I mean, so I had earlier question actually,

## Segment 067  [01:46:43 - 01:48:25]
Slide: slides/slide_067.jpg

**Monali Mavani** [01:46:44]: Ha ha ha.

**HARMANPREET SINGH** [01:46:45]: so one of the one of the question is that, you know, we already discussed social media, text in inferencing could be one of the

**Monali Mavani** [01:46:50]: No.

**HARMANPREET SINGH** [01:46:53]: applications where is bite level or you know,

**Monali Mavani** [01:46:53]: Yes.

**HARMANPREET SINGH** [01:46:55]: a character level even could be useful. Could you could you give any other example where it could be effective?

**Monali Mavani** [01:47:02]: No, no, see, you don't train your tokenizer when you're developing application, okay? When you develop an application, you use the LLM. And currently LLM, they know their Llms are going to be used

**HARMANPREET SINGH** [01:47:12]: Yes.

**Monali Mavani** [01:47:15]: in all of this application. So they, while training, they take care of all those things. Right from designing the tokenizer.

**HARMANPREET SINGH** [01:47:24]: Oh, okay, so it's universal.

**Monali Mavani** [01:47:25]: As an application designer, you don't have to do all these things. Yeah, yeah. I mean, that is the worry for the LLM. If Llms, they, you know, use such tokenizer, which, you know, like somebody's going to use that LLM in social media application, it's not going to be useful. You as an application designer will not

**HARMANPREET SINGH** [01:47:41]: Good evening.

**Monali Mavani** [01:47:43]: be worried about this thing. But this is if you're going to train your own tokenizer, you're going to train your own model. That's what I'm discussing over here.

**HARMANPREET SINGH** [01:47:53]: Okay, okay, makes sense. Thank you. Thanks, Anurag.

**Monali Mavani** [01:47:53]: Yeah. Yes, others.

**POWAR SAGAR GANPATI** [01:48:01]: Yeah, yes, madam. Yeah, so madam, I have a question regarding, see, finally, we use token IDs to retrieve the word embedding right for that words and word

**Monali Mavani** [01:48:13]: Yes.

**POWAR SAGAR GANPATI** [01:48:13]: embedding that is meaning vector plus the positional encoding vector, we pass it as input to the. Llms, right?

**Monali Mavani** [01:48:24]: Let me just write it here to be clear. You have tokens, okay?

## Segment 068  [01:48:25 - 01:49:53]
Slide: slides/slide_068.jpg

**POWAR SAGAR GANPATI** [01:48:29]: So, so I'm just, yeah, summarising process, yeah.

**Monali Mavani** [01:48:30]: One minute. Let me complete. That's what I'm summarising it for you. I have tokens which gets converted into token IDs. OK,

**POWAR SAGAR GANPATI** [01:48:37]: Mhm.

**Monali Mavani** [01:48:40]: so I have a token IDs respective. Then for each token IDs, we have the embeddings.

**POWAR SAGAR GANPATI** [01:48:47]: Right.

**Monali Mavani** [01:48:49]: Because embedding are not just a number, correct? They are the vectors, yeah.

**POWAR SAGAR GANPATI** [01:48:51]: Right. So, Embedding, yeah, for all vocabulary words, right, the and the timings.

**Monali Mavani** [01:48:58]: No, no token IDs. So now I have my vocabulary. I have a diagram for that also here. One minute, I'll show you the diagram where it is gone. This is, yeah,

**POWAR SAGAR GANPATI** [01:49:12]: That, yeah, last Exam.

**Monali Mavani** [01:49:13]: this is my token vocabulary. I have 50, 000 tokens. in my vocabulary, then I'll have my token IDs 0 to 50,000, I mean 1 to 50,000, say for example. Okay, now embeddings when, okay, here even it is shown that 50, 000 embedding, but what actually happens when you embeddings are not created in advance and they are stored, okay, I think probably I should say. This diagram
I've taken from a book, JLMR, but it's a little bit misleading diagram. I think that's where the confusion is coming. I was showing you this, right? Ha. This is my...

## Segment 069  [01:49:53 - 01:53:01]
Slide: slides/slide_069.jpg

**POWAR SAGAR GANPATI** [01:49:54]: Dip.

**Monali Mavani** [01:49:56]: When I'm processing the input. Okay, otherwise you understand when I'm performing. Llms inferencing my input prompt. gets tokenized, token IDs gets generated, and for each token, embeddings are generated. Now this where from where this token IDs are coming, I'll have 7, 8, 123 and 94 from where this token IDs are coming. You have your vocabulary built, you have
trained your tokenizer, where you have your token IDs for, say example, 50, 000 words in your vocabulary. So this is where you have to understand the token IDs gets assigned to every word in your vocabulary when you are building a vocabulary while you are training a tokenizer. That's all. When you use the model, it comes,

**BOLLIGORLA SHEKAR** [01:50:53]: Search.

**Monali Mavani** [01:50:55]: you have to use the same tokenizer with which model is trained on. So your input prompt gets tokenized, token IDs gets generated, and this tokenized IDs will come from here, which you have already built. And then embeddings gets generated by the Embedding layer.

**POWAR SAGAR GANPATI** [01:51:14]: Embedding will be generated or it will be added in our one screen now.

**BOLLIGORLA SHEKAR** [01:51:18]: This is, yeah, this token is randomly generated,

**Monali Mavani** [01:51:19]: These are token one minute, they are token embeddings.

**BOLLIGORLA SHEKAR** [01:51:22]: say randomly, this token is randomly generated, right,

**POWAR SAGAR GANPATI** [01:51:25]: But, but...

**Monali Mavani** [01:51:26]: No.

**BOLLIGORLA SHEKAR** [01:51:27]: index based.

**POWAR SAGAR GANPATI** [01:51:27]: No, no, it is, it is one time, yeah, it is one time assigned right when the

**Monali Mavani** [01:51:28]: Not that.

**POWAR SAGAR GANPATI** [01:51:32]: when the tokenizer is trained, it is assigned one time, right? So...

**Monali Mavani** [01:51:34]: Yes, yes, it is there. It has got every token has got its own position here in the vocabulary.

**POWAR SAGAR GANPATI** [01:51:41]: So, Adam, question is not with the token IDs.

**Monali Mavani** [01:51:41]: Mm.

**POWAR SAGAR GANPATI** [01:51:43]: We are clear on that. The question is this word embeddings,

**Monali Mavani** [01:51:43]: Ha. Mm.

**POWAR SAGAR GANPATI** [01:51:46]: right? Those will also created for this.

**Monali Mavani** [01:51:47]: Token embedding, don't use one minute, one minute, one minute, do not use a word embedding, use a word token embeddings.

**POWAR SAGAR GANPATI** [01:51:53]: OK, token embeddings. OK, then these token embeddings, like it has,

**Monali Mavani** [01:51:55]: Hmm.

**POWAR SAGAR GANPATI** [01:51:58]: let's say, 10 dimensions for each token. OK, let's say whether it is animal,

**Monali Mavani** [01:51:59]: Mm. Hmm.

**POWAR SAGAR GANPATI** [01:52:04]: whether it is a noun, whether it is verb. OK,

**Monali Mavani** [01:52:07]: Mm.

**POWAR SAGAR GANPATI** [01:52:07]: so all the let's say in vocabulary I have 50 words, then 50 cross 10.

**Monali Mavani** [01:52:11]: Hmm.

**POWAR SAGAR GANPATI** [01:52:12]: So this matrix is already there. It is already created. We have to just retrieve this token embedding, you know, using the token IDs.

**Monali Mavani** [01:52:16]: It's not there. Ha, ha, that's what you are telling during training. Yes, but it is during the inferencing. This is what token embedding only for the. the words which you have in your input only gets processed by the transformer.

**POWAR SAGAR GANPATI** [01:52:37]: Yes, yeah, so, so token embeddings are already created

**Monali Mavani** [01:52:37]: Okay. Ohh.

**POWAR SAGAR GANPATI** [01:52:41]: one step, okay, already before, yeah, so I'm not talking, yeah, during training,

**Monali Mavani** [01:52:45]: During training.

**POWAR SAGAR GANPATI** [01:52:47]: yeah, now while inferencing whatever sentence I

**Monali Mavani** [01:52:48]: Yes.

**POWAR SAGAR GANPATI** [01:52:50]: put as a prompt, the tokens are generated, I got the token IDs from this token IDs,

**Monali Mavani** [01:52:51]: Yeah. Mmh. Mm.

**POWAR SAGAR GANPATI** [01:52:57]: we... Got the token embeddings for this my sentence, right?

**Monali Mavani** [01:52:58]: Mm. Yes, yes, yes.
