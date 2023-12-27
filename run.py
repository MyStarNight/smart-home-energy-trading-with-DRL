import HEMS
manager = HEMS.HEMS()
manager.train()
manager.save('saved_nets/my_net')
manager = HEMS.HEMS(load=True, path='saved_nets/my_net')
manager.test()