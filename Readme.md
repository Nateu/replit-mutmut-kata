# Mutmut kata

This kata is created by me to learn more about combining unit testing and mutation testing to enhance TDD learnings.

Basic idea of TDD is that we do as little as possible as we wirte our test (RED), write the code (GREEN) and refactor; but at any given time we should not introduce code that isn't strictly needed.
This gave me the idea of using mutation testing to double check that we didn't introduce code that is not tested.  

## What you should do
Implement each task of the todo list below by doing the following:

1. Plan your first part of the feature; think baby steps and minimal change whilst still adding value.
2. Write the test that will check your future increment.
3. Implement the minimal code needed to get the test to pass.
4. When green; check for failures in the mutation tests.
5. Refactor if needed the code making sure you  
  a) keep the unit test green  
  b) you improve the code so the mutant won't show up

# To-Do-List

1. Make a list with 5 chores  
  Clean the rain gutters  
  Buy the groceries  
  Walk the dog  
  Make diner  
  Spoil the spouse  

2. The list should be prioritized in a way that older items are at the top 
3. Create a way to indicate that a chore is depending on another
4. Dependencies should change the the prioritization; the thing that needs to go first will have to be before the others

### Why I use Makefiles
* Another reason: [python path issues](https://stackoverflow.com/questions/54895002/modulenotfounderror-with-pytest)

### Replit issue with python repls
When you get errors on virtualenv or setuptools run this:

```
pip install -U virtualenv setuptools
```
