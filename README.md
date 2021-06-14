# how-to-read-RMB-numbers-
Convert float numbers to corresponding RMB characters
In China, when writing RMB(the official currency) amounts, there is a specific Chinese character for each number (0-9), 
and the total amount is divided into four-digit sections, as the Chinese use "10 thousand" and "100 million" as units.
This program shows how to read any amount under 100 billion in RMB characters.
The decimal part is rounded up to 2 digits, however,
Any amount less than 1 RMB yuan will not be rounded up to 1 yuan, e.g. 0.999 is 0.99 rather than 1.
