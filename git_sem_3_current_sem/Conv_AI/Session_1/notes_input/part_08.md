# Part 08  [01:53:58 - 02:04:28]

## Segment 054  [01:53:58 - 01:55:00]
Slide: slides/slide_054.jpg

**Bharathi R** [01:53:59]: Find me a good Italian restaurant near my office that opens tonight and make a reservation for, so this is the agent. If I close this question with this, find me a good Italian restaurant near my office that opens tonight, this is an LLM task, a ChatGPT, a simple ChatGPT task. But here, an autonomy, I'm giving an autonomy to an agent that agent only can make a
reservation. And the LLM cannot do a reservation on its own. Make a reservation for two at 7 P.m. So this is where the question is to make clear. This is the need of an AI agent. A agent only can do a task. So this is all hypothetical study that how an Agentic system works. So everywhere we have to because you know the testing, the observability,

## Segment 055  [01:55:00 - 01:56:02]
Slide: slides/slide_055.jpg

**Bharathi R** [01:55:02]: building a reliable system is again a big study that we have to do. Now let us do this hands-on, a simple Conversational agent hands-on. Already I have shared the code with you. We'll open here. What is the question is, what is the weather like in Mumbai? So this is also not an complete agent, literally speaking. I'm just asking the question. This is not an agent. This
is actually a. Workflow, OK. Because it is just to extract the location that is the entity it will extract. And the user wants to find the weather, find the weather, it will call the weather API, it receives that, and it will give you the rest part. Okay. Though we call it as an agent, it is not a complete agent. Let me close this and open that code.

## Segment 056  [01:56:02 - 01:57:20]
Slide: slides/slide_056.jpg

**RAGHAVENDRA V** [01:56:03]: Meanwhile, one question I have, like, will we be considering the security also

**Bharathi R** [01:56:05]: Yes, yes, yes.

**RAGHAVENDRA V** [01:56:08]: while designing the Conversational?

**Bharathi R** [01:56:08]: Yes, yes, yes, yes, yes, yes, please, yes, we'll do that.

**RAGHAVENDRA V** [01:56:13]: Thank you.

**Bharathi R** [01:56:15]: So, open when I open this weather agent using quen model. Yes, here. So, whether information agent, so now Python, native Python, and open source Quinn model, it is Quinn, you know, VIMALA.

**AKASH KUMAR JAIN** [01:56:40]: Power.

**RAGHAVENDRA V** [01:56:40]: But we we could still see the CPT on it.

**Bharathi R** [01:56:43]: Yes.

**RAGHAVENDRA V** [01:56:44]: We we could still see the Pgcp only, not the other screen.

**Bharathi R** [01:56:46]: Okay, sorry, sorry, sorry. Yes, here. So you know, VIMALA server, right? So, Olama.com, if you go, can you see that screen?

## Segment 057  [01:57:20 - 01:58:12]
Slide: slides/slide_057.jpg

**SURESH BABU V** [01:57:25]: Yes, ma'am.

**Bharathi R** [01:57:25]: You would have used this, right? Ulama. com. So if you look at this models,

**RAGHAVENDRA V** [01:57:25]: Yeah, yes ma'am, yes ma'am, we can see.

**ARUN SINGH SHAH** [01:57:26]: Yes, yes, yes.

**Bharathi R** [01:57:30]: if you click the models, it will list out. This is an open source, so it will list out all the models. It will tell you what is the model size. You know, the Deepak is 1 million parameters. It can do vision tools thinking. So I have taken, there are many, all models are listed out here. Water down, Olama is giving. You can look, so you can choose by size also. You can
download it. Generally, I was downloading these models, but it takes too much of my resource. Now I'm using a... Collab, and if you want to use a heavy model, you can you please use Prayog Shala, our lab, and you can use it. OK, and now suppose if the user asks, "So, what is the weather like in Mumbai?" So,

## Segment 058  [01:58:12 - 01:59:36]
Slide: slides/slide_058.jpg

**Bharathi R** [01:58:17]: the agent will extract the location that is entity intent classification and entity extraction entity is Mumbai. So the model will understand the Mumbai and it will call the weather API. So we should have given the API, which API I want to use, I can give. So I can give two, three APIs also, two weather API only, two, three APIs. It will choose on its own and it receives
the temperature and it has to get it. So there is a tool called connection. And nothing to do with, because agent here is not doing any reasoning capability, just it does the take the temperature and do give you the. temperature, that's it. So here I have used the QIN 2. 5515B instruct model. This is you can use any model here, model ID. So now. What is the weather like in Mumbai? So now suppose
the stage one, if you look at the stage one, LLMs without tools. So I'm asking if I ask the question. Directly to an LLM, there is no tools attached. No, there is no tool use. If I ask what is the weather like in Mumbai, it will say, I am sorry, I cannot answer this question.

## Segment 059  [01:59:36 - 02:00:42]
Slide: slides/slide_059.jpg

**Bharathi R** [01:59:38]: It says something because the Quinn is giving, this might be a political sensitive, something relates to India, which a country, diverse culture, something, hallucinations, all blah, blah, blah, it is telling. You give some other model without tool access, it will try to give some answer, some kind of and it will try to give. So, Quinn is answering, was answering to me
like this when I ran yesterday. Okay, so if this answer grounded in real current time data, because LLMs itself are stateless. It does not have access to any external information, so now we have to define the tool. So here I'm using open Meteo. This is an open source free. There is no key involved. So here. Tool selections. So now, LLM, LLM decides when to use the tool. This line is important. OK,
suppose when the user, so I will tell this is a system prompt.

## Segment 060  [02:00:42 - 02:01:54]
Slide: slides/slide_060.jpg

**Bharathi R** [02:00:44]: I'm telling the LLMs that. You are a weather information agent. Use the Get Weather tool for any weather question. This is the control we do have. You got it? Use the get weather tool. This, we will tell, and we will use the list of tools also. So do you get this particular question here? This without tool, what happens? LLM will hallucinate. There is no tool connection.
Now I'm giving a tool connection using a JSON script. So this is the thing. So I'm telling a message, role is system, role user. Content is what is the weather like in Mumbai? So it will go and pass all the tool calls. So it will get to whether tool is there and the arguments is the city. The city is a Mumbai. This is a JSON structure. This how this JSON structure, those things we will learn
later. Okay.

## Segment 061  [02:01:54 - 02:03:12]
Slide: slides/slide_061.jpg

**Bharathi R** [02:01:54]: Suppose if the non-weather question comes. Suppose if I am asking, though I am giving the tool also, if I am asking, what is the capital of France? Ml is a good reasoning model. It knows that this is a general answer. The model itself can answer, no need to fetch the tool. It will not call the tools. You can see that tool calls this empty. You understood this one. Number
tool calls is equal to empty, does not call the tool. Whereas when I ask a question for respect to temporary, whether it has the pass tool call, this call is required. Though you have a weather agent, you are building a weather agent, you might ask a general question. It is, what is the capital of France? So there is no tool call happens. Ml decides. For this question, whether I want to access the
tool or not. So this is the actual weather API. Response generation also stage 5. So a complete agent. Definition of weather reagent. OK, and. So what is the weather like in Mumbai? The competence is extract the location

## Segment 062  [02:03:12 - 02:04:00]
Slide: slides/slide_062.jpg

**Bharathi R** [02:03:14]: city Mumbai. It calls the tool get weather and receives that city is Mumbai, country India, temperature is 36. 4 yesterday or day before yesterday, condition is clear sky and so on. Then it responds, current weather in Mumbai is clear sky with temperature. It tells humidity also, level level is so and so on. So you will change the models and observe this. Okay, this is a
simple agent and it is not, the question is not doing any task that the level of liberty is not given to the agent. It only finds the temperature and you ask some other question also. Now I still are running out of time.

## Segment 063  [02:04:00 - 02:04:28]
Slide: slides/slide_063.jpg

**Bharathi R** [02:04:01]: Already I have shared this file. OK, yes, it is in the front. In the beginning only, I shared the two posts. Let us discuss in the next class. Thank you for joining. I mean, the slides are uploaded in the Taxila. You can see that.

**BOLLIGORLA SHEKAR** [02:04:20]: Thank you, Max. We have another class.

**Bharathi R** [02:04:21]: Thank you. Yeah, thank you.

**AMIT KULSHRESTHA** [02:04:23]: Thank you.
