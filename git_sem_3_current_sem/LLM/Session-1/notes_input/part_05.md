# Part 05  [01:05:43 - 01:21:17]

## Segment 036  [01:05:43 - 01:07:05]
Slide: slides/slide_036.jpg

**Monali Mavani** [01:05:48]: So, this M is not even in the vocabulary. You can see my character BGHNPSU. M is not in the vocabulary. Even my word mug is also not in the vocabulary. So, in that case, a known word will get. A Non token will be assigned to this word. But that does not happen because here the example is very small corpus and just 10 token vocabulary. This byte pair encoding solve
most of the out of vocabulary issues. But still, there are some tokens, they are still out of vocabulary. Like, you know, if we talk about the new languages, so the new domains, they may not be a perfect part of the English corpus. In that case, we have alternative, and a lot of today's models they are going towards byte-level BPE. I'll explain that before that. Let me take any questions if you
have for BPE. Hmm. UN is less than UG count. It is there in vocabulary. Oh,

## Segment 037  [01:07:05 - 01:08:07]
Slide: slides/slide_037.jpg

**Monali Mavani** [01:07:07]: you're building the vocabulary, right? You will start building and you will, we will keep some rule, say minimum frequency. I can only merge different characters together if say minimum frequency is 2 or 3 and so on. So it's not like always you have to pick up the, you will start merging the characters with a maximum frequency and then you will build your vocabulary,
but this is your hyper parameter. that I will need to merge 2 characters if those two characters are coming together in my corpus, minimum two times, minimum three times, minimum five times. That's how the actual vocabulary is built. So I think I have answered your question that UG and. Ah, PU can be added. This is just an example. OK, PU also can be added. PU is not added because you can see we
have to build on the previous iteration.

## Segment 038  [01:08:07 - 01:09:05]
Slide: slides/slide_038.jpg

**Monali Mavani** [01:08:14]: In the second iteration, do you have PU? Oh, I have a PU over here. Yes, yes, then it can be added. Here I have PU, it can be added. This is an example, but yes, when you will actually have the, to solve this problem, yes, you can add a PU also here. I can add PU also here. Because if I set my minimum frequency, As 5, that I can only add those combinations of
characters in my vocabulary. If minimum frequency is five, then my PU also can be part of my vocabulary, because PU's frequency is 12, which is greater than minimum frequency. Yes, you are correct to point out, but, as I said, this was just an example to tell you the mechanism. Hmm.

## Segment 039  [01:09:05 - 01:10:33]
Slide: slides/slide_039.jpg

**Monali Mavani** [01:09:07]: That is what the order of characters has to be maintained in. The way it is appearing in your corpus. See, it's UG, you can't have GU. GU, you can have it is if it is there in your corpus. If GU combination is not there in corpus, your algorithm will anyway not pick up it. Byte level, I'll talk about it. The name that given byte per encoding. Yeah. Okay, how do we
discard tokens that are not relevant based on the language? Those that don't have a meaning from the vocabulary is that a different process? No, there is no different process on that. Then you have to take care during the pre-processing and value create your corpus. Generally, nobody does it that way. It is just, you know, you're building a vocabulary. Ohh. Okay, so... Meaningful for example.
Okay, I don't have right now that full example, but it's there in the question paper. So I'll upload the question paper with the answer key and that there is a full example. I'll quickly go through so how we do BPE. You can pre-tokenize your corpus into the

## Segment 040  [01:10:33 - 01:11:17]
Slide: slides/slide_040.jpg

**Monali Mavani** [01:10:34]: words, then you will count the frequency of each words. That's how we have done here. Then you will start building your vocabulary. You will start with the characters, single characters, like here we have started with the single characters. Then you will set your hyper parameter called minimum frequency. Oh, I should have added in the slide. OK, maybe I'll modify this
slide later, so that every section will be benefited. This minimum frequency is a hyperparameter. You can set this say minimum frequency 5. Based on that, you will apply the merge rules starting with two character combination. So that's what we did here. We combine UG because the UG is coming

## Segment 041  [01:11:17 - 01:13:07]
Slide: slides/slide_041.jpg

**Monali Mavani** [01:11:22]: for 20 times. Then we combined what? UN here, we combine UN because it has come for 16 times, then you can we have combined PU because it has come 12 times, because I have set my hyper parameter minimum frequency is equal to five. Now, in this example, if we are omitting PU, then what should be the minimum frequency? Say... Fifteen. If my minimum frequency is 15, then
PU. Will not become. Part of... Vocabulary. So, that is the reason PU is not here. So that minimum frequency will decide whether any combination of characters are part of your vocabulary or not. Now we have completed all the two combination of two characters, then you can go with the third combination of three characters. But based on the previous iteration. So now previous iteration here. You can
see HUG. He is having the highest count combination of H, U, and G, which is 15, so your HUG has become the part of your vocabulary. And you will keep on continuing till you will build your desired number of tokens in your vocabulary. Your desired number of tokens is your hyper parameter that max. Vocab size. In tokens. Is your hyper parameter? OK, so that's a BP algorithm. But byte level BPE is a
subtype of BPE that uses bytes instead of characters as

## Segment 042  [01:13:07 - 01:13:55]
Slide: slides/slide_042.jpg

**Monali Mavani** [01:13:13]: a basic token component. So even if you know some of the characters are not part of your corpus and your application when you are deploying it, it is being used when you are using the Llms to search input. it can be taken care of. So many of the Llms today, many not like all, but they are using byte level BPE. So, vocabulary is not based on the characters, but based
on bytes. If you see in BPE, we started with the characters. And then we started merging characters. Here, what happens? Take a byte. Say, for example, U is a character, is being represented as a byte 117,

## Segment 043  [01:13:55 - 01:14:45]
Slide: slides/slide_043.jpg

**Monali Mavani** [01:14:00]: G is a character, is represented as a byte 103. If my merge rule says UG have to be merged together. But the bytes 117 and 103 will be merged together and ultimately I have to generate the token ID. So this is my merge rather than UG. This will be represented as UG and my token ID, the next available token ID will be given. So as you can see over here, all of this
ultimately have been have to be given as a token ID. So this is my, yeah. If I have this, where should I write one minute? UGHMP, I'm just writing randomly, UG hug, all of these tokens will get.

## Segment 044  [01:14:45 - 01:15:13]
Slide: slides/slide_044.jpg

**Monali Mavani** [01:14:54]: My token IDs. So that's byte level BPE. So any unseen characters. Will have its own place. So that's the byte level bdb. What is the good part about BPE? Rare words can be easily handled because

## Segment 045  [01:15:13 - 01:15:49]
Slide: slides/slide_045.jpg

**Monali Mavani** [01:15:17]: we are dividing rare words into all the words into subword units. It helps to reduce the vocab size. The same word having a different form, a different lemma, will still have the... We don't have to create a separate vocabulary for that, like I gave the example here. Where was this example given here? Yeah. Yeah, apology, apologise, and apologist will not have a three

## Segment 046  [01:15:49 - 01:16:27]
Slide: slides/slide_046.jpg

**Monali Mavani** [01:15:50]: different entries in your vocabulary, but it will be divided into subword apolog. You can have a POLOG as one subword, maybe Y is another subword, IZE is another subword, IST is another subword. This is just I am giving you from the heuristics, but ultimately depends upon your training corpus. So, apologise, modernise, all of this will not have their own vocabulary.
So that's the advantage. Then in the kind of limitation,

## Segment 047  [01:16:27 - 01:17:19]
Slide: slides/slide_047.jpg

**Monali Mavani** [01:16:28]: like some of the languages nowadays, we have LLM train on many languages. We get a fragmented tokens because they are simple, frequency-based rules are applied. There are no linguistic rules are followed. Like every language, other languages other than English, they can have a very complex morphology. That means they can have very complex rules. How do we write the
different South Indian languages or French languages or things like that? And those models may not, BPs may not be suitable for that. And because it doesn't capture the semantic meaning. And there are no standard grammatical rules which are followed. But still, BPE is a very popular algorithm or some variance of BPE. How this algorithm is actually you can use when you build your own tokenizer,

## Segment 048  [01:17:19 - 01:18:29]
Slide: slides/slide_048.jpg

**Monali Mavani** [01:17:21]: you don't have to write any of such algorithm. We have our libraries framework available with us and they do this. So Sentence Piece is one of the open source library which uses BPE and Unigram language algorithm. You can choose between the algorithm. Again, Unigram is. Simple single grammes are used together, single N grammes are used together, 1 gramme are used
together. The only change over here is how the white space white spaces are handled. BP algorithm uses a pre-tokenized step where this is you have tokenization matters. You have to run a pre-tokenizer script, which will divide this into two different words, tokenization and metas. Sentence-based library handles this space as a leading underscore. So different library uses deals with a white space
in a different way. I've given you another example here in one minute in the slide. Yeah. In A byte level BP algorithm, which is used by latest GPT,

## Segment 049  [01:18:29 - 01:19:13]
Slide: slides/slide_049.jpg

**Monali Mavani** [01:18:34]: Lama and Quen Models, latest one, they use this leading space. How do they mark the leading space by this G test? This is a token which comes out, so all of this you will be able to see in webinar one. And you will see this output. So which tokenizer framework you should use? I'm talking about the library framework. Say your objective is train a new tokenizer or
extend the existing one. You can use the open source tokenizer available in Hugging Face library. Are you aware of what is Hugging Face?

## Segment 050  [01:19:13 - 01:21:17]
Slide: slides/slide_050.jpg

**Monali Mavani** [01:19:19]: Okay. Oh, no. Okay. Oh, let me ask that question. How some same sequence in BP get? Because that hug is probably part of a different corpus. You are dividing your corpus. OK, so you have a different documents and per document you are doing it, so it may have a different frequency count. Anyway, you will combine it together because either you do it together, hug all
combine together, or you do it later. B HARIPRIYA, that's what I've answered your question. 256, not 256 bytes, 0 to 255. No, we have unique name. BP doesn't use bytes, byte level BP use the bytes, and Unicode character limit is 0 to 255. Hence, we use 0 to 255. We just don't use 256 bytes. We have the all symbols characters. given an individual bite. That's what we use. Rare words, anywhere rare
words gets their subword parts. Tasty, it's a rare word. T so many times A, it's a rare word. So it will be using this BP algorithm, it will be divided into different subwords. And that's how rare words are handled. Okay, yeah, so hugging phase, I'll just quickly show you. We will be using this extensively, hugging face library. I'm showing you the tokenizer library here. Okay, and in webinar one
you will see, we will give you this demo. But before that, if you just want to go through. I'll show you here Hugging Face. So this is a PI. OK,
