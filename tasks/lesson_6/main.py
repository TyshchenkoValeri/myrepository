from change_element_pos import change_list_element_position
from home_task_5 import sum_range
from prime_numbers import is_prime
from sequence_to_dict import to_dict
from square_calculation import square
from exact_degree_of_two import exact_degree_of_two

if __name__ == '__main__':
    lst = ["Age", 33, "Name", "Valeriia", 4, 5]
    print(to_dict(lst))
    print(is_prime(5))
    print(change_list_element_position([1, 2, 3, 4]))
    print(sum_range(5, 1))
    print(square(4))
    print(exact_degree_of_two(4))
