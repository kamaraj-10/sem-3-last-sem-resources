# Part 07  [01:37:58 - 01:53:58]

## Segment 048  [01:37:58 - 01:41:42]
Slide: slides/slide_048.jpg

**Bharathi R** [01:38:00]: What is my account balance and the recent transactions? This is the question ask. So now observe, look at this, what is happening under request, what is happening, routing, reasoning, tool invocation, memory, safety, and response. So what is my account balance and recent transactions? So recent transactions, it will pull 5 recent transactions, for example. By default,
bank will give you 5 recent transactions, so request user, so user authenticated, look at the, you know, the account information, you get authenticated. So, what are all the entities extracted? We the balance. has to be and the transactions. These are all the entities. Then routing to a banking agent. Tools, these are the tools, get balance and get transactions. So this is like our C Programming
function calling, right? So then the permission check is user has the access. Sanitization should happen. Then the reasoning, this is the plan. So it has to fetch the account balance. This is planned will be done by the LLM. We are not doing it will be done by the LLM. Fetch the account balance, fetch recent transactions, then format response. With the both, that is a balance and the transactions,
last five transactions, then what are the tools there given to get balance is there, get transaction is there, and get balance of the user ID and get transactions given the user ID and the limit is 5 transactions, you extract. So, it will return, this will return the balance, and this particular call will return the last five transactions, and these two will happen. at every stage, right? Because
the user is asking about the balance at 2.30 PM, not in the sequential order. This memory and safety, okay? And it will update the user prefers transaction details. Then safety, it will check all the safety, no PI exposure in the logs. Then once this look at the balance and transactions, it will check for the, it will observe, the model will observe. Once it finds okay, it will give you the
response. Your current balance is this much. These are the last five transactions that happened today, yesterday, two days ago, three days ago, et cetera. And would you like details on any of this? So this is the an Agentic life cycle. So here also I have taken a bank because banking process everyone knows. It's a very local example. Any queries in this? So we are going to, when we create an
agent, we will give the list of tools. It will, the agent will decide when to call. It will decide this has to call the tool, get balance first, then get transactions again, and so on. Yes, Nikhil.

## Segment 049  [01:41:42 - 01:42:18]
Slide: slides/slide_049.jpg

**NIKHIL V. KAPRE** [01:41:42]: Man, when you're actually thinking of building an agent, just drawing up the concept when we used to build bots, right? Where is the feedback loop in this? And where did the agent get to know that the action taken was right or wrong?

**Bharathi R** [01:41:58]: Yeah.

**NIKHIL V. KAPRE** [01:42:01]: But that's just the plan generation, right?

**Bharathi R** [01:42:03]: Your plan, because agent has...

**NIKHIL V. KAPRE** [01:42:04]: That unless some execution has happened, no, my point is unless some execution has happened and the agent is told or given a

**Bharathi R** [01:42:07]: Danger. Mm.

**NIKHIL V. KAPRE** [01:42:12]: feedback that it's incorrect action, right? Where is the feedback loop here?

**Bharathi R** [01:42:15]: Hmm. Here, here, it will actually, it is not shown here, but here,

## Segment 050  [01:42:18 - 01:42:38]
Slide: slides/slide_050.jpg

**Bharathi R** [01:42:22]: like I can see that the tool, it will see the results, observation will happen here. This will be detailed in the further classes. OK, then there will be a reasoning. It will be observed here.

**NIKHIL V. KAPRE** [01:42:33]: Okay, sure.

**Bharathi R** [01:42:35]: This is what a loop I said. This loop I showed you here itself. See?

## Segment 051  [01:42:38 - 01:46:22]
Slide: slides/slide_051.jpg

**Bharathi R** [01:42:41]: This is where the tool invocation get the result; it will come back here, then it will again, if it is wrong, OK, or it has to redo again, it will go back here, so this is where the loop observe this.

**NIKHIL V. KAPRE** [01:42:53]: So, the at the step 7, where the response went out, it could very well have been a.

**Bharathi R** [01:42:57]: This is the final final response reply.

**NIKHIL V. KAPRE** [01:43:01]: No, no, that's what I'm saying, but that's where you will get a meaningful feedback from the user, whether the agent worked correctly or not. And that part seems to be like missing, yeah.

**Bharathi R** [01:43:09]: Feedback? No, you are asking feedback from the user or feedback from the... I got confused.

**NIKHIL V. KAPRE** [01:43:15]: No, no, the they it's at the end of the day, it's the user whose whose job is being done, right? Right, so...

**Bharathi R** [01:43:18]: No, no, here only, here only, here only. User can see you here only.

**NIKHIL V. KAPRE** [01:43:25]: Okay.

**Bharathi R** [01:43:25]: User.

**NIKHIL V. KAPRE** [01:43:27]: There is a even in the loop there.

**Bharathi R** [01:43:30]: Yeah, yeah, no, no, not in the human in the loop. Ultimately, the end user will get to see, will happen to see the result here.

**NIKHIL V. KAPRE** [01:43:37]: Mmh.

**Bharathi R** [01:43:39]: But you are asking human in the loop means human in the loop, HIL, is used as an evaluation strategy, right?

**NIKHIL V. KAPRE** [01:43:47]: Correct.

**Bharathi R** [01:43:49]: So that is why when I said we want to build a reliable system. So we don't use the reliable metrics in the traditional software most of the time. Okay, unless until you have some physical parts, reliably, it has to give the result. In traditional software, always the results are, yeah, yeah, we can put, wait, let me come here. Yeah, so here we use. Observability matrix.
This is an evaluation strategy. Used in the evaluation strategy observed metrics, we can use human in the loop or LLMs in the loop. And we will measure everywhere, every time stamp here, all the intermediate outputs will be measured, actually evaluations. There will be, there are so many frameworks available to do this. So we can incorporate whether you want to put a human in the loop in between
here, that is different. I told at the beginning stage, this is the user request and this is a user. The response will get, the end user will get the response. We can put under this observability framework, under evaluation strategies, there will be a human in the loop inside human, I mean, LLMs also machine in the loop, everything will be there. That is our evaluation design strategy. You want
it?

**NIKHIL V. KAPRE** [01:45:37]: Yeah.

**Bharathi R** [01:45:39]: So this is different and this is different. I got confused when the human will come. Human will see the end user I'm talking. I was answering with respect to end user who have given this request.

**NIKHIL V. KAPRE** [01:45:52]: Just take the example you took of flight booking, right? Unless the flights were booked incorrectly and the feedback given that,

**Bharathi R** [01:45:56]: Ohh.

**NIKHIL V. KAPRE** [01:46:00]: no, no, hey, the preference was for Air India versus

**Bharathi R** [01:46:03]: Mm.

**NIKHIL V. KAPRE** [01:46:03]: Indigo, how would the agent ever learn with respect to say I as a user, right? I was referring to those kind of feedback loops. Yeah.

**Bharathi R** [01:46:14]: See, there we have to check like that, that that we have here that we also we will study, uh, you know.

**NIKHIL V. KAPRE** [01:46:19]: HE.

## Segment 052  [01:46:22 - 01:47:40]
Slide: slides/slide_052.jpg

**Bharathi R** [01:46:22]: This one. See. What to track? Track conversation flows, track monitor tool invocations, token usage per conversation, response latency set is there.

**NIKHIL V. KAPRE** [01:46:35]: Okay.

**Bharathi R** [01:46:38]: We have these tools available and we can also set this. This is a separate area again. You got it. This is what you are asking, right? Flight booking, whether it is doing it properly or not, right? So that we have to do. We are talking only about the objective.

**ARUN SINGH SHAH** [01:46:58]: Actually, I was... Yeah.

**Bharathi R** [01:47:02]: We did not talk yet. We have, there is a long way to go to come to this level.

**NIKHIL V. KAPRE** [01:47:08]: Sure. The other part I wanted to ask was, you talked about tool calling, et cetera,

**Bharathi R** [01:47:13]: Mm-mm.

**NIKHIL V. KAPRE** [01:47:13]: right? The part where it makes a plan about, well, what are the tools to call, et cetera. How do you measure the efficiency or effectiveness of that? The tooling could have actually made a very, very inefficient calling. I'm sorry, the agent would have made-up, so how is that measured?

**Bharathi R** [01:47:28]: Yeah, yeah, there are, yeah, there are, see, there are, that is the trick that we have to learn. That is why I said, right, you know, correctly it is, it came to that particular slide. See,

## Segment 053  [01:47:40 - 01:53:58]
Slide: slides/slide_053.jpg

**Bharathi R** [01:47:40]: how do you, this is an old mindset, my chatbot works now, we want, my agent works correctly. Repeatedly, under all conditions, whether, like, you know, whether it, you know, where it says... Correctly calling the correctly calling the tools correct, whether it it gives always a I mean the correctness in a repeatable way, in a robust way, so how it does. Everything we
have to do it. This is it is in our hand how to build a reliable AI system, AI agent.

**NIKHIL V. KAPRE** [01:48:19]: I guess the question was, is this course going to actually cover some strategies around that?

**Bharathi R** [01:48:26]: To some extent, to some extent, it will cover, yeah, it will cover.

**NIKHIL V. KAPRE** [01:48:31]: Because even the old style, you call it the old mindset,

**Bharathi R** [01:48:31]: Yeah.

**NIKHIL V. KAPRE** [01:48:35]: testing bots is not a simple thing actually.

**Bharathi R** [01:48:37]: Damn!

**NIKHIL V. KAPRE** [01:48:38]: It is the extremely complex set of activities that go into it. Yeah. Yeah.

**Bharathi R** [01:48:41]: Yes, yes, yes, yes, even more, much more complex than this.

**NIKHIL V. KAPRE** [01:48:47]: Thank you.

**Bharathi R** [01:48:48]: Yeah, yes, so you have, Arun, you have one more question.

**ARUN SINGH SHAH** [01:48:52]: Yeah, actually the same question actually I have like asked in the chat also regarding the memory updation part and what to store, what not to store. So this thing also same like the

**Bharathi R** [01:49:02]: Alright.

**ARUN SINGH SHAH** [01:49:04]: observability comes in the picture like before memory, what to store like during conversation.

**Bharathi R** [01:49:10]: No, like, see, in the interest of time, I just, I will tell you that we will discuss that in detail when we come to Session 3 or 4, I guess, on the memory, but what to store, what not to store.

**ARUN SINGH SHAH** [01:49:24]: Okay.

**Bharathi R** [01:49:25]: And there also it depends upon, I mean, if you look at the proprietary models,

**ARUN SINGH SHAH** [01:49:26]: But.

**Bharathi R** [01:49:30]: every model have their own algorithms.

**ARUN SINGH SHAH** [01:49:35]: Okay.

**Bharathi R** [01:49:36]: You got it. It is on, see, everything depends on what strategy we are choosing. So, LLMs is not is a magic of course, it is not magic on its own. So how judiciously we have to use this components to build an AI system is in our hand, right?

**ARUN SINGH SHAH** [01:50:02]: RAM. So that memory is all is.

**Bharathi R** [01:50:04]: So for every task, now every task, people mindset, most of the mindset is for every task, now we will use AI agent. For every task, using AI agent is our foolishness. So we have to, you can, we will refer many papers, many examples also. It is not that for every task we have to use an AI agent. No, for every task we have to use an LLM. No, everything is cost. Everything
you have to pay for it. So that's what I said, judicious usage of these AI systems,

**ARUN SINGH SHAH** [01:50:41]: Yes.

**Bharathi R** [01:50:43]: where you have to, how you're going to make your design. That is very, very important. And how the correctness, how which tool is called, that we have to make a design on that proper design, we have to make it. Even then, there will be a failure. No system is perfect, correct?

**ARUN SINGH SHAH** [01:51:02]: Mn.

**Bharathi R** [01:51:05]: So that is what we are going to learn in this course also, how we will build an AI system. And how do we make sure the system will work well? So we cannot expect 100%, right? There might be some pits and falls in how to handle that and what are the different strategies available. And now this evolving field, right? A lot of strategies are coming up, which one to use for
our particular requirements. So everything is in our hand. So for that, we have to do an extensive study on what is existing, what is available, and how people have done so far to understand the various already built-in systems so that we can use that very effectively, we can deploy. that effectively in our system, in our company or organization, wherever you want. So it's not like a magic if you
give some input, LLM will give whatever we want. No, definitely not. You just observe the evolution of ChatGPT itself right from 2022 to 2026. You would have seen, right? You would have interacted with ChatGPT from that point, right? Yes or no?

**ARUN SINGH SHAH** [01:52:30]: Yes, yes, yes.

**Bharathi R** [01:52:32]: They are also growing day by day, correct? Claude also, why Claude comes with so many models and every model they have, you know, Sonnet or in a Haiku or you know, a Fable for every model they have a version and they're updating it. Right, why they come with? Because whenever one new model comes, all of a sudden there is one more requirement, right? So human mind never
satisfied. They want more and more and the model has to complete the task. They come up with another strategy. There are many failures. It's a teamwork, right? Many failures. How they come? overcome those failures, everything we have to observe. It is not just like a button. If you give a switch on button, it will give you the answer. Everywhere we have to put, you know, a gate and check. Yes, a
checkpoint we have to put. whether it is doing correctly or not. This is all hypothetical study we are making. This is the example is our hypothetical study. just to understand the basics of what an agent can do. But no more, there is no banking agent like this. If I close this and if I show you, you know, this is one example given.
