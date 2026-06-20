# Longest Print
How to make print take extremely long.

## Rules
### 1. No pointless waiting 
No `time.sleep()`, infinite loops, or idle waiting. 
Anything that takes time must produce some output or perform an actual operation.

### 2. No Repeat
If a specific method (like translation) is used, it cannot be reused within the same run.

### 3. Is for print 
Action must be connected to print **IN ANY WAY!!!**

## Functions
### Translate
Program request on Google Translate to translate to `de, cs, en, pl, ja, zh-TW`

Time Spend: 1.286928s

### W/R to File
Write to file printed text and then Read from same file.

Time Spend: 0.000376s

### For in For loop print
Simulates typing by looping through all printable characters until a match is found for each letter.

Time Spend: 0.000050s

### GC
Force call of garbage collector

Time Spend: 0.006044s

**Note:** it doesn't brake [Rule 3](#3-is-for-print) because it clears RAM after **print**.


