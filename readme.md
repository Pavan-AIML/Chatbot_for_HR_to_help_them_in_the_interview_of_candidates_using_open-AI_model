<h1> Creating a chatbot to help HR in recruiting the people <h1>

<h2> Getting to know about all the model parameters <h2>
- Creating the prototypes of the chatbot
- taking the Help of Chatgpt playground for the choosign and testing of models and other settings.
- Max tokens -: Allowing us to setup the max tokens allowed.
- Stop Sequence -:These are strings that tell model when to stop generating 
unnecessary text.

Ex- : Let me know if you have anymore questions., I hope this helped you. Goodbye.
- Top P - Nucleus Sampling -: Determines the smallest set of probable outcomes whose combined probability sums to given threshold. (It controls the randomness of the response.)

Ex -: Lets seay we asked the question Th sky is then Top P will be having a list and the model will choose the words as per teh setting of temperature. If the temperature is higher then the model is equaliy likely to choose any word from the list can be aslo word with less probability but if the temperature is less then model will choose to pick the higher probable words from Top -P list.

- Frequency penality -: Reduces the model's liklihood of repeating the same line or phrase.

- Presence penality -: Encourages the model to introduce new topics by penalizing the presence of already-mentioned tokens.

<h2>Optimizing the temperature and top p for different use casese.<h2>