#!/usr/bin/env python3
"""Defines users service functions"""
from api.models.group import Group


def find_groups(user):
    """Find groups for a student or a tutor"""
    if user.role == 'tutor':
        groups = Group.objects(tutor=user)
    else:
        groups = Group.objects(students=user)

    return groups


def create_group(tutor, args):
    """Creates new group"""
    existing = Group.objects(name=args.get('name'), tutor=tutor)
    if existing:
        return None
    group = Group(
        name=args.get('name'),
        description=args.get('description'),
        tutor=tutor,
    )
    group.save()
    return group


def update_group(tutor):
    """"""
    pass


def delete_group(tutor):
    pass
