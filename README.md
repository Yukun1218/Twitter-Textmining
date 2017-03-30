# Twitter-Text-mining
Use Twitter Streaming API to collect tweets that contain certain words and hashtag
The file contains 4 parts: 1. twitter_streaming.py, which is used to build up API handshake and start collect raw data
                           2. TweeterAnalysisWordCloud.ipynb, which is used to clean and analyze the raw data and generate word cloud to see what are people talking about when they tweet "(#)youth" and "(#)youthleadership".
                           3. Results: include descending order most frequent words in excel and text format, and worldcloud picture.
                           4. Additional: a piece of code help remove the retweets if needed; a concatenate code used to pin two pieces of data together, when your streaming api stoped working, which happened several times for me. 
