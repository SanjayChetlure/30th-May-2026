#Module3: AnimalAndBird

print("---------------Apr1----------------")

import Animal
import Bird

print("--call Animal module contents---")
Animal.fly()
Animal.colour()

print("--call Bird module contents---")
Bird.fly()
Bird.colour()



print("---------------Apr2--------------")

from Animal import colour,fly
colour()
fly()

print("-----")

from Bird import colour,fly
colour()
fly()


print("------import all contents using 2nd Apr-----")
from Bird import *
colour()
fly()




