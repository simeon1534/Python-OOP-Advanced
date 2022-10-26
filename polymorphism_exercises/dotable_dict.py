import collections


class DotableDict(dict):

    def __getitem__(self, items):
        # val = dict.__getitem__(self, item)
        list_items = items.split('.')
        if len(list_items) == 1:
            try:
                val = dict.__getitem__(self, items)
                return val
            except KeyError:
                return 'Bad Key'
        else:
            outermost = None

            for item in list_items:
                try:
                    iter(item)

                    if outermost is None:
                        outermost = dict.__getitem__(self, item)

                    else:
                        outermost = outermost.__getitem__(item)


                except TypeError:
                    print(item, 'is not iterable')
                    outermost = outermost.__getitem__(item)
                except KeyError:
                    print('I need valid keys')
                    break
                except AttributeError:
                    return outermost
            return outermost


basic_d = {'x': 1,
           'y': {'z': {'a': 8}},
           'p': 5
           }

d = DotableDict(basic_d)
print(basic_d['y']['z'])
print(d['y.z'])
