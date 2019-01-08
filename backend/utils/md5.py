import hashlib
import random
import string


def gen_md5(*str_args):
    return hashlib.md5("".join(str_args).encode('utf-8')).hexdigest().upper()

def gen_params_str(dict_args):
    secret = "LYSCSZF088888967"
    key_sort = sorted(dict_args.keys())
    sign_content = secret
    for i in key_sort:
        sign_content += i + dict_args[i]

    new_sign_content = sign_content + secret

    return new_sign_content

def gen_random_string(str_len):
    return ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(str_len))