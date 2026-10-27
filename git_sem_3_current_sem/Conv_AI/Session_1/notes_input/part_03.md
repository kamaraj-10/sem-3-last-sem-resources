# Part 03  [00:30:30 - 00:46:40]

## Segment 026  [00:30:30 - 00:35:28]
Slide: slides/slide_026.jpg

**Bharathi R** [00:30:34]: So you would have studied about Eliza and Alice in Nlp, correct? Yes. Did you go through this, Elisa and Alice? No. So these are all the rule based. This is the first chat bot. OK, 1960s it came. Actually, this was built for with respect to medical. Both Alice and Eliza, they were acting as, you know, psychologist. So the capabilities you can see, it can answer, they
have a predefined questions and answers. So if there is no question, if there is no response, human response, that is matching with the set of question and answer, it will say very politely, I don't understand. So they have some, you know, more 300 words only. So predefined question and answers were there. So keyword detection and simple scripted question answer were there. So here there is no
learning at all, no models, no neural networks, nothing. It's very rigid and no context. There comes at the Ml model, machine learning models like SVMs, conditional random fields, hidden Markov models. which does this intent, you know, what is an intent and what is an entity? How do you define an intent in a given sentence? How do you identify that is an intent? How do you identify that is an
entity in a given sentence or a text? very basic definition.

**SREEMANTHULA SRAVANI** [00:32:24]: In that is something what user wants to know,

**Bharathi R** [00:32:27]: Yeah.

**SREEMANTHULA SRAVANI** [00:32:27]: the complete sentence and entities in which category that intent belongs to, like entity relationship of that particular intent.

**Bharathi R** [00:32:37]: Yeah, so I think Suresh Babu has replied with respect to your PIYUSH tagging. And when you look at the sentence, you can identify verb as an intent and you know, nouns as an entity, right? So literally what you have said, the meaningful, right? So what the user wants. And what, how we connects to. with an entity extraction. And next comes a deep learning using RN and
cell stSemAIMLstudentsdocs sequence to sequence model. So there was an end to end learning and but here we have to build the data set. And we have to make a task specific training. So like whether it's a simple question answer or a detailed question answering and so on. And there comes our transformers. So this, the transformers, the capabilities or transfer learning, contextual embedding and so
on, still requires task specific fine tuning. Then 2020-2023 LLMs came that is built from the transformers. So there actually the limitations are, you know, hallucinations and no real-time data and no actions. So LLM is a pure. intelligent reasoning model, intelligent, intelligent. But it will not know the current information and it does not have any memory. It will answer whatever it has trained
so far. So the capabilities are, you can go for a few short learning, general purpose, and of course, the responses are very fluent. Natural responses. Then that was not sufficient. Then the agent KI came. So when you add Ml with the tools hands and you give the memory to remember, and when you have a reasoning, very good reasoning to plan how to execute the task, so it can execute the actions,
multi-step reasoning, autonomous workflow came. Now, they discuss a lot of discussion and research is going on on on device and multi-modal, you know, chat bots. So, using small language models and native multi-modality models are coming up. A lot of us are still here and still we find a lot of research is going on and this is coming up where the capabilities are real time voice, video, privacy
first local processing and all. But the limitation is hardware constraints and the fragmented ecosystems. So but we will stop our discussion till this Agentic Ai and also with the multi agents how to built a multi agents. So this evolution journey, like you can see that errors are one. To. Three, 4, 5, 6, 7. So, I have put together all together and in

## Segment 027  [00:35:28 - 00:36:26]
Slide: slides/slide_027.jpg

**Bharathi R** [00:35:29]: three levels. OK, so one is first one is a rule-based chat bots. OK, so this rule and second one is the LLMs powered assistance, and the third one is autonomous AI Agents. So... If you take a rule-based chat bot, like rule-driven, so it answers based upon the keyword. No learning, no training, nothing. So it is on scripts and decision trees and it has a limited
conversation context. It answers the questions. Whereas when the LLM came powered assistance, it is context aware, LLM based understanding and generation. And here also in the LLM powered assistance, there are tool calling and there are memory. Okay, so this is LLM powered assistance. So, here. these two I'm talking about. And here when you look at this is

## Segment 028  [00:36:26 - 00:40:52]
Slide: slides/slide_028.jpg

**Bharathi R** [00:36:26]: autonomous agents. So what is the difference between these two? Any of your observation here, also, when I say LLMs. is augmented with tools. And it has got memory also, so a context server tool enabled and memory enabled, so you have this. Okay, and it has a very good memory. You have a RAG also. You can retrieve the content also. But still, this is called an Ml powered
assistant. It is why this is not called an agent.

**VIVEK RANJAN UPADHYAY** [00:37:21]: Autonomous with capabilities.

**SREEMANTHULA SRAVANI** [00:37:21]: If it has to be an agent, oh, sorry, go ahead.

**Bharathi R** [00:37:21]: Yeah. No, no, please, please give your that process. Nothing, so give a try.

**SREEMANTHULA SRAVANI** [00:37:32]: If it is like LLM powered assistant, we are using it only for some specific output rendering or after retrieving from RAG, we are combining the system prompt that user has like whatever the intent user has given and with the RAG response and it is generating an output that can be LLM powered assistant. And if it is an atomous agent, it itself is an agent and it
has some specific rule-based agent card and it gets triggered from orchestrator or some other agent based on the intent that user has given.

**Bharathi R** [00:38:10]: Yeah, very good, very good, Troy. So here, actually, this LLM powered assistant is actually it's a workflow, right? We are telling the flow where this kind of assistance is you used for closed end solutions. So we will tell that, I mean, there is no reasoning working here. It cannot plan on its own. No planning. We have to tell the plan. Like you call this tool and you
fetch this memory and you give the response. Whereas here, when you call an LLM powered assistance as an agent means here, the LLM itself will plan how to execute. So that is where the difference between the LLM powered assistance or an LLM workflow and an AI agent. LLM is the autonomy, autonomy is given to an LLMs to do the planning, to do the reasoning, to complete the task. So, that's a
fundamental difference between, you know, and this is called actually, and whenever you have an LLM with tools and memory, it is called, and as per Cloud, they define this as an augmented LLM, but still not an agent. I am, we are as a, you know, user and like a. We are going to tell through the code that you do this at this time. You call the tool, this tool at this time, you retrieve from the
memory for this and you give the response. And we are defining the plan. Okay, plan is made by us. So when you make the LLM itself to... do the plan, you are giving an autonomy to do the reasoning, then this LLM powered assistant will become an agent. So it plans and decomposes the goals. It adds, observes, and revises. And suppose if you have a complex task, you can go for multi-agents and it
coordinates multi-step workflows. So it manages the outcomes. So this is for open-ended problems. We generally go for agents. So here the plan is done by code. Here the plan is done by the LLM itself. That's a fundamental difference between an augmented LLM or LLM powered assistance with autonomous AI adjustance. So autonomy is given to the LLM. Now, in detail, when you look at the rule-based,
yeah,

## Segment 029  [00:40:52 - 00:46:40]
Slide: slides/slide_029.jpg

**Bharathi R** [00:40:53]: Devashish.

**DEVASHISH VERMA** [00:40:55]: Yeah, ma'am, just one clarification. So the difference is that in LLM and powered assistance, the workflow is fixed, as in we are already defining if this kind of request comes, you call this tool. We are not letting the LLM decide what

**Bharathi R** [00:41:09]: Yes, yes, yes, yes, yes, yeah.

**DEVASHISH VERMA** [00:41:10]: kind of tools to call. Right? Okay.

**Bharathi R** [00:41:14]: We are hard coding it.

**AKANKSHA SHRIVASTAVA** [00:41:17]: One more thing, ma'am.

**Bharathi R** [00:41:17]: So in the other agent, one second agent, we will throw,

**DEVASHISH VERMA** [00:41:17]: Understood.

**Bharathi R** [00:41:20]: we will give the list of tools, agent itself, it will decide which tool to call when.

**DEVASHISH VERMA** [00:41:29]: Okay, Martin.

**Bharathi R** [00:41:31]: But in LLM powered assistance, I will tell this time you call this tool for this, you call this tool to the code I'm

**DEVASHISH VERMA** [00:41:36]: Okay, okay.

**Bharathi R** [00:41:37]: telling.

**AKANKSHA SHRIVASTAVA** [00:41:38]: Okay, so ma'am, can I say that autonomous AI agents uses LLM? Is it a correct understanding?

**Bharathi R** [00:41:49]: LLMs for reasoning itself, planning.

**AKANKSHA SHRIVASTAVA** [00:41:51]: Yes, Okay.

**Bharathi R** [00:41:54]: So, we will give, see, we will give the list of tools and we'll get a memory also, and we will make the Ml to decide the sequence of actions, planning everything, reasoning everything. If it goes wrong again, it will go and try several times. If I set that iteration for five times, yes, that's autonomy.

**BOLLIGORLA SHEKAR** [00:42:08]: So... So, so in the autonomous AI agents, we can say the agent intelligently think itself and do some actions, right?

**Bharathi R** [00:42:19]: Yes, yes, yes, given the facility. Given the facility means I will give a set of tools. I'll give the, you know,

**MAHENDER SINGH** [00:42:26]: Machine.

**Bharathi R** [00:42:29]: I will tell I want to do this task. That's it. Like a personal assistant, you give the money and you give, you book the ticket, you plan for this and you'll give your, if you have a personal assistant, you tell, right? So he will do the actions on his own. You are not directing that you come at 8:00, take the, you know, the vehicle, go there, here, there. That complete
instruction you are not going to give.

**MAHENDER SINGH** [00:42:59]: One question.

**Bharathi R** [00:42:59]: You are better.

**MAHENDER SINGH** [00:43:02]: So if we do, so RAG, it is understandable, right? Because RAG,

**Bharathi R** [00:43:02]: Yes.

**MAHENDER SINGH** [00:43:07]: we kind of give an output and the context is enriched through the retrieval augmentation, right? But for SMPC servers, right,

**Bharathi R** [00:43:13]: Mm.

**MAHENDER SINGH** [00:43:16]: where we kind of define a SMPC server and then in there. we define the tools, will that fall under the SLM powered assistant or autonomous AI agent?

**Bharathi R** [00:43:26]: No, no, MCP can be used both in MCP is a standard protocol to connect with the tools other external parties.

**MAHENDER SINGH** [00:43:36]: Mm.

**Bharathi R** [00:43:36]: HTTP protocol MCP protocol has come. HTP is standardized, right?

**MAHENDER SINGH** [00:43:41]: And so.

**Bharathi R** [00:43:43]: So that protocol you can use anywhere.

**MAHENDER SINGH** [00:43:43]: Right, right. No, because there also we define tools, right? Meaning this is the tool and then LLMs decide which tools to call to address our

**Bharathi R** [00:43:55]: M.C.P. See, M.C.P. is like your USB.

**MAHENDER SINGH** [00:43:56]: case, right? Correct.

**Bharathi R** [00:44:04]: Yeah, to connect with your tools, standardized way of connecting with your

**MAHENDER SINGH** [00:44:07]: Correct, correct.

**Bharathi R** [00:44:08]: tools. No need to write, you know, a separate, you know, code for one tool and separate one strategy for another access, all such things. Just standardizing through the MCP,

**MAHENDER SINGH** [00:44:18]: Okay.

**Bharathi R** [00:44:19]: that's it. Even without a, it is not that you have to. Use only for AI Agents.

**MAHENDER SINGH** [00:44:28]: Mm.

**Bharathi R** [00:44:29]: So for any LLMs, if you want to access any tools,

**MAHENDER SINGH** [00:44:29]: Connect.

**Bharathi R** [00:44:33]: I'm going to use a plugin called SMPC. So one connection, I can connect all the tools here.

**MAHENDER SINGH** [00:44:41]: No, but my question was on the fact that the

**Bharathi R** [00:44:41]: Otherwise.

**MAHENDER SINGH** [00:44:44]: once MCP server and tools are defined and the MCP client,

**Bharathi R** [00:44:47]: Yeah.

**MAHENDER SINGH** [00:44:48]: which is essentially the LLM is 1 interacting with the LLM,

**Bharathi R** [00:44:51]: Yeah.

**MAHENDER SINGH** [00:44:52]: then LLM itself decides which tool to call, right?

**Bharathi R** [00:44:55]: No, L.L.M. See, L.L.M. is not by itself is not an agent.

**MAHENDER SINGH** [00:45:04]: Mm.

**Bharathi R** [00:45:08]: OK. LLMs is purely a model, that's it.

**SHRIYANSH DWIVEDI** [00:45:15]: So, ma'am, agent has that autonomous command to call and plan and, you know, take actions, but an LM can't.

**Bharathi R** [00:45:19]: E. Yeah, but LLM, yeah, through LLM only, I can make a, I can build an AI agent, okay? But I'm giving the power autonomy to the LLM that you behave like this. That's called autonomy. Okay, anyhow, we are going to discuss this in the every

**SHRIYANSH DWIVEDI** [00:45:44]: Okay.

**Bharathi R** [00:45:46]: session we are going to discuss this, that autonomy, all those things. So as of now.

**MAHENDER SINGH** [00:45:51]: So, so, so before we close, just to one point, ma'am. So, basically, if we have a SMPC server client architecture, in that case, it becomes an agent itself, because there also we just give the command or written text, right? Then, LLMs decide how to kind of resolve. or give out the output for that, right, using various tools which we have predefined, but we don't
plan, we don't tell LM that call this, call this, call this, right?

**Bharathi R** [00:46:19]: Yes, yes, yes. I'll show you the code also. I will with the code I will demonstrate how LLM powered assistant will become an agent, autonomous agent. Okay.

**MAHENDER SINGH** [00:46:37]: I don't think.
