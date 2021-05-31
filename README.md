### PI Number with Collisions

This code has a pygame animation to show how to find the PI number digits with collisions. Given a block with mass = 1kg with speed = 0, and given another block with mass = first_block_mass * pow(100, number_of_digits - 1) with a given speed, when they collide, we count the number of collisions between the two blocks and the block with mass = 1kg and wall, and at the end, when block 1 can not collide with neither block 2 and the wall, the final count represents the number PI, with total digits defined by the number_of_digits variable in block 2 mas calculation.

## Install
On Windows:
```
py -m venv picollisionenv
.\picollisionenv\scripts\Activate
py -m pip install -r requirements.txt

# Run the code
py main.py
```

## References
We can find math explanation about why this happens [here.](https://www.youtube.com/watch?v=HEfHFsfGXjs)

The article about the relation between collisions and number PI [here.](https://www.maths.tcd.ie/~lebed/Galperin.%20Playing%20pool%20with%20pi.pdf)

Code challenge that inspires me to do this python version [here.](https://www.youtube.com/watch?v=PoW8g67XNxA)