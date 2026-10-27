# Part 02  [00:15:10 - 00:30:30]

## Segment 017  [00:15:10 - 00:15:52]
Slide: slides/slide_017.jpg

**Bharathi R** [00:15:10]: to course handout and the evaluation scheme discussion? Okay, fine. So let me now move on to the content. If I am fast, you can always tell me.

**SHEETAL PRAKASH BARANWAL** [00:15:27]: Yes. Remember, assignment would be in a group or it would be in an individual.

**Bharathi R** [00:15:32]: Group, group, group assignment.

**SHEETAL PRAKASH BARANWAL** [00:15:35]: Okay, thanks.

**Bharathi R** [00:15:38]: So you will be given a chance to make your group. So we will give a timeline. If you don't make a group, we will make the group.

## Segment 018  [00:15:52 - 00:16:42]
Slide: slides/slide_018.jpg

**SHEETAL PRAKASH BARANWAL** [00:15:52]: Thanks, ma'am.

**Bharathi R** [00:15:54]: Yeah. So is my voice breaking? I could see the Chat section.

**AKANKSHA SHRIVASTAVA** [00:16:07]: No, ma'am.

**SHEETAL PRAKASH BARANWAL** [00:16:07]: No, it is it is clear, man.

**NAVIN KUMAR** [00:16:08]: No, man, it's fine.

**BOLLIGORLA SHEKAR** [00:16:09]: Now, now looks.

**Bharathi R** [00:16:10]: Okay. Thank you. Thank you.

## Segment 019  [00:16:42 - 00:18:00]
Slide: slides/slide_019.jpg

**Bharathi R** [00:16:43]: Yeah, these are the other operation, yes, please.

**AKASH KUMAR JAIN** [00:16:44]: So, ma'am, one question about labs. So will there be any dedicated lab like

**Bharathi R** [00:16:49]: Mm.

**AKASH KUMAR JAIN** [00:16:51]: we had in the previous semesters?

**Bharathi R** [00:16:54]: Yeah, yeah, yeah. You will get an axis very quickly. So, we insist to use those labs for, you know, for the webinars or your hands-on. So, sometimes hands-on, we use a collab, but you can use it for assign, because it will take a time to load. So, if you wish, you can always keep open and use that, and... Also, for assignments, you can use that lab. If you want to use
seriously very good models, because you know, open source models, lightweight models will not, I mean, satisfy the user requirement. So, if you want to use a very good LLM of your choice, open source LLM, you can use our lab resource pre option. We insist. all of you to use that.

**AKASH KUMAR JAIN** [00:17:47]: Thank you, ma'am.

**Bharathi R** [00:17:49]: Yes, so now let me get into the content first: Foundations of Conversational Agentic Ai. So, already I have shared at the Taxila portal.

## Segment 020  [00:18:00 - 00:20:22]
Slide: slides/slide_020.jpg

**Bharathi R** [00:18:00]: So, this is the, you know, the four modules. The 16 lectures are split into four modules. The first model is about the Foundations from Lecture 1 to Lecture 3, and the second set of modules is about the building blocks, like how to augment the LLM. So, LLM itself is like one, you know, a very good reasoning model does not have access to the real world, and it does not
have a memory to remember what happened before. So we have to give hands to access the real world called tools, and we have to access the tools in a standard, structured way, and we have to give a memory, whether a Naive memory, an inbuilt memory is there with the model, or we are going to add an extra memory with the model. So all those things will be discussed, short term, long term memories,
and also we will discuss about the embeddings in detail, how to get the contextual embedding and how where it will be stored. And then also we will discuss about in detail about the RAG pipelines. So the RAG pipelines and all you would have learned in. Nlp, correct? So, you know a bit, very good introduction about RAG, correct? Then the lecture, third module is about agents. So, what is an AI
agent? How do you plan the flow for AI agent and when you will go for multi-agent systems? And what are all the different, in network, we have different patterns, right? So here also, when you go for a multi-agent, there are different patterns, orchestration patterns available. So we will discuss that and then we will discuss about the evaluations. So as a model evaluation and a system evaluation,
okay? So 2 different categories of evaluation will be and cost optimization. This is same with L9 to 11 and the 4th model is about the production ecosystem, like safety mechanisms, protocols, MCPs, A2A, and how to build an ethical AI and also how to follow the various government rules. What are all the Indian government rules? What are all the US? UK and so on. So these are all these are all the
four modules that across 12 lectures. So these are all the learning outcomes

## Segment 021  [00:20:22 - 00:21:18]
Slide: slides/slide_021.jpg

**Bharathi R** [00:20:22]: and evaluation plan already we discussed. These are all the prerequisites. So you Python, we use extensively Python and you know the Ml basics, what is the training, what is inference and what is evaluations? These key terms already you know, and you know how a neural network is formed. What do you mean by parameters? What do you mean by training? And the basic
understanding of our transformers. Then also API basics. So to connect with the tools, right? So we use, I said, a structured data. We use a JSON structured data. For tool use, OK, then the basic statistics, you know this right? The metrics, the very basic fundamental metrics called precision, recall, and also you know a little probability also, right? So, this is all the pre-requisites and... So
please check your Taxila regularly. So let us come to this today's session

## Segment 022  [00:21:18 - 00:22:34]
Slide: slides/slide_022.jpg

**Bharathi R** [00:21:22]: outline. So here we will just discuss about what is exactly a Conversational AI, and we will discuss the evolution of this chat bots, okay? And, as on now, we... We build chat bots using agents. So why agents are required? So this also we'll be discussing and what are the building blocks? OK, components for building these chat bots and agentic chat bots and what is
agentic life cycle and what are the different protocols on the and on on the, you know, high level, we'll discuss all these things. Then we will discuss about the Nlp Foundations, the tokenization that we, you would have learned in Nlp Kit, right? Using Nlp Kit in Nlp, you would have done a tokenization where there you would have done word-wise tokenization, but here we will not use a word-wise
tokenization. The tokenization is completely different, okay, that we will discuss and what is context window and the database. So, introduction to Conversational Ai, so we will definition is an AI system

## Segment 023  [00:22:34 - 00:25:46]
Slide: slides/slide_023.jpg

**Bharathi R** [00:22:36]: that converses. Natural language. To understand, intent. Retain the context. retrieve the knowledge and respond or take action and generate output in a natural language. So since we talk about Conversational AI, our generative system. Is limited to text. Okay, so here we will not discuss about multi-modality like images or you know Regenerating videos, and so on. So,
what we expect in the conversation AI, what are all the core capabilities? A Conversational system that we are building is the system that we are building should understand the natural language, first one. And it has to generate natural language, generate human-like responses. In the meanwhile, during the conversation, it has to manage the conversational flow and the context. So on the what topic
we are discussing with the bot. And also it has to remember the conversation history. And a conversation will not like a single one word question and answer. Always a conversational system, we built a continuous, right, a multi-turn interaction. So a lot of queries and a lot of responses. For every query, we get a response from the AI system. So it will be a, you know, multi-turn. a turn
conversation. A turn is nothing but... One turn is called. One greedy. And one response. This pair is called one turn. So generally, we converse, our conversation with any of these AI system will be multi-turn. There will be many queries, right? We don't end up always with one query and one response. We will not close the window. We will ask next question, related question to the first one, right?
So it's called multi-turn and how do we... maintain the coherence. Then also personalization, adapting to user preferences, correct? So now when you open your cloud, and it will be always signed in, right, with your credentials, and it will remember you are, you know, the profile, right? So what do you, in which programming language you do, and all those things, history about you, your name,
everything it remembers, right? So, so every bot that is built will adapt to the user. So how that user preferences are stored. So this is the core capabilities of any AI system. So understand, reason and act. These are all the three, you know, main objectives that will be carried out.

## Segment 024  [00:25:46 - 00:29:56]
Slide: slides/slide_024.jpg

**Bharathi R** [00:25:46]: So, when you look at examples in daily life, daily, like we come and talk to Alexa, we talk to Siri, we talk to Google Assistant, so maybe when Alexa came, like it was following a. I mean, the mid, like, it's not exactly an LLM was used in the beginning, so it was adapting with the machine learning concepts, but nowadays they are using, they are Alexa and you know,
Google Assistant, Siri, they all use, you know, these kind of AIs, right? LLMs they use, they use agents, right? So, in the early days. It always, right, whenever you talk to Alexa, you simply don't, you cannot ask, play music. It will not play. You have to tell Alexa, play music, right? Open. Um... Amazon Music. So every time you use the word called Alexa, then only Alexa will understand that you
are communicating with the Alexa. So always a wake word. So, hey, Siri, we say, hey, Google, right? Siri, we say, we call with the keyword, wake up word called Siri. We use the Google, hey, Google, right? wake up word. So when the wake word is given, it will understand that we are communicating with these systems. So actually we call a wake up word. Upward, and there will be, you know... So speech
to speech reorganization, automatic speech reorganization, it is not the text week talk, right? So there will be a speech reorganization conversion will happen. So speech to text. then it should have NLU, Natural Language Understanding. So once it understands, it will do the action. Suppose what I said, Alexa, please open Amazon Music, right? Then it will understand that the user is asking for
opening the Amazon Music app. Then it will. open the music app, then we can tell further, right? Play this song. So on this genre, you play all those things and it will again, it will reply, right? It is text to speech. TSS text to speech. And if you take a second example, customer support, like if you take a HDFC Bank is a pioneer, they have a customer support. Can you anyone tell the name for
the HDFC customer support chatbot? So, they are pioneers, actually. Or Amazon has some child. What is the name of the chat bot, the name of the persona in the Amazon?

**NIKHIL V. KAPRE** [00:28:53]: Rufus.

**Bharathi R** [00:28:54]: Rufus, perfect.

**ARUN SINGH SHAH** [00:28:56]: Group.

**Bharathi R** [00:28:57]: And HDFC has Eva. So there are, yeah, exactly. So you have banking chat bots, e-commerce help. When you look at the banking chat bots, now even Eva also, it's a rule-based one. So we look at that, it's a rule-based one. So it is not actually, HDFC Eva is not having any AI system. It is just an rule-based one. But also we have healthcare virtual agents, healthcare, trial,
HHR assistance and so on. So if you take in healthcare, like, you know, there will be a receptionist, literally like a receptionist. When we go to receptionist, she will divert to which section, looking at the report, she will tell whether we have to go to. you know, ortho, neuro, and all such things she will tell. So try age, looking at the symptom, it will do the try aging. And also you have
many HR assistants, right? Virtual agents available. This is a market trends and industry impact, so you know better than me,

## Segment 025  [00:29:56 - 00:30:30]
Slide: slides/slide_025.jpg

**Bharathi R** [00:30:01]: so no need to discuss on this. And this is, you know, the Conversational AI market by 2030, and the ChatGPT users, how it's increasing every month. So the AI Agents, Fortune 500 company using AI Agents and so on. Now, let us discuss interestingly about the evolution of these chat bots, right from the rule-based chat bots to autonomous agents. So, this is the, you know,
evolution journey. So, it starts from Elisa.
