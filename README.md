Input file should contain identifier separated with number of seats. The path to the input file is taken on the command line

For customer satisfaction, I tried to keep all groups together <br>
I put them in the rows in the order they arrive and try to fill each row before moving on to the next row.<br>

If this is not possible for the group, then I try to place them wherever.<br>
This does not backtrack, meaning that the seats are assigned on a first come first serve basis

To run this, you need some form of Python 3 (I used Python 3.10.0, but other versions should work as well)<br>
The command to run this is:
```shell
python theater.py in.txt
```
Here, you can replace in.txt with the path to your input file