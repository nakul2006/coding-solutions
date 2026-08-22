# Digit Frequency

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string, $s$, consisting of alphabets and digits, find the frequency of each digit in the given string.

**Input Format**

The first line contains a string, $num$ which is the given number.

**Constraints**

$ 1 \le len(num) \le 1000$  
All the elements of num are made of english alphabets and digits.


**Output Format**

Print ten space-separated integers in a single line denoting the frequency of each digit from $0$ to $9$.

## Solution

**Language:** C  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-22T10:40:54.381Z  

```c
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    char s[1000];
    int freq[10] = {0};

    scanf("%s", s);

    for(int i = 0; s[i] != '\0'; i++)
    {
        if(s[i] >= '0' && s[i] <= '9')
        {
            freq[s[i] - '0']++;
        }
    }

    for(int i = 0; i < 10; i++)
    {
        printf("%d ", freq[i]);
    }

    return 0;
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/frequency-of-digits-1/problem)