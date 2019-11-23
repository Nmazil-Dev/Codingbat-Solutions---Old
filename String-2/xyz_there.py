def xyz_there(str):
    count = 0
    if '.xyz' in str:
        return False
    if 'xyz' in str and not '.xyz' in str:
        count += 2
    if count > 0:
        return True
    elif count <= 0:
        return False
xyz_there('xyz.abc.xyz')