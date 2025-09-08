def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    singers = list(map(int, data[1:1+n]))
    
    freq_dict = {}
    for singer in singers:
        if singer in freq_dict:
            freq_dict[singer] += 1
        else:
            freq_dict[singer] = 1
            
    max_count = 0
    for count in freq_dict.values():
        if count > max_count:
            max_count = count
            
    count_fav = 0
    for count in freq_dict.values():
        if count == max_count:
            count_fav += 1
            
    print(count_fav)

if __name__ == "__main__":
    main()