# Leetcode-1921-Just-Coding...
A question asking for how many monsters you can eliminate before being eliminated. 
You are given the distance and speed of monsters, thus you can calculate the time it takes for them to arrive individually and store those in a sorted array, time

After a complex initialization (can be improved), I got the number, the days (or seconds), and tested for several times. Making all the conditions debugged, it ran correctly.

One stupid thing I did is initializing a variable to represent the days. In fact, the index of the time elements is their arriving days, or days+1. That part took me some time since 
I got too many variables to conciliate among.
