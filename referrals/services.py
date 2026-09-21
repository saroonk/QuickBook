from collections import deque

from accounts.models import User


def find_placement(referrer):
    queue = deque([referrer])

    while queue:
        parent = queue.popleft()

        if not User.objects.filter(
            referred_by=parent,
            position="left"
        ).exists():
            return parent, "left"

        if not User.objects.filter(
            referred_by=parent,
            position="right"
        ).exists():
            return parent, "right"


        children = User.objects.filter(
            referred_by=parent
        ).order_by("id")

        queue.extend(children)

    return None, None




def get_root_user(user):
    while user.referred_by:
        user = user.referred_by

    return user


def get_team_counts(user):
    left_count = 0
    right_count = 0

    def count_descendants(parent):
        count = 1

        children = User.objects.filter(referred_by=parent)

        for child in children:
            count += count_descendants(child)

        return count

    left_user = User.objects.filter(
        referred_by=user,
        position="left"
    ).first()

    right_user = User.objects.filter(
        referred_by=user,
        position="right"
    ).first()

    if left_user:
        left_count = count_descendants(left_user)

    if right_user:
        right_count = count_descendants(right_user)

    return {
        "left_count": left_count,
        "right_count": right_count,
    }