def left_join(dic, dic_two):
    output = []
    if dic.size < 1:
        return output
    else:
        for bucket in dic.bucket:
            # print(key)
            if bucket == None:
                pass
            else:
                if dic_two.contains(bucket.key):
                    antonym = dic_two.get(bucket.key)
                    output.append((bucket.key, bucket.value, antonym))
                else:
                    output.append((bucket.key, bucket.value, None))
        return output

