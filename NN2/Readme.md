ALL CODE IS ON GOOGLE COLLAB!!!

The model's performance on the prompts was very interesting. Sometimes the prompt was answered very nicely and make sense as if a human were writing it. However, sometimes the prompt was answered very poorly and did not make much sense or brought up irrelevant information. Also the model would use very toxic words. The negative responses tend to have a lot of hateful and toxic words whereas the positive responses are actually positive like using the word love a lot.

Toxicity definition: In the context of the internet, toxic behavior refers to negative and harmful actions, such as online harassment, cyberbullying, or the spread of hate speech. Some examples of this could include the words, hate, kill, die, etc.

Non-toxic behavior suggests something that is positive. There are no words like hate, die, kill etc there are words in place of that such as passed away, dislike, or murder.

I updated the make_non_toxic function to only replace whole words so if word1 was 'hate' and the response included the word 'whatever' instead of outputing 'w***ver' it now outputs whatever.

The toxicity scores are as follows:

Toxic score: 0.29905733466148376
Severe toxic score: 0.0005713753052987158

This is less than the threshold of 0.3 so it passed the test!