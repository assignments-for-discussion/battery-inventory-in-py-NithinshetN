# Bucketing Batteries

Let's say we have a bunch of batteries. 
As batteries get used, they get charged and re-charged. In other words, they undergo charging-cycles.
After many charge-cycles, batteries lose their capacity to store charge.

We want to group and count our batteries, according to the number of charge-cycles they have undergone. This can be useful to predict how many we would need to replace in the near future.

## Battery Counting

We need to classify the charge-cycles as 'high', 'medium', 'low'
and count the number of batteries in each classification.

Batteries are classified as follows:

- charged less than 310 times: classified as `low`
- charged between 310 and 929 times: classified as `medium`
- charged 930 times or more: classified as `high`

The code in this repository has a function that needs to count the number of low, medium and high usage batteries. However, this function is not yet implemented.

There is also a test function in the code.
Read the test to find out what's expected from the code.
Of course, the test fails now, since the function isn't implemented.

Implement the function to count correctly and pass the test.

## Evaluation Criteria

- Readability: including variable names, code-flow, useage of comments only when necessary
- Improvements to existing code and tests
- Precision: adding new tests (such as boundary conditions)
