__author__ = 'ritaotao'

# names = ["annie", "bonnie", "liz", "albonnie", "cjbonnie"]
# names = sorted(names, reverse=True)
#
# values = []
# n = len(names)
#
# for i in range(n):
#     values.append(0)
#     for char in names[i]:
#         values[i] += ord(char)-96
#
# names_new = []
# k = 0
#
# while n >= 1:
#     m = max(values)
#     pos_max = [i for i,j in enumerate(values) if j == m][0]
#     names_new.append(names[pos_max])
#     names.pop(pos_max)
#     values.pop(pos_max)
#     n -= 1
#     if n == 1:
#         names_new.append(names[0])
#         break

######################
# intervals = [[1, 3], [3, 6]]
#
# def answer(intervals):
#     # Input: a list of 2-element lists
#     # Output: an integer of union
#     intervals.sort()
#     # split into starting and ending time of each minion
#     left = [item[0] for item in intervals]
#     right = [item[1] for item in intervals]
#     start = intervals[0][0]
#     end = intervals[0][1]
#     length = 0
#     i = 1
#     while i < len(intervals):
#         if left[i] <= end:
#             if right[i] <= end:
#                 pass
#             else:
#                 end = right[i]
#         else:
#             length += end - start
#             start = left[i]
#             end = right[i]
#         i += 1
#     length += end - start
#     return length
#
# print answer(intervals)

######################
# Inputs:
#     (string) chunk = "lololololo"
#     (string) word = "lol"
# Output:
#     (string) "looo"
#
# Inputs:
#     (string) chunk = "goodgooogoogfogoood"
#     (string) word = "goo"
# Output:
#     (string) "dogfood"

# chunk1 = "aaaabbbb"
# word1 = "ab"
# chunk2 = "goodgooogoogfogoood"
# word2 = "goo"
# chunk3 = "lololololo"
# word3 = "lol"
# chunk4 = "aaaaaaaaaaaaaaaaaaaaaaa"
# word4 = "a"
# def answer(chunk, word):
#     # your code here
#     ls = [chunk]
#     result = []
#     while len(ls) > 0:
#         a = ls[0]
#         for i in range(len(a)):
#             if a[i:(i+len(word))] == word:
#                 b = (a[:i]+a[(i+len(word)):]).replace(word,'')
#                 if word in b:
#                     ls.append(b)
#                 else:
#                     result.append(b)
#         ls.pop(0)
#
#     result.sort()
#     return result[0]
#
# print answer(chunk1,word1)
# print answer(chunk2,word2)
# print answer(chunk3,word3)
# print answer(chunk4,word4)


######################
# Inputs:
#     (int list) digest = [0, 129, 3, 129, 7, 129, 3, 129, 15, 129, 3, 129, 7, 129, 3, 129]
# Output:
#     (int list) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
# Inputs:
#     (int list) digest = [0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165]
# Output:
#     (int list) [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
#

# def answer(digest):
#     message = [0]*len(digest)
#     for i in xrange(0,len(digest)):
#         x = 0
#         while x <= 255:
#             if ((129*x)^message[i-1])%256 == digest[i]:
#                 message[i] = x
#                 break
#             else:
#                 x += 1
#     return message
#
# digest = [0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165]
# print answer(digest)

# ######################
# Inputs:
#     (int list) heights = [1, 4, 2, 5, 1, 2, 3]
# Output:
#     (int) 5
#
# Inputs:
#     (int list) heights = [1, 2, 3, 2, 1]
# Output:
#     (int) 0

#
# def answer(heights):
#     # your code here
#     pos = []
#     lm = []
#     ht = [0]
#     ht.extend(heights)
#     ht.append(0)
#     volume = 0
#     # seek peaks
#     for i in xrange(1,len(ht)-1):
#         if (ht[i-1] - ht[i] < 0) & (ht[i+1] - ht[i] <= 0):
#             pos.append(i-1)
#             lm.append(heights[i-1])
#     j = 1
#     while j < len(pos)-1:
#         if (lm[j] <= lm[j-1]) & (lm[j] <= lm[j+1]):
#             pos.pop(j)
#             lm.pop(j)
#             j = 1
#         else:
#             j += 1
#     volume = 0
#     for k in xrange(0,len(pos)-1):
#         m = min(lm[k],lm[k+1])
#         for l in xrange(pos[k]+1,pos[k+1]):
#             droplet = m - heights[l]
#             if droplet >= 0:
#                 volume += droplet
#     return volume
#     # htt = heights[:]
#     # for j in xrange(0,len(pos)):
#     #     for k in xrange(pos[j]+1,pos[j+1]):
#     #         htt[k] = min(heights[pos[j]], heights[pos[j+1]])
#     #         print k,htt[k]
#     # return htt
#
#
#     # volume = 0
#     # for i in xrange(1, max(heights)+1):
#     #     ls = [j for j in xrange(0, len(heights)) if heights[j] >= i]
#     #     volume += ls[-1] - ls[0] + 1
#     # volume -= sum(heights)
#     # return volume
#
#
# heights = [1, 4, 2, 5, 1, 2, 3]
# heights1 = [1, 2, 3, 2, 1]
# print answer(heights1)



# """
# Implement an HTTP web server in Python that knows how to run server-side
# CGI scripts coded in Python;  serves files and scripts from current working
# dir;  Python scripts must be stored in webdir\cgi-bin or webdir\htbin;
# """

# import sys
# import BaseHTTPServer
# from SimpleHTTPServer import SimpleHTTPRequestHandler
#
#
# HandlerClass = SimpleHTTPRequestHandler
# ServerClass  = BaseHTTPServer.HTTPServer
# Protocol     = "HTTP/1.0"
#
# if sys.argv[1:]:
#     port = int(sys.argv[1])
# else:
#     port = 8000
# server_address = ('127.0.0.1', port)
#
# HandlerClass.protocol_version = Protocol
# httpd = ServerClass(server_address, HandlerClass)
#
# sa = httpd.socket.getsockname()
# print "Serving HTTP on", sa[0], "port", sa[1], "..."
# httpd.serve_forever()
# import SimpleHTTPServer
# import SocketServer
#
# PORT = 8000
#
# Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
#
# httpd = SocketServer.TCPServer(("", PORT), Handler)
#
# print "serving at port", PORT
# httpd.serve_forever()

