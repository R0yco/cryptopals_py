from collections import defaultdict

def main():
    BLOCKSIZE = 16
    INPUT_LEN = 304
    with open("ex_1_8_input.txt","rb") as inputs_file:
        inputs = inputs_file.read().splitlines()
    for input in inputs:
        repeat_counter = defaultdict(int)
        # iterate over 16 byte blocks because we know its aes-ecb128
        for i in range(0, INPUT_LEN, BLOCKSIZE):
            cur_block = input[i:i+16]
            repeat_counter[cur_block] += 1
        for k, v in repeat_counter.items():
            if v > 1:
                print(input)
                break()
if __name__=="__main__":
    main()
