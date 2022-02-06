# https://1o24bbs.com/t/topic/10033

# /**
# * # Step 1
# * Throughout this interview, we'll pretend we're building a new analytical
# * database. Don't worry about actually building a database though -- these will
# * all be toy problems.
# *
# * Here's how the database works: all records are represented as maps, with string
# * keys and integer values. The records are contained in an array, in no
# * particular order.
# *
# * To begin with, the database will support just one function: min_by_key. This
# * function scans the array of records and returns the record that has the minimum
# * value for a specified key. Records that do not contain the specified key are
# * considered to have value 0 for the key. Note that keys may map to negative values!
# *
# * Here's an example use case: each of your records contains data about a school
# * student. You can use min_by_key to answer questions such as "who is the youngest
# * student?" and "who is the student with the lowest grade-point average?"
# *
# * Implementation notes:
# * * You should handle an empty array of records in an idiomatic way in your
# * language of choice.
# * * If several records share the same minimum value for the chosen key, you
# * may return any of them.
# /**
# * # Step 2
# * Our next step in database development is to add a new function. We'll call this
# * function first_by_key. It has much in common with min_by_key. first_by_key
# * takes three arguments:
# *
# * 1. a string key
# * 2. a string sort direction (which must be either "asc" or "desc")
# * 3. an array of records, just as in min_by_key.
# *
# * If the sort direction is "asc", then we should return the minimum record,
# * otherwise we should return the maximum record. As before, records without a
# * value for the key should be treated as having value 0.
# *
# * Once you have a working solution, you should re-implement min_by_key in terms
# * of first_by_key .

# /**
# * # Step 3
# * As we build increasingly rich orderings for our records, we'll find it useful
# * to extract the comparison of records into a comparator. This is a function or
# * object (depending on your language) which determines if a record is
# * "less than", equal, or "greater than" another.
# *
# * In object-oriented languages, you should write a class whose constructor
# * accepts two parameters: a string key and a string direction. The class should
# * implement a method compare that takes as its parameters two records. This
# * method should return -1 if the first record comes before the second record
# * (according to key and direction), zero if neither record comes before the
# * other, or 1 if the first record comes after the second.
# *
# * In functional languages, you should write a function which accepts two
# * parameters: a string key and a string direction. The function should return
# * a function that takes as its parameters two records. This function should return
# * -1 if the first record comes before the second record (according to key and
# * direction), zero if neither record comes before the other, or 1 if the first
# * record comes after the second.
# *
# * You should then use your comparator in your implementation of first_by_key.
# */
# * # Step 4. check 1point3acres for more.
# *
# * Time to take this "first-by" functionality further, to sort by more than one
# * key at a time.
# *
# * Consider an array of records like this one:
# * ```
# * [{"a": 1, "b": 1}, {"a": 1, "b": 2}, {"a": 2, "b": 1}, {"a": 2, "b": 2}]
# * ```
# *
# * Using first_by_key with this array of records with key "a" might not give us as
# * much control as we'd like over the result, since more than one record has the
# * same value for "a" (similarly for "b"). More generally, we might say "order by
# * the first key, in the first direction. Break ties according to the second key,
# * in the second direction. Break remaining ties by the third key, in the third
# * direction, and so on." Note that the sort direction for different keys need not
# * be the same.
# *
# * We might represent this ordering with a list of pairs like
# * ```
# * [
# * ("a", "asc"),
# * ("b", "asc"),
# * ("c", "desc"),
# * ]
# * ```
# *
# * We'll call this type of representation a sort_order.
# *
# * You'll need to write a function first_by_sort_order. It takes two arguments:
# *
# * * a sort_order
# * * an array of records
# *
# * It returns the first record according to the given sort_order.
# *
# * As before, we'll ask that you re-implement your previous functionality
# * (first_by_key) in terms of first_by_sort_order.
# *
# * Hint: can you construct a "sort order" comparator using your comparator from
# * the previous step? How might constructing a sort order comparator be helpful?
# * ```
# *
# * ### Examples (in Python):
# * ```
# * assert(
# * first_by_sort_order(
# * [("a", "desc")],
# * [{"a": 5.0}, {"a": 6.0}],
# * ) == {"a": 6.0}
# * )
# *
# * assert(
# * first_by_sort_order(
# * [("b", "asc"), ("a", "asc")],
# * [{"a": -5, "b": 10}, {"a": -4, "b": 9}],
# * ) == {"a": -4, "b": 9}
# * )
# *
# * assert(
# * first_by_sort_order(
# * [("b", "asc"), ("a", "asc")],
# * [{"a": -5, "b": 10}, {"a": -4, "b": 10}],
# * ) == {"a": -5, "b": 10}
# * )
# * ```
# */

import functools
from typing import List, Dict, Tuple

# Step 1
def min_by_key(key: str, records: List[Dict[str, int]]) -> List[Dict[str, int]]:
    """
    Return the record that has the min value for the key.
    If the key is not in the record the value is 0 for that key.
    """
    if not records:
        return [{}]

    if len(records) == 1:
        return records[0]

    min_i = 0
    for i in range(1, len(records)):
        value = records[i].get(key)
        if value is None:
            value = 0
        min_value = records[min_i].get(key)
        if min_value is None:
            min_value = 0
        if value < min_value:
            min_i = i
    return records[min_i]


assert min_by_key("a", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 1, "b": 2}
assert min_by_key("a", [{"a": 2}, {"a": 1, "b": 2}]) == {"a": 1, "b": 2}
assert min_by_key("b", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 2}
assert min_by_key("a", [{}]) == {}
assert min_by_key("b", [{"a": -1}, {"b": -1}]) == {"b": -1}

# Step 2
def first_by_key(
    key: str, direction: str, records: List[Dict[str, int]]
) -> List[Dict[str, int]]:
    """
    Same as min_by_key but direction (asc, desc) will dictate sort by max or min value.
    """
    if not records:
        return [{}]

    target_i = 0
    for i in range(1, len(records)):
        value = records[i].get(key)
        if value is None:
            value = 0
        target_value = records[target_i].get(key)
        if target_value is None:
            target_value = 0

        if direction == "asc" and value < target_value:
            target_i = i
        elif direction == "desc" and value > target_value:
            target_i = i
    return records[target_i]


def min_by_key_refactor(
    key: str, records: List[Dict[str, int]]
) -> List[Dict[str, int]]:
    return first_by_key(key, "asc", records)


assert min_by_key_refactor("a", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 1, "b": 2}
assert min_by_key_refactor("a", [{"a": 2}, {"a": 1, "b": 2}]) == {"a": 1, "b": 2}
assert min_by_key_refactor("b", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 2}
assert min_by_key_refactor("a", [{}]) == {}
assert min_by_key_refactor("b", [{"a": -1}, {"b": -1}]) == {"b": -1}

assert first_by_key("a", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) in [
    {"b": 1},
    {"b": -2},
]
assert first_by_key("a", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"a": 10}
assert first_by_key("b", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": -2}
assert first_by_key("b", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": 1}
assert first_by_key("a", "desc", [{}, {"a": 10, "b": -10}, {}, {"a": 3, "c": 3}]) == {
    "a": 10,
    "b": -10,
}

# Step 3
class RecordComparator:
    """
    * In object-oriented languages, you should write a class whose constructor
    * accepts two parameters: a string key and a string direction. The class should
    * implement a method compare that takes as its parameters two records. This
    * method should return -1 if the first record comes before the second record
    * (according to key and direction), zero if neither record comes before the
    * other, or 1 if the first record comes after the second.
    """

    def __init__(self, key: str, direction: str):
        self.key = key
        self.direction = direction

    def _get_value(self, record: List[Dict[str, int]]) -> int:
        value = record.get(self.key)
        return value if value is not None else 0

    def compare(
        self, record_a: List[Dict[str, int]], record_b: List[Dict[str, int]]
    ) -> int:
        """
        -1 if recordA comes before recordB
        0 if equal
        1 if recordA comes after record B
        """

        value_a = self._get_value(record_a)
        value_b = self._get_value(record_b)

        if self.direction == "asc":
            if value_a < value_b:
                return -1
            elif value_a == value_b:
                return 0
            else:
                return 1
        elif self.direction == "desc":
            if value_a < value_b:
                return 1
            elif value_a == value_b:
                return 0
            else:
                return -1


def first_by_key_refactor(
    key: str, direction: str, records: List[Dict[str, int]]
) -> List[Dict[str, int]]:
    comparator = RecordComparator(key, direction)
    sorted_records = sorted(records, key=functools.cmp_to_key(comparator.compare))
    return sorted_records[0]


assert first_by_key_refactor("a", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) in [
    {"b": 1},
    {"b": -2},
]
assert first_by_key_refactor("a", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"a": 10}
assert first_by_key_refactor("b", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": -2}
assert first_by_key_refactor("b", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": 1}
assert first_by_key_refactor(
    "a", "desc", [{}, {"a": 10, "b": -10}, {}, {"a": 3, "c": 3}]
) == {
    "a": 10,
    "b": -10,
}

# * You'll need to write a function first_by_sort_order. It takes two arguments:
# *
# * * a sort_order
# * * an array of records
# *
# * It returns the first record according to the given sort_order.
# *
# * As before, we'll ask that you re-implement your previous functionality
# * (first_by_key) in terms of first_by_sort_order.
# *
# * Hint: can you construct a "sort order" comparator using your comparator from
# * the previous step? How might constructing a sort order comparator be helpful?
# * ```


def first_by_sort_order(
    sort_order: List[Tuple[str, str]], records: List[Dict[str, int]]
) -> List[Dict[str, int]]:
    """
    Returns the first record according to the given sort_order.
    """
    sorted_records = records
    for key, direction in reversed(sort_order):
        comparator = RecordComparator(key, direction)
        sorted_records = sorted(
            sorted_records, key=functools.cmp_to_key(comparator.compare)
        )
    return sorted_records[0]


assert (
    first_by_sort_order(
        [("a", "desc")],
        [{"a": 5.0}, {"a": 6.0}],
    )
    == {"a": 6.0}
)
assert (
    first_by_sort_order(
        [("b", "asc"), ("a", "asc")],
        [{"a": -5, "b": 10}, {"a": -4, "b": 9}],
    )
    == {"a": -4, "b": 9}
)
assert (
    first_by_sort_order(
        [("b", "asc"), ("a", "asc")],
        [{"a": -5, "b": 10}, {"a": -4, "b": 10}],
    )
    == {"a": -5, "b": 10}
)
assert (
    first_by_sort_order(
        [("c", "desc"), ("b", "desc"), ("a", "asc")],
        [{"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 3, "c": 5}],
    )
    == {"a": 1, "b": 3, "c": 5}
)

def first_by_key_refactor_again(
    key: str, direction: str, records: List[Dict[str, int]]
) -> List[Dict[str, int]]:
    return first_by_sort_order([(key, direction)], records)

assert first_by_key_refactor_again("a", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) in [
    {"b": 1},
    {"b": -2},
]
assert first_by_key_refactor_again("a", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"a": 10}
assert first_by_key_refactor_again("b", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": -2}
assert first_by_key_refactor_again("b", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": 1}
assert first_by_key_refactor_again(
    "a", "desc", [{}, {"a": 10, "b": -10}, {}, {"a": 3, "c": 3}]
) == {
    "a": 10,
    "b": -10,
}
