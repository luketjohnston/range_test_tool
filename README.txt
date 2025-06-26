Hey Nimit! lmk if you have any questions, I wrote up how to use this below.
I may make it more user friendly at some point and/or add features but right now
it's really basic. 


steps to use

1. make a directory where you will save the range you want to test
2. go to gtowizard, go to a spot you want to test yourself on, click on the 
   "ranges" tab, and there will be a "copy" button in one of the corners of the range.
   In the drop down menu of the copy button, for each action you want to test,
   select "copy" and then paste it into a text file in the directory
   with an identifying name (like "raise19" for example). 
3. Once you have done this for all the actions you want to test (I usually skip "fold"
   but do all the others), then you can just go to the bottom of ranges.py and change 
   it to run "test(<path_to_directory>)"

I've zipped up some example directories to reference.

When testing, it will tell you the spot you're in and the hand you have, and let you 
type something, but it doesn't do anything with the stuff you type. I like to type in
something like "r20f" to indicate raise 20 percent and fold the rest, for example,
but you can just press enter and look at the answer when you have your answer in your mind
too.

If you don't load the "fold" range, then lots of hands will just say "Correct Answer: " 
and then be blank, that means they're all folds. 

