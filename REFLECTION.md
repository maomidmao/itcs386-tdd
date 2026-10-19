# Reflection: TDD Lab (W9)

## 1. How many tests did I write in Part A, and how many lines of production code?
I have 9 tests in test_kitchen.py, and kitchen.py has 41 non-blank lines of
production code. The ratio is about 1 test for every 4.5 lines of production code.
Every behaviour in the class needed its own test, so I wrote more test code
than I expected compared with the amount of real code.

## 2. When was my bar red for the longest time, and what made it last so long?
The bar was red longest in A7 (mixed units). The test needed several changes
before it could pass: a rates dictionary, a rate() method, passing the converter into reduce(), and the real conversion. Until the last change it kept failing with 201 g instead of 228 g. 

## 3. Find one place where you used Fake It, one where you triangulated, and one where you used Obvious Implementation. Looking back, was each choice right?
- **Fake It:** In A1 I made times() return 600, and in A6 plus() returned
  grams(500). This was the right choice, because it proved that the test, the
  import and pytest all worked before I wrote real logic.
- **Triangulate:** In A2 I added a second test (200 x 2 = 400) which a hard-coded
  600 could not pass, so it forced me to write the real multiplication. This was
  the right choice, because I could see exactly why the constant failed.
- **Obvious Implementation:** I used it for __eq__ in A4 and for Sum.times in A8.
  Both were short and I was confident, and neither gave an unexpected red bar,
  so it was the right choice there. It would have been risky for the conversion
  logic in A7, which is why I built that in small steps.

## 4. Which items are still on your test list? Which would you implement next, and which should you delete because they were speculation?
All the items on the original list are done. The one thing I wrote down but did
not do is __hash__: defining __eq__ without __hash__ makes Quantity unhashable, so
it cannot go in a set or be a dictionary key. I would implement it next, but only
if a real use needed it. I would not add speculative extras such as converting
grams back to ounces or handling a missing rate (which currently raises a
KeyError), because nothing in the lab asks for them yet.

## 5. Look at Quantity.reduce. If you had designed the whole system on paper first, would you have written this method?
No, I don't think so. On paper I would probably have written a simple conversion
function. Quantity.reduce only exists because Converter.reduce needed to treat a
Quantity and a Sum in the same way. It is a little odd that a Quantity "reduces"
to itself with a rate, but it keeps Converter simple, so I think the design that
the tests led to is reasonable.

## 6. In Part 0 you wrote the tests after the code, and in Part A before it. How did the two feel different, and which tests shaped your design?
In Part 0 the code already existed, so writing tests felt like checking someone
else's work, and the bug hunt in shipping.py was a clear example of that. In
Part A I had to decide what the code should do before writing it, which felt slow and strange at first, especially Fake It. The tests that shaped my design most were test_multiplication_returns_a_new_quantity, which made me return a new object, and test_mixed_addition, which led to the Converter and the idea of
passing it into reduce().

## Things that went wrong
- I did not notice the instruction to commit after every step in Part 0 until
  I had already committed, so steps 0.1 to 0.7 are combined in the commit before the 0.8 red and green commits.