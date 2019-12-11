# The collections which we will study in python collections module are:
# OrderedDict
# defaultdict
# counter
# namedtuple
# deque

# OrderedDict

from collections import OrderedDict

roll_no=OrderedDict([
    (11,"Shubham"),
    (9,"Pankaj"),
    (17,"Jounaldev"),
    (11,"Sharad")

])
for key,value in roll_no.items():
    print(key,value)


