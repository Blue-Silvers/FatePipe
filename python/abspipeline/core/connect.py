import shotgun_api3
from abspipeline.conf.__env import credentials


sg = None

def get_sg(do_new = False):
    '''
    Gets a SG connection

    Args:
        do_new:

    Returns:

    '''
    global sg

    if do_new: # TODO : better implementation - should set sg if not connection exist
        print("[sgtest] Creating new SG connection")
        return shotgun_api3.Shotgun(**credentials)

    if not sg:
        print("[sgtest] Creating SG connection")
        sg = shotgun_api3.Shotgun(**credentials)

    return sg

if __name__ == "__main__":

    sg = get_sg()
    print(sg)

    sg2 = get_sg()
    print(sg2)

    sg3 = get_sg(do_new = True)
    print(sg3)