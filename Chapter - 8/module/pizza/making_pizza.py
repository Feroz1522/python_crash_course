# 1 | method for importing module 
import pizza
pizza.make_pizza('feroz','cheesy','spicy','tendery')

# 2 | method for importing module 
from pizza import make_pizza
#we dont need to use . dot operation for calling the function
make_pizza('anwar','mexican flavour','oily')

# 3 | method for importing module by alias
import pizza as p
p.make_pizza('kathir','barbique','chrispy','dry')

# 4 | method for importing all function from module
from pizza import *
make_pizza('jones','tendery','spicy','salady')


