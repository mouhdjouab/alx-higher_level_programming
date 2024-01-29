#!/usr/bin/python3
"""Finds  peak in a list """


def find_peak(list_of_integers):
    """Finds  peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    loo = 0
    lnhi = len(list_of_integers)
    mid_ra = ((lnhi - loo) // 2) + loo
    mid_ra = int(mid_ra)
    if lnhi == 1:
        return list_of_integers[0]
    if lnhi == 2:
        return max(list_of_integers)
    if list_of_integers[mid_ra] >= list_of_integers[mid_ra - 1] and\
            list_of_integers[mid_ra] >= list_of_integers[mid_ra + 1]:
        return list_of_integers[mid_ra]
    if mid_ra > 0 and list_of_integers[mid_ra] < list_of_integers[mid_ra + 1]:
        return find_peak(list_of_integers[mid_ra:])
    if mid_ra > 0 and list_of_integers[mid_ra] < list_of_integers[mid_ra - 1]:
        return find_peak(list_of_integers[:mid_ra])
