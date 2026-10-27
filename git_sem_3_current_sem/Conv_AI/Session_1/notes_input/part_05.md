# Part 05  [01:04:34 - 01:22:24]

## Segment 041  [01:04:34 - 01:08:12]
Slide: slides/slide_041.jpg

**Bharathi R** [01:04:34]: Now, to make the first to make the, you know, you know, a Conversational AI system. We want. LLM. How LLMs are made? LLMs are built from transformers. Right? So right from the transformers, on the transformer, we do a pre-training on the massive data. Then once we train, retrain on the LLM with the massive data that is a very large data that will become an LLM, it could
be a GPT, Cloud, or LLAMA, any models, okay? And again, this pre-training is not sufficient. We do the fine tuning. or instruction tuning, whatever is. Anyhow, we'll detail it later. And then on the fine-tuned model is not enough. I said it is like a intelligent student in the closed room. You give hands, you give extra books, memory, and you give a planning. This is a reasoning. Autonomy to the
model, then it will become a conversational agent. So, without this planning, it is called an assistant, not an agent. So, you can see the technical capabilities, and... These capabilities gives what kind of, I know. inference to the model. So self-attention, you would have come across this word self-attention several times when you studied about the transformer architecture, right? So relate
every word to all others, the input that will the self-attention resolves the ambiguity. It will resolve unclear and underspecified request. Contextual understanding. So embeddings are all contextual understanding, dynamic understanding. No more, you know, what to wake or, you know, what to wake and glow and see bow will give you static embedding, right? Not a contextual embedding. So here, the
word meaning depends upon the context. That will help us. Help the model to understand the intent. And long range dependencies. So connect ideas across very long passages. So this long passages relate to the context window. Now we have almost all models, proprietary models, the context window sizes 2 million, correct? 2 million tokens it can have it is in the window. So NLM can see 2 million
tokens. at that time limitation. So this 2 million tokens help in multi-turn coherence, right? When you open one chat window with applaud, so you will upload some document, on that document you will ask questions. So within 2 million it remembers everything and you will have a very, you know, a coherent conversation, multi-turn conversation you can have. So remember and track earlier parts of a
conversation. Then parallel processing, so faster training than RNNs. This is the capability of the transformer. So that will make the model to understand and generate a fluent human-like replies. So these technical capabilities make the conversations, AI conversations, more good and efficient. So the internal, this is the internal capability transformer shows up a visible conversational behavior.
Now, this is the though we want ultimately we want to build a conversational agent. OK, so here.

## Segment 042  [01:08:12 - 01:10:36]
Slide: slides/slide_042.jpg

**Bharathi R** [01:08:15]: In what areas LLMs are good and what are all the limitations of LLM? You know, LLM. Is. A naive LLM, a model, is a stateless. That means you don't remember anything. To make the LLMs to remember the previous things, you have to give a memory. LLMs is always stateless. But LLMs is a very, very good trained model. It has a very good reasoning capability. That reasoning
capability comes from. Training. Okay, so it has, it can generate, you know, human-like dialogue, it can understand intense, it can have a, because of the, you know, the long-range dependency, it can have a context retention, the context window is quite large, you know, it can remember the multi-turn conversations. And of course, it generates fluent and contextual replies, and it can do
summarization and keep it on its own, contents information. And of course, entity extraction, sentiment analysis, or by default, LLM has, because LLM is a good reasoning model. But it does not have access to tools on its own. Okay, so no real-time data training cutoff date. If the model is trained till 2025, it knows only till what has happened till 2025. So, hallucinations, plausible but false
output, and it cannot act, no access to external systems, no memory, forget after the context window, calculation errors, struggle with math, varying answers to one questions, and no verification, can't check facts. So these are all the limitations of LLM. That's why we augment the LLM. Give a connection with the external world through tools. You give memory to remember what has happened, okay? So
that way you are augmenting the model.

## Segment 043  [01:10:36 - 01:11:42]
Slide: slides/slide_043.jpg

**Bharathi R** [01:10:36]: So why we need Agentic architecture? Solution is argument LLMs with external capabilities. So you give tool calling. And to avoid hallucinations, you give RAG capability, and you can can't take actions, you give the capability of function calling, or it is called tool use. Other name is tool use. Okay, and no memory, Excel memory systems. You can't do calculations, you
know, in 2020. 2023, if you ask any, you know, math question to ChatGPT, it will confidently giving wrong answers, right? So now it can have access to calculator tool, it access to code executions, it can do precise math computations, and plus. reasoning power also, that is planning, that is called the react tool. Reasoning and acting capability to the LLMs.

**SREEMANTHULA SRAVANI** [01:11:40]: And what does external memory mean, ma'am?

## Segment 044  [01:11:42 - 01:18:46]
Slide: slides/slide_044.jpg

**Bharathi R** [01:11:46]: Yes, X.

**SREEMANTHULA SRAVANI** [01:11:46]: Other than rank, what is external?

**Bharathi R** [01:11:50]: See, memories are, you know, this is hallucinations, to reduce hallucinations, this is no memory. So memories, I told you, there are three, I mean, broadly classified into two memories. One is short term. Other one is long-term. Long term, we have three kinds of memory now. One is called semantic memory. Next one is episodic memory. And the third one is procedural
memory. Okay, so... RAG is used, I know, as another kind of a memory here also, like procedure also, we can use a RAG system. RAG is the kind of, you know, a memory storing and retrieval capacity is one of the mechanism to store, but we want these kinds of memory, like, you know. Episodic means in the previous conversations, what happened? So now if you interact with the cloud, right, or in a
ChatGPT, right, you would have, you will have a conversations before a month or so. Still that document is available, even it still remembers, right? RAG means the answers will be grounded. To the document. If I attach a document, if you suppose in your ChatGPT, you are uploading one PDF document. On the PDF document, you will ask when query. Right, so imagine 2 scenarios. OK, let me erase the ink
here. Suppose. This is your any one chat chat bot, LLM based chat bot, okay? Or, if you, if you are building your company chat bot, OK, HR bot. So, in this in the HR bot, suppose if you are asking some query. At your company, related to your document or related to some HR policy, if you don't give any HR document to this bot. It might, it may be LLM based bot. Imagine this is an LLM based bot. And
this LLM based HR bot at your company does not hold your HR company HR policies. And if you are asking a query, it might give the answer. related to a general HR policies, not your company specific HR policies. Yes. Or otherwise, in the ChatGPT, you are asking one question. OK, so what is some specific question? Okay. OK, well, what any some very specific question if you have? Some very specific
question let me ask and if you ask a chat bot, chat bot, any chat, maybe a ChatGPT. It might give you a general reasoning, general reasoning answer. But here, when you, yeah, when you upload a PDF document to your Chat GPD, you upload one PDF document and you ask a query, this will go and refer this PDF, whatever it is available in the PDF, it will give you the answer. This is called actually a
RAG. This RAG alone is not sufficient. We want other memories also. That is a memory system here. RAG is for grounding your answer with the with the document you are attaching. This memory is not alone enough. We want some other memories also. How it will remember now with the ChatGPT or a cloud remembers you. So suppose you have a, you are habituated to do a Rust programming always. So whenever
you ask ChatGPT or a cloud, you write a program for this particular use case. It automatically will give you a Rust programming. It will not ask you in which language you want. Over a period of time, have you observed?

**AKANKSHA SHRIVASTAVA** [01:17:02]: Yes, ma'am.

**Bharathi R** [01:17:04]: So, how this will not happen before, before we have to tell specifically, you give you write a code in this language, we have to tell specifically now, it would have it would have kept all your user preferences there. that you are generally you do Rust programming or you use a Go programming or you use a Python programming. So those things also, user preferences also
will get stored in the memory, correct? So, RAG is a kind of a memory, I agree, but that is... Used for, yeah, it is a word is your word ground ground answers with the particular document, whereas you need memory systems that remembers user preferences, what happened in other instances with respect to your credentials, everything it will remember for that we need Excel memory systems called the.
you know, short term memory over 1 instance on one episode or how to remember the user, how to remember the various procedures to do that will, I mean, span over the sessions, episodes. So don't worry, we are going to look at every, for everything we have an hands-on, we will look at that. So now, agent, we do have one small case study, agent lifecycle, reasoning, planning, and action loops. Yo,
did I answer your question?

**SREEMANTHULA SRAVANI** [01:18:40]: Yes, ma'am, that you want?

**Bharathi R** [01:18:42]: So, so one case study, we will do one interesting case study.

## Segment 045  [01:18:46 - 01:22:24]
Slide: slides/slide_045.jpg

**Bharathi R** [01:18:47]: Now, agent lifecycle have, you know... Yeah, Akansha.

**AKANKSHA SHRIVASTAVA** [01:18:52]: Ma'am, I have a very basic question. So when we say that we will need RAG and

**Bharathi R** [01:18:54]: Yes.

**AKANKSHA SHRIVASTAVA** [01:18:57]: then some extra external memory like episodic or something, by which we saying that we are not going to actually choose them. It is like the model we are choosing. It is coming within all and already built in that way.

**Bharathi R** [01:19:13]: That is an AI system.

**AKANKSHA SHRIVASTAVA** [01:19:13]: It's. Okay.

**Bharathi R** [01:19:16]: That is the AI system that we are going to learn how to build it. OK,

**AKANKSHA SHRIVASTAVA** [01:19:21]: Okay.

**Bharathi R** [01:19:21]: so in the AI system, LLMs is just one component.

**AKANKSHA SHRIVASTAVA** [01:19:26]: Okay, okay.

**Bharathi R** [01:19:27]: 90. OK, so we have we should know for my AI system what and all kind of memories we have to use.

**AKANKSHA SHRIVASTAVA** [01:19:34]: Yeah. Okay, got it, ma'am. Thank you.

**Bharathi R** [01:19:40]: So an AI system is not equivalent to an LLM always. An agent is not equivalent to an LLM. LLMs is 1 component for that. So what are all the other components required to build that particular AI system? Or an Agentic system. That is what? is all about. So here, like you have a 7 stages and these seven stages is not like though I've given 7 stages here. Okay, so the
numbering will not go like this in the conceptual order. Okay, it is a conceptual order, not a strict timeline. So numbering is just to have a count. Numbering here, that you have to remember, not a strict order. Order here. OK, so it conceptually it is OK. OK, now you see that there are, you know, 7. What do you say? Lines are given over here, 7 stages are given here. So you have a request,
routing, reasoning, tool invocation, memory, safety, and response. So if you look at this stages three and four, I have included one loop here. Reasoning and tool invocation, right? There is a loop, because suppose if we ask, suppose if I am building an AI weather agent, OK, weather agent. So I said that you just check the weather and plan me for the some plan, give me some plan what I will do for
the Saturday evening. So weather agent, when I ask the LLM what will happen, it will call the tool, weather tool, it will go and try to fix the weather today at Bangalore. So it is always not that the connection will establish and whether API is working. So it might return a false, it might no failure also, it might return. So again, it will not stop. So again, it will go and try with the same
weather API. It will try to fetch the weather at Bangalore. It might give or it might fail two times. So what will happen? It will try to fetch the other weather API. And it might come with the result. So there will be always a loop.
