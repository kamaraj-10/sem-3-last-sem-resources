# Part 06  [01:22:24 - 01:37:58]

## Segment 046  [01:22:24 - 01:36:56]
Slide: slides/slide_046.jpg

**Bharathi R** [01:22:25]: It will try for two, three times. Okay, so that is why here that there is a loop always and also break the goal. And if the goal, if the plan is not good, again, it will come back and do the re-planning also. So break the goal into steps, find information gaps, plan the tool calls. Then tool invocation, call APIs, it can query the databases and execute the code. So these
two stages have a looping. So I have had that here. So a question may skip the tools entirely because some failure connection, connection we will not get. So the tool call may end up in failure. It cannot fetch the database. That might end up in failure. So it will try again and again. So the objective of an agent is to complete the task that is given by us. So let us take the steps 1 by 1 here.
First one is a request. OK, the agent receives the input and validates the input. whether the user input is correct. For example, it might, the user might ask a wrong question also. Okay. Ethically it should be correct and it should not, suppose in the banking account or in the company HR policy, HR bot, we should not go and ask about what my colleague Pierre is having how many leaves he has. So
you cannot bluff the bot also, right? So that must be validate and sanitize the user input. So anyone can't access the bot. such as even I cannot access the dates, names, credentials, all such things. So validation happens in many directions. So validation should happen here. Request and sanitize and extract the entities and extract the intent also. Then the routing, then the routing. their agent
will classify the intent, decides which tool to call, and which tool to select given the set of tools. And if it has a sub-agents, multi-agents, it will route to a sub-agent. Now let us take one single agent. So no routing, it itself will do. Then the reasoning is given a task, the agent will break the goal into steps, notices what information is missing, plans which tools, calls to make. Then it
will plan. Here only plan will happen. Actual tool invocation happens here. So the agent acts according to the plan and calls the planned tools, call the APIs. If it wants, it can access any databases given. So whatever it wants, it can do. So the result execute the code. Okay, so the reasoning will what it will go again. It will go back here and check whether it has got sufficient answer. Okay,
so this through will come into the step. In between the memory, it will store the history. It is not in a sequential step. Memory is, you know, the agent stores the conversation history, what the user has asked. Okay, and it will store the, you know, the important entities. maintain the session state and so on, update the user preferences. Everything will happen here in the memory. It should not
go in the sequence. And this is also not in the sequence. Okay, the sequence should come. Once the tool is, the proper tool is invocated, it will go back to reasoning. It will do the observation. Yeah, it has got the enough answer. Then it will go for response. In between, this memory and safety check will happen. Suppose if the user is asking some toxic question, okay, it has to, we have to
incorporate responsible always, we have to build a responsible AI. And P.I.I. P.I. is personally identifiable information. Personnel. Identifiable, yes. Thank you, Vipin. Identity, information. Guard rights information. We have to protect the personal information, so this five and six will not come in sequence. OK, so request routing, reasoning, tool invocation. If you want it, go back to suppose
if the user sets 5 iteration, it will tie for. Uh, first time itself, it got the result good. Otherwise, it will try for five times and it can give the response. In between, it will set the safety guidelines, sanitation check at the input and sanitation check at the output. Everything will happen. And memory, all this preferences will be stored here, so the agent stores the conversation history,
updates user preferences, everything. OK, suppose if the say, if I give you one some task, like, for example, the user ask. Book. Give me a flight. to Genai. Next to Fri, next Fri Friday. Under. Rupees 8000. Okay, if this is the query, if I tell an agent, this is a booking, flight booking agent, and I'm asking, book me a flight. So from Bangalore to Chennai on next Friday under rupees 8000. So
what it will has to do, it has to extract the entities, extract the entities. Bangalore. And do Genai, and either what is the other entity? Tell me what are all the entities that should be extracted here.

**ARUN SINGH SHAH** [01:28:39]: Date, time.

**AKANKSHA SHRIVASTAVA** [01:28:39]: Friday.

**Bharathi R** [01:28:40]: Very good. Date, time also, because the time is not given, so it has to ask the time because they and also the budget, right? Budget also. Then the routing is given a set of tools. We have to already we would have given

**ARUN SINGH SHAH** [01:28:51]: Yes.

**Bharathi R** [01:28:56]: some set of tools to the agent. It has to pick the travel booking tool, right? For example. And reasoning is what it has to break the goals into steps. What is that it has to look for the flights where the ticket cost is 8000. Okay, search flights, find that which fare, which flights gives rupees 8000 and on that particular date. So, search again, then choose an option,
then record the user preferences in the memory. OK, and it looks a memory, whether the user has any preferred airline also have flowed in the recent past or in the previous slides and so on, but also it goes and refers, and yes.

**ARUN SINGH SHAH** [01:29:48]: So, ma'am. So, in this example, like when we are saying a book a flight, so book me a flight, so in the reasoning part, like when will be the agent stop reasoning, like, like how we get to know that our goal is achieved in the repeat?

**Bharathi R** [01:30:05]: No, let me write what reasoning, yes, is what it will do reasoning steps.

**ARUN SINGH SHAH** [01:30:11]: Yeah, yeah, the termination point when the RAG agent

**Bharathi R** [01:30:14]: These are the steps, yeah, it will say, look for flight.

**ARUN SINGH SHAH** [01:30:14]: stop.

**Bharathi R** [01:30:23]: On Friday, that is a Friday will be the date might be 30th, okay, 30th October. Okay, and you have to put a constraint. Constraint is look for flight where the flight charges under rupees 8000. Planet. Then, first, you list out all the flights. And filter which are the flight fares are 8000, isn't it? Yes or no? Generally, how do we plan?

**ARUN SINGH SHAH** [01:31:00]: Yeah.

**Bharathi R** [01:31:02]: Same thing, it will do on its own because LLMs has a good reasoning capability, right? It will do.

**ARUN SINGH SHAH** [01:31:09]: Otherwise, keep following the tools and unnecessary.

**Bharathi R** [01:31:12]: That will become a workflow.

**ARUN SINGH SHAH** [01:31:14]: Yeah.

**Bharathi R** [01:31:17]: We are giving autonomy to the agent itself to select the flight. And book also. See, your workflow will select the flight if you ask when the ChatGPT or a Claude if you ask this person. It will give you the list of flights, isn't it? Which has above 8000 and below 8000, right? It will not book. Agent autonomy is what? It has to go to the next to what it has to go to the,
you know, the particular flight, I mean, the booking website, correct? Booking tool, it has to go. So can you list the tools required for this? What are the tools it requires? It has to look around any common tool is available for Exam, yeah. Flight API.

**ARUN SINGH SHAH** [01:32:22]: Yes, yes.

**Bharathi R** [01:32:22]: We have to search for Flight API. Or we can go for web search also.

**ARUN SINGH SHAH** [01:32:28]: Tabs search.

**Bharathi R** [01:32:30]: Web search. You know, Taveli is a very good web search. It does that. It's a free API. We will be using the Taveli API. Web search it can do. So it will list out all the flights. So once if you identify which flight, you have to go for booking website, correct? That is another API, the tool has to, the agent has to connect, correct. Then it has to connect with booking
what has to go payment. Also, correct? You look completely as an individual, what and all you will do.

**ARUN SINGH SHAH** [01:33:10]: Yes, ma'am. Yes, ma'am.

**Bharathi R** [01:33:17]: Agents has to complete the task. So my question is what? Book me a flight. Look at the intent. Book me a flight. Or simply you are going to block a ticket without giving the card. Or whether you want an agent to list out only the flights. Even if you ask book me a flight to a ChatGPT, you wanted to do it will only list the flight, right? And will give you suggested
flights on that day, correct? Will that will the ChatGPT will book you?

**ARUN SINGH SHAH** [01:34:01]: No, no.

**Bharathi R** [01:34:02]: No, even if you ask the same question, book me a flight to Chennai next Friday under rupees 8000, even if you ask the same question, it will identify, filter out the flights and it will tell the portal, these are all the portals where you can go and book the flight. It will not say no, it will give you one answer, definitely a related answer. But agent, we are, we want
to build an agent which can do a task. Literally, booking means it has to book. Other LLMs, I mean the chat chat bots will tell you how to do. Here, do, do a task. That's a difference. Some more responses, what is that in the? Ohh. No, no, we will learn a generic framework, Land Graph, ADK, or Crew AI. We will use, we will, for demonstration, we can use any, we'll study all of these things.
Actually, is it share to share financial details? That is what the, you know, the, you know, the objective, but still it is not full autonomy is not given. That's why I said the level of autonomy. No, as of to my knowledge, you know, financial transaction is still happening. Complete autonomy is not given. I just booking a flight. I gave an example. We have no one has given a full autonomy to do
the financial transactions, literally speaking. Vishant. Yeah, level of autonomy, we can, we are going to take a call on that. See, given the tools only, it can take and see, given the list of tools and list of APIs and that is on our hand, right? If you share everything, then it will be actually, uh, it's a burden on us. So literally speaking, no one has, I mean, initiated the financial
transactions with the agent. That is actually, as of now, I don't think so. No one is confident on that.

## Segment 047  [01:36:56 - 01:37:58]
Slide: slides/slide_047.jpg

**Bharathi R** [01:36:57]: So this is what I said. See the three and four will have get a react loop repeat until the goal is met. Okay, and this is what the flow actually requests, routing, reasoning, tool invocation, and response. So, the memory and the safety is and like it will come at every point. Okay, so only stages three and four form a loop, a simple question can skip through. Tools
straight can go to the response. So if you ask a very simple question, it will no need of going for this reasoning into invocation directly. It will go to give the response. So this is not a, you know, the definite cycle. It's a numbering. These are all the components, I mean, the stages required to build an agent, and this is the real, the picture. Seven stages, how this is the agent lifecycle
will happen. So now you can see one lifecycle banking agent.
