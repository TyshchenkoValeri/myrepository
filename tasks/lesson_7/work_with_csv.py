import os
import pickle


def counter(file_path):
    dct = {}
    size = 0
    longest_filename_len = 0
    min_size = float('inf')
    shortest_filename_len = float('inf')
    largest_file = ''
    smallest_file = ''
    shortest_filename_len_path = ''
    longest_filename_len_path = ''
    file_path = file_path if os.path.exists(file_path) else '/'
    pickled = []
    if os.path.exists('data.pkl'):
        with open('data.pkl', 'rb') as f:
            loaded = pickle.load(f)
            dct = loaded['result']
            pickled = loaded['paths']
        os.remove('data.pkl')
    try:
        for dirpath, dirnames, filenames in os.walk(file_path, topdown=True):
            dct['dir_count'] = dct.get('dir_count', 0) + len(dirnames)
            dct['file_count'] = dct.get('file_count', 0) + len(filenames)
            if dirpath not in pickled:
                for filename in filenames:
                    full_path = os.path.join(dirpath, filename)
                    file_size = os.stat(full_path).st_size
                    if file_size > size:
                        size = file_size
                        largest_file = full_path
                    if file_size < min_size:
                        min_size = file_size
                        smallest_file = full_path
                    if shortest_filename_len > len(filename):
                        shortest_filename_len = len(filename)
                        shortest_filename_len_path = full_path
                    if longest_filename_len < len(filename):
                        longest_filename_len = len(filename)
                        longest_filename_len_path = full_path
                dct['largest_file_size'] = largest_file
                dct['smallest_file_size'] = smallest_file
                dct['longest_filename'] = longest_filename_len_path
                dct['shortest_filename'] = shortest_filename_len_path
                pickled.append(dirpath)
    except KeyboardInterrupt as e:
        with open('data.pkl', 'wb') as f:
            pickle.dump({'result': dct,
                         'paths': pickled}, f)
    return dct

