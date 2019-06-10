# from collections import deque
#
#
# def search(lines,pattern,history=5):
#     previous_lines=deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line,previous_lines
#         previous_lines.append(line)
#
#
#
# if __name__=='__main__':
#     with open('somefile.txt') as f:
#         for line,prevlines in search(f,'python',5):
#             for pline in prevlines:
#                 print(pline,end='')
#             print(line,end='')
#             print('-'*20)

# a=9;i=0;print(a,i)

#协程
# def print_matches(matchtext):
#     print("Looking for",matchtext)
#     while True:
#         line=(yield )
#         if matchtext in line:
#             print(line)
#
# matcher=print_matches('python')
# matcher.__next__()
# matcher.send("Hello World")
#
# # matcher.__next__()
# matcher.send("Python is cool")
# matcher.close()

for i in range(10,0,-1):
    print(i)