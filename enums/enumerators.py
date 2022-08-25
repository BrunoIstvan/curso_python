from enum import Enum
from pprint import pprint
import enum



class ResponseStatus(Enum):
    # in progress
    IN_PROGRESS = 1 
    REQUESTING = 1              # alias de IN_PROGRESS
    PENDING = 1                 # alias de IN_PROGRESS

    # success
    SUCCESS = 2
    OK = 2                      # alias de SUCCESS
    FULFILLED = 2               # alias de SUCCESS

    # error
    ERROR = 3
    NOT_OK = 3                  # alias de ERROR
    REJECTED = 3                # alias de ERROR


# aqui so serão exibidos os valores principais e não os seus aliases
for rs in ResponseStatus:
    print(rs)


# aqui sim é possível ver todos os membros do enumerador
pprint(ResponseStatus.__members__)


# é possível fazer a busca pelos aliases
code = 'OK'
if ResponseStatus[code] is ResponseStatus.SUCCESS:
    print('The request completed successfully')

code = 'FULFILLED'
if ResponseStatus[code] is ResponseStatus.SUCCESS:
    print('The request completed successfully')

# ************************************************************************************************

try:
    # Essa anotação impedirá que haja aliases dentro do enumerador
    @enum.unique 
    class Day(Enum):
        MON = 'Monday'
        TUE = 'Monday'
        WED = 'Wednesday'
        THU = 'Thursday'
        FRI = 'Friday'
        SAT = 'Saturday'
        SUN = 'Sunday'
except ValueError:
    print('erro capturado por conta de enumerador de um alias e está usando a anotação que valida isso')

# ************************************************************************************************
# criando métodos para o enumerador

from functools import total_ordering


@total_ordering
class PaymentStatus(Enum):
    PENDING = 1
    COMPLETED = 2
    REFUNDED = 3

    def __str__(self):
        return f'{self.name.lower()}({self.value})'

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other

        if isinstance(other, PaymentStatus):
            return self is other

        return False

    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < other

        if isinstance(other, PaymentStatus):
            return self.value < other.value

        return False

    def __bool__(self):
        if self is self.COMPLETED:
            return True

        return False


# uso do __str__
print(PaymentStatus.PENDING)

# uso do __eq__
if PaymentStatus.PENDING == 1:
    print('The payment is pending.')

# uso do __lt__
status = 1
if status < PaymentStatus.COMPLETED:
    print('The payment has not completed')

# uso do __lt__
status = PaymentStatus.PENDING
if status >= PaymentStatus.COMPLETED:
    print('The payment is not pending')

# uso do __bool__
for member in PaymentStatus:
    print(member, bool(member))

# ************************************************************************************************
# usando auto()

'''
By default, the _generate_next_value_() generates the next number in a sequence of integers starting from one. However, Python may change this logic in the future.

It’s possible to override the _generate_next_value_() method to add a custom logic that generates unique values. If so, you need to place the _generate_next_value_() method before defining all the members.

The following shows how to override the _generate_next_value_() method to generate values for members by using their names:
'''
from enum import Enum, auto


class State(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    PENDING = auto()
    FULFILLED = auto()
    REJECTED = auto()


for state in State:
    print(state.name, state.value)

# ************************************************************************************************



# ************************************************************************************************



# ************************************************************************************************



# ************************************************************************************************



# ************************************************************************************************



# ************************************************************************************************