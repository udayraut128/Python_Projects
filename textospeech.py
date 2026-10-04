from gtts import gTTS

text =  '''
There was a young boy named Leo who lived in a small village near a huge mountain.
Every morning, he looked at the mountain and dreamed of reaching the top.
One day, he decided to climb it.
He started early in the morning.
After a few hours, his legs became tired.
The path became difficult, and the weather became cold.
Leo wanted to go back.
Then he looked up and saw the sunlight shining over the mountain.
He took a deep breath and said,
“I have come this far. I can take one more step.”
So he continued.
One step became ten steps.
Ten steps became a hundred.
Finally, after many hours, Leo reached the top.
He looked at the village below and smiled.
The mountain had not become smaller.
Leo had become stronger.
He understood that the biggest challenge was not the mountain.
It was the voice inside him saying, “You can't do it.”

The Lesson
Sometimes, the goal is difficult because it is meant to make you stronger.
Don't be afraid of the mountain in front of you. Take one step, then another, and keep going.
Every big achievement begins with one small step.

'''

tts =gTTS(text=text,lang="hi")

tts.save("voicene.mp3")

print("audio saved")