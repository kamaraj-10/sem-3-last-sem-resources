# Part 01  [00:00:00 - 00:15:10]

## Segment 001  [00:00:00 - 00:00:04]
Slide: slides/slide_001.jpg

## Segment 002  [00:00:04 - 00:01:22]
Slide: slides/slide_002.jpg

**Bharathi R** [00:00:13]: So very good afternoon. Welcome to the first session of Conversational AI. Hope I am audible. Yeah, thank you. So today let us start the session and already as a prerequisite, you already learned, you know, what is natural language processing and also, you know, the deep neural networks, right? So let us, before starting the session, Let us look at the course handout,
and also I have shared the course handout and the today's session slide with the hands-on and the Taxila portal, so you can all refer. Now, let me share. You know, the handout here. So the Conversational AI subject is, you know, it's a need of the art. So how to design a system that can understand and generate natural language,

## Segment 003  [00:01:22 - 00:03:00]
Slide: slides/slide_003.jpg

**Bharathi R** [00:01:26]: right? So the course description says that design and build real Conversational AI agents that can think, plan, and act autonomously. And develop intelligent systems using large language models, then augment the Llms using memory. using tools, right, and also using information retrieval. So here we will, you know, I think many of you would have taken the other elective
called LLM for Gen. Ai. Most of you would have taken and few would have not taken. That is fine. So these two are, you know, independent courses. So wherever a prerequisite is required, we'll quickly brush up. If you have not taken that elective, we will have a quick brush up on the techniques that we'll be using for building this conversation in our systems. So, we will drive the course towards a
production ready, you know, skills including system architecture, security, ethical considerations, you know, how to build a responsible AI system, and you know, how to, you know, say, I mean, defense, what are the defense mechanisms required, and how to monitor these systems. these things we will and also we will design certain systems, how to do the implementation and evaluate as well. So this
course, you know, it's always spread across 16 sessions and we do have 4 modules so that anyhow we will be detailing in the slides. And these are the textbooks, you know.

## Segment 004  [00:03:00 - 00:03:46]
Slide: slides/slide_004.jpg

**Bharathi R** [00:03:00]: So, when you look at these two, the these two textbooks, you know, already you are very familiar because you would have used this for your natural language processing, and this is the, you know, 2026 edition that is openly available. You can download the book. So, because of the size, I'm not sharing this book anywhere. You can download on yourself. And also the second
textbook is also, it's freely available. That is a practical approach to rags. Okay, it's an open online, very good book, online e-book, useful for how to build the RAG pipelines and how to create, you know, the embeddings and store in the vector databases. All such things will be discussed in this book. And also some of the, you know, openly available journal papers,

## Segment 005  [00:03:46 - 00:05:22]
Slide: slides/slide_005.jpg

**Bharathi R** [00:03:50]: conference papers will be discussed across all the sessions and which other paper is that is used that I will share in the during the lecture session, I will share wherever it is required. And sometimes I have included all the URLs of those, you know, freely available resources across the web sessions in the slides. It is available, so you can access it always, and these
are all some of the, you know, reference books. And then this particular third book is available, freely available in the online. You can download the other three books. If you want, you can buy those books. And then some of the core research papers that will be used. I will share this paper also. And these are some of the other research papers, reference papers, and of course we use a lot of
research papers for, because this subject is an evolving subject and we need to refer the, you know, the current state of art whenever we want to build an EA system or any model we want to use. Sorry. And this is the spread over of the, you know, contact sessions, the dash for the, you know, the session one. The first of all is Foundations of Conversational and Agentic Ai. Today, we will be
discussing about the evolution of these bots, okay? And what is an agent and so on. And second session is about LLMs Foundations for Conversational Agents. Then the third session is all about, you know,

## Segment 006  [00:05:22 - 00:06:34]
Slide: slides/slide_006.jpg

**Bharathi R** [00:05:23]: building when you want to build a conversation systems, what are all the, you know, concepts that we should learn. Okay, so how to hold the conversation, conversations, where, which is the memory part that will store these conversation states, those instances. and very important information where it will be used and how these, you know, when you want to build an AI
systems and how these, the components in the AI systems, how to communicate to each other in a what in a structured way, how it will communicate. And also we will discuss about the various prompting strategies, what is a prompt engineering, various prompt techniques. And how to control the, you know, this is very important, interesting, how to control the, you know, generally all LLMs have the
capability of generating content, right? Text. By and large, it is the text. And now, you know, generating images, generating audios, generating videos, and all coming up. So, how to control, you know, the response control can happen? What are all the available techniques we will discuss in Lecture 2? And in Lecture 3, we will discuss about, you know,

## Segment 007  [00:06:34 - 00:07:14]
Slide: slides/slide_007.jpg

**Bharathi R** [00:06:35]: when we want to build any system. So, how do we do this, you know, orchestration? Of course, This particular session, if you look at, we have a detail, this is on the high level view, will be discussed in Lecture 3, and we have this, you know, high level view is connectivity to the other sessions as well, so that also I have made very, very clearly in the Session 3, DP.
Then we will discuss about tool integration and function calling, a structured way of connecting the components in Lecture 4, and Lecture 5 is we will talk about, you know,

## Segment 008  [00:07:14 - 00:08:04]
Slide: slides/slide_008.jpg

**Bharathi R** [00:07:16]: how the memory mechanisms are incorporated in augmented LLMs and also in Agentic. concepts. So here we discuss about what is the working memory or the short-term memory and how the user preferences are stored the long-term memory.

**VIVEK RANJAN UPADHYAY** [00:07:32]: Japani Leo.

**Bharathi R** [00:07:33]: Yeah, I request.

**VIVEK RANJAN UPADHYAY** [00:07:37]: Pani le kiao.

**Bharathi R** [00:07:43]: I request, if you want to talk, please mute yourself because I have unmuted you all. So here we'll discuss about what is context engineering, what is short-term memory, how the context window is managed, what is long-term memory, all. these things in lecture 5. And lecture 6 is about, you know,

## Segment 009  [00:08:04 - 00:09:02]
Slide: slides/slide_009.jpg

**Bharathi R** [00:08:05]: what exactly is the embedding. You would have learned embedding in Nlp, that is a static embedding using, you know, a continuous bag of words and glow representations. But here, LLMs use contextual embeddings. So we will learn how the static embedding is taken forward to get into a contextual embedding that we will learn, and how these embeddings are stored. So we will
discuss different vector bases and how we will retrieve it, how we will retrieve the content from these vector databases. From there, we will start discussing about this RAG. Okay, so different kinds of what exactly is a RAG? What are the different kinds of RAG? Okay, advanced RAG is available until Agentic RAG, we will discuss here. Then, EL, after this is still your mid sem. Post mid sem, we
have discussed about, you know, the agent.

## Segment 010  [00:09:02 - 00:09:34]
Slide: slides/slide_010.jpg

**Bharathi R** [00:09:03]: How to build an AI agent, okay, and how you will plan, I mean, how will you plan the workflow for completing the task? And suppose if the task is very complex, how will you break the task into a smaller task and how will you assign to multiple agents? So multiple, how will you incorporate multiple agents? What are the different orchestration techniques that will be
carried out in Lecture 10? Then, so we will learn what is this LLM, what is augmented LLM, what is Agentic Ai,

## Segment 011  [00:09:34 - 00:11:00]
Slide: slides/slide_011.jpg

**Bharathi R** [00:09:38]: so how to build this AI system, all is fine. But how do we know that these will work fine? Okay, these are all working fine. How do we check that? So we have to look around evaluation. And we use one new word called reliability. OK, so how reliable your AI system is continuously? It has, because these, you know, AI systems, AI models have the, you know, capability of
learning continuously, right? So, your the adaptation of the model also... keep changing. So how do you, you know, build a reliable system that's most important? So this evaluation and testing this AI system is very much different from the traditional softwares. How it is different and how do we do that? And complete the AI systems depends upon, you know, consuming the tokens. So we always buy the
pro versions, right? Pro versions of ChatGPT or a cloud, isn't it? Or a Gemini, whatever it is. Cloud code, even if you want a cloud code, we have to buy a pro version. And how to use that efficiently, because how do you manage the tokens? So here we will discuss about the cost economics, token economics also. So, how do you choose the models that also will be widely discussed? And then, how do
the Lecture 12 is about, you know,

## Segment 012  [00:11:00 - 00:11:54]
Slide: slides/slide_012.jpg

**Bharathi R** [00:11:04]: how to, you know, set the guard rails, how to guard the system from... how to create a difference mechanism such that how do you prevent the data leakages and how to prevent the unwanted access and how to protect the data that is more important. So here we discuss about the red teaming strategies and what are the safety filters we are going to use. And how to set the
guard rails at the every, you know, a point in the flow line in the AI system flow. Then we will discuss about the production deployment, so continuous integration and, you know, deployment, we will discuss what are the rollout strategies, all such things. Then in the L4, we will discuss about how we are going to do the integration.

## Segment 013  [00:11:54 - 00:12:46]
Slide: slides/slide_013.jpg

**Bharathi R** [00:11:58]: So what are all the standard communication mechanisms, protocols available? like, you know, model control context protocol and A2A, how we will set agent to agent communication, how suppose in the pool of agents across the network, how do we access the agents, third party agents, is called agent network protocol. So all this will be discussed in the lecture 14 and Again,
lecture 15, we will discuss about how to build a responsible AI. So how to build and how to incorporate the ethics, how to mitigate the biases. So all these things and end-to-end deployment, that is lecture 15 and lecture 16, of course, the revision sections. Right, so the evaluation scheme is, you know, EC one component has 30%.

## Segment 014  [00:12:46 - 00:13:32]
Slide: slides/slide_014.jpg

**Bharathi R** [00:12:49]: So generally quiz will be, you know, 3 quizzes. So out of three quizzes, we will take the best two. So because some of you will miss one quiz. So to give a chance, we will conduct 3 quizzes. So many best two will be considered for. the final marks. And assignment, you have two assignments. One is pre-mid sem, the other one is post-mid sem. So each 10 percent. So put
together, you have 30 marks for EC 1 component. And for EC 2, as usual, a closed book, which carries 30 marks and EC 3 post-mid sem, you have your 40 marks. K.

## Segment 015  [00:13:32 - 00:14:22]
Slide: slides/slide_015.jpg

**Bharathi R** [00:13:32]: And this I want you to follow very strictly that like when you, we will be giving a lot of reminders, okay? But please submit. Submit your quiz and submit your assignments. As per the deadline given, no more extension will be given because we manage, I mean, a large pool of students, it is very hard to, you know, monitor and control. So we strictly follow this. So
strictly no makeups for quiz and assignments and all submissions after the announced deadlines will not be considered for evaluation. So anything if you find any difficulty, you please well in advance, you tell us. So these are all the guidelines given. And of course, for experiential learning,

## Segment 016  [00:14:22 - 00:15:10]
Slide: slides/slide_016.jpg

**Bharathi R** [00:14:22]: we have 4 webinars. So you will get your the dates and the pro forma for that. That is approximately when quiz will open for the conversation AI, when assignments will open for conversation AI, and also when webinars. So those details you will get like very soon, as soon as possible. We'll share you that I'll upload in now. Taxila portal, and some of the hands-on
experience in the class. So, this is all tentative, so it's all prone to changes whenever you know this is the as per the requirement we can change. the hands-on in the class. So this is all I need to discuss about the course handout. So do you have any queries with respect
