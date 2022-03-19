# Phonebook
Input: text file consisting of N lines. Each line contains a Name and Phone Number separated by a comma.

Phone numbers are unique to a text file. Names may be repeated.
After starting the program, the user can enter search data into the console.

Examples:
+79876543290 - At the exit we expect 1 last name or a message that there are none.
Sokolov - At the exit, we expect a list of numbers or a message that they are not.
+79867* - List of names
Juice* - phone list.
+79867* Juice* - all intersections

Necessary:
A basic level of:
Upload the file to the program.
Search for all duplicate names
Implement a name lookup for a given phone number.
Search for all numbers by given name.

Lvl 2 - It is necessary to use a prefix tree, there can be only one wildcard symbol and the line ends with it:
Search for names by wildcard phone.
Phone search by Wildcard last name

Lvl 3 - You must use regular expressions, there can be several wildcard characters:
Search for all intersections by wildcard phone number + last name.
